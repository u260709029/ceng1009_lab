# def isOdd(n):
#     return n%2==1
#
# print(isOdd(4))
import string
from operator import truediv

# def isleap(year):
#     if year%400==0:
#         return True
#     elif year%100==0:
#         return False
#     elif year%4==0:
#         return True
#     return False
#
# print(isleap(2000))
# print(isleap(2001))

# def print_triangular_numbers(n):
#     for i in range(1, n+1):
#         print(i,int((i*(i+1))/2))
#
# print_triangular_numbers(5)

# def is_prime(n):
#     i = 2
#     while not n%i == 0:
#         i+=1
#     if n == i:
#         return True
#     else:
#         return False
#
# print(is_prime(19))

# def reverse(s):
#     result = ""
#     for ch in s:
#         result = ch + result
#     return result
#
# print(reverse("hello world"))
#
# def reverseSlice(s):
#     return s[::-1]
#
# print(reverseSlice("hello world"))

# def removeAll(sub,main):
#     return main.replace(sub,"")
#
# print(removeAll("l","Hello World!"))

def substitude(s,cipher):
    alphabet=string.ascii_lowercase
    result=""
    for c in s:
        index = alphabet.find(c.lower())
        if index == -1:
            result = result + c
        elif c.isupper():
            result = result + cipher[index].upper()
        else:
            result = result + cipher[index].lower()
    return result

key = "qtgbjxfiluhkcayopzdvnwsmre"

print(substitude("Hello World!",key))

# def remove_dups(s):
#     result = ""
#     for ch in s:
#         if not ch in result:
#             result = result +ch
#     return result
#
# print(remove_dups("Hello World!"))