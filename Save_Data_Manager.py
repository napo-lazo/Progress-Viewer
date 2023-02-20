from Constants import *
from datetime import datetime, timedelta
from File_Manager import LoadDictFromFile, SaveDictToFile

def HasTimeFrameElapsed(entryDate: datetime, timeFrame: str) -> bool:
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

        entryDate += timedelta(days=days)

        return currentDate >= entryDate

def ParseSaveFileName(entryName: str) -> str:
    saveFileName = SAVE_DATA_FILE.replace("{entryName}", entryName.replace(" ", "_"))
    return f"{SAVE_DATA_FOLDER}/{saveFileName}"

def CheckForExpiredEntries(progressEntries: dict) -> None:
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
            entry[LAST_UPDATE_DATE] = datetime.now().strftime(DATE_TIME_FORMAT)
            saveData[RECORD_LIST].append({START_DATE: entryDate.strftime(DATE_TIME_FORMAT), RECORDS_KEY: recentRecords})

            SaveDictToFile(saveData, ParseSaveFileName(entryName))
    
    if (changesMade):
        SaveDictToFile(progressEntries, PROGRESS_ENTRIES_FILE)

def GetEntryRecordList(entryName: str) -> list:
    saveData = LoadDictFromFile(ParseSaveFileName(entryName))
    return saveData[RECORD_LIST]
            

        
