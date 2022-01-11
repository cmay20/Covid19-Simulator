import math, copy, random

from cmu_112_graphics import *
#from yeah  import *
# from sliderTest import value

from Person import *
# slider1 = Scale(root, from_=1, to=100, showvalue=1)
# slider1.pack()

def appStarted(app):
    #initial scaling widgets
    app.removeScalingWidgets = False
    drawScaleAndTimeWidgets(app)
    app.creatingRoom = True
    app.pointsSelected = 0
    app.room = []
    app.scale = app.slider1.get() # INPUT FROM USER SOON BUT 1 PIXEL = 1 INCH
    app.scaleInFeet = app.scale/12
    app.initialInfected = 0
    app.creatingPeople = False
    app.copyingPerson = False
    app.people = []
    app.timerDelay = 1000
    app.r = 6
    app.encounters = 0
    app.notInfectRate = 0.999828
    app.infectRate = 0.0000172
    app.timeElapsed = 0
    app.timeStep = 10
    app.timeScale = 1
    app.gameOver = False
    app.drawPoints = False
    app.infections = []
    app.nameList = ['Jeff', 'John', 'Jerry', 'James', 'Jason',
    'Jackson', 'Jack', 'Jacob', 'Jeffery', 'Johnson', 'Jaques',
    'Jennifer', 'Jenny', 'Jess', 'Jessie', 'Jessica', 'Jimmy', 
    'Jimmothy', 'Jim', 'Joe', 'Joseph', 'Johnny', 'Geoff',
    'Jane', 'JJ', 'Jub-Jub']
    app.surfaces = []
    app.surfaceSize = 20
    app.table = False

################################################################################
# Advanced Tkinter stuff
################################################################################

def drawScaleAndTimeWidgets(app):
    app.win = Tk()
    app.win.title("Scale the Simulator")
    app.win.configure(bg='orange')
    #scale/time Instructions
    app.instFrame = Frame(app.win, background='orange')
    app.instFrame.pack()
    app.text1 = Label(app.instFrame, text="Please select your desired\n\
    room scale and time speed", background='orange', font=('Helvetica', 14, 'bold'))
    app.text1.pack()
    
    #room scale
    app.textFrame2 = Frame(app.win, background='orange')
    app.textFrame2.pack()
    app.text2 = Label(app.textFrame2, text="Room Scale (set # inches per px): ", background='orange')
    app.text2.pack()
    app.slider1 = Scale(app.win, from_=10, to=1, showvalue=1, orient=HORIZONTAL, background='orange')    
    app.slider1.pack()

    #time scale
    app.textFrame3 = Frame(app.win, background='orange')
    app.textFrame3.pack()
    #app.text3 = Label(app.textFrame2, text="Time Speed: ", background='orange')
    #app.text3.pack()
    app.slider2 = Scale(app.win, from_=1, to=500, showvalue=1, orient=HORIZONTAL, background='orange')    
    app.slider2.pack()

    #submit button
    app.submitButton = Button(app.win, text="Submit Room/People", command = lambda: beginSimulation(app, app.win), bg='orange')
    app.submitButton.pack()   

def removeScalingWidgets(app, win):
    app.win.destroy()
    
