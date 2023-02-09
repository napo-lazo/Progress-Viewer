from Main_Manager import Main_Manager
from Dependencies.Menu_Plotter.Menu_Plotter import Menu_Plotter

def GenerateMenuStructure() -> Menu_Plotter:
    menu = Menu_Plotter()
    mainManager = Main_Manager()

    menu.AddActionNode("Initial Check", ["Main Screen"], mainManager.InitialCheck)
    menu.AddActionNode("Create New Progress Entry", ["Main Screen"], mainManager.CreateNewProgressEntry)
    menu.AddActionNode("Add New Record", ["Main Screen"], mainManager.AddNewRecord)
    menu.AddActionNode("Delete Progress Entry", ["Main Screen"], mainManager.DeleteProgressEntry)

    menu.AddMenuNode("Main Screen", 
                     ["Create New Progress Entry", "Add New Record", "Delete Progress Entry", "exit"], 
                     ["Create New Progress Entry", "Add New Record", "Delete Progress Entry", "Exit"])
    
    menu.SetStartNode("Initial Check")

    return menu

if __name__ == "__main__":

    menu = GenerateMenuStructure()
    menu.Start()