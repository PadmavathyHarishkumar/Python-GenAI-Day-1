print('-------- Remove lowercase from string --------')
print()
name=input('Enter your name:-')
result=''
print()
l=len(name)
for i in range(l):
    if name[i].isupper():
        result=(name[i])
        print(result,end='')
print()

print('-------- Evaluating an expression --------')
print()
expression=input('Enter your expression:')
print()
print(eval(expression))
print()

print('------- Insert spaces between uppercase -------')
print()
greet=input('Enter your greet:-')
print()
l=len(greet)
result=''
for i in range(l):
    if(greet[i].isupper() and i>0):
        result+=' '+greet[i]
    else:
        result+=greet[i]
print(result)
print()

print('------ Remove paranthesis area in string ------')
print()
greet=input('Enter your input:-')
print()
l=len(greet)
result=''
text=0
for i in range(l):
    if greet[i]=='(':
        text=1
    elif greet[i]==')':
        text=0
    elif text==0:
        result+=greet[i]
print(result)
print()

print('------- Split with multiple delimiters -------')
print()
word=input('Enter your sentence:-')
print()
word=word.replace(',',' ').replace('.',' ')
result=word.split()
print(result)
print()
print('----- Finding adverbs and their position -----')
print()
word=input('Enter your sentence:-')
print()
words=word.split()
l=len(words)
for i in range(l):
    if words[i].endswith('ly'):
        print('adverb =>',words[i],'---->', 'Position =>',i+1)
print()

print('-------- Case insensitive replacement --------')
print()
word=input('Enter your sentence:-')
print()
word_to_be_replaced='fully'
new_word='partially'
words=word.split()
l=len(words)
for i in range(l):
    if words[i].casefold()== word_to_be_replaced.casefold():
        words[i]=new_word
words=' '.join(words)
print(words)
print()

print('-------- Split at uppercase --------')
print()
word=input('Enter your sentence:-')
print()
l=len(word)
result=''
for i in range(l):
    if word[i].isupper():
        result+=' '+word[i]
    else:
        result+=word[i]
        parts=result.split()
print(parts)
print()

print('-------- Removing non alphanumeric --------')
print()
word=input('Enter your word:-')
print()
l=len(word)
result=''
for i in range(l):
    if word[i].isalnum():
        result+=''+word[i]
print(result)
print()

print('-------- Removing whitespaces --------')
print()
word=input('Enter your word:-')
print()
l=len(word)
result=''
for i in range(l):
    if word[i]==' ':
        result=word.replace(' ','')
print(result)
print()
    