def inputPersonWidgets(app, person):
    app.win2 = Tk()
    app.win2.configure(background='lime')
    app.win2.title("Input New Person")
    #name
    frame1 = Frame(app.win2, bg='lime')
    frame1.pack()
    nameText = Label(frame1, text="Name", background='lime')
    nameText.grid(row=0, column=0, sticky=W)
    app.namevar = StringVar()
    app.name = Entry(frame1, textvariable=app.namevar, background='lime')
    app.name.grid(row=0, column=1, sticky=W)
    
    #infected
    frame2 = Frame(app.win2)
    frame2.pack()
    infText = Label(frame2, text="Infected: ", background='lime')
    infText.pack(side=LEFT)
    
    frame3 = Frame(app.win2)
    frame3.pack()
    app.v = IntVar()
    app.radioV1a = False
    app.radioV1b = False
    app.infRadioButton = Radiobutton(app.win2, text="Yes", variable=app.v, value=1, bg='lime', command=lambda: setRadio1a(app, app.win2, person))
    app.infRadioButton.pack(side=LEFT) 
    app.inf2RadioButton = Radiobutton(app.win2, text="No", variable=app.v, value=0, bg='lime', command=lambda: setRadio1b(app, app.win2, person))
    app.inf2RadioButton.pack(side=LEFT)
    
    #symptomatic 
    frame4 = Frame(app.win2)
    frame4.pack()
    symText = Label(frame4, text="Symptomatic: ", background='lime')
    symText.grid(row=2, column=0, sticky=W)
    app.v1 = IntVar()
    app.radioV2a = False
    app.radioV2b = False
    app.symRadioButton = Radiobutton(app.win2, text="Yes", variable=app.v1, value=1, bg='lime', command=lambda: setRadio2a(app, app.win2, person))
    app.symRadioButton.pack(side=LEFT) 
    app.sym2RadioButton = Radiobutton(app.win2, text="No", variable=app.v1, value=0, bg='lime', command=lambda: setRadio2b(app, app.win2, person))
    app.sym2RadioButton.pack(side=LEFT) 

    #mask
    frame4 = Frame(app.win2)
    frame4.pack()
    mText = Label(frame4, text="Wearing Mask: ", background='lime')
    mText.grid(row=3, column=0, sticky=W)
    #mText.pack()
    app.v2 = IntVar()
    app.radioV3a = False
    app.radioV3b = False
    app.mRadioButton = Radiobutton(app.win2, text="Yes", variable=app.v2, value=1, bg='lime', command=lambda: setRadio3a(app, app.win2, person))
    app.mRadioButton.pack(side=LEFT) 
    app.m2RadioButton = Radiobutton(app.win2, text="No", variable=app.v2, value=0, bg='lime', command=lambda: setRadio3b(app, app.win2, person))
    app.m2RadioButton.pack(side=LEFT) 
    
    app.submitButton = Button(app.win2, text="Submit Person", command = lambda: setPersonValues(app, app.win2, person), bg='lime')
    app.submitButton.pack() 
    
def setRadio1a(app, win2, person):
    app.radioV1a = not app.radioV1a

def setRadio1b(app, win2, person):
    app.radioV1b = not app.radioV1b

def setRadio2a(app, win2, person):
    app.radioV2a = not app.radioV2a

def setRadio2b(app, win2, person):
    app.radioV2b = not app.radioV2b

def setRadio3a(app, win2, person):
    app.radioV3a = not app.radioV3a

def setRadio3b(app, win2, person):
    app.radioV3b = not app.radioV3b

def setPersonValues(app, win2, person):
    person.name = app.name.get()
    #infection
    if app.radioV1a == True and app.radioV1b == False:
        person.infected = True
        person.updateColor()
    elif app.radioV1a == False and app.radioV1b == True:
        person.infected = False
        person.updateColor()
    #symptomatic
    if app.radioV2a == True and app.radioV2b == False:
        person.symptomatic = True
        person.updateColor()
    elif app.radioV2a == False and app.radioV2b == True:
        person.symptomatic = False
        person.updateColor()
    #mask
    if app.radioV3a == True and app.radioV3b == False:
        person.maskOn()
    elif app.radioV3a == False and app.radioV3b == True:
        person.maskOff()
    app.win2.destroy()

def beginSimulation(app, win):
    app.creatingRoom = False
    app.creatingPeople = False
    app.gameOver = False
    app.initialInfected = calculateInfected(app)
    removeScalingWidgets(app, win)

################################################################################
# Person Stuff
################################################################################

def calculateInfected(app):
    infected = 0
    for person in app.people:
        if person.infected:
            infected += 1
    return infected

