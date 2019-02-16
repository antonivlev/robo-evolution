import vrep
import time

def checkDataFetch(retCode, obj, descr=''):
    if retCode == vrep.simx_return_ok:
        print('---'+descr+' successfully retrieved: '+str(obj))
    else:
        print('Failed fetch with return code: {:d}\n'.format(retCode))

def getRobotPosition(nsecs):
    print ('Program started')
    vrep.simxFinish(-1) # just in case, close all opened connections
    clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to V-REP

    if clientID!=-1:
        print ('Connected to remote API server')

        vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)

        retCodeHandle, robotHandle = vrep.simxGetObjectHandle(clientID, 'robot_shape', vrep.simx_opmode_blocking)
        checkDataFetch(retCodeHandle, robotHandle, 'handle')

        # give the robot time to move
        time.sleep(nsecs)

        retCodePos, objectPos = vrep.simxGetObjectPosition(clientID, robotHandle, -1, vrep.simx_opmode_blocking);
        checkDataFetch(retCodePos, objectPos, 'position')

        vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot_wait)

        # Before closing the connection to V-REP, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
        vrep.simxGetPingTime(clientID)
        # Now close the connection to V-REP:
        vrep.simxFinish(clientID)
    else:
        print ('Failed connecting to remote API server')
    print ('Program ended')

    return objectPos[0]
