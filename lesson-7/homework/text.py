#1-task 
def is_prime(son):
    if son <2:
        return False
    for i in range(2, int(son**0.5) + 1): 
        if son % i == 0:
            return False
        else:
            return True
son=(int(input('son kiriting:')))
if is_prime(son):
    print('tub emas')
else:
    print('tub')
#2-task 
def digit_sum(k):
    total = 0
    for digit in str(k):
        total+=int(digit)
    return total
k=int(input('son kiriting:'))
print(f"sonlar yigindisi:{digit_sum(k)}")
#3-task
def squares(n):
    power=2
    result=[]
    while power<=n:
        result.append(power)
        power*=2
    return result
n=int(input('son kiriting:'))
print(f"{n} sonini 2 daraja lari:{','.join(map(str,squares(n)))}")
