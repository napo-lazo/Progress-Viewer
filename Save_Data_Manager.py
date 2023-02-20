from Constants import *
from datetime import datetime, timedelta
from File_Manager import LoadDictFromFile, SaveDictToFile

def TimeFrameSwitch(timeFrame: str) -> int:
    '''Switch used to convert the time frame string into its equivalent number'''
    if (timeFrame == "daily"):
        return 1
    elif (timeFrame == "weekly"):
        return 7
    elif (timeFrame == "bi-weekly"):
        return 14
    elif (timeFrame == "monthly"):
        return 30
    elif (timeFrame == "yearly"):
        return 365 

def HasTimeFrameElapsed(entryDate: datetime, timeFrame: str) -> bool:
    '''Checks if the time frame for a specific entry date has transcurred'''
    currentDate = datetime.now()
    days = TimeFrameSwitch(timeFrame)
    entryDate += timedelta(days=days)

    return currentDate >= entryDate

def CalculateNextStartPeriod(entryDate: datetime, timeFrame: str) -> str:
    '''Calculates the next valid time frame for the provided entry date'''
    currentDate = datetime.now()
    days = TimeFrameSwitch(timeFrame)

    previousFrame = entryDate + timedelta(days=days)
    nextFrame = previousFrame + timedelta(days=days)

    while not previousFrame <= currentDate and currentDate < nextFrame:
        previousFrame = entryDate + timedelta(days=days)
        nextFrame = previousFrame + timedelta(days=days)
    
    return previousFrame.strftime(DATE_TIME_FORMAT)

def ParseSaveFileName(entryName: str) -> str:
    '''Parses the file name into the constant used for the file name'''
    saveFileName = SAVE_DATA_FILE.replace("{entryName}", entryName.replace(" ", "_"))
    return f"{SAVE_DATA_FOLDER}/{saveFileName}"

def CheckForExpiredEntries(progressEntries: dict) -> None:
    '''
    Iterates through the entries dictionary and saves the records into their 
    respective save files if any of them are expired
    '''
    changesMade = False

    for entryName, entry in progressEntries.items():
        entryDate = datetime.strptime(entry[LAST_UPDATE_DATE], DATE_TIME_FORMAT)
        entryTimeFrame = entry[TIME_FRAME_KEY]

        if HasTimeFrameElapsed(entryDate, entryTimeFrame):
            changesMade = True
            saveData = LoadDictFromFile(ParseSaveFileName(entryName))
            
            #Checks if dictionary is empty
            if not saveData:
                saveData[RECORD_LIST] = []
            
            recentRecords = entry[RECORDS_KEY].copy()
            entry[RECORDS_KEY] = []
            entry[LAST_UPDATE_DATE] = CalculateNextStartPeriod(entryDate, entryTimeFrame)
            saveData[RECORD_LIST].append({START_DATE: entryDate.strftime(DATE_TIME_FORMAT), RECORDS_KEY: recentRecords})

            SaveDictToFile(saveData, ParseSaveFileName(entryName))
    
    if (changesMade):
        SaveDictToFile(progressEntries, PROGRESS_ENTRIES_FILE)

def GetEntryRecordList(entryName: str) -> list:
    '''Gets the records list from a specific entry'''
    saveData = LoadDictFromFile(ParseSaveFileName(entryName))
    return saveData[RECORD_LIST]
            

        