def movePeople(app):
    for person in app.people:
        dx = random.randint(-3,3)
        dy = random.randint(-3,3) 
        if person.cx > person.destX + 20:
            destX = -3
        elif person.cx < person.destX - 20:
            destX = 3
        else:
            destX = 0
        if person.cy > person.destY + 20:
            destY = -3
        elif person.cy < person.destY - 20:
            destY = 3
        else:
            destY = 0
        minCheck = (1000000, None)
        for check in person.nearbyPeople:
            if(check[0] < minCheck[0] and check[0] != 0):
                minCheck = check
        if(minCheck[0] < 60 / app.scale and minCheck[1].symptomatic):
                x = person.cx - minCheck[1].cx
                y = person.cy - minCheck[1].cy
                dx = (x/minCheck[0])*abs(dx)
                dy = (y/minCheck[0])*abs(dy)

        newX = person.cx + (dx + destX) / (app.scale)
        newY = person.cy + (dy + destY) / (app.scale)

        if isInRoom(app, newX, newY) and not isInSurface(app, newX, newY):
            person.cx = newX
            person.cy = newY

def didVirusSpread(app, person1, person2):
    chanceOfSpread = 1 - (app.notInfectRate**(app.timeScale))
    if(person1.infected == person2.infected): 
        return person1.infected
    elif(not person1.infected):
        if(person1.wearingMask):
            chanceOfSpread *= .65
        if(person2.wearingMask):
            chanceOfSpread *= .90
    else:
        if(person1.wearingMask):
            chanceOfSpread *= .90
        if(person2.wearingMask):
            chanceOfSpread *= .65
    distance = (getDistance(person1.cx, person1.cy,
        person2.cx, person2.cy)) * app.scale
    if distance > 120:
        return False    
    chanceOfSpread /= max(distance, 12)/72
    if chanceOfSpread >= random.uniform(0,1):
        return True
        
def infectPeople(app):
    infectedSet = set()
    for i in range(len(app.people) - 1):
        x0 = app.people[i].cx
        y0 = app.people[i].cy
        for j in range(i + 1, len(app.people)):
            spread = didVirusSpread(app, app.people[i], app.people[j])
            if spread:
                infectedSet.add(i)
                infectedSet.add(j)
    for index in infectedSet:
        app.people[index].infected = True

def generatePerson(app):
    radius = max(10 / app.scale, 5)
    rn1 = random.uniform(0,1)
    rn2 = random.uniform(0,1)
    rn3 = random.uniform(0,1)
    if rn1 < .7:
        wearingMask = True
    else:
        wearingMask = False
    if rn2 < .05:
        infected = True
        if rn3 < 0.5:
            symptomatic = True
        else: 
            symptomatic = False
    else:
        infected = False
        symptomatic = False
    name = app.nameList[len(app.people) % len(app.nameList)]
    destX = random.randint(app.roomX0, app.roomX1)
    destY = random.randint(app.roomY0, app.roomY1)
    return (radius, name, infected, symptomatic, wearingMask, destX, destY)

def skipTime(app, time):
    encounterRate = app.encounters / app.timeElapsed
    encounters = 0
    infections = 0
    infected = 0
    for _ in range(time):
        encounters += encounterRate // 1
        if random.uniform(0,1) < encounterRate % 1:
            encounters += 1
    for person in app.people:
        if person.infected == True:
            infected += 1
    infectionRate = infections / encounters
    for _ in range(infected):
        if random.uniform(0,1) < infectionRate:
            infections += 1
    while infections > 0:
        for person in app.people:
            if person.infected == False:
                person.infected = True
                infections -= 1


