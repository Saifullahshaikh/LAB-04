print('saifullah- 1bB-092-CS  A')
print('Lab-04, P.Ex.4')
Name = input('Enter your name:')
F_name = input('Enter your father name:')
R_num = input('Enter your roll number:')
#Subjects
sub1 = str(input('Enter subject 1:'))
sub2 = str(input('Enter subject 2:'))
sub3 = str(input('Enter subject 3:'))
sub4 = str(input('Enter subject 4:'))
sub5 = str(input('Enter subject 5:'))
Marks = 100
#Obtained marks
m_sub1 = int(input('Enter your marks in sub1:'))
m_sub2 = int(input('Enter your marks in sub2:'))
m_sub3 = int(input('Enter your marks in sub3:'))
m_sub4 = int(input('Enter your marks in sub4:'))
m_sub5 = int(input('Enter your marks in sub5:'))
Total_Obtain_m =(m_sub1+m_sub2+m_sub3+m_sub4+m_sub5)
percnt = ((Total_Obtain_m/(Marks*5))*100)
print('Name:', Name)
print('Father Name:', F_name)
print('Roll No:', R_num)
print('Sr.no \t\t Subjects \t\t Marks \t\t Obtained Marks\n1\t\t',(sub1),'\t\t', (Marks),'\t\t', (m_sub1),'\n2\t\t', (sub2),'\t\t\t', (Marks),'\t\t', (m_sub2),'\n3\t\t', (sub3),'\t\t\t', (Marks),'\t\t', (m_sub3),'\n4\t\t', (sub4),'\t\t', (Marks),'\t\t', (m_sub4),'\n5\t\t', (sub5),'\t\t', (Marks),'\t\t', (m_sub5),'\n6\t\t', 'Total','\t\t\t', (Marks*5),'\t\t', (Total_Obtain_m))
print('Percentage = \t', percnt, '%')
if percnt > 80:
      print('Grade \t A \n Conratulation!')
elif percnt > 70:
      print('Grade \t B \n Conratulation!')
elif percnt > 60:
      print('Grade \t C \n Good!')
elif percnt > 50:
      print('Grade \t D \n pass')
elif percnt > 40:
      print('Grade \t E \n pass but work hard')
else:
      print('Grade \t F \n Sorry you are fail')
