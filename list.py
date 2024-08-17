#Q1. Create an empty list.
#li=[]

#Q2. Create a list and add an element to the end of this list.
li=[]
li.append(1)
li.append(2)
li.append(3)
print(li)

#Q3. For the above created list print the last element.
print(li[-1])

#Q4. Reverse the above created list.
li.reverse()
print(li)

#Q5. Sort the above created list.
li.sort()
print(li)

#Q6. Create a list of your top three favorite movies, then print the second movie title.
li=["hera pheri","LOC kargil","shershah"]
print(li[1])

#Q7. Create a list of your favorite animals, then add a new animal to the list and print the updated list.
li=["ant","tiger","monkey","dog"]
li.append("lion")
print(li)

#Q8. Create a list of your favorite cities, then use the index() method to find the position of a specific city in the list and print it
li=["pune","delhi","banglore","mumbai","hyderabad"]
print(li.index("pune"))#0
print(li.index("mumbai"))#3
print(li.index("delhi"))#1
print(li.index("banglore"))#2
print(li.index("hyderabad"))#4