################################################################################
# Controllers
################################################################################
def keyPressed(app, event):
    if event.key == 'r':
        appStarted(app)
    elif event.key == 'Escape':
        app.gameOver = True
    elif event.key == 'a' and app.creatingPeople:
        cx = random.randint(app.roomX0, app.roomX1)
        cy = random.randint(app.roomY0, app.roomY1)
        (radius, name, infected, symptomatic, wearingMask, destX, destY) = generatePerson(app)
        app.people.append(Person(cx,cy,radius, name, infected, symptomatic, wearingMask, destX, destY))
    elif event.key == 'Up':
        app.timeScale += 1
        app.timeStep = 10 * app.timeScale
    elif event.key == 'Down':
        if app.timeScale != 1:
            app.timeScale -= 1
            app.timeStep = 10 * app.timeScale
    elif event.key == 't':
        app.table = not app.table

def mousePressed(app, event):
    if app.table:
        app.surfaces.append(Surface(event.x, event.y))
    elif(app.creatingRoom):
        app.pointsSelected += 1
        app.room.append(event.x)
        app.room.append(event.y)
        app.drawPoints = True
        if(app.pointsSelected >= 2):
            app.drawPoints = False
            app.creatingRoom = False
            app.creatingPeople = True
            app.roomX0 = min(app.room[0], app.room[2])
            app.roomX1 = max(app.room[0], app.room[2])
            app.roomY0 = min(app.room[1], app.room[3])
            app.roomY1 = max(app.room[1], app.room[3])
    elif(app.creatingPeople):
        if app.table and isInRoom(app, event.x, event.y):
            app.surfaces.append(Surface(event.x, event.y))
        if(isInPerson(app, event.x, event.y)[0] and not app.copyingPerson):
            app.copyingPerson = True
            personToCopy = copy.deepcopy(isInPerson(app, event.x, event.y)[1])
            app.people.append(personToCopy)
        elif(app.copyingPerson and isInRoom(app, event.x, event.y)):
            app.people[-1].cx = event.x
            app.people[-1].cy = event.y
            app.copyingPerson = False
        if(isInRoom(app, event.x, event.y) and not isInPerson(app, event.x, event.y)[0]):
            destX = random.randint(app.roomX0, app.roomX1)
            destY = random.randint(app.roomY0, app.roomY1)
            app.people.append(Person(event.x, event.y, max(10 / app.scale, 5), "Default", False, False, False, destX, destY))
            inputPersonWidgets(app, app.people[-1])

def setDestinations(app):
    if app.timeElapsed % 1200 == 0:
        for person in app.people:
            tableNumber = random.randint(0, len(app.surfaces) + 2)
            if tableNumber >= len(app.surfaces):
                person.destX = random.randint(app.roomX0, app.roomX1)
                person.destY = random.randint(app.roomY0, app.roomY1)
            else:
                person.destX = app.surfaces[tableNumber].cx
                person.destY = app.surfaces[tableNumber].cy        
    
def mouseMoved(app, event):
    if(app.copyingPerson):
        app.people[-1].cx = event.x
        app.people[-1].cy = event.y            

def timerFired(app):
    if not(app.creatingRoom or app.creatingPeople or app.gameOver):
        doStep(app)
    elif not app.gameOver: 
        app.scale = app.slider1.get()
        app.timerDelay = app.slider2.get()   

def doStep(app):
    setDestinations(app)
    app.timeElapsed += app.timeStep
    movePeople(app)
    infectPeople(app)
    for person in app.people:
            person.update(app.people)
            person.updateColor()

################################################################################
# Other/Legal checks...
################################################################################

def isInRoom(app, cx, cy):
    if (app.roomX0 < cx < app.roomX1) and (app.roomY0 < cy < app.roomY1):
        return True
    return False

def isInSurface(app, cx, cy):
    for surface in app.surfaces:
        if abs(surface.cx - cx) < 20 and abs(surface.cy - cy) < 20:
            return True
    return False
    
def isInPerson(app, cx, cy):
    for person in app.people:
        x0 = person.cx
        y0 = person.cy
        x1 = cx
        y1 = cy
        if(getDistance(x0,y0,x1,y1) < 2 * person.r):
            return (True, person)
    return (False, None)
        
