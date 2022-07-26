# Invert the dictionaries below so that the keys are values are swapped. EX: d1 = {1: 'a', 2: 'b', 3: 'c'}

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'name': 'Zach', 'color': 'red', 'age': 22}
d3 = {'reptile': 'lizard', 'mammal': 'dog', 'aquatic': 'fish'}

def invert(dictionary):
    temp = {}
    for keys in dictionary:
        temp[keys[dictionary]] += keys
    return temp

def main():
    inv1 = invert(d1)
    inv2 = invert(d2)
    inv3 = invert(d3)
    print(inv1, inv2, inv3)

if __name__ in '__main__':
    main()