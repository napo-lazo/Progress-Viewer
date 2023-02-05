import os

class File_Manager():

    def CheckForFolder(self) -> None:
        '''Checks if the folder holding our files exists where the script was run from, if not creates a new one'''
        if (not os.path.exists("./Progress_Viewer_Data")):
            os.mkdir('./Progress_Viewer_Data')