def getDistance(x0,y0,x1,y1):
    return ((x0 - x1)**2 + (y1-y0)**2)**.5

################################################################################
# Drawing
################################################################################

#Mark two points on the blank screen to create a rectangular room
def drawCreateRoomPoint1(app, canvas):
    cx, cy, r = app.room[0], app.room[1], 5
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="cyan")

def drawCreateRoomPoint2(app, canvas):
    if len(app.room) > 2:
        cx, cy, r = app.room[2], app.room[3], 5
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="cyan")

def drawRoom(app, canvas):
    if(not app.creatingRoom):
        canvas.create_rectangle(app.room[0], app.room[1], app.room[2], app.room[3], fill="cyan")


def drawPeople(app, canvas):
    font = "Arial 8"
    for person in app.people:
        canvas.create_oval(person.cx - person.r, 
            person.cy - person.r, person.cx + person.r, 
            person.cy + person.r, fill=person.color)
        canvas.create_text(person.cx, person.cy - 15, text=person.name, font=font)
        if person.wearingMask:
            canvas.create_polygon(person.cx - person.r, person.cy, 
                person.cx + person.r, person.cy, person.cx, person.cy + person.r,
                fill='black')

def drawScale(app, canvas):
    scaleLengthInches = 72
    scaleLengthPixels = scaleLengthInches//app.scale
    canvas.create_line(20, app.height - 20, 20 + scaleLengthPixels, app.height - 20)
    canvas.create_line(20, app.height - 18, 20, app.height - 22)
    canvas.create_line(20+scaleLengthPixels, app.height - 18, 20+scaleLengthPixels, app.height - 22)
    canvas.create_text((25+scaleLengthPixels)//2, app.height-30, text="Scale")
    canvas.create_text((30+scaleLengthPixels)//2, app.height-10, text="6ft")

def drawInstructions(app, canvas):
    creatingRoomText = (
        '''
        Please click on the window to set the top
        left point of your room, then click again 
        to set the bottom right point of your room!
        '''
    )
    creatingPeopleText = (
        '''
        Please click within your room to 
        create your event attendees! To make a copy,
        click in a person you want to copy.
        '''
    )
    font = "Arial 10"
    if(app.creatingRoom):
        canvas.create_text(app.width-120, app.height-25, text=creatingRoomText, font=font)
    elif(app.creatingPeople):
        canvas.create_text(app.width-120, app.height-25, text=creatingPeopleText, font=font)
    
    
def drawStatistics(app, canvas):
    infections = 0
    seconds = app.timeElapsed % 60
    minutes = (app.timeElapsed // 60) % 60
    hours = app.timeElapsed // (60**2)
    canvas.create_text(app.width // 2, 100, 
        text= f'In {hours} hours, {minutes} minutes, {seconds} seconds')
    for person in app.people:
        if person.infected:
            infections += 1
    infections -= app.initialInfected
    canvas.create_text(app.width // 2, 200, text= f'{infections} infections occured')    

def drawTitle(app, canvas):
    font = "Helvetica 24 bold"
    canvas.create_text(app.width//2, 1/14*app.height, text="COVID-19 SIMULATOR", font=font)

def drawSurfaces(app, canvas):
    for surface in app.surfaces:
        cx = surface.cx
        cy = surface.cy
        canvas.create_rectangle(cx - 20,cy - 20, cx + 20, cy + 20, fill='black')

def redrawAll(app, canvas):
    if app.drawPoints:
        drawCreateRoomPoint1(app, canvas)
        drawCreateRoomPoint2(app, canvas)
    if(not app.gameOver):
        drawTitle(app, canvas)
        drawRoom(app, canvas)
        drawSurfaces(app, canvas)
        drawPeople(app, canvas)
        drawScale(app, canvas)
        drawInstructions(app, canvas)
    else:
        drawStatistics(app, canvas)

#################################################
# main
#################################################

def main():
    runApp(width=800, height=600)

if __name__ == '__main__':
    main()
