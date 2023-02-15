from Constants import *
from UtilityFunctions import ValidateUserInput
from datetime import datetime, timedelta
from File_Manager import *

class Entry_Creator():
    
    _progressEntries: dict
    _currentSelectedEntry: str = None

    def __init__(self):
        self._progressEntries = LoadProgressEntries()

    def _CalculateNextTimeFrameDate(self, timeFrame: str) -> str:
        currentDate = datetime.now()
        days = 0

        if (timeFrame == "daily"):
            days = 1
        elif (timeFrame == "weekly"):
            days = 7
        elif (timeFrame == "bi-weekly"):
            days = 14
        elif (timeFrame == "monthly"):
            days = 30
        elif (timeFrame == "yearly"):
            days = 365

        currentDate += timedelta(days=days)

        return currentDate.strftime("%d/%b/%Y")

    def CreateNewProgressEntry(self) -> None:
        '''Prompts the user to provide the info needed to create a new progress entry'''        
        entryName = input("What's the name of the new progress entry?\n")

        if (entryName in self._progressEntries):
            print("Error: A progress entry with that name already exists")
            return

        entryFormat = ValidateUserInput("What's the format of the new progress entry? (decimal/currency)\n", ["decimal", "currency"])
        entryCumulative = ValidateUserInput("Is the new entry cumulative? (yes/no)\n", ["yes", "no"])
        entryTimeFrame = ValidateUserInput("What's the timeframe of the new progress entry? (daily/weekly/bi-weekly/monthly/yearly)\n", 
                                                 ["daily", "weekly", "bi-weekly", "monthly", "yearly"])



        self._progressEntries[entryName] = {FORMAT_KEY: entryFormat, 
                                      CUMULATIVE_KEY: entryCumulative, 
                                      TIME_FRAME_KEY: entryTimeFrame, 
                                      NEXT_TIME_FRAME_DATE_KEY: self._CalculateNextTimeFrameDate(entryTimeFrame), 
                                      RECORDS_KEY: []}
        
        SaveProgressEntries(self._progressEntries)

    def DeleteProgressEntry(self) -> None:
        '''Deletes the desired progress entry'''
        entryName = input("What's the name of the progress entry you wish to delete?\n")
        
        if (entryName not in self._progressEntries):
            print("Error: The typed progress entry doesn't exist")
            return
        
        self._progressEntries.pop(entryName)
        SaveProgressEntries(self._progressEntries)

    def SetActiveProgressEntry(self) -> None:
        '''Sets the currently active progress entry'''
        self._currentSelectedEntry = input("What's the name of the progress entry you wish to set as active?\n")

    def DisplayActiveProgressEntry(self) -> str:
        '''Returns an string with the currently active progress entry'''
        if (self._currentSelectedEntry is not None):
            return f"The currently active progress entry is: {self._currentSelectedEntry}"
    
    def AddNewRecord(self) -> None:
        '''Adds a new record to the record collection of the currently active progress entry'''
        anotherRecord = True
        userAnswer = None

        entryName = input("What's the name of the progress entry you wish to add a record to?\n")

        if (entryName not in self._progressEntries):
            print("Error: The typed progress entry doesn't exist")
            return

        while(anotherRecord):
            newRecord = input("What's the value of the new record?\n")
            self._progressEntries[entryName][RECORDS_KEY].append(newRecord)
            
            userAnswer = ValidateUserInput("Do you want to add another record? (y/n)\n", ["y", "n"])
            
            if (userAnswer.lower() == "n"):
                anotherRecord = False

        SaveProgressEntries(self._progressEntries)

