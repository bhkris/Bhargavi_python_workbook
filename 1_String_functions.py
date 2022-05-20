#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=10


# In[4]:


a


# # Session 1 - String Functions

# forward index - s[0], s[1], s[2], etc - begin from start 
# backward index - s[-1] , s[-2] , s[-3] , etc - begin from end

# In[6]:


s = 'bhargavi k'


# In[7]:


s[1]


# In[8]:


s[-2]


# extract from the subset of the string . ie extract row of char
# below eg - it will exclude the last index. ie. 5th index. 1:5 means 1st to 4th index

# In[9]:


s[1:5]


# select alternative char from the string
# below eg - select 1st to 4th char with jump of 2 on every selection (alternative char )

# In[10]:


s[1:5:2]


# below eg - move in positive direction (from 1 st to 4th char).but jump in negative direction. it has contractiction, hence no output.

# In[11]:


s[1:5:-1]


# below e.g - move in negative direction. and jump in negative direction. so no contractiction

# In[12]:


s[5:0:-1]


# below e.g - move in negative direction. and jump in negative direction but extract alternate char. so no contractiction

# In[13]:


s[5:0:-2]


# below e.g - start from 0 index to 4th index

# In[14]:


s[:5]


# below e.g - start from 0 index to 4th index. select every third char from negative direction

# In[15]:


s[:5:-3]


# below e.g - start from 0 index till 3rd negtive char

# In[16]:


s[:-3]


# below e.g - start from negative 2nd char in forward dir till last index

# In[17]:


s[-2:]


#  --reverse the string

# In[20]:


s[::-1]


# below e.g - move in backward dir and jump in forward dir. contraction, hence no output

# In[21]:


s[-1:-5:1]


# below e.g - move in forward dir and jump in forward dir, hence shows output

# In[22]:


s[-10:-1:1]


# In[ ]:


below e.g - movein backward dir, but jump dir not mentioned so default it will take forward dir. contractiction occurs


# In[23]:


s[5:0]


# below e.g - type casting - concatenate the number with the string - string +1

# In[24]:


s+"1"


# In[25]:


s+str(1)


# below e.g - finding the length of the string

# In[26]:


len(s)


# below e.g - repeat the given string

# In[27]:


s * 2


# s.tab - gives all available inbuilt string functions
# s.str function - shift tab - gives the description of the selected str function
# below e.g - count of the number of occurences of te char

# In[30]:


s.count('k')


# below e.g - split the string by keeping 'a' as a seperator

# In[32]:


s.split('a')


# In[33]:


s.split(' ')


# In[34]:


s.upper()


# In[36]:


s.lower()


# belowe.g - convert start letter of every word in the string to upper case

# In[37]:


s.title()


# below e.g - convert only the first letter of the string to upper case

# In[38]:


s.capitalize()


# below e.g - convert upper to lower case and vice versa

# In[39]:


s.swapcase()


# In[44]:


reversed(s)


# In[45]:


''.join(reversed(s))


# below e.g - trim the white spaces(spaces before /after the string placed) fromboth the sides
# left - lstrip
# right -rstrip

# In[48]:


s1= '  bhargavi_ worksheet '


# In[49]:


s1.strip()


# In[51]:


s1.lstrip()


# In[52]:


s1.rstrip()


# below e.g - join space between each char

# In[53]:


' '.join(s)


# below eg - fil extra spaces with #

# In[58]:


s.center(15, '#')


# In[59]:


s.isupper()


# In[60]:


s.islower()


# In[61]:


s.isspace()


# In[62]:


s1.isspace()


# In[65]:


s2=" "


# In[66]:


s2.isspace()


# In[67]:


s3='97989'


# In[68]:


s3.isdigit()


# In[69]:


s4='97jk'


# In[70]:


s4.isdigit()


# In[71]:


s4.isalnum()


# In[73]:


s.startswith('B')


# In[74]:


s.startswith('b')


# above e.g - python is case sensitive lang

# In[88]:


s5=324.54


# In[89]:


s5.isdigit()


# In[77]:


s5.isnumeric()


# above e.g - isdigit/isnumeric desnt apply for decimal

# In[86]:


s6='bhar\test\dev'


# In[87]:


s6.expandtabs()


# # String Functions - Assignment

# In[105]:


b = "this is My First Python programming class and i am learNING python string and its function"


# 1. Try to extract data from index one to index 300 with a jump of 3 

# In[111]:


b[:20:3]


# 2. Try to reverse a string without using reverse function 

# In[113]:


b[::-1]


# 3. Try to split a string after conversion of entire string in uppercase 

# In[134]:


b1 = b.upper()
b1.split(' ')


# 4. Try to convert the whole string into lower case 

# In[116]:


b.lower()


# 5. Try to capitalize the whole string 

# In[118]:


b.capitalize()


# 6 . Write a diference between isalnum() and isalpha()
# Ans 
# isalnum() will return Boolean true and false based on the string contains alphanumeric characters.
# Isalpha() will return Boolean true/false based on the string contains only alphabetic characters.

# In[122]:


s.isalpha()


# In[121]:


b.isalnum()


# 7. Try to give an example of expand tab
# Ans
# ‘Shift+Tab’ will give the description of each string functions which we define.
# ‘Tab’ will give the list of available inbuilt python functions. E.g if we declare string var, it will give list of string functions.

# 8 . Give an example of strip , lstrip and rstrip 
# Ans
# ‘Strip’ function will trim the white spaces from both sides of the string
# ‘Lstrip’ will trim the whitespaces from left side of the string
# ‘Rstrip’ will trim the whitespaces from right side of the string

# 9.  Replace a string charecter by another character by taking your own example 

# In[135]:


c='bhargavideepak'
c.replace('a','z')


# 10 . Try  to give a definition of string center function with and example 
# Ans
# Center function will place the string in the center , left and right side of the string will be added with the characters which we pass as arguments.

# In[136]:


c='bhargavideepak'
c.center(20,'-')


# 11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language
# Ans
# Compiler – when the user writes the program and compile it, the machine will review the whole code and converts into machine level language for their understanding. It throws compilation error to the user if there is any syntax/logical error occurs while compiling the code. In python we don’t need this explicitly as it is done inbuilt.
# Interpreter – It interpretes the code written and produces the output of the program.

# 12 . Python is a interpreted of compiled language give a clear ans with your understanding 
# Ans
# Python is a interpreted language. It doesn’t do compilation as a explicit step. It interpretes and runs the code written into their understanding language  and produces output without storing it as machine code.

# 13 . Try to write a usecase of python with your understanding .
# Ans
# Pythons are used in following areas
# Data Science/Data Analytics
# Machine Learning
# Deep learning
# AI development
# Software development
# Web application development
