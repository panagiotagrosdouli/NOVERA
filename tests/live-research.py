"""Browser → API → supervisor state → browser; no physical robot or external service."""
from pathlib import Path
import os,sys,socket,subprocess,time,urllib.request
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
with socket.socket() as sock:sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
server=subprocess.Popen([sys.executable,'research/server.py'],cwd=root,env={**os.environ,'NOVERA_PORT':str(port)},stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
url=f'http://127.0.0.1:{port}'
try:
 for _ in range(50):
  try:urllib.request.urlopen(url+'/api/telemetry',timeout=1);break
  except OSError:time.sleep(.1)
 with sync_playwright() as p:
  path=os.environ.get('CHROMIUM_PATH');b=p.chromium.launch(**({'executable_path':path} if path else {}),headless=True,args=['--no-sandbox']);page=b.new_page();page.goto(url+'/digital-twin.html');page.wait_for_function("document.querySelector('#connection').textContent.includes('LIVE_LOCAL')")
  response=page.request.post(url+'/api/command',data={'action':'mission','destination':'exit'});assert response.status==400
  page.check('#consent');page.select_option('#destination','exit');page.click('#mission');page.wait_for_timeout(1000);t=page.request.get(url+'/api/telemetry').json();assert t['mission']=='NAVIGATING'
  page.uncheck('#consent');page.wait_for_timeout(200);t=page.request.get(url+'/api/telemetry').json();assert t['goal'] is None and t['velocity']['linear_m_s']==0
  page.check('#consent');page.click('#mission');page.click('#estop');page.wait_for_timeout(200);t=page.request.get(url+'/api/telemetry').json();assert t['estop'] and t['velocity']['linear_m_s']==0
  assert page.request.post(url+'/api/command',data={'action':'reset'},headers={'Origin':'https://untrusted.example'}).status==403
  page.fill('#chat','medical emergency');page.click('#ask');page.wait_for_function("document.querySelector('#answer').textContent.includes('qualified')")
  b.close();print('PASS: live telemetry, consent/revocation, mission, latched stop, cross-origin rejection, scripted handoff')
finally:server.terminate();server.wait(timeout=5)
