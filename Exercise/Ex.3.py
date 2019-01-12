print('saifullah- 1bB-092-CS  A')
print('Lab-04, P.Ex.3')
print('palindrome or not')
word = 'CIVIC'
word = word.casefold()
rev = reversed(word)
if list(word) == list(rev):
    print('Yes your string is palindrome')
else:
    print('Sorry your string is not palindrome')
     
