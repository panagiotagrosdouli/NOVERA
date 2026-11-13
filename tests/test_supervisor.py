import sys,unittest,time,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
from supervisor import Robot,reply
class SupervisorTests(unittest.TestCase):
 def ready(self):
  r=Robot();r.command({'action':'consent','enabled':True});return r
 def test_rejects_unapproved_and_no_consent(self):
  r=Robot()
  with self.assertRaises(ValueError):r.command({'action':'mission','destination':'exit'})
  r=self.ready()
  with self.assertRaises(ValueError):r.command({'action':'mission','destination':'arbitrary'})
 def test_waypoint_arrives(self):
  r=self.ready();r.command({'action':'mission','destination':'exit'})
  for _ in range(250):r.last_operator=time.monotonic();r.step(.1)
  self.assertEqual(r.mission,'ARRIVED');self.assertLess(math.hypot(r.x-2,r.y-6),.15)
 def test_estop_latched(self):
  r=self.ready();r.command({'action':'mission','destination':'exit'});r.command({'action':'estop'});p=(r.x,r.y)
  for _ in range(20):r.step(.1)
  self.assertEqual(p,(r.x,r.y));self.assertEqual(r.v,0)
  with self.assertRaises(ValueError):r.command({'action':'mission','destination':'exit'})
 def test_fault_low_energy_and_timeout(self):
  for fault in ['fault','battery','timeout']:
   r=self.ready();r.command({'action':'mission','destination':'exit'})
   if fault=='fault':r.command({'action':'fault'})
   if fault=='battery':r.battery_Wh=1
   if fault=='timeout':r.last_operator-=4
   r.step(.1);self.assertEqual(r.v,0);self.assertIsNotNone(r.fault)
 def test_obstacle_hold(self):
  r=self.ready();r.x=3.64;r.y=3;r.yaw=0;r.goal=[7,3];r.step(.1);self.assertEqual(r.mission,'OBSTACLE_HOLD');self.assertEqual(r.v,0)
 def test_sensor_and_dimensions(self):
  r=Robot();self.assertEqual(len(r.scan()),72);self.assertTrue(all(0<x<=8 for x in r.scan()));self.assertFalse(r.free(4.1,3));self.assertFalse(r.free(.1,.1))
 def test_hri_never_commands_motion(self):
  for lang in ['en','el']:
   self.assertIsNone(reply('navigate to exit',lang)['motion_command'])
  self.assertTrue(reply('medical emergency')['handoff'])
 def test_consent_withdrawal_stops(self):
  r=self.ready();r.command({'action':'mission','destination':'exit'});r.step(.1);r.command({'action':'consent','enabled':False});self.assertIsNone(r.goal);self.assertEqual(r.v,0)
 def test_invalid_dt(self):
  for dt in [0,-1,float('nan'),1]:
   with self.assertRaises(ValueError):Robot().step(dt)
if __name__=='__main__':unittest.main()
