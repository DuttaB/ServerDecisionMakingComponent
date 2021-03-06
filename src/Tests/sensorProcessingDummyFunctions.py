
tempArr = []
smokeArr = []
gasArr = []
waterArr = []
doorArr = []
weightArr = []
noneArr = []

# user list is the list of users for literally whatever we care about
# the test cases will set this up.  
# If we want a list of registered users in a room, fill this in
# If we want to check for intruders, this can be left empty
userList = []


def getSensorHistory(sensorID):
    '''
    Dummy function to return static sensor history until we have an actual 
    function ready to go.
    '''
    global tempArr
    global smokeArr
    global gasArr
    global waterArr
    global doorArr
    global weightArr
    global noneArr
    if sensorID == 'temp':
        return tempArr
    if sensorID == 'smoke':
        return smokeArr
    if sensorID == 'gas':
        return gasArr
    if sensorID == 'water pressure':
        return waterArr
    if sensorID == 'door':
        return doorArr
    if sensorID == 'weight':
        return weightArr
    if sensorID == 'none':
        return noneArr
    #if none of these sensors, just return generic list
    return [9,8,7,6,5,4,3,2,1,0]

def shiftHistory(sensorID, newData):
    '''
    Dummy function that prepends newData onto a list denoted by the sensor ID
    '''
    global tempArr
    global smokeArr
    global gasArr
    global waterArr
    global doorArr
    global weightArr
    global noneArr
    if sensorID == 'temp':
        tempArr.insert(0,newData)
    if sensorID == 'smoke':
        smokeArr.insert(0, newData)
    if sensorID == 'gas':
        gasArr.insert(0,newData)
    if sensorID == 'water pressure':
        waterArr.insert(0,newData)
    if sensorID == 'door':
        doorArr.insert(0,newData)
    if sensorID == 'weight':
        weightArr.insert(0,newData)
    if sensorID == 'none':
        noneArr.insert(0,newData)

def shiftLastDataHistory(sensorID, newData):
    global tempArrLast
    global smokeArrLast
    global gasArrLast
    global waterArrLast
    global weightArrLast
    if sensorID == 'temp':
        tempArrLast.insert(0,newData)
    if sensorID == 'smoke':
        smokeArrLast.insert(0, newData)
    if sensorID == 'gas':
        gasArrLast.insert(0,newData)
    if sensorID == 'water pressure':
        waterArrLast.insert(0,newData)
    if sensorID == 'weight':
        weightArrLast.insert(0,newData)

def getSensorData(sensorType, buildingID, room):
    global tempArr
    global smokeArr
    global gasArr
    global waterArr
    global doorArr
    global weightArr
    sensors = {}
    if sensorType == 'smoke':
        sensors['smokeid'] = smokeArr[0]
    if sensorType == 'weight':
        sensors['weightid'] = weightArr[0]
    if sensorType == 'temperature':
        sensors['tempid'] = tempArr[0]
    if sensorType == 'gas':
        sensors['gasid'] = gasArr[0]
    if sensorType == 'water pressure':
        sensors['water pressure id'] = waterArr[0]
    return sensors

def get_last_states(sensorId,size=1):
    global tempArrLast
    global smokeArrLast
    global gasArrLast
    global waterArrLast
    global weightArrLast
    if sensorId == 'weight':
        return [('', weightArrLast[0])]#'85'
    if sensorId == 'temp':
        return [('',tempArrLast[0])]#'40'
    if sensorId == 'water pressure':
        return [('', waterArrLast[0])]#'60'
    if sensorId == 'gas':
        return [('', gasArrLast[0])]#'0'
    if sensorId == 'smoke':
        return [('', smokeArrLast[0])]#'0'

def confirmEmergency(emergency, sensor):
    return True


def getUsersAtLocation(buildingId, room, floor, xpos, ypos):
    '''
    Get our dummy list of users that is initialized in each test
    '''
    return userList

def getPosition(sensorID):
    '''
    Returns a dummy position for the sensor.
    '''
    Position = collections.namedtuple('Position', 'room floor x y')
    pos = Position(room=sensor['room'], floor=sensor['floor'], x=sensor['xpos'], y=sensor['ypos'])
    return pos

def getSensorsAtLocation(buildingId, room, floor, x, y):
    '''
    Just return every list.  Anything calling this will parse through for the proper sensor type
    '''
    global weightArr
    global proximityArr
    sensors=[]
    sensor={}
    sensor['id'] = 'weight'
    sensor['buildingId'] = buildingId
    sensor['robotId'] = 'robotId'
    sensor['floor'] = floor
    sensor['room'] = room
    sensor['xpos'] = x
    sensor['ypos'] = y
    sensor['data'] = weightArr[0]
    sensor['model'] = 'model'
    sensor['type'] = 'weight'
    sensors.append(sensor)

    sensor1={}
    sensor1['id'] = 'proximity'
    sensor1['buildingId'] = buildingId
    sensor1['robotId'] = 'robotId'
    sensor1['floor'] = floor
    sensor1['room'] = room
    sensor1['xpos'] = x
    sensor1['ypos'] = y
    sensor1['data'] = '1'
    sensor1['model'] = 'model'
    sensor1['type'] = 'proximity'
    sensors.append(sensor1)

    return sensors

def setUpLists():
    global tempArr
    global smokeArr
    global gasArr
    global waterArr
    global doorArr
    global weightArr
    global noneArr
    global userList
    global proximityArr

    global tempArrLast
    global smokeArrLast
    global gasArrLast
    global waterArrLast
    global weightArrLast

    tempArr = ['21','20','21','22','21','20','19','18','19','20']
    smokeArr = ['0','1','0','1','0']
    gasArr = ['0','1','0']
    waterArr = ['41','44','46','45','47','45','42','40','42']
    doorArr = ['0','1','0','1','0','1','0','1','0']
    weightArr = ['0','80','0','20','85','0','15','0']
    noneArr = []
    noWeightArr = ['0']
    proximityArr = ['1']
    userList = []

    tempArrLast = ['40']
    weightArrLast = ['85']
    waterArrLast = ['60']
    gasArrLast = ['0']
    smokeArrLast = ['0']

def addUserInPosition(userId):
    userList.insert(0,userId)

def addUser(userId):
    pass
