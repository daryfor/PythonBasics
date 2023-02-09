# Mean
list1 = [12,16,20,20,12,30,25,23,24,20]
mean = sum(list1)/len(list1)
print('MEAN: ',mean)

# Median (using the same list)
list1.sort()

if len(list1) % 2 == 0 :
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2
else :
    median = list1[len(list1)//2]

print('MEDIAN: ',median)

# Mode (using the same list)
frequency = {}

for i in list1 :
    print(i)
    frequency.setdefault(i,0)
    print(frequency)
    frequency[i] += 1

print(frequency.values())
print(frequency.items())
frequent = max(frequency.values())
print(frequent)
for i,j in frequency.items() :
    if j == frequent :
        mode = i

print('MODE: ',mode)
