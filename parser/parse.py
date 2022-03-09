import csv

file = open("info.txt", "r")
data = file.read()
##print(data)
i = 0
j = 0
tAm = ""
t = ""
m = ""
k = 0
aUpp = 0
aLow = 0
tUpp = 0
tLow = 0
rung = 0
tName = ""
comments = ""
commentsPos = ""
dataLength = len(data)

for x in data:
    i += 1
    if i == 5:
        tAm = data[:6]
        data = data[6:]

for x in tAm:
    j += 1
    if j == 1:
        t = tAm[2:]
        m = tAm[:2]
#print(t, m)

def Comments():
    global k
    global dataLength
    global comments
    global commentsPos
    for x in commentsPos:
        comments = comments + x


def Teleop():
    global tUpp
    global tLow
    global rung
    global commentsPos
    global k
    for x in data:
        #print(x)
        if x == "L":
            tLow+=1
        elif x == "U":
            tUpp+=1
        elif x == "1":
            rung = 1
        elif x == "2":
            rung = 2
        elif x == "3":
            rung = 3
        elif x == "4":
            rung = 4
        elif x == "/":
            k = data.index("/")
            commentsPos = data[k+1:]
            Comments()

def Auton():
    global aUpp
    global aLow
    for x in data:
        #print(x)
        if x == "A":
            continue
        elif x == "E":
            Teleop()
            break
        elif x == "L":
            aLow += 1
        elif x == "U":
            aUpp += 1
        
    



tName += str(t)
tName += "_Match"
tName += m
tName += ".csv"

filename = tName

for x in data:
    if x == 'A':
        Auton()
    
    

fields = [t, "Match", "Auton Uppper Hub", " Auton Lower Hub", "Teleop Upper Hub", "Teleop Lower Hub", "Rung"]
rows = ["", "", aUpp, aLow, (tUpp-aUpp), (tLow-aLow), rung]
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