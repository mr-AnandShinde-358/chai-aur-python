# Number in python

### python ke andhar number is not single obj its group off all objects

### python number carry - integer,float,decimal,fraction ,complexnumber,set ,boolean

```
>>> x=2
>>> y=3
>>> z=4
>>> x+y
5   
>>> (x+y)*z
20  
>>> x+(y*z)  
14  
>>> 40+2.23
42.23
>>> 'hitesh'+3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> int(2.23)
2   
>>> float(40)
40.0

```

```
>>> 'chai'+'code'
'chaicode'
>>> x,y,z
(2, 3, 4)
>>> x+1,y*2
(3, 6)
>>> y%2
1
>>> z**2
16
>>> z**5
1024
>>> 100**2
10000
>>> 2**100
1267650600228229401496703205376
>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> 2***10
  File "<stdin>", line 1
    2***10
       ^
SyntaxError: invalid syntax
>>> repr('chai')
"'chai'"
>>> str('chai')
'chai'
>>> print('chai')
chai
>>>
```

```
>>> 1<2
True
>>> 5.0==5.0
True
>>> 4.0 != 5.0
True
>>> x,y,z
(2, 3, 4)
>>> x<y<z
True
>>> x<y and y<z
True
>>> 1==2<3
False
>>> 1==2 and 2<3
False
```

```
import math
>>> math.floor(3.5)
3
>>> math.floor(-3.5)
-4
>>> math.floor(3.6)
3
>>> math.floor(3.9)
3
```

- math.floor closes number of buttom number get it 2.3 ,2.6,2.9 it out 2

```
>>> math.trunc(3.5)
3
>>>
>>>
>>> math.floor(-3.9)
-4
>>>
```

- toware to 0 out get it 3.5 out is 3 and -3.9 out is -3

## imijanary number
```
>>> 2+1j
(2+1j)
>>> (2+1j)*3
(6+3j)
>>>   
```

## binary/ocatal /hexdecimal numbers
```
>>> 0o20
16
>>> 0xFF
255
>>> 0b100
4
>>> 0b1000
8
>>> oct(64)
'0o100'
>>>
>>> hex(64)
'0x40'
>>> bin(64)
'0b1000000'
>>>
>>> int('64',16)
100
>>> int('1000000',2)  
64
```

## random library
```
import random
>>> random.random()
0.11281142070106964
>>> random.randint(1,100)
75
>>> random.randint(1,100)
34
>>> random.randint(1,10)
8
>>> random.randint(1,10)
4
>>> random.randint(1,10)
3
>>> l1=['lemon','masala','ginger','mint']
>>> random.choice(l1)
'ginger'
>>> random.choice(l1)
'ginger'
>>> random.choice(l1)
'mint'
>>> random.choice(l1)
'lemon'
>>> random.choice(l1)
'lemon'
>>> random.choice(l1)
'ginger'
>>>
>>> random.shuffle(l1)
>>> l1
['mint', 'ginger', 'masala', 'lemon']
>>> random.shuffle(l1)
>>> l1
['lemon', 'masala', 'ginger', 'mint']
>>> random.shuffle(l1)
>>> l1
['masala', 'mint', 'lemon', 'ginger']
>>>
```

## deal with  decimal numbers 
```
>>> 0.1+0.1+0.1
0.30000000000000004
>>> 0.1+0.1+0.1-0.3
5.551115123125783e-17
>>> (0.1+0.1+0.1)-0.3
5.551115123125783e-17
>>> (0.1+0.1+0.1)-0.3
5.551115123125783e-17
>>>
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
Decimal('0.0')

>>> from fractions import Fraction
>>> myFra = Fraction(2,7)
>>> myFra
Fraction(2, 7)
>>>
```

## set 
```
>>> setone={1,2,3,4}
>>> setone & {1,3}
{1, 3}
>>> setone | {1,3}
{1, 2, 3, 4}
>>> setone | {1,3,7}
{1, 2, 3, 4, 7}
>>> setone
{1, 2, 3, 4}
>>> setone-{1,2,3,4}
set()
>>> type({})
<class 'dict'>

```

## boolean
```
>>> type(True)
<class 'bool'>
>>> True==1
True
>>> False==0
True
>>> True is 1
<stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False

>>> True
True
>>> 1
1
>>> True+4
5

>>>

```