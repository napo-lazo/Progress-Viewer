import os
from json import load, dumps
from Constants import BASE_FOLDER, SAVE_DATA_FOLDER

def CheckForFolder() -> None:
    '''Checks if the folder that holds the required files exists where the script was run from, if not creates a new one'''
    if (not os.path.exists(BASE_FOLDER)):
        os.mkdir(BASE_FOLDER)
        os.mkdir(f"{BASE_FOLDER}/{SAVE_DATA_FOLDER}")
        
def LoadDictFromFile(fileName: str) -> dict:
    '''Checks if the file already exists and loads it into a dictionary, else it creates a new file and dictionary'''
    if (not os.path.exists(f"{BASE_FOLDER}/{fileName}")):
        baseJsonDictionary = {}
        SaveDictToFile(baseJsonDictionary, fileName)

        return baseJsonDictionary
    else:
        with open(f"{BASE_FOLDER}/{fileName}", "r") as jsonFile:
            return load(jsonFile)
        
def SaveDictToFile(dictToSave: dict, fileName: str) -> None:
    '''Saves the dictionary into the file'''
    with open(f"{BASE_FOLDER}/{fileName}", "w") as jsonFile:
            serializedDictionary = dumps(dictToSave, indent=2)
            jsonFile.write(serializedDictionary)
