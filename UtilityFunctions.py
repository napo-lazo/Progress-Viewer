def ValidateUserInput(message: str, validAnswers: list) -> str:
    '''Validates that the user input fits with any of the elements of the validAnswers list'''
    validAnswersString = ", ".join(validAnswers)

    while (True):
        userInput = input(message)
        if (userInput.lower() in validAnswers):
            break
        else:
            print(f"Error: only ({validAnswersString}) are accepted")

    return userInput.lower()

def DisplayOptions(options: list, excluded: list = None, rowLimit: int = 3) -> None:
    currentRow = 0
    counter = 0
    rowString = ""

    if (options is None or len(options) == 0):
        return

    print("Options:")

    for option in options:
        counter += 1

        if (excluded is None or option not in excluded):
            currentRow += 1
            if (currentRow == 1):
                rowString += f"{option}"
            else:
                rowString += f"\t{option}"
        
        if (currentRow == rowLimit or counter == len(options)):
            print(f"{rowString}\n")
            rowString = ""
            currentRow = 0