"""Loopback-only local twin. No persistence, camera, mic, external API or credentials."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse
import json,threading,time,os
from supervisor import Robot,reply
robot=Robot();lock=threading.Lock()
class Handler(SimpleHTTPRequestHandler):
 def respond(self,status,data):
  b=json.dumps(data).encode();self.send_response(status);self.send_header('Content-Type','application/json');self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.end_headers();self.wfile.write(b)
 def do_GET(self):
  if self.path=='/api/telemetry':
   with lock:self.respond(200,robot.telemetry())
  else:super().do_GET()
 def do_POST(self):
  # Reject cross-origin browser writes; no CORS. Local research use only.
  origin=self.headers.get('Origin');host=self.headers.get('Host')
  if origin and origin!='http://'+host:return self.respond(403,{'error':'Origin denied'})
  try:
   length=int(self.headers.get('Content-Length','0'))
   if not 0<length<=4096:raise ValueError('Body size invalid')
   c=json.loads(self.rfile.read(length))
   if not isinstance(c,dict):raise ValueError('Object required')
   with lock:
    if self.path=='/api/command':robot.command(c);result=robot.telemetry()
    elif self.path=='/api/chat':result=reply(str(c.get('text',''))[:500],c.get('lang','en'))
    else:return self.respond(404,{'error':'Unknown route'})
   self.respond(200,result)
  except (ValueError,TypeError) as e:self.respond(400,{'error':str(e)})
def tick():
 while True:
  with lock:robot.step(.1)
  time.sleep(.1)
if __name__=='__main__':
 os.chdir(Path(__file__).resolve().parents[1]);threading.Thread(target=tick,daemon=True).start();print('Local twin: http://127.0.0.1:8765/digital-twin.html',flush=True);ThreadingHTTPServer(('127.0.0.1',int(os.environ.get('NOVERA_PORT','8765'))),Handler).serve_forever()
