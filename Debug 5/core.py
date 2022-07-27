# From a given list, find the two indexes where the numbers add to a given number


def hashadding(numberList:list[int], sumNumber:int):
    hashmap = {}
    for number, index in enumerate(numberList):
        otherNumber = sumNumber - number
        print(otherNumber)
        if otherNumber in hashmap:
            return [hashmap[otherNumber],index]
        else:
            hashmap[number] = index

def looping(numberList:list[int], sumNumber:int):
    for i in range(len(numberList)):
        for j in range(i, len(numberList)):
            if i != j and numberList[i] + numberList[j] == sumNumber:
                return [i, j]
                

listOne = [*list(range(1, 25)), 25]
goalOne = 49

listTwo = [3, 89, 2, 4]
goalTwo = 6

listThree = [8, *[int(i) for i in list( '123' * (9 ** 5))], 123, [int(i) for i in list( '123' * (9 ** 5))]]
goalThree = 131

listFour = [9, 8, 7, 6, 5, 10, 11, 12, 13, 14, 15, 16, 17, 21, 12, 1313]
goalFour = 1334

from datetime import datetime
start = datetime.now()
hashadding(listOne, goalOne)
hashadding(listTwo, goalTwo)
hashadding(listThree, goalThree)
hashadding(listFour, goalFour)
hashtime = datetime.now() - start
start = datetime.now()
looping(listOne, goalOne)
looping(listTwo, goalTwo)
looping(listThree, goalThree)
looping(listFour, goalFour)
looptime = datetime.now() - start
print(start)
print(f'It took {hashtime} seconds to solve the four problems using hashmaps.')
print(f'It took {looptime} seconds to solve the four problems using loops.')