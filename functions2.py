def times2(x):
    try:
       return int(x*2)
    except ValueError as error:
        print(str(x) + ' is no valid number')


print(times2(2))

print(times2('abc'))