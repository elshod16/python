#1-task
fruits=['apple','banana','peach','grapes','pineapple']
print(fruits[3])
#2-task 
numbers1=[16,24,12]
numbers2=[17,21,37]
print(numbers1+numbers2)
#3-task
numbers =[16,22,27,12,9]
result= numbers[0],numbers[len(numbers)//2],numbers[-1]
print(result)
#4-task 
movies=['interstellar','inception','breaking bad','sinister','psixolog']
movies_tuple=tuple(movies)
print(movies_tuple)
#5-task 
cities=['Paris','Tokio','Toshkent','Los-angeles']
if 'Paris' in cities:
    print("Paris shahri ro'yxatda bor")
else:
    print("Paris shahri ro'yxatda yo'q")
#6-task 
numbers =['16','18','28','15','7','31']
duplicate =list(numbers)
duplicate.extend(numbers)
print(duplicate)
#7-task 
numbers =['16','18','28','15','7','31']
numbers[0],numbers[-1] = numbers[-1],numbers[0]
print (numbers)
#8-task
numbers =('1','2','3','4','5','6','7','8','9','10')
print(numbers[3:7])
#9-task
colours=['black','blue','red','green','blue','red','yellow']
print (colours.count('blue'))
#10-task
animals=('crocodile','tiger','lion','elephant')
print (animals.index('lion'))
#11-task
numbers1=(16,27,12)
numbers2=(17,28,13)
merged_numbers=numbers1+numbers2
print(merged_numbers)
#12-task
tuple_numbers=(16,27,12)
list_numbers =[17,28,13]
print(len(tuple_numbers))
print(len(list_numbers))
#13-task
numbers_tuple=(16,17,19,43,24,28)
numbers_list=list(numbers_tuple)
print(numbers_list)
#14-task
numbers_tuple=(16,17,19,14,24,28)
print(max(numbers_tuple))
print(min(numbers_tuple))
#15-task
words_tuple=('python','sql','html','javascript','golang')
print(tuple(reversed(words_tuple)))
