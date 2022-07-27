# Fix the code below to capitalize the first letter of each word passed through user input. Ex: Artifical Intelligence - (AI)

def main():
    # First thing we need to do is capture the user input
    userInput = input('Enter your sentence: ')

    # We then split that input into a list
    inputList = userInput.split()
    
    # Then we return the first letter of each word as a capital letter
    return inputList

if __name__ in '__main__':
    acronym = main()
    acronym= [i.title() for i in acronym]
    print(acronym)
    
    