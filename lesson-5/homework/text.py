#1-task
year=int(input('yil kiriting:'))
if year % 4 == 0 and year % 100 !=0  or year % 400 == 0:
    print(f"{year}  leap year")
else:
    print(f"{year} bu leap year emas")
    
#2-task     
n=int(input('son kiriting:'))     
if n%2!=0:
    print('weird')
elif n%2==0 and 2 <= n <= 5:
    print('not weird')
elif n%2==0 and 6<=n<=20:
    print('weird')
else:
    print('not weird')

#3-task
a=int(input("a:"))
b=int(input("b:"))
if a%2==0:
    start=a
else:
    start=a+1

evens = list(range(start, b + 1, 2))
print(evens)
