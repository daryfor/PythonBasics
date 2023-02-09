from time import time

# Function to format numbers with 'e'
def formatNum(num) :
    n = str(num).split('e')
    if len(n) == 1 :
        return 0
    x = 0 if len(n[0].split('.')) == 1 else len(n[0].split('.')[1])
    return x + abs(int(n[1]))
####### End of program #############

start = time()
print(start)

# Python program to create acronyms
text = "Artificial Intelligence"
words = text.split()
a = " "

for i in words :
    a = a+str(i[0]).upper()
print(a)
####### End of program #############


end = time()
print(end)
exec_time = end - start
# Time in seconds without format
print("Execution Time: ",exec_time)
# Time in seconds with format 
print("Execution Time: ", '{num:.{formatNum}f}'.format(num=exec_time, formatNum=formatNum(exec_time)))