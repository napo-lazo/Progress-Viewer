import os
from json import load, dumps

class File_Manager():

    def CheckForFolder(self) -> None:
        '''Checks if the folder that holds the required files exists where the script was run from, if not creates a new one'''
        if (not os.path.exists("./Progress_Viewer_Data")):
            os.mkdir("./Progress_Viewer_Data")
            
    def LoadProgressEntries(self) -> dict:
        '''Checks if there the file holding our progress entries exists and loads it into a dictionary, else it creates a new file and dictionary'''
        if (not os.path.exists("./Progress_Viewer_Data/Progress_Entries.json")):
            baseJsonDictionary = {"Entries": []}
            with open("./Progress_Viewer_Data/Progress_Entries.json", "x") as jsonFile:
                serializedDictionary = dumps(baseJsonDictionary, indent=2)
                jsonFile.write(serializedDictionary)

            return baseJsonDictionary
        else:
            with open("./Progress_Viewer_Data/Progress_Entries.json", "r") as jsonFile:
                return load(jsonFile)
