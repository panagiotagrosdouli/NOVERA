"""Dependency-free 2D kinematic research simulator, NOT Gazebo or physical evidence."""
import json, math, time
from pathlib import Path
CONFIG=json.loads(Path(__file__).with_name('config.json').read_text())
class Robot:
 def __init__(self):
  self.x,self.y,self.yaw=2.,2.,0.;self.battery_Wh=CONFIG['battery_Wh']*CONFIG['usable_fraction'];self.estop=False;self.fault=None;self.goal=None;self.mission='IDLE';self.v=self.w=0.;self.history=[];self.last_operator=time.monotonic();self.consent=False;self.sequence=0
 def free(self,x,y):
  world=CONFIG['world'];m=math.hypot(CONFIG['width_m'],CONFIG['depth_m'])/2
  return m<=x<=world['width_m']-m and m<=y<=world['height_m']-m and not any(a-m<=x<=a+c+m and b-m<=y<=b+d+m for a,b,c,d in world['obstacles'])
 def scan(self):
  values=[]
  for i in range(72):
   angle=self.yaw+i*2*math.pi/72;dist=.05
   while dist<8:
    x=self.x+dist*math.cos(angle);y=self.y+dist*math.sin(angle);world=CONFIG['world']
    if not(0<x<world['width_m'] and 0<y<world['height_m']) or any(a<=x<=a+c and b<=y<=b+d for a,b,c,d in world['obstacles']):break
    dist+=.05
   values.append(round(min(dist,8),2))
  return values
 def command(self,c):
  action=c.get('action')
  if action=='heartbeat':self.last_operator=time.monotonic()
  elif action=='estop':self.estop=True;self.goal=None;self.mission='STOPPED';self.v=self.w=0
  elif action=='reset':
   if self.fault or self.battery_Wh<20:raise ValueError('Resolve fault before deliberate reset')
   self.estop=False;self.mission='IDLE'
  elif action=='fault':self.fault='INJECTED_SENSOR_FAULT';self.goal=None;self.v=self.w=0;self.mission='FAULT'
  elif action=='clear_fault':self.fault=None;self.mission='STOPPED';self.estop=True
  elif action=='consent':
   self.consent=c.get('enabled') is True
   if not self.consent:self.goal=None;self.mission='CONSENT_WITHDRAWN';self.v=self.w=0
  elif action=='mission':
   if self.estop or self.fault or not self.consent or self.battery_Wh<20:raise ValueError('Mission inhibited: consent, reset, energy and healthy state required')
   if c.get('destination') not in CONFIG['destinations']:raise ValueError('Only approved fixture destinations accepted')
   self.goal=CONFIG['destinations'][c['destination']];self.mission='NAVIGATING';self.last_operator=time.monotonic()
  elif action=='handoff':self.goal=None;self.mission='OPERATOR_HANDOFF';self.v=self.w=0
  else:raise ValueError('Unknown supervisory action')
 def step(self,dt):
  if not math.isfinite(dt) or not 0<dt<=.25:raise ValueError('Invalid timestep')
  self.v=self.w=0
  if self.battery_Wh<20:self.fault='LOW_BATTERY';self.goal=None;self.mission='FAULT'
  if time.monotonic()-self.last_operator>3 and self.goal:self.fault='OPERATOR_LINK_TIMEOUT';self.goal=None;self.mission='FAULT'
  if self.goal and not self.estop and not self.fault:
   dx,dy=self.goal[0]-self.x,self.goal[1]-self.y;distance=math.hypot(dx,dy)
   if distance<.15:self.goal=None;self.mission='ARRIVED'
   else:
    error=math.atan2(math.sin(math.atan2(dy,dx)-self.yaw),math.cos(math.atan2(dy,dx)-self.yaw));self.w=max(-.6,min(.6,error*2));self.v=min(.25,distance) if abs(error)<.3 else 0
    yaw=self.yaw+self.w*dt;x=self.x+self.v*dt*math.cos(yaw);y=self.y+self.v*dt*math.sin(yaw)
    if not self.free(x,y):self.v=self.w=0;self.mission='OBSTACLE_HOLD'
    else:self.x,self.y,self.yaw=x,y,yaw;self.mission='NAVIGATING'
  self.battery_Wh=max(0,self.battery_Wh-(CONFIG['idle_W']+CONFIG['drive_W']*(abs(self.v)/.25))*dt/3600)
  self.sequence+=1;self.history.append([round(self.x,3),round(self.y,3)]);self.history=self.history[-200:]
 def telemetry(self):
  return {'source':'LIVE_LOCAL_2D_KINEMATIC_SIMULATION','not_gazebo':True,'sequence':self.sequence,'pose':{'x_m':self.x,'y_m':self.y,'yaw_rad':self.yaw},'velocity':{'linear_m_s':self.v,'angular_rad_s':self.w},'wheel_rad_s':[(self.v-self.w*CONFIG['track_m']/2)/CONFIG['wheel_radius_m'],(self.v+self.w*CONFIG['track_m']/2)/CONFIG['wheel_radius_m']],'battery_model_Wh':self.battery_Wh,'mission':self.mission,'goal':self.goal,'estop':self.estop,'fault':self.fault,'sensors':{'lidar':'RAYCAST_MODEL','rgbd':'NOT_IMPLEMENTED','imu':'KINEMATIC_YAW_ONLY'},'scan_m':self.scan(),'history':self.history,'world':CONFIG['world'],'microphone':'OFF','camera':'OFF','consent':self.consent}
def reply(text,lang='en'):
 text=text.strip().lower()
 if lang not in ['en','el']:raise ValueError('Unsupported language')
 if any(t in text for t in ['medical','emergency','child','ιατρ','έκτακ','παιδ']):return {'text':'Ask qualified staff. / Ζητήστε βοήθεια από αρμόδιο προσωπικό.','handoff':True}
 return {'text':CONFIG['building_information'][lang], 'handoff':False,'motion_command':None,'confidence':'SCRIPTED_FIXTURE_ONLY'}
