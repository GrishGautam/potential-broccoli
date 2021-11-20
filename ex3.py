numbers = [10,20,30, 40,60,80, 50,60]
uniques = []

for number in numbers:
    print (number)
    if number not in uniques:
        
        uniques.append(number)
print(uniques)
        