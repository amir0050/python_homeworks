'''txt = "abcabcabcdeabcdefabcdefg"  # ← сюда подставь свою строку

vowels = 'aeiouAEIOU'
i = 0
count = 0
result = ''

while i < len(txt):
    result += txt[i]
    count += 1

    if count == 3:
        if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == '_'):
            if i + 1 < len(txt) - 1:
                result += txt[i + 1]
                result += '_'
                i += 1
        elif i != len(txt) - 1:
            result += '_'
        count = 0
    i += 1

print(result)'''

'''num=1
i=int(input('sonni kiriting:' ))
while True:
       if num>=i:
        break
       print(num*num)
       num+=1'''

'''row = 1
while row <= 5:
    num = 1
    while num <= row:
        print(num, end=' ')
        num += 1
    print()  
    row += 1'''


'''i=int(input('son kirit:'))
num=1
total=0
while num<=i:
    total+=num
    num+=1
    print(total)'''



'''numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
      if num == 75 or num == 150 or num == 145:
        print(num)'''
  


'''num=input('son kirit;')
if num.isdigit():
    print(len(num))
else: print('problem')'''


'''for j in range(i, 0, -1):
    print(j, end=' ')
print()'''



'''list1=[10,20,30,40,50]
for i in reversed(list1):
    print(i)'''


'''for i in range(-10, 0):
    print(i)'''

'''for i in range(5):
    print(i)
    print('done')'''



'''print("Prime numbers between 25 and 50:")
for num in range(25, 51):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)



print("\nFibonacci sequence:")
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b



num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"\n\n{num}! = {fact}")



def uncommon_elements(list1, list2):
    from collections import Counter
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []
    for elem in c1:
        if elem not in c2:
            result.extend([elem] * c1[elem])
    for elem in c2:
        if elem not in c1:
            result.extend([elem] * c2[elem])
    for elem in c1:
        if elem in c2:
            diff = c1[elem] - c2[elem]
            if diff > 0:
                result.extend([elem] * diff)
    for elem in c2:
        if elem in c1:
            diff = c2[elem] - c1[elem]
            if diff > 0:
                result.extend([elem] * diff)
    return result'''
