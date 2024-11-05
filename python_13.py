ali = [40,60]
ali_ort = 40 * 0.4+ 60 *0.6
ali_ort

veli = [80,50]
veli_ort = 80 * 0.4+ 50 *0.6
veli_ort

murat = [40,90]
murat_ort = 40 * 0.4+ 90 *0.6
murat_ort

def ortalama(a,b):
    print(a * 0.4+ b *0.6)
    
ortalama(ali[0], ali[1])
ortalama(veli[0],veli[1])
ortalama(*ali)

# guncelleme geldi. vize %30 final % 70 oldu.
def ortalama(a,b):
    print(a * 0.3+ b *0.7)

ortalama(*ali)
ortalama(*veli)

def merhaba():
    print('Canim cigerim Nasilsin')
merhaba()

def selamlama(a):
    print('Merhaba', a, "Nasilsin?")

selamlama('Yasin')

def selamlama(Nalan):
    print('Merhaba ', Nalan, "Nasilsin?")

selamlama(20)

def toplama(x,y):
    print(x+y)
toplama(5,7)
toplama(2,3)
toplama('ali', 'Veli')

def multiply_1(a, b) :
    print(a * b) # it prints something
multiply_1(10, 5)

a = toplama(3,4)
print(a)

def toplama(x,y) :
    return (x+y)
toplama(3,4)
a = toplama(3,4)
print(a)
toplama(3,4) +5

def printli_fonk():
    print('Ben sadece ekrana cikti yazdiririm')

def returnlu_fonk():
    return 'Deger Dondururum'

print(printli_fonk())
print(returnlu_fonk())

a = printli_fonk()
b = returnlu_fonk()

type(a)
b + 'string'
type(b)

a = [1,2,3]
a. append(4)
a

print(a.append(5))
a

print(print('abc'))
type(print())

def multiply_1(a, b) :
    print(a * b) # it prints something
multiply_1(10, 5)

def multiply_2(a, b) :
    return(a * b) # returns any numeric data type value
print(multiply_2(10, 5))

print(type(multiply_1(10, 5)))
print(type(multiply_2(10, 5)))


def calculator(x, y, o):
    if o == "+" :
        return(x + y)
    elif o == "-" :
        return(x - y)
    elif o == "*" :
        return(x * y)
    elif o == "/" :
        return(x / y)
    else : return ("enter valid arguments!")

print(calculator(-12, 2, "+"))

def absolute_value(x):
    if x>=0 :
        return x
    else:
        return -x
    
absolute_value(8)
absolute_value(-23)
absolute_value(-23) + 23

def absolute_value(num) :
    """This function returns the absolute
    value of the entered number"""
    if num >= 0:
        return num
    else:
        return -num
print(absolute_value.__doc__)

absolute_value(5)
print(absolute_value(3.3))
print(absolute_value(-4))

def absolute_value(x):
    '''fonksiyon bir numeric deger aliyor
    ve bu degerin mutlak degerini donduruyor
    input ==== >numeric
    output ---- >numeric'''
    if x>=0 :
        return x
    else:
        return -x
    
absolute_value(5)
print(absolute_value.__doc__)
help(absolute_value)

def who(first, last) : # 'first' and 'last' are the parameters(or variables)
    print('Your first name is :', first)
    print('Your last name is :', last)
who ('Guido', 'van Rossum' ) # 'Guido' and 'van Rossum' are the arguments
print()
who ('Marry', 'Bold' ) # 'Marry' and 'Bold' are also the arguments

def pos_args(a, b) :
    print(a, 'is the first argument' )
    print(b, 'is the second argument' )
pos_args(3,4)
print()
pos_args(4,3)

pos_args('first', 'second' )
print()
pos_args('second', 'first')


def texter(text1, text2, text3) :
    print(f"{text2} {text3} {text1}")
a = "i"
b = "love"
c = "you"
texter(c, a, b)

a = 'i'
b = 'love'
c = 'you'
def texter(x,y,z):
    print(y,z,x)
texter(c,a,b)

def who(first, last) : # same structure as the previous one
    print('Your first name is : ', first)
    print ('Your last name is : ', last)
who(first='Guido', last='van Rossum' ) # calling the function is different
# we used kwargs to pass the values into the function


def tanisma(isim, soyad, yas ,meslek):
    print(f'Merhaba benim adim {isim} soyadim {soyad}, yasim {yas}. Meslegim ise {meslek}' )
tanisma('yasin', 'gunduz', 43, 'Data Analyst' )
tanisma('yasim',meslek = 'Data Analyst', soyad = 'Gunduz', yas = 43)
tanisma(isim = 'Yasin',meslek = 'Data Analyst', soyad = 'Gunduz', yas = 43)
tanisma(meslek = 'Data Analyst', soyad = 'Gunduz', yas = 43, isim = 'Yasin')
tanisma('Yasin', 'Gunduz', meslek = 'Data Analyst', yas = 43, )

count = 0
while count >= 0:
    print(count)
    count += 1
    if count == 10:
        break

count = 0
while count >= 0:
    print(count)
    count += 1
    if count == 10:
        count = -1

d = ['a' , 'b' , 'c' , 'd']
while d:
    print (d.pop())
print ('Done. ')

a = [1,2,3]
k = a.pop()
a
k
print(a.pop())

listem = [1,2,3,4,5,6]
cikti = listem.pop()
listem
cikti
print(listem.pop())

d = ['a' , 'b' , 'c' , 'd']
while len(d)>4:
    print (d.pop())
print ('Done. ')

d = [ 'a' , 'b', ' c', 'd' ]
while len(d)>4:
    print (d.pop ())
else:
    print ('Done. ')

s = "ABCDEF"
for i in range(5,0, -1):
    if (i%2) :
        print (s[i])

list(range(5,0,-1))

b = 0
d = []
while (b := b+1)<4:
    d. append (b)
print (d)

count = 0
while count <= 8:
    print(count)
    count += 1

for i in 'bus':
    print(i, end='')

print()

count = 0
for i in ['bus']:
    count += 1
    print(i, count, end='')

print()

a = ['foo' , 'bar' , 'baz' , 'qux' , ' corge' ]
while a:
    if(len(a)<3) :
        break
    print (a.pop(), end="")
print ( 'Done. ' )