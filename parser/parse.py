import csv
from glob import glob

file = open("info.txt", "r")
data = file.read()
##print(data)
i = 0
j = 0
tAm = ""
t = ""
m = ""
k = 0
aUpp = 0 #NUMERICAL
#aUMiss = 0
#aLMiss = 0
miss = 0 #NUMERICAL
taxi = "N" #BINARY
defense = "N" #BINARY
speed = "N" #Binary
swerve = ""
alliance = ""
climbAttempt = ""
failOrFall = ""
fouls = 0 #NUMERICAL
aLow = 0 #NUMERICAL
tUpp = 0 #NUMERICAL
tLow = 0 #NUMERICAL
#tUMiss = 0
#tLMiss = 0
rung = 0 #NUMERICAL
tName = "" 
comments = "" 
fullComment = ""
dataLength = len(data)

for x in data:
    i += 1
    if i == 5:
        alliance = data[6:7]
        if alliance == ""
        swerve = data[7:8]
        if swerve == "W" or swerve == "w":
            swerve = "Y"
        tAm = data[:6]
        data = data[7:]


for x in tAm:
    j += 1
    if j == 1:
        t = tAm[2:]
        m = tAm[:2]
print(t, m)

def Comments():
    global k
    global dataLength
    global comments
    global fullComment
    for x in fullComment:
        comments = comments + x


def Teleop():
    global tUpp
    global tLow
    global rung
    global fullComment
    global k
    global tLMiss
    global tUMiss
    global defense
    global fouls
    global speed
    global climbAttempt
    global failOrFall
    print(data, "teleop")
    for x in data:
        #print(x)
        if x == "D" or x == "d":
            defense = "Yes"
        elif x == "L" or x =="l":
            tLow+=1
        elif x == "U" or x =="u":
            tUpp+=1
        elif x == "F" or x == "f":
            fouls += 1
        elif x == "I" or x == "i":
            climbAttempt = "Y"
        elif x == "0":
            failOrFall = "Y"
            climbAttempt = "Y"
        elif x == "1":
            rung = 1
            climbAttempt = "Y"
            failOrFall = "N"
        elif x == "2":
            rung = 2
            climbAttempt = "Y"
            failOrFall = "N"
        elif x == "3":
            rung = 3
            climbAttempt = "Y"
            failOrFall = "N"
        elif x == "4":
            rung = 4
            climbAttempt = "Y"
            failOrFall = "N"
        elif x == "S" or x == "s":
            speed = "Fast"
        elif x == "/":
            k = data.index("/")
            fullComment = data[k+1:]
            Comments()

def Auton():
    global aUpp
    global aLow
    global aUMiss
    global aLMiss
    global taxi
    print(data)
    print("auton")
    for x in data:
        print(x)
        if x == "A" or x =="a":
            continue
        elif x == "T" or x =="t":
            Teleop()
            break
        elif x == "X" or x == "x":
            taxi = "Yes"
        elif x == "L" or x =="l":
            aLow += 1
        elif x == "U" or x =="u":
            aUpp += 1
        elif x == "M" or x == "m":
            miss == 1
        else:
            print("Error at " + x + ". Please check for illegal variables")
        
    



tName += str(t)
tName += "_Match"
tName += m
tName += ".csv"

filename = tName

for x in data:
    if x == 'A' or x =="a":
        Auton()
    
    

fields = [t, "Match", "Alliance","Swerve","Taxi", "Auton Uppper Hub", " Auton Lower Hub", "Teleop Upper Hub", "Teleop Lower Hub","Defense?", "Fouls", "Misses", "Attempted Climb?","Failed or Fell?","Rung"]
rows = ["", m, alliance, swerve, taxi, aUpp, aLow, (tUpp-aUpp), (tLow-aLow), defense, fouls, miss, climbAttempt, failOrFall, rung]
field = ["Comments"]
row = [comments]

with open(filename, 'w') as csvfile:

    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)

    csvwriter.writerow(rows)

    csvwriter.writerow(field)

    csvwriter.writerow(row)



#TODO
#add comments

#NOTE
#BINARY VALUES (Y or N values) are going to be strings
#NUMERICAL VALUES (number of) are going to be ints