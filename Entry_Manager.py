from File_Manager import File_Manager

class Entry_Manager():
    _fileManager: File_Manager
    _entriesDictionary: dict

    def __init__(self) -> None:
        self.fileManager = File_Manager()

    def InitialCheck(self):
        self.fileManager.CheckForFolder()
        self.entriesDictionary = self.fileManager.LoadProgressEntries()