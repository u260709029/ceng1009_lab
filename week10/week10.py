# myList = [76,92.3,"hello",True,4,76]
# print(myList)
#
# myList.append("apple")
# myList.append(76)
# print(myList)
#
# myList.insert(3,"cat")
# print(myList)
#
# myList.insert(0,99)
# print(myList)
#
# print(myList.index("hello"))
#
# print(myList.count(76))
#
# myList.remove(76)
# print(myList)
#
# myList.pop(myList.index(True))
# print(myList)

# def sum_of_squares(numList):
#     sum = 0
#     for num in numList:
#         sum += num**2
#     return sum
# print(sum_of_squares([3, 4, 5]))

# def sum_evens(numList):
#     sum = 0
#     for num in numList:
#         if num % 2 == 0:
#             sum += num
#     return sum
# print(sum_evens([1,2,3,4,5,6,7,8,9,10]))

# def count_five_letter(wordList):
#     count = 0
#     for word in wordlist:
#         if len(word) == 5:
#             num += 1
#     return num
# print(count_five_letter(["hello", "world","banana","apple","classroom"]))

# def sum_exclude_1st_even(numList):
#     sum = 0
#     for num in numList:
#         if num % 2 == 0:
#             break
#         sum += num
#     return sum
# print(sum_exclude_1st_even([1, 3, 3, 7, 5, 6]))

# def num_until_sam(wordList):
#     num = 0
#     for word in wordList:
#         num += 1
#         if word.lower() == "sam":
#             break
#     return num
# print(num_until_sam(["Who","did","you","call,","Sam","?"]))

def replace(s, old, new):
    tempList =[]
    for char1 in s:
        tempList.append(char1)
    print(tempList)
    for char2 in tempList:
        if char2 == old:
            place = char2.index(old)
            tempList.pop(place)
            tempList.insert(place,new)
    return tempList
print(replace("missisippi","i","I"))

# def find_max_val_in_a_list(numList):
#     maxVal = numList[0]
#     for num in numList:
#         if num > maxVal:
#             maxVal = num
#     return maxVal
# my_list = [3,1,2,0,5,7,8,10,2]
# print(find_max_val_in_a_list(my_list))