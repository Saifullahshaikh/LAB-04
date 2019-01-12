print('saifullah 18B-092-CS')
print('Lab 4, Program 5')
initial_value = eval(input('Enter the initial value for the range:'))
final_value = eval(input('Enter the final valuefor the range:'))
numbers = range(initial_value,final_value)
sum = 0
for value in numbers:
    sum = sum+value
print('The sum is',sum)
