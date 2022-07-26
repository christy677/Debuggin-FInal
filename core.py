# From the list below, convert all negative numbers into positive numbers and add them into a new array.

data = [-18, 5, 913, -83, -1, 8, -94]
newData = []
for x in data:
    if '-' in str(x):
        n = x.replace('-')
        newData.append(int(n))
    else:
        newData.append('-')
print(newData)