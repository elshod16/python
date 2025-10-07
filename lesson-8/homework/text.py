#task-1
try:
    result=16 / 0
except ZeroDivisionError:
    print("0 ga bo'lish xatoligi bor!")
else:
    print("to'g'ri")
finally:
    print('code done successfully')
#task-2
try:
    result=int(input('integer kiriting:'))
except ValueError:
    print('not valid value for input!')
else:
    print('correct')
finally:
    print('code done successfully')
#3-task 
try:
    file=open('C:\\Users\\ACER\\Desktop\\python.txt','r')
except FileNotFoundError:
    print('file not found')
else:
    print('file found')
    file.close()
finally:
    print('code done successfully')
#4-task
try:
    num1=(input('1-sonni kiriting:'))
    num2=(input('2-sonni kiriting:'))
    if not (num1.isdigit() and num2.isdigit()):
        raise TypeError('iltimos faqat son kiriting')
    
    num1 = int(num1)
    num2 = int(num2)
    result=num1+num2
except TypeError as error:
    print(error)
else:
    print('correct',result)
finally:
    print('code done successfully')

#5-task
try:
    file = open('C:\\Users\\ACER\\Desktop\\python.txt','w')
except PermissionError:
    print("fileni ochishga ruxsat yo'q ")
else:
    print("fileni ochishingiz mumkin ")
    file.close()
finally:
    print('code done successfully')

#6-task
try:
    num_list=[12,16,21,99]
    index=int(input('insert the index:'))
    print(num_list[index])
except IndexError:
    print('unknown index')
else:
    print(f"index found, number is {num_list[index]}")
finally:
    print('code done successfully')
#7-task
try:
    number=int(input('insert the number:'))
except KeyboardInterrupt:
    print ('do not skip the input with(ctrl+c)')
else:
    print(f"number was found:{number}")
finally:
    print('code done successfully')

#8-task
try:
    a = int(input('insert the number a:'))
    b = int(input('insert the number b:'))
    division = a/b
except ArithmeticError:
    print('arithmetic error found!')
else:
    print(f'correct code ! {division}')
finally:
    print('code done successfully')
#9-task
try:
    with open('C:\\Users\\ACER\\Desktop\\python.txt',encoding = 'utf-8') as file:
        content=file.read() 
except UnicodeDecodeError:
    print('encoding error')
else:
    print('file read successfully')
finally:
    print('code done successfully')
#10-task

try:
    my_list=[12,76,99]
    my_list.lower()
except AttributeError:
    print('method error')
else:
    print("correct method!,result is here", my_list)
finally:
    print('code done successfully')


#file input output exercises
#1-task 
with open('C:\\Users\\ACER\\Desktop\\python.txt',encoding='utf-8') as file :
    content=file.read()
    print(content)
#2-task

n=int(input("nechta qator o'qimoqchisiz:"))
with open('C:\\Users\\ACER\\classrew\\py2.txt') as file :
    for l in range(n):
        line=file.readline()
        if not line:
            break
        print(line.strip())

#3-task 
with open('C:\\Users\\ACER\\classrew\\py2.txt','a') as file:
    file.write('\ni will just learn BI \n for being data analyst\n')
    print(file)
with open('C:\\Users\\ACER\\classrew\\py2.txt', 'r') as file:
    content = file.read()
    print(content)
#4-task
n=int(input("oxiridan nechta qator o'qimoqchisiz:"))
with open('C:\\Users\\ACER\\classrew\\py2.txt') as file :
    lines=file.readlines()
    for line in lines[-n:]:
        print(line.strip())
#5-task
with open('C:\\Users\\ACER\\py.txt', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())         
#6-task
with open('C:\\Users\\ACER\\py.txt', encoding='utf-8') as file:
    text=file.read()
print(text)
#7-task
import array 

with open("C:\\Users\\ACER\\numbers.txt")as file:
    numbers=array.array('i', [int(x) for x in file.read().split(',')])
    print(numbers)
#8-task
with open("C:\\Users\\ACER\\numbers.txt") as file:
    numbers=file.read().split(',')
    numbers=[int(x) for x in numbers]
    print(numbers)
    print(max(numbers))
#9-task
count=0
with open("C:\\Users\\ACER\\numbers.txt") as file:
    for line in file:
        count+=1
    print(count)
#10-task 
freq={}
with open("C:\\Users\\ACER\\py.txt",'r') as file:
    for line in file:
        line=line.strip()
        words=line.split()
        for word in words:
            word = word.strip()
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
for word,count in freq.items():
    print(f"{word}:{count}")

#11-task
import os
size = os.path.getsize("C:\\Users\\ACER\\py.txt")
print(f"file hajmi:{size}")
#12-task
data=['elshod','toshkentov','sherzodovich']
with open("C:\\Users\\ACER\\py.txt",'a') as file:
    for item in data:
        file.write(f"{item}\n")
#13-task
with open("C:\\Users\\ACER\\py.txt",'r') as file:
    data=file.read()
with open("C:\\Users\\ACER\\pyy.txt",'w') as copy:
    copy.write(data)
#14-task
with open("C:\\Users\\ACER\\num.txt",'r')as f1,open("C:\\Users\\ACER\\str.txt",'r')as f2:
    for line1,line2 in zip(f1,f2):
        print(f"{line1.strip()} {line2.strip()}")

#15-task
with open("C:\\Users\\ACER\\py.txt",'r') as file:
    lines=file.readlines()
import random
random_line=random.choice(lines)
print(random_line.strip())
#16-task
file = open("C:\\Users\\ACER\\py.txt", "r")
print(file.closed)
file.close()
print(file.closed)
#17-task
with open("C:\\Users\\ACER\\py.txt",'r') as file:
    lines=file.readlines()
clean_lines=[line.strip() for line in lines]
#18-task
with open("C:\\Users\\ACER\\py.txt",'r') as file:
    text=file.read()
text=text.replace(' ',',')
words=text.split(',')
allwords=[]
for word in words:
    allwords.extend(word.split(','))
print(len(allwords))
