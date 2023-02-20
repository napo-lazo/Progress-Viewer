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

    def DisplayCurrenylyActiveProgressEntry(self) -> str:
        return self._entryCreator.DisplayActiveProgressEntry()
    
    def AddNewRecord(self):
        self._entryCreator.AddNewRecord()

    def DisplayRecordsList(self):
        entryName = self._entryCreator.GetEntryName()
        
        if (entryName is not None):
            DisplayRecordsList(entryName, GetEntryRecordList(entryName))
