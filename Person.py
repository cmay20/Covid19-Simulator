class Person(object):

    def __init__(self, cx, cy, r, name, infected, symptomatic, wearingMask, destinationX, destinationY):
        self.cx = cx
        self.cy = cy
        self.destX = destinationX
        self.destY = destinationY
        if(symptomatic):
            self.color = 'red'
        elif(not symptomatic and infected):
            self.color = 'yellow'
        else:
            self.color = 'green'

        self.name = name
        self.r = r
        self.infected = infected
        self.symptomatic = symptomatic
        self.wearingMask = wearingMask
        self.nearbyPeople = []
    
    def update(self, people):
        if(len(self.nearbyPeople) == 0):
            for person in people:
                distance = self.getDistance(self.cx, self.cy, person.cx, person.cy)
                self.nearbyPeople.append((distance, person))
        else:
            for i in range(len(people)):
                distance = self.getDistance(self.cx, self.cy, people[i].cx, people[i].cy)
                self.nearbyPeople[i] = (distance, people[i])

    def updateColor(self):
        if(self.symptomatic):
            self.color = 'red'
        elif(not self.symptomatic and self.infected):
            self.color = 'yellow'
        else:
            self.color = 'green'

    def getDistance(self,x0,y0,x1,y1):
        return ((x0 - x1)**2 + (y1-y0)**2)**.5
    
    def maskOn(self):
        self.wearingMask = True

    def maskOff(self):
        self.wearingMask = False

class Surface(object):

    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy



