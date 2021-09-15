def say_hello(name):
    print(name)


say_hello('dimi')



def say_hi(naam, age=None):
    if age is not None:
        return naam, age
    return naam

print(say_hi('jessy'))
print(say_hi('jessy', 45))
# print(list(say_hi('abc', 123)) to return a list (of just return [naam, age] al line 11


def say_hi2(naam, age2=None):
    if age2 is not None:
        return [naam, age2]
    return naam

mylist = say_hi2('abc', 123)
print(mylist[0])


def cutsttring(mystring):
    return mystring[0:3]
print(cutsttring('mijntest'))