#1
t_yil =int(input("tug'ilgan yilingizni kiriting:"))
print (f"siz {2025-t_yil} yoshda ekansiz ")
#2
txt = 'LMaasleitbtui'
print(txt[1::2])
print(txt[::2])
#3
txt = 'MsaatmiazD'
print(txt[::2])
print (txt[-1]  + txt[2] + txt[5] + txt[7]+txt[1])
#4
txt = "I'am John. I am from London"
print(txt.split('from'))
#5
string = input('matn kiriting:')
print("".join(reversed(string)))
#6
string = input('matn kiriting:')
vowels ='aeiouAEIOU'
print (f"unli harflar soni {sum(n in vowels for n in string)}ta")
#7
numbers=list(map(int, input('sonlarni kiriting:').split()))
print(numbers)
#8
word=input('matn kiriting:')
if word ==word[::-1]:
    print('palindrome')
else:
    print('palindrome emas ')
#9
email=input('emailingizni kiriting:')
position = email.find('@')
print(f"domein:{email[position+1:]}")
#10
import random
import string

length = int(input("Parol uzunligini kiriting: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for i in range(length))

print("Yaratilgan parol:", password)
