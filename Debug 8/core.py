
# A simple program that compares the speed of multiprocessing.pool, for loops, and list comprehensions

def getWord(word):
    if word == 0:
        print("Zero")
    elif word == 1:
        print("One")
    elif word == 2:
        print("Two")
    elif word == 3:
        print("Three")
    elif word == 4:
        print("Four")
    elif word == 5:
        print("Five")
    elif word == 6:
        print("Six")
    elif word == 7:
        print("Seven")
    elif word == 8:
        print("Eight")
    elif word == 9:
        print("Nine")


if __name__ == "__main__":
    from multiprocessing import Pool
    from datetime import datetime

    stopNum = (150 ** 2) * 5
    listOfStuff = list(range(1, stopNum))
    listOfStuff = ''.join(list(listOfStuff))

    start = datetime.now()
    pool = None
    with Pool(pool) as p:
        p.map(getWord, [int(i) for i in listOfStuff])
    poolTime = datetime.now() - start


    start = datetime.now()
    [getWord(int(i)) for i in listOfStuff]
    listTime = datetime.now() - start


    start = datetime.now()
    for i in listOfStuff:
        getWord(i)
    loopTime = datetime.now() - start

    print(poolTime)
    print(loopTime)
    print(listTime)