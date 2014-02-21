import naoqi
from naoqi import ALProxy

IP = "192.168.1.106"
PORT = 9559

motion=ALProxy("ALMotion",IP,PORT)
dcm = ALProxy("DCM",IP,PORT)

motion.setStiffnesses('Body',1.0)
motion.setStiffnesses('Head',0.0)
motion.moveInit()
#motion.moveTo(0.1,0.01,0)
motion.stopMove()

dcm.createAlias([
"SingleFoot",
[
"Device/SubDeviceList/LHipYawPitch/Position/Actuator/Value",

"Device/SubDeviceList/LAnklePitch/Position/Actuator/Value",
"Device/SubDeviceList/LAnkleRoll/Position/Actuator/Value",
"Device/SubDeviceList/LHipPitch/Position/Actuator/Value",
"Device/SubDeviceList/LHipRoll/Position/Actuator/Value",
"Device/SubDeviceList/LKneePitch/Position/Actuator/Value",

"Device/SubDeviceList/RAnklePitch/Position/Actuator/Value",
"Device/SubDeviceList/RAnkleRoll/Position/Actuator/Value",
"Device/SubDeviceList/RHipPitch/Position/Actuator/Value",
"Device/SubDeviceList/RHipRoll/Position/Actuator/Value",
"Device/SubDeviceList/RKneePitch/Position/Actuator/Value",
]
])


t = dcm.getTime(0)

dcm.setAlias([
"SingleFoot",
"ClearAll",
"time-separate",
0,
[t+2000,t+4000,t+6000,t+8000,t+10000,t+12000],
[
[0.0,-0.260738044977,-0.164096042514,-0.157960042357,-0.124212041497,-0.167164042592],
#HIPYAW
[-0.522528290749,-0.15344196558,-0.983335971832,0.417206048965,-0.6995459795,-0.607505977154],
#LAP
[-0.000274926336715,-0.296020030975,-0.126684755087,-0.174834042788,0.0353239625692,0.251617968082],
#LAR
[-0.324198633432,-0.0122300386429,-1.02160203457,-0.834454059601,-1.22562408447,-1.22102212906],
#LHP
[0.000170444007381,0.233209967613,0.293035984039,0.124295957386,0.11815995723,-0.148756042123],
#LHR
[0.846726834774,0.246932044625,2.11252808571,0.443284034729,1.87143802643,1.8192820549],
#LKP

[-0.522528350353,-0.412604033947,-0.412604033947,-0.412604033947,-0.85286206007,-0.791502058506],
[-4.91664141009e-05,-0.257670044899,-0.257670044899,-0.257670044899,0.0506639629602,0.255483537912],
[-0.324198484421,-0.0844119638205,-0.0844119638205,-0.0844119638205,0.0996680408716,0.335904061794],
[0.000121649740322,0.168781965971,0.168781965971,0.168781965971,0.105887956917,-0.190174043179],
[0.846726775169,0.586030006409,0.586030006409,0.586030006409,0.745566010475,0.4602419734],
]
])
