from Main_Manager import Main_Manager
from Dependencies.Menu_Plotter.Menu_Plotter import Menu_Plotter

def GenerateMenuStructure() -> Menu_Plotter:
    menu = Menu_Plotter()
    mainManager = Main_Manager()

    menu.AddActionNode("Initial Check", ["Main Screen"], mainManager.InitialCheck)
    menu.AddActionNode("Create New Progress Entry", ["Main Screen"], mainManager.CreateNewProgressEntry)
    menu.AddActionNode("Add New Record", ["Main Screen"], mainManager.AddNewRecord)
    menu.AddActionNode("Delete Progress Entry", ["Main Screen"], mainManager.DeleteProgressEntry)
    menu.AddActionNode("Check If Cumulative", ["Display Records", "Display Record Options", "Main Screen"], mainManager.SetActiveProgressEntry, mainManager.CheckIfCumulative)
    menu.AddActionNode("Display Records", ["Main Screen"], mainManager.DisplayRecordsList)
    menu.AddActionNode("Display Records Cumulative", ["Main Screen"], mainManager.DisplayRecordsListCumulative)

    menu.AddMenuNode("Main Screen", 
                     ["Create New Progress Entry", "Add New Record", "Delete Progress Entry", "Check If Cumulative", "exit"], 
                     ["Create New Progress Entry", "Add New Record", "Delete Progress Entry", "Display Records", "Exit"])
    menu.AddMenuNode("Display Record Options",
                    ["Display Records", "Display Records Cumulative", "Main Screen"],
                    ["Display Normally", "Display As Cumualtive", "Back"])

    menu.SetStartNode("Initial Check")

    return menu

if __name__ == "__main__":

    menu = GenerateMenuStructure()
    menu.Start()