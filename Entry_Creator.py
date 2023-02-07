class Entry_Creator():
    
    _currentSelectedEntry: str = None

    #TODO: Add input validation
    def CreateNewProgressEntry(self, progressEntries: dict) -> None:
        '''Prompts the user to provide the info needed to create a new progress entry'''        
        entryName = input("What's the name of the new progress entry?\n")
        entryFormat = input("What's the format of the new progress entry?\n")
        entryCumulative = input("Is the new entry cumulative?\n")
        entryTimeFrame = input("What's the timeframe of the new progress entry?\n")

        progressEntries[entryName] = {"Format": entryFormat, "Cumulative": entryCumulative, "TimeFrame": entryTimeFrame}

    def DeleteProgressEntry(self, progressEntries: dict) -> None:
        '''Deletes the desired progress entry'''
        entryName = input("What's the name of the progress entry you wish to delete?\n")
        progressEntries.pop(entryName)

    def SetActiveProgressEntry(self) -> None:
        '''Sets the currently active progress entry'''
        self._currentSelectedEntry = input("What's the name of the progress entry you wish to set as active?\n")

    def DisplayActiveProgressEntry(self) -> str:
        '''Returns an string with the currently active progress entry'''
        if (self._currentSelectedEntry is not None):
            return f"The currently active progress entry is: {self._currentSelectedEntry}"