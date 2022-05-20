Session1 - Python String Functions
Last live session assignment:
b = "this is My First Python programming class and i am learNING python string and its function"
1 . Try to extract data from index one to index 300 with a jump of 3 
Ans 
b[:20:3]
o/p - 'tssyity'

2. Try to reverse a string without using reverse function 
Ans 
b[::-1]
o/p - 'noitcnuf sti dna gnirts nohtyp GNINrael ma i dna ssalc gnimmargorp nohtyP tsriF yM si siht'

3. Try to split a string after conversion of entire string in uppercase 
Ans 
b1 = b.upper()
b1.split(' ')
o/p - ['THIS',
 'IS',
 'MY',
 'FIRST',
 'PYTHON',
 'PROGRAMMING',
 'CLASS',
 'AND',
 'I',
 'AM',
 'LEARNING',
 'PYTHON',
 'STRING',
 'AND',
 'ITS',
 'FUNCTION']

4. Try to convert the whole string into lower case 
Ans 
b.lower()
o/p - 'this is my first python programming class and i am learning python string and its function'

5 . Try to capitalize the whole string 
Ans 
b.capitalize()
o/p - 'This is my first python programming class and i am learning python string and its function'

6 . Write a diference between isalnum() and isalpha()
Ans 
isalnum() will return Boolean true and false based on the string contains alphanumeric characters.
Isalpha() will return Boolean true/false based on the string contains only alphabetic characters.

7. Try to give an example of expand tab
Ans
Expand tab will split the string based on the tab as delimiter
e.g s6='bhar\test\dev'
s6.expandtabs()
o/p = bhar test dev


‘Shift+Tab’ will give the description of each string functions which we define.
‘Tab’ will give the list of available inbuilt python functions. E.g if we declare string var, it will give list of string functions.


8 . Give an example of strip , lstrip and rstrip 
Ans
‘Strip’ function will trim the white spaces from both sides of the string
‘Lstrip’ will trim the whitespaces from left side of the string
‘Rstrip’ will trim the whitespaces from right side of the string

9.  Replace a string charecter by another charector by taking your own example 
Ans
c='bhargavideepak'
c.replace('a','z')
o/p - 'bhzrgzvideepzk'

10 . Try  to give a definition of string center function with and example 
Ans
Center function will place the string in the center , left and right side of the string will be added with the characters which we pass as arguments.
c='bhargavideepak'
c.center(20,'-')
o/p - '---bhargavideepak---'

11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language
Ans
Compiler – when the user writes the program and compile it, the machine will review the whole code and converts into machine level language for their understanding. It throws compilation error to the user if there is any syntax/logical error occurs while compiling the code. In python we don’t need this explicitly as it is done inbuilt.
Interpreter – It interpretes the code written and produces the output of the program.


12 . Python is a interpreted of compiled language give a clear ans with your understanding 
Ans
Python is a interpreted language. It doesn’t do compilation as a explicit step. It interpretes and runs the code written into their understanding language  and produces output without storing it as machine code.

13 . Try to write a usecase of python with your understanding .
Ans
Pythons are used in following areas
Data Science/Data Analytics
Machine Learning
Deep learning
AI development
Software development
Web application development

Assignment1 :
1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
*   expressions
'hello' values
-87.8 values
-  expressions
/  expressions
+	 expressions
6  values
Ans
*  =  expressions
'hello' = values
-87.8 = values
-  = expressions
/  expressions
+	 expressions
6  values

2. What is the difference between string and variable?
Ans String is a datatype which defines string characters , variable is the declaration given to the values.

3. Describe three different data types.
Ans
Int – to represent integer numbers
String – to represent strings
Float – to represent floating point

4. What is an expression made up of? What do all expressions do?
Ans Expression contains mathematical functions.

5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
Ans
Expression contains mathematical functions.
Statements contains declarations.

6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1
Ans 23

7. What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3
Ans spamspamspam

8. Why is eggs a valid variable name while 100 is invalid?
Ans Variable cannot be declared in digit format. It should be in alphabetical.

9. What three functions can be used to get the integer, floating-point number, or string version of a value?
Ans int for integer , float for floating point , string for string version

10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'
Ans 99 is a integer which cannot be concatenated with string


