def MissingNumbers(list):
    numbers = set(list)
    #length = len(list)
    output = []

    for i in range(1, list[-1]):
        if i not in numbers:
            output.append(i)
    
    return output

listNumbers = [1,2,3,4,5,6,7,9,11,15]
print(MissingNumbers(listNumbers))