from Entry_Creator import Entry_Creator
from File_Manager import CheckForFolder
from Display_Handler import *
from Save_Data_Manager import GetEntryRecordList

class Main_Manager():
    _entryCreator: Entry_Creator

    def InitialCheck(self) -> None:
        CheckForFolder()
        self._entryCreator = Entry_Creator()

    def CreateNewProgressEntry(self) -> None:
        self._entryCreator.CreateNewProgressEntry()

    def DeleteProgressEntry(self) -> None:
        self._entryCreator.DeleteProgressEntry()

    def SetActiveProgressEntry(self) -> None:
        self._entryCreator.SetActiveProgressEntry()
    
    def AddNewRecord(self) -> None:
        self._entryCreator.AddNewRecord()

    def CheckIfCumulative(self) -> int:
        if (self._entryCreator.currentSelectedEntry is None):
            return 2
        
        return self._entryCreator.isCumulative(self._entryCreator.currentSelectedEntry)

    def DisplayRecordsList(self) -> None:
        entryName = self._entryCreator.currentSelectedEntry
        self._entryCreator.currentSelectedEntry = None

        if (entryName is not None):
            DisplayRecordsList(entryName, GetEntryRecordList(entryName), asCumulative=False)
    
    def DisplayRecordsListCumulative(self) -> None:
        entryName = self._entryCreator.currentSelectedEntry
        self._entryCreator.currentSelectedEntry = None
        
        if (entryName is not None):
            DisplayRecordsList(entryName, GetEntryRecordList(entryName), asCumulative=True)
