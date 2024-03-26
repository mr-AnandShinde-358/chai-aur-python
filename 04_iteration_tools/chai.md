# inner workin in loop

## for loop iteration in file
```
>>> for line in open('chai.py'):
...     print(line,end="")
...
import time

print("chai is here")

username = "Hitesh"

print(username)>>>
```

## while loop iteration in file
```
>>> f = open('chai.py')
>>> while True:
...     line=f.readline()
...     if not line:break
...     print(line,end='')
... 
import time

print("chai is here")

username = "Hitesh"  

print(username)>>>
```

## Not keyword use

```
>>> test="hitesh"
>>> if not test:
...     print("chai")
... 
>>> test=""
>>> if not test:
...     print('chai')
... 
chai
>>>
```
## list inner working for loop
```
>>> myList = [1,2,3,4]
>>> I= iter(myList)
>>> I
<list_iterator object at 0x0000022334466A10>
>>> I.__next__()
1   
>>> I            
<list_iterator object at 0x0000022334466A10>
>>> I= iter(myList)
>>> I.__next__()       
1   
>>> I.__next__()
2   
>>> I.__next__()
3   
>>> I.__next__()
4   
>>> 
```

iter() method are  are get refrence (point) of first element of itarable object like string , list etc.

```
 I= iter(myList)
 >>> I
<list_iterator object at 0x0000022334466A10>
```
in this case I get refrence(memory address) of mylist object first element 

```
>>> I.__next__()
```
__next__() method are have another pointer variable it's self it  starting point I memory obj but next time obj ++ (according data type) 
I - point old memory address but
I.__next__() point a new (next) memory address

```
>>> myList = [1,2,3,4]
>>> I= iter(myList)
>>> I
<list_iterator object at 0x0000022334466A10>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x0000022334466A10>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
```
list khatam hone ke bad StopIteration expetion raise ho jayega

```
>>> f=open('chai.py')
>>> iter(f) is f
True
>>> iter(f) is f.__iter__()
True
>>> 

>>> mylist=[1,2,3]
>>> iter(mylist) is mylist
False
>>>  
```

file ko jab ab kisi varible ke under store karate ho refrence lete ho
to oh apane aapame ek iterable obj hai 

lekin jab apane list ka is varible me memory location (refrence) liya hai oh usaka iterable obj nahi hai oh sirf us actual object ka refrence hai

## dictonay itrable exp
```
>>> D={'a':1,'b':2}
>>> for key in D.keys():
...     print(key)
... 
a   
b   
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x00000201E1F13010>
>>> I.__next__()
'a'
>>> I.__next__()
'b'
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

## range itrable

```
>>> range(5)
range(0, 5)
>>> R=range(5)
>>> R
range(0, 5)
>>> I = iter(R)
>>> I
<range_iterator object at 0x00000201E1B7A0B0>
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```