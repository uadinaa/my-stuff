#lab 2!

#first way
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print (a , b , c , d , sep = '\n')

#second way

a = int(input())
b = int(input())

print (a)
print (b)

lst = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) # adding the element
      
print(lst)