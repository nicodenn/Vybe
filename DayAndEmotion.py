### Vybe's Day, Week, and Emotion Classes ###
  #  Written by Joe Hart and Nico Dennis  #

from datetime import datetime
from queue import Queue
import pickle

class Emotion:
    
    def __init__(self, name):
        self.name = name
        self.vybeScore = 0 #a sum of all durations of the emotion * those durations' intensity
        self.totalTime = 0 #saved in minutes

    def getEmoInfo(self):
        return [self.name, self.vybeScore, self.totalTime]

class Day:

    def __init__(self):
        self.timeDelta = datetime.now() 
        self.date = self.timeDelta.strftime("%d/%m/%Y") #a string of the day's date (day/month/year)
        self.indexes = ['Sad', 'Happy', 'Stressed', 'Angry', 'Confused', 'Tired', 'Excited'] #list of all emotions tracked by program
        self.emotionObjs = self.initEmotions() #an array of Emotion Objects to store the day's emotion info
        self.currEmotions = [0, 0, 0, 0, 0, 0, 0] #tracks what the user is feeling currently
        
    def initEmotions(self):
        #helper that builds the list of new Emotion objects when a day is created
        rtr = []
        for i in range(len(self.indexes)):
            rtr.append(Emotion(self.indexes[i]))
        
        return rtr

    def changeEmotions(self):
        check = False
        for item in self.currEmotions:
            if (item != 0):
                check = True

        if (check): #if there are current emotions, program asks you which ones you do not feel anymore and saves them to the Emotion Objs
            print("Your current emotions are:")
            for i in range(len(self.currEmotions)):
                if (self.currEmotions[i] != 0):
                    print(self.indexes[i] + " : " + str(i), end=' / ')
            
            print("What emotions are you no longer feeling?\nPlease list all the numbers associated with the emotions\nyou would like to change separated by commas.")
            value = input("> ")
            value = value.split(',')
            for emo in value:
                try:
                    emoIndex = int(emo.strip())
                    self.saveEmotion(emoIndex, self.currEmotions[emoIndex])
                    print("Saved emotion: " + self.indexes[emoIndex])
                except:
                    print("Invalid value: " + emo)
        #program asks you what new emotions would you like to track and inputs them into currEmotions
        print("\nWhat new emotions are you feeling?\nSad : 0 / Happy : 1 / Stressed : 2 / Angry : 3 / Confused : 4 / Tired : 5 / Excited : 6")
        print("Type \"exit\" when you are finished.\n")
        check = 1
        while(check):
            inVal = input("Please write number associated with your emotion\nand the intensity of your emotion, separated by a comma > ")
            emotionIndices = inVal.split(',')
            if(inVal.strip() == "exit"):
                check = 0
            elif(len(emotionIndices) == 2) and ("-" not in emotionIndices[0]) and ("-" not in emotionIndices[1]): #### ToDo: check if the 2 entries are ints within proper range, handle -ints
                try:
                    emoInfo = (int(emotionIndices[0].strip()),int(emotionIndices[1].strip()))
                    if(emoInfo[1]>-1) and (emoInfo[1] < 6):
                        self.createEmotion(emoInfo)
                    else:
                        print("Intensity is a value between 1 and 5. Your input: " + str(emoInfo[1]))
                except:
                    print("Invalid entry: Please Try Again")
                
            else: 
                print("Invalid entry: Please Try Again")
                
        print("Thank you for changing your current emotions.\n\n")
        
    def createEmotion(self, emoInfo):
        if self.currEmotions[emoInfo[0]] != 0:
            self.saveEmotion(emoInfo[0], self.currEmotions[emoInfo[0]])

        self.currEmotions[emoInfo[0]] = (datetime.now(), emoInfo[1])

    def saveEmotion(self, index, startTimeIntensity):
        self.currEmotions[index] = 0
        tempTime = datetime.now()
        timeDelta = (tempTime - startTimeIntensity[0])
        time = timeDelta.seconds/60
        score = time*startTimeIntensity[1]
        self.emotionObjs[index].totalTime += time
        self.emotionObjs[index].vybeScore += score

    def saveAllCurrEmo(self):
        for i in range (len(self.currEmotions)):
            if(self.currEmotions[i] != 0):
                self.saveEmotion(i, self.currEmotions[i])

    def wipeAllCurrEmo(self):
        for i in range(len(self.currEmotions)):
            if(self.currEmotions[i] != 0):
                temp = self.currEmotions[i]
                self.currEmotions[i] = 0
                midnight = datetime(year=temp[0].year,month=temp[0].month,day=temp[0].day,hour=23,minute=59,second=59)
                timeDiff = midnight - temp[0]
                time = timeDiff.seconds/60
                score = time*temp[1]
                self.emotionObjs[i].totalTime += time
                self.emotionObjs[i].vybeScore += score
    
    def test(self):
        for emo in self.emotionObjs:
            print(emo.name, end = " / ")
            print(emo.totalTime, end = " / ")
            print(emo.vybeScore)

    def info(self):
        infoAr = [self.date]
        for emo in self.emotionObjs:
            infoAr.append(emo.getEmoInfo())
        return infoAr #returns an array where index 0 is the date and all of the following are arrays of style [name, vybeScore, totalTime]

class Week:

    def __init__(self):
        self.weekQ = [None,None,None,None,None,None,None]

    def addDay(self):
        #use this to add a new current day (only a current day) to the week
        for i in range(6, 0, -1):
            self.weekQ[i] = self.weekQ[i-1]
        self.weekQ[0] = Day()

    def getInfo(self):
        rtrAr = []
        for day in self.weekQ:
            if (day != None):
                rtrAr.append(day.info())
        return rtrAr #returns an array of the day.info()s explained above

class PickleHelper:
    def __init__(self):
        message = "hello, am alive"
    def pickleWeek(self, wk):
        #takes in a week obj and saves it in 'storedWeek.bin'
        pickleFile = open('storedWeek', 'wb') 
        pickle.Pickler(pickleFile).dump(wk)
        pickleFile.close()

    def unpickleWeek(self):
        #returns the week obj stored in 'storedWeek.bin'
        dbfile = open('storedWeek', 'rb')      
        return pickle.load(dbfile)
