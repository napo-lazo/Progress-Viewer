from File_Manager import File_Manager
from Dependencies.Menu_Plotter.Menu_Plotter import Menu_Plotter

def GenerateMenuStructure() -> Menu_Plotter:
    menu = Menu_Plotter()
    fileManager = File_Manager()

    menu.AddActionNode("Initial Check", ["Main Screen"], fileManager.CheckForFolder)
    menu.AddMenuNode("Main Screen", ["exit"], ["Exit"])
    menu.SetStartNode("Initial Check")

    return menu

if __name__ == "__main__":

    menu = GenerateMenuStructure()
    menu.Start()