'''def isprime(n):
 if n < 2:
  return False
 for i in range(2, n):
  if n%i==0:
   return False
  return True

print(isprime(8))'''


'''def digitsum(n):
    return sum(int(digit) for digit in str(n))


print(digitsum(555))'''
        
'''def digitsum(n):
    total=0
    for digit in str(n):
        total=total+int(digit)
    return total

print(digitsum(555))'''


'''def daraja(n):
    son=1
    while True:
        son*=2
        if son>n:
            break
        print (son,end=(' '))

daraja(10)'''
