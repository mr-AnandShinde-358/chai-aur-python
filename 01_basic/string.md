# string in python

```
>>> chai = 'Lemon chai'
>>> chai
'Lemon chai'
>>> print(chai)
Lemon chai

>>> chai = "Masala Chai"
>>> first_char=chai[0]
>>> print(first_char)
M   
>>> 
```

## slicing and dacing
```
>>> num_list="0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[:7] 
'0123456'
>>> num_list[0:7:2]
'0246'
>>> num_list[0:7:3]
'036'
```

## more methods
```
chai="masala chai"
>>> chai
'masala chai'
>>> print(chai.lower())
masala chai
>>> print(chai.upper()) 
MASALA CHAI
>>> chai
'masala chai'
>>> chai="   Masala Chai  "
>>> chai
'   Masala Chai  '
>>> print(chai.strip())
Masala Chai
>>> chai = "Lemon Chai"
>>> print(chai.replace("Lemon","Ginger"))
Ginger Chai
>>> chai
'Lemon Chai'
>>> chai = "Lemon, Ginger, Masala, Mint"
>>> print(chai.split())
['Lemon,', 'Ginger,', 'Masala,', 'Mint']
>>> print(chai.split(", "))
['Lemon', 'Ginger', 'Masala', 'Mint']
```



```
>>> chai="Masala Chai"     
>>> print(chai.find("chai"))
-1
>>> print(chai.find("chai"))


>>> chai="   Masala Chai  "
>>> chai
'   Masala Chai  '
>>> print(chai.strip())
Masala Chai
>>> chai = "Lemon Chai"
>>> print(chai.replace("Lemon","Ginger"))
Ginger Chai
>>> chai
'Lemon Chai'
>>> chai = "Lemon, Ginger, Masala, Mint"
>>> print(chai.split())
['Lemon,', 'Ginger,', 'Masala,', 'Mint']
>>> print(chai.split(", "))
['Lemon', 'Ginger', 'Masala', 'Mint']
>>>
>>> chai="Masala Chai"
>>> print(chai.find("chai"))
-1
>>> print(chai.find("Chai"))
7
>>> chai = "Masala Chai Chai Chai Chai chai"
>>> print(chai.count("Chai")
...
... )
4
```

## formating string
```
chai_type="Masala"
>>> quantity=2
>>> order="I ordered {} cups of {} chai"
>>> order                               
'I ordered {} cups of {} chai'
>>> print(order.format(quantity,chai_type))
I ordered 2 cups of Masala chai
```

## list to string
```
>>> chai_variety=["Lemon","Masala","Ginger"]
>>> chai_variety
['Lemon', 'Masala', 'Ginger']
>>> print("".join(chai_variety))
LemonMasalaGinger
>>> print(" ".join(chai_variety))
Lemon Masala Ginger
>>> print(", ".join(chai_variety))  
Lemon, Masala, Ginger
>>>
```

```
>>> chai
'Masala Chai Chai Chai Chai chai'
>>> chai="Masala Chai"
>>> print(len(chai))
11
>>> chai
'Masala Chai'
>>> for letter in chai:
...     print(letter)
... 
M
a
s
a
l
a

C
h
a
i
>>>
```

```
>>> chai = "He said, \"Masala chai is awesome\" " 
>>> chai
'He said, "Masala chai is awesome" '
>>> chai="Masala\nChai"
>>> chai
'Masala\nChai'
>>> print(chai)
Masala
Chai
>>> chai = r"Masala\nchai"
>>> chai
'Masala\\nchai'
>>> print(chai)
Masala\nchai
>>> chai=r"Masala\nchai"
>>> chai
'Masala\\nchai'
>>> chai=r"c:\user\pwd\"
  File "<stdin>", line 1
    chai=r"c:\user\pwd\"
         ^
SyntaxError: unterminated string literal (detected at line 1)
>>> chai=r"c:\\user\\pwd\\"
>>> print(chai)
c:\\user\\pwd\\
>>>
```

```
>>> chai = r"c:\user\pwd"                         
>>> print(chai)
c:\user\pwd
>>>
```

```
>>> chai = "c:\user\pwd"  
  File "<stdin>", line 1
    chai = "c:\user\pwd"
           ^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
>>>
>>> chai = "c:\\user\\pwd"
>>> chai
'c:\\user\\pwd'
>>>
```

```
>>> chai="Masala Chai"
>>> "Masala" in chai
True
>>> "Masalaa" in chai 
False
>>> print( "Masalaa" in chai)
False
>>> print( "Masala" in chai)  
True
```