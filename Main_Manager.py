from Entry_Creator import Entry_Creator
from File_Manager import CheckForFolder

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