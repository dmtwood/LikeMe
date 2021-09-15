myList = [10, 20, 30, 40, 50, 60]

values = enumerate(myList)
for values in enumerate(myList):
    print(values[0], values[1])

# or

for id, val in enumerate(l):
    print(id, val)


myDict = {
    "keyword": 10,
    "name": "myName"
}