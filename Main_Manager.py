from File_Manager import File_Manager
from Entry_Creator import Entry_Creator

class Main_Manager():
    _fileManager: File_Manager
    _entryCreator: Entry_Creator
    _entriesDictionary: dict

    def __init__(self) -> None:
        self._fileManager = File_Manager()
        self._entryCreator = Entry_Creator()

    def InitialCheck(self):
        self._fileManager.CheckForFolder()
        self._entriesDictionary = self._fileManager.LoadProgressEntries()

    def CreateNewProgressEntry(self):
        self._entryCreator.CreateNewProgressEntry(self._entriesDictionary)
        self._fileManager.SaveProgressEntries(self._entriesDictionary)