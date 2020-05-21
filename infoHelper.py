import numpy as np

"""
Date: 5/8/20
Author: Tatiana Barbone
Object oriented concepts used:
- Objects
- Classes
"""
class InfoHelper:
    def __init__(self):
        on = 1

    def dayFreq(self, currDay):
        """
        Gets emotions felt throughout the day along with their respective frequencies

        Args:
            string: curDate: day to get emotions from
        Returns:
            list of ints: emotionsList
        """
        dayInfo = currDay.info()
        totalTime = [0,0,0,0,0,0,0]
        avVybeScore = [0,0,0,0,0,0,0]
        indexes = ['Sad', 'Happy', 'Stressed', 'Angry', 'Confused', 'Tired', 'Excited']

        
        for i in range(1, len(dayInfo)):
                
                totalTime[i-1] += dayInfo[i][2]
                avVybeScore[i-1] += dayInfo[i][1]

        print("Your emotional frequency for the emotion: ")
        for i in range(len(indexes)):
            print(str(indexes[i]) + " = " + str(int(totalTime[i])) + " minutes.")

        print("\nYour vybeScore for the emotion: ")
        for j in range(len(indexes)):
            print(str(indexes[j]) + " = " + str(int(avVybeScore[j])))

    def weekFreq(self, currWeek):
        """
        Gets emotions felt throughout the week along with their respective frequencies
        
        Args:
            list: curWeek: Week array
        Returns:
            list of lists of ints: week_freq

        """
        indexes = ['Sad', 'Happy', 'Stressed', 'Angry', 'Confused', 'Tired', 'Excited']
        totalTime = [0,0,0,0,0,0,0]
        avVybeScore = [0,0,0,0,0,0,0]
        weekInfo = currWeek.getInfo()
        for day in weekInfo:
        # access each day in 
        # get VybeScore for each day
            #sum each vybescore for all emotions
            for i in range(1, 8):
                
                totalTime[i-1] += day[i][2]
                avVybeScore[i-1] += day[i][1]

        print("Your emotional frequency for the emotion: " )
        for i in range(len(indexes)):
            print(str(indexes[i]) + " = " + str(int(totalTime[i])) + " minutes.")
        
        print("\nYour average vybeScore for the emotion: ")
        for j in range(len(indexes)):
            print(str(indexes[j]) + " = " + str(int(avVybeScore[j]/7)))



    def weekVolatility(self, week):
        """
        Informs the user whether their week was volatile or not
        
        get the variance of the individual day vybescores
        """
        totalVybes = 0
        weekInfo = week.getInfo()
        dailyVybes = []
        for day in weekInfo:
        # access each day in 
        # get VybeScore for each day
            #sum each vybescore for all emotions
            for i in range(1, 8):
                
                totalVybes += day[i][1]
                
            dailyVybes.append(totalVybes)

        print("Your emotional volatility for the week was: " + str(np.var(dailyVybes)))

        # If you had at least 4/7 volatile days, your week is considered volatile.
    

