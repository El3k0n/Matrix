# Matrix

Matrix, a simple Python class for managing matrices.
Matrix supports various operations with matrices, like addition and multiplication.

### Why? ###

* To consolidate my knowledge of Python classes
* To learn more about how matrices work
* To learn git basics

### Supported operations ###

* Sum between matrices
* Subtraction between matrices
* Multiplication of a matrix by a number
* Multiplication between matrices
* Inverse matrix
* Matrix of algebric complements
* Check if a matrix contains an certain number
* Equality and inequality test between matrices
* Transpose matrix
* Determinant of a matrix (Uses Laplace's theorem)

### Usage ###

##### Importing the module and creating a matrix object #####

```Python
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from matrix import *
>>> m = Matrix(2, 3)
>>> m
[0, 0, 0]
[0, 0, 0]
>>>
```

##### Filling the matrix with random values #####

```Python
>>> m.random()
>>> m
[0, 28, 5]
[20, 7, 7]
>>>
```

You can also specify the range of the random values:

```Python
>>> m.random(1, 5)
>>> m
[5, 3, 4]
[1, 1, 5]
>>>
```

##### Basic matrix operations #####

```Python
>>> m * 3  #Multiplication
[15, 9, 12]
[3, 3, 15]
>>> m + 3  #Addition
[8, 6, 7]
[4, 4, 8]
>>> m - 5  #Subtraction
[0, -2, -1]
[-4, -4, 0]
>>>
```

##### Advanced matrix operations #####

```Python
>>> s = Matrix(3,3)  #We create a new square matrix
>>> s.random(1,5)
>>> s
[4, 1, 1]
[1, 2, 2]
[3, 2, 1]
>>> s.is_square()
True
>>> s.determinant()  #Calculating the determinant
-7
>>> s.transpose()  #Calculating the transpose matrix
[4, 1, 3]
[1, 2, 2]
[1, 2, 1]
>>> f = Matrix(3,3)
>>> f.random(-10, 10)
>>> f
[-1, 2, 1]
[5, -8, -6]
[-3, 5, 4]
>>> f.inverse_matrix()  #Calculate the inverse matrix
[2.0, 3.0, 4.0]
[2.0, 1.0, 1.0]
[-1.0, 1.0, 2.0]
>>> f * s  #Product between matrices
[1, 5, 4]
[-6, -23, -17]
[5, 15, 11]
>>>
```

##### Accessing and modifying the elements of a matrix #####

```Python
>>> s[0]  #Get the first row
[4, 1, 1]
>>> s[0][2]  #Get the third element of the first row
1
>>> s[0][2] = 15  #Set the element (1, 3) as 15
>>> s
[4, 1, 15]
[1, 2, 2]
[3, 2, 1]
>>> 15 in s  #Check if the matrix contains a number
True
>>> del(s[1])  #Delete the second row
>>> s
[4, 1, 15]
[3, 2, 1]
>>> s.rows  #The dimensions are automatically updated
2
>>>
```

### Contributions ###

Contributions are welcome! Please feel free to submit a Pull Request.
