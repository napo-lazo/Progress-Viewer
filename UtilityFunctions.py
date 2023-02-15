def ValidateUserInput(message: str, validAnswers: list):
        
        validAnswersString = ", ".join(validAnswers)

        while (True):
            userInput = input(message)
            if (userInput.lower() in validAnswers):
                break
            else:
                print(f"Error: only ({validAnswersString}) are accepted")

        return userInput.lower()