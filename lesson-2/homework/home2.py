#from datetime import datetime

#name = input("What's your name? ")
#age = int(input("How old are you? "))

#current_year = datetime.now().year
#year_of_birth = current_year - age

#print(f"Hello {name}, you were born in {year_of_birth}.")



#txt = 'LMaasleitbtui'
#car_brands = ['bmw', 'audi', 'mercedes', 'tesla', 'toyota', 'honda', 'ford', 'kia', 'mazda', 'jeep']

#found_brands = []

#for brand in car_brands:
    #if brand.lower() in txt.lower():
        #found_brands.append(brand)

#print("Found car names:", found_brands)


#txt="i'am john. i am from london"
#cut_txt=txt[20:27]
#print('residets area:',cut_txt)

#txt=input('give string:')
#revers=txt[::-1]
#print('reverse:',revers)


#txt=input('give string:')
#vow=('a','o','u','i','e')
#count=sum(char in vow for char in txt)
#print('count vowels=',count)

#inputstr=input('give num')
#num=list(map(int,inputstr.split()))
#maxx=max(num)
#print(maxx)

#inp=input('check:')
#inp=inp.lower()
#if inp==inp[::-1]:print('palinderome')
#else:print('no')

#inp=input('email:')
#cut=inp.split('@')[1]
#print('domain is:',cut)


import random
import string

# Define password length
length = 12  # You can change this value

# Define character sets
letters = string.ascii_letters       # a-z + A-Z
digits = string.digits               # 0-9
specials = string.punctuation        # !@#$%^&*()_+-=[]{};: etc.

# Combine all characters
all_chars = letters + digits + specials

# Generate password
password = ''.join(random.choice(all_chars) for _ in range(length))

print("Generated password:", password)
