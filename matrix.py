#TODO: Implementa eccezioni
#TODO: Definisci moltiplicazione tra matrici (ed eccezioni se non si può fare)
#TODO: Aggiungi check del tipo a ogni operatore
#TODO: Aggiungi addizione tra matrice e numero
#TODO: Calcolo del determinante in modo ricorsivo con teorema di Laplace

from random import randint

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
        if (self.rows != otherMatrix.rows) or (self.columns != otherMatrix.columns):
            return False #They don't have the same dimensions, they can't be equal

        for row in range(self.rows): #Check the elements one by one
            for column in range(self.columns):
                if self.matrix[row][column] != otherMatrix[row][column]:
                    return False

        return True

    def __ne__(self, otherMatrix):
        #Inequality
        #Check's for equality, then reverses the result
        return not self.__eq__(otherMatrix)

    def __add__(self, otherMatrix):
        #Adds 2 matrices of the same type
        return self.__add_or_sub__(otherMatrix, "add")

    def __sub__(self, otherMatrix):
        #Subtracts otherMatrix from self
        return self.__add_or_sub__(otherMatrix, "sub")

    def __mul__(self, secondTerm):
        if isinstance(secondTerm, (int, float, complex)):
            return self.__scalar_product__(secondTerm)
        elif isinstance(secondTerm, Matrix):
            raise Exception("Matrix multiplication is not defined")
        else:
            raise TypeError("Can't multiply a matrix by non-int of type " + type(secondTerm).__name__)

    def __scalar_product__(self, number):
        newMatrix = Matrix(self.rows, self.columns)

        for row in range(self.rows):
            for column in range(self.columns):
                newMatrix[row][column] = self[row][column] * number

        return newMatrix

    def __add_or_sub__(self, otherMatrix, operation):
        if (self.rows == otherMatrix.rows) and (self.columns == otherMatrix.columns):

            newMatrix = Matrix(self.rows, self.columns)
            for row in range(self.rows):
                for column in range(self.columns):
                    if operation == "add":
                        newMatrix[row][column] = self[row][column] + otherMatrix[row][column]
                    elif operation == "sub":
                        newMatrix[row][column] = self[row][column] - otherMatrix[row][column]
                    else:
                        raise Exception("Invalid operation type")

            return newMatrix
        else:
            #TODO: Migliora formattazione del codice
            raise Exception(
                "Can't add or subtract (%d, %d) matrix with (%d, %d) matrix" %
                (self.rows, self.columns, otherMatrix.rows, otherMatrix.columns)
            )
            #We only support operations between matrices of the same type

    def is_square(self):
        return self.rows == self.columns

    def transpose(self):
        newMatrix = Matrix(self.columns, self.rows)

        for row in range(self.rows):
            for column in range(self.columns):
                newMatrix[column][row] = self.matrix[row][column] #a(i,j) = a(j,i)

        return newMatrix

    def determinant(self):
        if self.is_square():
            pass
        else:
            raise Exception("Can only calculate the determinant of a square matrix")

    def random(self, lower=0, upper=30):
        #Fills the matrix with random numbers (integers)
        for row in self.matrix:
            for i in range(self.columns):
                row[i] = randint(lower, upper)
