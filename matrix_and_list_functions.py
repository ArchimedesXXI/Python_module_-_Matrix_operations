def make_matrix(rows=0, columns=0, list_of_list=[[]]):
    '''
    (int, int, list of list) -> list of list (i.e. matrix)
    Return a list of list (i.e. matrix) from "list_of_list" if given
    or if not given a "list_of_list" parameter,
    then prompt user to type in values for each row
    and return a matrix with dimentions: rows x columns.
    '''
    if list_of_list == [[]]:
        matrix = make_matrix_manually(rows, columns)
        return matrix
    else:
        rows = size_of(list_of_list)
        columns = size_of(list_of_list[0])
        for item in list_of_list:
            if size_of(item) != size_of(list_of_list[0]):
                print('The number of columns in every row should be equal, but isn\'t!')
                return None                
        matrix = list_of_list
        return matrix
    

def make_matrix_manually(rows=0, columns=0):
    '''
    (int, int) -> list of list (i.e. matrix)
    Prompt user to type in values for each row and return a matrix
    with dimentions: rows x columns.
    '''
    matrix = []
    for i in range(rows):
        print('Type in values for ROW', i+1, 'seperated by commas: ', end='')
        
        current_row = convert_str_into_list(input())
        matrix.append(current_row)
        if size_of(current_row) != columns:
            print('Number of values different then declared columns!')
            return None
    return matrix


def make_Id_matrix(size=1):
    '''
    (int) -> list of list (i.e. matrix)
    Return an Identity Matrix (1's across the diagonal and all other entries 0's)
    with dimentions: size x size.
    '''
    Id_matrix = []
    for i in range(1, size+1):
        current_row = convert_str_into_list('0,'*(i-1) + '1,' + '0,'*(size-i))
        Id_matrix.append(current_row)
    return Id_matrix
    
    

def convert_str_into_list(string):
    '''
    (str)-> list of numbers
    Return a list of numbers from a string.
    Precondition: the string should consist of numbers separated by commas.
    '''
    list = []
    
    # step 1: remove all empty spaces.
    i = 0
    length = len(string)
    while i <=(length-1):
        if string[i] == ' ':
            string = string[:i] + string[i+1:]
            length = len(string)
        else:
            i += 1    # (a += b)  is equivalent to (a = a + b)

    # step 2: extract sections seperated by commas, turn them into floats
    #         and append them to the list. 
    j = 0
    i = 0
    for j in range(len(string)+1):
        if j==(len(string)) or string[j]==',':
            item = string[i:j]
            i = j+1
            if item =='':
                pass
            else:
                list.append(float(item))
        j = j + 1
    return list


# *values - means, that we do not know up front, what number of
# parameters (atributes) we're going to pass to the function.
def convert_into_list(*values):
    '''
    (items separated by commas) -> list
    Return a list of values.
    (Return values in the form a variable of type LIST.)
    '''
    list = []
    for value in values:
        list.append(value)
    return list
    
        
def size_of(list):
    '''
    (list) -> int
    Return the number of entries (items) in a given list.
    '''
    size = 0
    for item in list:
        size = size+1
    return size


def add_matrix(matrix1, matrix2):
    '''
    (list of list, list of list) -> list of list
    Return the result of addition of two matrices: matrix1 and matrix2.
    Precondition: matrix1 and matix2 have to have the same dimentions.
    '''
    if size_of(matrix1) != size_of(matrix2):
        print('Error: matrices do not have the same dimentions (size)!')
        return None
    matrix_sum = []
    for i in range(size_of(matrix1)):
        if size_of(matrix1[i]) != size_of(matrix2[i]):
            print('Error: matrices do not have the same dimentions (size)!')
            return None
        matrix_sum.append([])
        for j in range(size_of(matrix1[i])):
            matrix_sum[i].append(matrix1[i][j] + matrix2[i][j])
    return matrix_sum


def neg_matrix(matrix1):
    '''
    (list of list) -> list of list
    Return the result of the operation of negation on matrix1.
    '''
    matrix_n = []
    for i in range(size_of(matrix1)):
        matrix_n.append([])
        for j in range(size_of(matrix1[i])):
            matrix_n[i].append(-matrix1[i][j])
    return matrix_n


def substract_matrix(matrix1, matrix2):
    '''
    (list of list, list of list) -> list of list
    Return the result of substraction of two matrices: matrix1 and matrix2.
    Precondition: matrix1 and matix2 have to have the same dimentions.
    '''
    sub_matrix = add_matrix(matrix1, neg_matrix(matrix2))
    return sub_matrix


def multiply_matrix_by_float(arg1, matrix1):
    '''
    (number, list of list) -> list of list
    Return the result of multiplication of matrix1 by arg1.
    '''
    matrix_new = []
    for i in range(size_of(matrix1)):
        matrix_new.append([])
        for j in range(size_of(matrix1[i])):
            matrix_new[i].append(arg1 * matrix1[i][j])
    return matrix_new

    
def multiply_matrix_by_matrix(matrix1, matrix2):
    '''
    (list of list, list of list) -> list of list
    Return the result of multiplication of matrix1 by matrix2.
    '''
    matrix_new = []
    #
    # Checking if matrices can be multiplied.
    #
    # rows     =  matrix_and_list_functions.size_of(Matrix_name)
    # columns  =  matrix_and_list_functions.size_of(Matrix_name[0])
    #
    if size_of(matrix1[0]) == size_of(matrix2):
        #
        # implementing Matrix multiplication here.
        #   
        for i in range(size_of(matrix1)):
            matrix_new.append([])
            for j in range(size_of(matrix2[0])):
                ABij = 0
                for k in range(size_of(matrix1[0])):
                    ABij = ABij + (matrix1[i][k]*matrix2[k][j])
                matrix_new[i].append(ABij)
        return matrix_new

    else:
        print('Error: The number of columns in matrix1 has to be equal to the number of rows in matrix2!')
        return []
    



    
