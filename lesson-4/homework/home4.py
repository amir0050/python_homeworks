'''data = {
    'apple': 10,
    'banana': 5,
    'orange': 8,
    'mango': 12,
    'grape': 3
}

def get_value(pair):
    return pair[1]

ascending = dict(sorted(data.items(), key=get_value))


descending = dict(sorted(data.items(), key=get_value, reverse=True))

print("Сортировка по значениям (по возрастанию):")
print(ascending)

print("\nСортировка по значениям (по убыванию):")
print(descending)'''




'''mydict={0:10,1:20}
mydict['2']='30'''

'''dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
overall={**dic1,**dic2,**dic3}
print(overall)'''



'''n = 5
squares_dict = {}
for x in range(1, n + 1):
    squares_dict[x] = x * x

print("Dictionary of Squares:")
print(squares_dict)'''




'''squares_dict = {}
for x in range(1, 16):
    squares_dict[x] = x * x
print("Dictionary of squares from 1 to 15:")
print(squares_dict)'''



'''sett={1,2,'a','b'}
print(sett)'''



'''myset={'aplle','banana','kiwi','melon'}
for fruits in myset:print(fruits)'''



'''sett={1,2,'a','b'}
sett.update(['rrr'])
print(sett)'''




'''sett={1,2,'a','b'}
sett.discard(1)
print(sett)'''



'''myset={'aplle','banana','kiwi','melon'}
remov=('aplle')
if remov in myset:myset.discard(remov)
print(myset)'''
