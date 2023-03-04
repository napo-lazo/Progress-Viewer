from Constants import *
from UtilityFunctions import ValidateUserInput, DisplayOptions
from datetime import datetime, timedelta
from File_Manager import *
from Save_Data_Manager import *

class Entry_Creator():
    _progressEntries: dict
    currentSelectedEntry: str = None

    def __init__(self):
        self._progressEntries = LoadDictFromFile(PROGRESS_ENTRIES_FILE)
        CheckForExpiredEntries(self._progressEntries)

    def CheckIfEntryExists(self, entryName: str) -> bool:
        '''Checks if an entry with that name exists in the entry dictionary'''
        if (entryName in self._progressEntries):
            return True
        
        return False

    def isCumulative(self, entryName: str) -> bool:
        '''Checks if the entry is cumulative'''
        return self._progressEntries[entryName][CUMULATIVE_KEY] == 'yes'

    def GetEntryName(self) -> str:
        '''Trys to get an entry name from the entries dictionary, if it can't find it a None value will be returned'''
        DisplayOptions(list(self._progressEntries.keys()))
        
        entryName = input("What's the name of the progress entry?\n")

        if (self.CheckIfEntryExists(entryName)):
            return entryName
        else:
            print("Error: The typed progress entry doesn't exist")
            return None


    def CreateNewProgressEntry(self) -> None:
        '''Prompts the user to provide the info needed to create a new progress entry'''        
        entryName = input("What's the name of the new progress entry?\n")

        if (self.CheckIfEntryExists(entryName)):
            print("Error: A progress entry with that name already exists")
            return

        entryFormat = ValidateUserInput("What's the format of the new progress entry? (decimal/currency)\n", ["decimal", "currency"])
        entryCumulative = ValidateUserInput("Is the new entry cumulative? (yes/no)\n", ["yes", "no"])
        entryTimeFrame = ValidateUserInput("What's the timeframe of the new progress entry? (daily/weekly/bi-weekly/monthly/yearly)\n", 
                                                 ["daily", "weekly", "bi-weekly", "monthly", "yearly"])
        
        self._progressEntries[entryName] = {FORMAT_KEY: entryFormat, 
                                      CUMULATIVE_KEY: entryCumulative, 
                                      TIME_FRAME_KEY: entryTimeFrame, 
                                      LAST_UPDATE_DATE: datetime.now().strftime(DATE_TIME_FORMAT), 
                                      RECORDS_KEY: []}
        
        SaveDictToFile(self._progressEntries, PROGRESS_ENTRIES_FILE)

    def DeleteProgressEntry(self) -> None:
        '''Deletes the desired progress entry'''
        entryName = self.GetEntryName()
        
        if (entryName is None):
            return
        
        self._progressEntries.pop(entryName)
        SaveDictToFile(self._progressEntries, PROGRESS_ENTRIES_FILE)

    def SetActiveProgressEntry(self) -> None:
        '''Sets the currently active progress entry'''
        self.currentSelectedEntry = self.GetEntryName()
    
    def AddNewRecord(self) -> None:
        '''Adds a new record to the record collection of the currently active progress entry'''
        anotherRecord = True
        userAnswer = None

        entryName = self.GetEntryName()

        if (entryName is None):
            return

        while(anotherRecord):
            newRecord = input("What's the value of the new record?\n")
        
            try:
                newRecordAsNumber = float(newRecord)
                self._progressEntries[entryName][RECORDS_KEY].append(newRecordAsNumber)
            except ValueError:
                print("ERROR: The new record is not a number")
                continue

            userAnswer = ValidateUserInput("Do you want to add another record? (y/n)\n", ["y", "n"])
            
            if (userAnswer.lower() == "n"):
                anotherRecord = False

        SaveDictToFile(self._progressEntries, PROGRESS_ENTRIES_FILE)

