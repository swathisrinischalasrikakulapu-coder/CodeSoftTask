import random

letters = ['a','b','c','d','e','f','g','h','i','j',
'k','l','m','n','o','p','q','r','s','t',
'u','v','w','x','y','z''A','B','C','D','E','F','G','H','I','J',
'K','L','M','N','O','P','Q','R','S','T',
'U','V','W','X','Y','Z']

numbers = [
'0','1','2','3','4','5','6','7','8','9'
]

symbols = [
'!','@','#','$','%','^','&','*','(',')',
'_','+','-','=','{','}','[',']','|',':',
';','<','>',',','.','?','/'
]
print("welcome to the password generator!")
n_letter = int(input("how many letters would you like to generate?"))
n_symbol = int(input("how many symbols would you like to generate?"))
n_number = int(input("how many numbers would you like to generate?"))
password = []
for i in range(1,n_letter+1):
    char = random.choice(letters)
    password += char
for i in range(1,n_symbol+1):
    char = random.choice(symbols)
    password += char
for i in range(1,n_number+1):
    char = random.choice(numbers)
    password += char
print(password)#['X', 'y', 'I', '+', '?', '+', ')', '0', '6', '1', '3', '5']
random.shuffle(password)# shuffle is used for list to shuffle
print(password)#['6', 'X', ')', '?', '1', '5', '+', '3', 'I', 'y', '0', '+']
password_str=" "
for i in password:
    password_str += i
print(password_str)# 6X)?15+3Iy0+
