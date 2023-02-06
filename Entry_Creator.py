class Entry_Creator():
    
    #TODO: Add input validation
    def CreateNewProgressEntry(self, progressEntries: dict) -> None:
        '''Prompts the user to provide the info needed to create a new progress entry'''
        entryName = input("What's the name of the new progress entry?\n")
        entryFormat = input("What's the format of the new progress entry?\n")
        entryCumulative = input("Is the new entry cumulative?\n")
        entryTimeFrame = input("What's the timeframe of the new progress entry?\n")

        newEntry = {"Name": entryName, "Format": entryFormat, "Cumulative": entryCumulative, "TimeFrame": entryTimeFrame}
        progressEntries["Entries"].append(newEntry)
