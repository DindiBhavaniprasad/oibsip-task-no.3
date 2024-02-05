import random2

letters = ['a','b','c','d','e','f','g','h','i','j','k',
         'l','m','n','o','p','q','r','s','t','u','v','w',
         'x','y','z','A','B','C','D','E','F','G','H','I',
         'J','K','L','M','N','O','P','Q','R','S','T','U',
         'V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*',]

letter = int(input("how many letters you want in your password ?\n" ))
number = int(input("how many numbers you want in your password ?\n" ))
symbol = int(input("how many symbols you want in your password ?\n" ))

password = " "

for i in range(1,letter+1):
    char = random2.choice(letters)
    password = password + char


for i in range(1,symbol+1):
    sym = random2.choice(symbols)
    password = password + sym


for i in range(1,number+1):
    num = random2.choice(numbers)
    password = password + num

print(password)