import sys

from datetime import datetime

from DayAndEmotion import Day
from DayAndEmotion import Week
from DayAndEmotion import Emotion
from DayAndEmotion import PickleHelper

from infoHelper import InfoHelper

"""
Object oriented concepts used:
- Classes
- Objects
"""
ph = PickleHelper()
ih = InfoHelper()

def main():
    try:
        week = openStoredWeek()
        checkCurrDay(week)

        check = True
        while (check):
            __print_menu__()
            user_input = input().strip()
            if user_input == '1':
                print("Option 1 Selected...\n")
                week.weekQ[0].changeEmotions()
                
            elif user_input == '2':
                print("Option 2 Selected...\n")
                print("Here is your emotion report for the last 7 days:")
                week.weekQ[0].saveAllCurrEmo()
                ih.weekFreq(week)
                ih.weekVolatility(week) 
                week.weekQ[0].changeEmotions()

            elif user_input == '3':
                print("Option 3 Selected...\n")
                print("Here are your emotion records for today: ")
                week.weekQ[0].saveAllCurrEmo()
                ih.dayFreq(week.weekQ[0])
                week.weekQ[0].changeEmotions()

            elif user_input == '4':
                print("Closing Program...")
                ph.pickleWeek(week)
                check = False
            else:
                print("Invalid input. Please enter a number from 1 to 4\n")
        
        print("Thank you for using Vybe today! \n-From the Vybe Team\n")
    except:
        print("Program crashed. Saving data...\n")
        ph.pickleWeek(week)

def openStoredWeek():
    try:
        week = ph.unpickleWeek()
        return week
    except:
        print("Could not find the storage file: Creating a new one...")
        newWeek = Week()
        newWeek.addDay()
        return newWeek

def checkCurrDay(week):
    temp = datetime.now() 
    currDate = temp.strftime("%d/%m/%Y")
    if (week.weekQ[0].date != currDate):
        print("Thanks for starting a new day with Vybe...\n")
        week.weekQ[0].wipeAllCurrEmo()
        logDelta = temp - week.weekQ[0].timeDelta
        week.addDay()
        for i in range(logDelta.days):
            week.addDay()

def __print_menu__():
    print("Welcome to Vybe!\nChoose an option by entering a number from the menu below:")
    print("1. Change your current emotions")
    print("2. Get a report on the last 7 days")
    print("3. Show the emotion records for today")
    print("4. Close the program")


if __name__ == "__main__":
    main()