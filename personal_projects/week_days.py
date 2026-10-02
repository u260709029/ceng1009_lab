starting_day_text = input("Enter starting day in text: ").lower()
starting_day_int = {"sunday":0,"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6}
vacation_length = int(input("Enter vacation length: "))
vacation_end = (starting_day_int[starting_day_text] + vacation_length) % 7
vacation_end_day =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print("Your vacation will end on " + vacation_end_day[vacation_end] + ".")

#input error verdirmicek şekilde yazılcak

# dictionary = {"bartu":[20,"abroad"],"ilter":20}
# dictionary["bartu"][0]=21
# print(dictionary)
# print(dictionary["bartu"])
# print(dictionary["bartu"][0])
# for i in range(len(dictionary["bartu"])):
#  print(dictionary["bartu"][i])
# liste = [1,2,3,4,5,6,7,8,9,10,1]
# set1 = set(liste)
# print(set1[0])
# print(liste[0])
