# Invert the dictionaries below so that the keys are values are swapped. EX: d1 = {1: 'a', 2: 'b', 3: 'c'}

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'name': 'Zach', 'color': 'red', 'age': 22}
d3 = {'reptile': 'lizard', 'mammal': 'dog', 'aquatic': 'fish'}

# print (d1,d2, d3)

def main():
    inv1 = d1
    inv2 = d2
    inv3 = d3
    print(inv1, inv2, inv3)
    
def invert(dictionary):
    temp = {}
    for keys in dictionary:
        temp[keys[dictionary]] += keys
    return temp

if __name__ in '__main__':
    main()
    