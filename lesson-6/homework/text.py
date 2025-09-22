#1-task 
txt='abcabcabcdeabcdefabcdefg'
vowels='aeiou'
result=""
count=0
i=0
while i<len(txt):
    result +=txt[i]
    count +=1
    if count==3 and i+1<len(txt):
        if txt[i+1]in vowels or txt[i+1]=="_":
            i+=1
            result +=txt[i]
        result+="_"
        count=0
    i+=1
print(result)


#2-task
n=int(input('son kiriting:'))
for i in range(n):
    print(i**2)

#loop-based tasks
#1-task
i=1
while i<= 10:
    print(i)
    i+=1
#2-task 
rows=5
for n in range(1,rows+1):
    for t in range(1,n+1):
        print(t,end=' ')
    print()



#3-task 
n=int(input('son kiriting:'))
i=1
total=0
while i<=n:
    total=total+i
    i=i+1
print(f"yig'indi:{total}")
####2nd way###
n=int(input('son kiriting:'))
total=0
for i in range(1,n+1):
    total+=i
print(f"yig'indi: {total}")

#4-task
n=int(input('son kiriting:'))
for i in range(1,10+1):
    print(n*i)
#5-task
numbers = [12, 75, 150, 180, 145, 525, 50]
count=0
for n in numbers:
    if n%5==0 and n<=150:
        print(n)
        count +=1
    if count ==3:
        break
#6-task
n=int(input('son kiriting:'))
count=0
while n>0:
    n=n//10
    count+=1
print(f"total digits:{count}")

#2nd way
n=int(input('son kiriting:'))
count=0
for i in str(n):
    count+=1
print(f"total digits: {count}")
#7-task
rows=5
for n in range(rows,0,-1):
    for t in range(n,0,-1):
        print(t,end=' ')
    print()
        
#8-task 
list1 = [10, 20, 30, 40, 50]
list1=list(reversed(list1))
for n in list1:
    print(n)

#9-task
for i in range(-10,0):
    print(i)

#10-task 
for i in range(5):
    print(i)
print('Done')
#11-task
start=25
end=50
for n in range(start,end+1):
    if n>1:
        prime =True
        for i in range(2,n):
            if n%i==0:
                prime=False
                break 
        if prime:
            print(n)

#12-task
terms=10
a=0
b=1
for t in range(terms):
    print(a, end=" ")
    a,b=b,a+b
#13-task 
n=5
f=1
for i in range(1,n+1):
    f=f*i
print(f"{n}!{f}")

#14-task
list1 = [1,2,3,4,5]
list2 = [1,3,4,5,6]
result=[]
for x in list1:
    if x not in list2:
        result.append(x)
for x in list2:
    if x not in list1:
        result.append(x)
print(result)

