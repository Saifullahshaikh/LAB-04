print('saifullah 18B-092-CS')
print('Lab 4, Program 6')
row_num = int(input("Input number of rows:"))
col_num = int(input("Input number of columns:"))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
   for col in range(col_num):
     multi_list[row][col]=row*col
print(multi_list)
