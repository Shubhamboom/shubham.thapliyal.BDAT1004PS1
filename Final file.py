#!/usr/bin/env python
# coding: utf-8

# Assignment 

# In[1]:


#Ques 1
# What data type is each of the following (evaluate where necessary)?

# 5 
# 5.0
# 5 > 1
# '5'
# 5 * 2
# '5' * 2
# '5' + '2'
# 5 / 2
# 5 % 2
# {5, 2, 1}
# 5 == 3
# Pi (the number)


import math

print(type(5))
print(type(5.0))
print(type(5 > 1))
print(type('5'))
print(type(5 * 2))
print(type('5' * 2))
print(type('5' + '2'))
print(type(5 / 2))
print(type(5 % 2))
print(type({5, 2, 1}))
print(type(5 == 3))
print(type(math.pi))


# In[2]:


#Ques 2
# Write (and evaluate) python expressions that answer these questions:
# 
# a. How many letters are there in 'Supercalifragilisticexpialidocious'?
# 
# b. Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring? 
# 
# c. Which of the following words is the longest: 
#    Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or 
#    Bababadalgharaghtakamminarronnkonn? 
# 
# d. Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian', 
#   'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?


# Part a Solution
print(len('Supercalifragilisticexpialidocious'))

# Part b Solution
print('YES it has ice as substring') if('ice' in 'Supercalifragilisticexpialidocious') else print('NO it does not has ice as substring')

# Part c Solution
print('Longest Word: ' + max('Supercalifragilisticexpialidocious', 'Honorificabilitudinitatibus', 'Bababadalgharaghtakamminarronnkonn'))

# Part d Solution
sorted_str = sorted(['Berlioz', 'Borodin', 'Brian', 
'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'])

print('First Name: ' + sorted_str[0] + ', Last Name: ' + sorted_str[-1])


# In[3]:


#Ques 3
# Implement function triangleArea(a,b,c) that takes as input the lengths of the 3
# sides of a triangle and returns the area of the triangle. By Heron's formula, the area 
# of a triangle with side lengths a, b, and c is
# s(s - a)(s -b)(s -c)
# , where 
# s = (a+b+c)/2. 
# >>> triangleArea(2,2,2)
# 1.7320508075688772


def triangleArea(a, b, c):
    s = (a+b+c)/2

    area = (s * (s - a) * (s - b) * (s - c))**(0.5)

    return(area)


if __name__ == '__main__':
    a = float(input('Please enter the first side length: '))
    b = float(input('Please enter the second side length: '))
    c = float(input('Please enter the third side length: '))

    area = triangleArea(a, b, c)
    print('The area of triangle: ' + str(area))


# In[8]:


#Ques 4
# Write a program in python to separate odd and even integers in separate arrays. Go 
# to the editor
# Test Data :
# Input the number of elements to be stored in the array :5
# Input 5 elements in the array :
# element - 0 : 25
# element - 1 : 47
# element - 2 : 42
# element - 3 : 56
# element - 4 : 32
# Expected Output:
# The Even elements are:
# 42 56 32
# The Odd elements are :
# 25 47


ele_list = list()

list_len = int(input('Input the number of elements to be stored in the array: '))

for i in range(list_len):
    ele_list.append(int(input('Enter Element: ')))

print('The Even elements are: ')
for i in range(list_len):
    if ele_list[i]%2 == 0:
        print(ele_list[i], end=' ')

print()

print('The Odd elements are: ')
for i in range(list_len):
    if ele_list[i]%2 != 0:
        print(ele_list[i], end=' ')


# In[4]:


#Ques 5
def inside(a,b,a1,b1,a2,b2):
    if a1 <= a <= a2 and b1 <= b <=b2:
        return True
    return False
# Part a->
x= input("Enter x")
y= input("Enter y")
x1= input("Enter x1")
y1= input("Enter y1")
x2= input("Enter x2")
y2= input("Enter y2")
print(inside(x,y,x1,y1,x2,y2))
#Part b->
if inside(1,1,0.3,0.5,1.1,0.7) and inside(1,1,0.5,0.2,1.1,2):
    print("1,1 lies between both the points")
else:
    print("1,1 does not lie between the points.")


# In[5]:


#Ques 6
def pig(line):
    line = line.lower()
    vowels = ['a','e','i','o','u']
    if line[0] in vowels:
        return line + "way"
    else:
        first = line[0 : 1]
        second = line[1 :]
        return second + first + "ay"

print(pig("happy"))
print(pig("Enter"))


# In[9]:


#Ques 7
# 7th question
file =  open("bloodtype1.txt", "r")
arr = file.read().split(" ")
print(f"There are {arr.count('A')} patients of blood type A.")
print(f"There are {arr.count('B')} patients of blood type B.")
print(f"There are {arr.count('AB')} patients of blood type AB.")
print(f"There are {arr.count('O')} patients of blood type O.")
print(f"There are {arr.count('OO')} patients of blood type OO.")


# In[10]:


#Ques 8
def curconv(symbol,price):
    f =  open("currencies.txt", "r")
    arr = f.read().split("\n")
    dictionary = {}
    for i in arr:
        arr_one = i.split("\t")
        dictionary[f"{arr_one[0]}"] = arr_one[1]
    multiplier = dictionary.get(symbol)
    return float(price) * float(multiplier)

curr_symbol = input("Enter Currency Symbol:")
curr_amount = input("Enter Currency Amount:")
print(curconv(curr_symbol,curr_amount), "USD")


# In[6]:


#Ques 9
try:
    a = 0+'a'
except Exception as e:
  print("Exception:",e)
try:
    a = math.sqrt(-1.1)

except Exception as e:
  print("Exception:",e)
try:
    print(b)

except Exception as e:
  print("Exception:",e)
try:
    f = open("file.txt", "r")

except Exception as e:
  print("Exception:",e)


# In[7]:


#Ques 10
import math


def frequencies(line):
    alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabets_upper_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in line:
        if i in alphabets:
            count[alphabets.index(i)]=count[alphabets.index(i)]+1
        if i in alphabets_upper_case:
            count[alphabets_upper_case.index(i)]=count[alphabets_upper_case.index(i)]+1
    return count

sentence=input("Enter you message: ")
print("Line:",sentence)
print("frequencies:",frequencies(sentence))

