#TODO: Implementa eccezioni
#TODO: Definisci moltiplicazione tra matrici (ed eccezioni se non si può fare)
#TODO: Aggiungi check del tipo a ogni operatore
#TODO: Aggiungi addizione tra matrice e numero

from random import randint
from copy import deepcopy

class Matrix(object):

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = []

        for i in range(rows):
            self.matrix.append([]) #Initialize empty rows

        for row in self.matrix:
            for i in range(columns):
                row.append(0) #Fill the rows with 0s

    def __repr__(self):
        #Just print the matrix row after row
        rep = ""
        for row in self.matrix:
            rep += str(row)
            rep += "\n"
        return rep.rstrip()

    def __getitem__(self, key):
        return self.matrix[key]

    def __setitem__(self, key, value):
        if isinstance(value, list):
            self.matrix[key] = value
        else:
            raise TypeError("A matrix object can only contain lists of numbers")
        return

    def __delitem__(self, key):
        del(self.matrix[key])
        return

    def __contains__(self, value):
        for row in self.matrix:
            for element in row:
                if element == value:
                    return True
                else:
                    pass
        return False

    def __eq__(self, otherMatrix):
        #Equality
        if isinstance(otherMatrix, Matrix):
            if (self.rows != otherMatrix.rows) or (self.columns != otherMatrix.columns):
                return False #They don't have the same dimensions, they can't be equal

            for row in range(self.rows): #Check the elements one by one
                for column in range(self.columns):
                    if self.matrix[row][column] != otherMatrix[row][column]:
                        return False

            return True
        else:
            return False

    def __ne__(self, otherMatrix):
        #Inequality
        #Check's for equality, then reverses the result
        return not self.__eq__(otherMatrix)

    def __add__(self, otherMatrix):
        #Adds 2 matrices of the same type
        return self.__add_or_sub(otherMatrix, "add")

    def __sub__(self, otherMatrix):
        #Subtracts otherMatrix from self
        return self.__add_or_sub(otherMatrix, "sub")

    def __mul__(self, secondTerm):
        if isinstance(secondTerm, (int, float, complex)):
            return self.__scalar_product(secondTerm)
        elif isinstance(secondTerm, Matrix):
            raise Exception("Matrix multiplication is not defined")
        else:
            raise TypeError("Can't multiply a matrix by non-int of type " + type(secondTerm).__name__)

    def __scalar_product(self, number):
        newMatrix = Matrix(self.rows, self.columns)

        for row in range(self.rows):
            for column in range(self.columns):
                newMatrix[row][column] = self[row][column] * number

        return newMatrix

    def __add_or_sub(self, other, operation):
        newMatrix = Matrix(self.rows, self.columns)

        if isinstance(other, (int, float, complex)):
            for row in range(self.rows):
                for column in range(self.columns):
                    if operation == "add":
                        newMatrix[row][column] = self[row][column] + other
                    if operation == "sub":
                        newMatrix[row][column] = self[row][column] - other
        elif isinstance(other, Matrix):
            if (self.rows == other.rows) and (self.columns == other.columns):
                for row in range(self.rows):
                    for column in range(self.columns):
                        if operation == "add":
                            newMatrix[row][column] = self[row][column] + other[row][column]
                        elif operation == "sub":
                            newMatrix[row][column] = self[row][column] - other[row][column]
                        else:
                            raise Exception("Invalid operation type")
            else:
                raise Exception(
                    "Can't add or subtract (%d, %d) matrix with (%d, %d) matrix" %
                    (self.rows, self.columns, other.rows, other.columns)
                )
                #We only support operations between matrices of the same type
        else:
            raise TypeError("Can only add or subtract a matrix with another matrix or a number")

        return newMatrix

    def is_square(self):
        return self.rows == self.columns

    def transpose(self):
        newMatrix = Matrix(self.columns, self.rows)

        for row in range(self.rows):
            for column in range(self.columns):
                newMatrix[column][row] = self.matrix[row][column] #a(i,j) = a(j,i)

        return newMatrix

    def complement_matrix(self, rowToDelete, columnToDelete):
        newMatrix = deepcopy(self)
        del(newMatrix[rowToDelete])
        newMatrix.rows -= 1

        for row in range(newMatrix.rows):
            del(newMatrix[row][columnToDelete])

        newMatrix.columns -= 1

        return newMatrix

    def algebric_complement(self, row, column):
        complementMatrix = self.complement_matrix(row, column)
        algebricComplement = (-1)**(row+column+2) * complementMatrix.determinant()

        return algebricComplement

    def determinant(self):
        if self.is_square():
            if self.rows == 1:
                #If it's a square matrix with only 1 row, it has only 1 element
                det = self[0][0] #The determinant is equal to the element
            elif self.rows == 2:
                det = (self[0][0] * self[1][1]) - (self[0][1] * self[1][0])
            else:
                #We calculate the determinant using Laplace's theorem
                det = 0
                for element in range(self.columns):
                    det += self[0][element] * self.algebric_complement(0, element)
            return det
        else:
            raise Exception("Can only calculate the determinant of a square matrix")

    def random(self, lower=0, upper=30):
        #Fills the matrix with random numbers (integers)
        for row in self.matrix:
            for i in range(self.columns):
                row[i] = randint(lower, upper)
