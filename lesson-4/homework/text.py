
#1-task
my_dict = {"a": 3, "b": 1, "c": 5, "d": 2}
asc=sorted(my_dict.items(), key=lambda x: x[1])
print("ascending",asc)
desc=sorted(my_dict.items(),key=lambda x:x[1],reverse=True)
print("descending",desc)
#2-task
my_dict.update([('g',6)])
print(my_dict)
#3-task
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
print(dic1|dic2|dic3)
#4-task 
n=10
squares={}
for x in range(1,1+n):
    squares[x]=x*x
print(squares)
#5-task 
n=15
squares={}
for x in range(1,1+n):
    squares[x]=x*x
print(squares)
#set exercises
#1
my_set={'a','b','c','d'}
print(my_set)
#2
my_set={'a','b','c','d'}
for item in my_set:
    print(item)
#3
my_set.update(['e','f'])
print(my_set)
#4
my_set.remove('e')
print(my_set)
#5
if 'a' in my_set:
    my_set.remove('a')
else:
    print('bunday element topilmadi')
#second way
my_set.discard('a')
print(my_set)
