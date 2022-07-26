# Broken Ook Interpreter
# Good luck

cells = [0]
pointer = 0
loopStarts = []
inputIter = None

def validateCell(place:int, array:list):
    '''
    Checks to ensure that the current array of memory cells contains the pointer value

    Parameters
    ------
    ``place`` : int
        The memory cell to verify the existance of
    ``array`` : list
        The list of memory cells

    Returns
    ------
    Bool value for testing and troubleshooting

    ``True`` if a new cell was created
    ``False`` if no new cell needed to be created
    '''
    if len(array) < place:
        array.append(0)
        return True
    return False
    

def currentPointer():
    '''
    Returns the current location of the pointer for the memory array
    '''
    global pointer
    return pointer

def getCells():
    '''
    Returns the current list of memory cells
    '''
    global cells
    return cells

def changeCellValue(amount:int, place:int, array:list):
    '''
    Changes the value of the cell at ``place`` by ``amount``

    Parameters
    ------

    ``amount`` : int
        The amount to add or remove from the memory cell
    ``place`` : int
        The memory cell to modify
    ``array`` : list
        The list of memory cells
    '''
    validateCell(place=place, array=array)
    array[place] += amount

def movePointer(amount:int, set=False):
    '''
    Moves the pointer by, or sets to the value of ``amount``

    Parameters
    ------
    ``amount`` : int
        The amount to modify the value by
    ``set`` : bool
        if true the value of the pointer is set directly to ``amount``
        if false the value of the pointer is just incremented by ``amount``
    '''

    global pointer
    if set:
        pointer = amount
    else:
        pointer += amount

def getCellValue(place:int, array:list):
    validateCell(place=place, array=array)
    return array[place]

def outputCell(place:int, array:list):
    value = getCellValue(place, array)
    print(chr(value), end="")

def inputCell(place:int, array:list):
    global inputIter
    try:
        strValue = next(inputIter)
        uniValue = ord(strValue)
        array[place] = uniValue
    except StopIteration:
        print("End of Iter")

def debug():
    print(currentPointer())
    print(getCells()[:10])

def parseChar(character:str):
    match character:
        case '+':
            changeCellValue(1, currentPointer(), getCells())
        case '-': 
            changeCellValue(-1, currentPointer(), getCells())
        case '>': 
            movePointer(1)
        case '<':
            movePointer(-1)
        case '[':
            return 'start'
        case ']': 
            return 'stop'
        case '.': 
            outputCell(currentPointer(), getCells())
        case ',':
            inputCell(currentPointer(), getCells())
        case '#':
            debug()
    return 'good'

def skipLoop(commands:str, startList:list):
    for i in range(len(commands)):
        state = parseChar(commands[i])
        if state == 'start':
            startList.append(i)
        elif state == 'stop':
            return int(i + 1)
    return 0

def parseBrain(brainText:str):
    global loopStarts
    skipTo = 0
    i = 0
    while i < len(brainText):
        if i < skipTo:
            i += 1
            continue

        if brainText[i] not in ['+', '-', '>', '<', '[', ']', '.', ',', '#']:
            i += 1
            continue

        state = parseChar(brainText[i])
        if state == 'good':
            i += 1
            continue
        elif state == 'start':
            loopStarts.append(i)
            value = getCellValue(currentPointer(), getCells())

            if value == 0:
                i = skipLoop(brainText[i:], loopStarts)
            else:
                i += 1
                continue

        elif state == 'stop':
            value = getCellValue(currentPointer(), getCells())
            if value == 0:
                i += 1
                loopStarts.pop()
                continue
            else:
                i = loopStarts.pop()


def getArguments(args:str):
    import argparse
    parser = argparse.ArgumentParser(description='A terrible Ook Interpreter')
    parser.add_argument('File', type=open, help='The file to interpret.')
    return parser.parse_args(args)

def checkInput(text:str):
    return ',' in text

def parseOok(text:str):
    ookLine = ''.join((''.join(text.split('Ook'))).split())
    ookArray = []
    for i in range(len(ookLine)):
        if i % 2 == 0:
            ookArray.append(ookLine[i])
        else:
            place = i // 2
            ookArray[place] += ookLine[i]

    ookBrain = ''
    for i in ookArray:
        match i:
            case '.?':
                ookBrain += '>'
            case '?.':
                ookBrain += '<'
            case '..':
                ookBrain += '+'
            case '!!':
                ookBrain += '-'
            case '!.':
                ookBrain += '.'
            case '.!':
                ookBrain += ','
            case '!?':
                ookBrain += '['
            case '?!':
                ookBrain += ']'
            case '??':
                ookBrain += '#'
    return ookBrain

def main(arguments):
    parsedArgs = getArguments(arguments)
    bText = ''
    with parsedArgs.File as f:
        for line in f:
            bText += line
    if checkInput(bText):
        global inputIter
        userIn = input("Enter the required input: ")
        inputIter = iter(userIn)

    bText = parseOok(bText)
    parseBrain(bText)
    print()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1:]))
