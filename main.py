#create an empty arraylist
array=[]

#create a loop that will ask the user to input a string and will add it to the array
for i in range (0,5):
  userInput=input("Enter a task to do RIGHT NOW!!!!!!!:")
  array.append(userInput)

#print the array
print(array)

#ask the user to input a string to search for
search=input("For the love of god, ENTER A TASK FOR YOU TO COMPLETE!:")

for i in range(0,5):
  if array[i]==search:
    print("The task is at index:",i)

#IF THE STRING IS NOT FOUND, PRINT A MESSAGE SAYING SO
if search not in array:
  print("REALLY???? That task is not in the list!!!:(")
