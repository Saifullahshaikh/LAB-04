print('saifullah 18B-092-CS   A')
print('Lab04 program11')
print('This program will count total number of vowels from user defined sentence')
string=input('Enter your string:')
vowels=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
print('Number of vowels are:')
print(vowels)
