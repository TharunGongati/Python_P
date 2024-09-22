#password Generator
#here we use "random.choices " because it can generate multiple sequence of elements in a list randomly 
import random 

A = int(input("welcome to 'PASSWORD GENERATOR'  \nHow many letters do you like in your password : "))

B = int(input("How many symbols do you like in your password : "))

C = int(input("How many numbers do you like in your password : "))

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']
numbers = ['1','2','3','4','5','6','7','8','9','0']

M = random.choices(letters,k=A)
Sl= random.choices(symbols,k=B)
NL = random.choices(numbers,k=C)
#D= int(len(M))
#E= int(len(Sl))
#F=int(len(NL))
K = ''
L =''
N=''
#for i in range(0,D-1) : #here every item in the list is converted into the int
 #   (M[i])=(M[i])
for j in M:
    K=K+j


#for i in range(0,E-1) :
  #  (Sl[i])=(Sl[i])
for j in Sl:
    L=L+j

#for i in range(0,F-1) :
   # (NL[i])=(NL[i])
for j in NL:
    N=N+j
#print(f'your secret code is {K}{L}{N}')
Password = K+L+N
print(f'your secret code is {Password}')


