#Q1. What is the syntax for adding an element to a list in Python?
# element can be added in the list by append method or insert method() or extend method()

#2What is the difference between remove() and pop() functions in Python?
# The major difference between the pop () method and the remove () method is that the pop () method uses the index of an element to delete it while the remove () method takes the value of the element as an input argument to delete the element . The pop () method can be used without an input argument.

#Q3. Write a Python code to sort a list in descending order.
li=[1,3,4,0,5,6,1,1]
li.sort()
li.reverse()
print(li)#[6, 5, 4, 3, 1, 1, 1, 0]

#Q4. Write a Python code to count the number of occurrences of an element in a list.
print(li.count(1))#3
print(li.count(0))#1
print(li.count(3))#1
print(li.count(4))#1
print(li.count(5))#1
print(li.count(6))#1
print(li.count(2))#0


#Q5. Write a Python code to reverse a list
li.reverse()
print(li)
