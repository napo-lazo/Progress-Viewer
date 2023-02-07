from File_Manager import File_Manager
from Entry_Creator import Entry_Creator

class Main_Manager():
    _fileManager: File_Manager
    _entryCreator: Entry_Creator
    _entriesDictionary: dict

    def __init__(self) -> None:
        self._fileManager = File_Manager()
        self._entryCreator = Entry_Creator()

    def InitialCheck(self) -> None:
        self._fileManager.CheckForFolder()
        self._entriesDictionary = self._fileManager.LoadProgressEntries()

    def CreateNewProgressEntry(self) -> None:
        self._entryCreator.CreateNewProgressEntry(self._entriesDictionary)
        self._fileManager.SaveProgressEntries(self._entriesDictionary)

    def DeleteProgressEntry(self) -> None:
        self._entryCreator.DeleteProgressEntry(self._entriesDictionary)
        self._fileManager.SaveProgressEntries(self._entriesDictionary)

    def SetActiveProgressEntry(self) -> None:
        self._entryCreator.SetActiveProgressEntry()

    def DisplayCurrenylyActiveProgressEntry(self) -> str:
        return self._entryCreator.DisplayActiveProgressEntry()