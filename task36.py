def print_operation_table (operation, num_rows, num_cols):
    for x in range (1,num_cols+1):
        for y in range (1,num_rows+1):
            print (operation (x, y), end=" ")
        print ()
x = int (input ("Введите x: ",))
y = int (input ("Введите y: ",))
print_operation_table (lambda x,y: x+y, x, y)
