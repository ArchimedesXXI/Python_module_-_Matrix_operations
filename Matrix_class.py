import matrix_and_list_functions
import operator

class Matrix(object):
    def __init__(self, rows=0, columns=0, list_of_list=[[]]):
        self.rows = rows
        self.columns = columns
        self.list_of_list = list_of_list
        self.matrix = matrix_and_list_functions.make_matrix(self.rows, self.columns, self.list_of_list)
        self.rows = matrix_and_list_functions.size_of(self.matrix)
        self.columns = matrix_and_list_functions.size_of(self.matrix[0])
#        print(self.matrix)

    def __str__(self):
        '''
        The special function (so called: "magic function"):  __str__
        tells Python what to do if we execute function   print()
        on object of this class.
        '''
        for i in range(matrix_and_list_functions.size_of(self.matrix)):
            print(self.matrix[i])
        return('is a matrix of size: ' + str(self.rows) + ' , ' + str(self.columns))

    def __add__(self, other):
        '''
        "Magic function" __add__ implements what happens to objects of
        this class if I use the addition '+' operator on them.
        '''
        self.result = matrix_and_list_functions.add_matrix(self.matrix, other.matrix)
        self.Added_Matrix = Matrix(list_of_list = self.result)
        return(self.Added_Matrix)

    def __neg__(self):
        '''
        "Magic function" __neg__ implements what happens to an object of
        this class if I use the negation '-' operator before them.
        '''
        self.result = matrix_and_list_functions.neg_matrix(self.matrix)
        self.Neg_Matrix = Matrix(list_of_list = self.result)
        return(self.Neg_Matrix)

    def __sub__(self, other):
        '''
        "Magic function" __sub__ implements what happens to objects of
        this class if I use the substraction '-' operator on them.
        '''
        self.result = matrix_and_list_functions.substract_matrix(self.matrix, other.matrix)
        self.Substracted_Matrix = Matrix(list_of_list = self.result)
        return(self.Substracted_Matrix)

    def __mul__(self, other):
        '''
        "Magic function" __mul__ implements what happens to objects of
        this class if I use the multiplication '*' operator on them.
        '''
        if type(other) == int or type(other) == float:
            self.result = matrix_and_list_functions.multiply_matrix_by_float(other, self.matrix)
            self.New_Matrix = Matrix(list_of_list = self.result)
            return(self.New_Matrix)
        elif isinstance(other, Matrix):
            self.result = matrix_and_list_functions.multiply_matrix_by_matrix(self.matrix, other.matrix)
            self.New_Matrix = Matrix(list_of_list = self.result)
            return(self.New_Matrix)
        else:
            print('You can only multiply Matrices by other Matrices or by scalars (e.g. int, float)!')

    def __rmul__(self, other):
        '''
        "Magic function" __rmul__ implements what happens to objects of
        this class if I use the multiplication '*' operator on them, but
        the order of arguments is reversed.
        '''
        if type(other) == int or type(other) == float:
            self.result = matrix_and_list_functions.multiply_matrix_by_float(other, self.matrix)
            self.New_Matrix = Matrix(list_of_list = self.result)
            return(self.New_Matrix)
        elif isinstance(other, Matrix):
            self.result = matrix_and_list_functions.multiply_matrix_by_matrix(other.matrix, self.matrix)
            self.New_Matrix = Matrix(list_of_list = self.result)
            return(self.New_Matrix)
        else:
            print('You can only multiply Matrices by other Matrices or by scalars (e.g. int, float)!')

        

class Square_Matrix(Matrix):
    def __init__(self, size=0):
        self.size = size
        self.matrix = matrix_and_list_functions.make_matrix(self.size, self.size)

    def __str__(self):
        for i in range(matrix_and_list_functions.size_of(self.matrix)):
            print(self.matrix[i])
        return('is a matrix of size: ' + str(self.size) + ' , ' + str(self.size))


class Id_Matrix(Square_Matrix):
    def __init__(self, size=1):
        self.size = size
        self.matrix = matrix_and_list_functions.make_Id_matrix(self.size)
        



