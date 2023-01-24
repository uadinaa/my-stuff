#syntax 
a = int(input())
b = int(input())

if a > b:
    print("a is greather than b")
elif b > a:
    print ("b is greather than a")
else:
    print("they are equal")

#Many Values to Multiple Variables
d , am , b = "Dina" , "Amina" , "Balzhan"

print(d)
print(am)
print(b)

fruits = ["apple", "banana", "cherry" , "pineapple"]
print(fruits[::-1])
r , x , y , z = fruits 

print(r)
print(x)
print(y)
print(z)

#Global Variables
fuck = (input())
mother = (input())

def function():
    if fuck == mother:
        print("equal")
    else:
        print("not same")

function()

#dict 
jake = {"name" : "John" , "age" : 36}
print(jake)

#converting 
y = int(2.5542)

#complex 
x = 3 + 5j

a = 'abcdefghijklmnopqrstuvwxyz'
# len is size of the a
print(a, a[0] , a[len(a) - 1])

# substring 
print (a[2:5])

print (a[:5]) # from the beginning till the 5

print (a[3:]) #from 3 till end

print (a[-3:]) # задний счет

print(a[::-1]) #reverse 

print (a[5:2:-1]) #reverse substring from 5 to 2 

print(b[-5:-2]) #counting when it is reversed starts with 1

# algorithms 
k = "   Dina, I love you    "

print(k.upper())
print(k.lower())
print(k.strip()) #removes the space srom beginning and the end

#String Format
age = 17
aboutme = "Hi, my name is Dina. and i am"
print(aboutme , age)
'''orr we can use there a new function 
it is for INSERT num into str
'''
momage = 55
aboutmom = "Hey, my name is Gulzhan, and i am {}"

print(aboutmom.format(momage))


c = '33 66 44 33 '
print(c.split(sep = ' ')) #output ['33', '66', '44', '33', '']



