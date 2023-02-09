from Constants import *
from UtilityFunctions import ValidateUserInput

class Entry_Creator():
    
    _currentSelectedEntry: str = None

    def CreateNewProgressEntry(self, progressEntries: dict) -> None:
        '''Prompts the user to provide the info needed to create a new progress entry'''        
        entryName = input("What's the name of the new progress entry?\n")

        if (entryName in progressEntries):
            print("Error: A progress entry with that name already exists")
            return

        entryFormat = ValidateUserInput("What's the format of the new progress entry? (decimal/currency)\n", ["decimal", "currency"])
        entryCumulative = ValidateUserInput("Is the new entry cumulative? (yes/no)\n", ["yes", "no"])
        entryTimeFrame = ValidateUserInput("What's the timeframe of the new progress entry? (daily/weekly/bi-weekly/monthly/yearly)\n", 
                                                 ["daily", "weekly", "bi-weekly", "monthly", "yearly"])

        progressEntries[entryName] = {FORMAT_KEY: entryFormat, CUMULATIVE_KEY: entryCumulative, TIME_FRAME_KEY: entryTimeFrame, RECORDS_KEY: []}

    def DeleteProgressEntry(self, progressEntries: dict) -> None:
        '''Deletes the desired progress entry'''
        entryName = input("What's the name of the progress entry you wish to delete?\n")
        
        if (entryName not in progressEntries):
            print("Error: The typed progress entry doesn't exist")
            return
        
        progressEntries.pop(entryName)

    def SetActiveProgressEntry(self) -> None:
        '''Sets the currently active progress entry'''
        self._currentSelectedEntry = input("What's the name of the progress entry you wish to set as active?\n")

    def DisplayActiveProgressEntry(self) -> str:
        '''Returns an string with the currently active progress entry'''
        if (self._currentSelectedEntry is not None):
            return f"The currently active progress entry is: {self._currentSelectedEntry}"
    
    def AddNewRecord(self, progressEntries: dict) -> None:
        '''Adds a new record to the record collection of the currently active progress entry'''
        anotherRecord = True
        userAnswer = None

        entryName = input("What's the name of the progress entry you wish to add a record to?\n")

        if (entryName not in progressEntries):
            print("Error: The typed progress entry doesn't exist")
            return

        while(anotherRecord):
            newRecord = input("What's the value of the new record?\n")
            progressEntries[entryName][RECORDS_KEY].append(newRecord)
            
            userAnswer = ValidateUserInput("Do you want to add another record? (y/n)\n", ["y", "n"])
            
            if (userAnswer.lower() == "n"):
                anotherRecord = False
