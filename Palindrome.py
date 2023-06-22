def Palindrome(poll): #функция которая провиряет является ли строка полиндромом
    return poll == poll[::-1]

print(Palindrome(input()))

