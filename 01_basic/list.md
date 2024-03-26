# List in python

```
>>> tea_varities=["Black","Green","Oolong","White"]
>>> print(tea_varities)
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities[0])
Black
>>> print(tea_varities[1]) 
Green
>>> print(tea_varities[-1])
White
>>> print(tea_varities[1:3])
['Green', 'Oolong']
>>> print(tea_varities[:3])  
['Black', 'Green', 'Oolong']
>>> print(tea_varities[2:]) 
['Oolong', 'White']
>>> print(tea_varities[:3:1])
['Black', 'Green', 'Oolong']
>>> print(tea_varities[:3:2]) 
['Black', 'Oolong']
>>> tea_varities[3]="Harber" 
>>> print(tea_varities)
['Black', 'Green', 'Oolong', 'Harber']
>>>
```

```
KeyboardInterrupt
>>> print(tea_varities)
['Black', 'Green', 'Oolong', 'Harber']
>>> tea_varities[1:2]
['Green']
>>> tea_varities[1:2]="Lemon"
>>> print(tea_varities)
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Harber']
>>>
```

```
>>> tea_varities=["Black","Green","Oolong","White"]
>>> tea_varities=["Black","Green","Oolong","White"]
>>> tea_varities
['Black', 'Green', 'Oolong', 'White']
>>> tea_varities[1:2]
['Green']
>>> tea_varities[1:2]=["Lemon"]
>>> tea_varities
['Black', 'Lemon', 'Oolong', 'White']
>>> tea_varities[1:3]
['Lemon', 'Oolong']
>>> tea_varities
['Black', 'Lemon', 'Oolong', 'White']
>>> tea_varities[1:3]
['Lemon', 'Oolong']
>>> tea_varities[1:3]:["green","Masala"]
>>> tea_varities
['Black', 'Lemon', 'Oolong', 'White']
>>> tea_varities[1:3]=["green","Masala"]
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>>
```

```
>>> tea_varities[1:1]
[]
>>> tea_varities[1:1]=["test","test"]
>>> tea_varities
['Black', 'test', 'test', 'green', 'Masala', 'White']
```

```
>>> test_varities = ['Black','test','test','green','Masala','White']
>>> test_varities[1:3]
['test', 'test']
>>> test_varities[1:3]=[]
>>> test_varities     
['Black', 'green', 'Masala', 'White']
>>> for tea in tea_varities:
...     print(tea)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tea_varities' is not defined. Did you mean: 'test_varities'?
>>> tea_varities = ['Black','test','test','green','Masala','White']  
>>> for tea in tea_varities:
...     print(tea)
... 
Black 
test  
test  
green 
Masala
White 
>>> tea_varities[1:3]=[]
>>> for tea in tea_varities:
...     print(tea)
... 
Black
green
Masala
White
>>>
```

```
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
... 
>>> 
```
```
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
... 
>>> tea_varities.append("Oolong")
>>> tea_varities                   
['Black', 'green', 'Masala', 'White', 'Oolong']

>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
... 
I have Oolong tea
>>>
```

```
>>> tea_varities
['Black', 'green', 'Masala', 'White', 'Oolong']
>>> tea_varities.pop()
'Oolong'
>>>
>>>
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>>
```

```
>>> tea_varities.remove("green")
>>> tea_varities
['Black', 'Masala', 'White']
>>>
>>> tea_varities.remove("green")
>>> tea_varities
['Black', 'Masala', 'White']
>>> tea_varities.insert(1,"green")
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>>
```
## diving refrence in memory same copy
```
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> tea_varities_copy=tea_varities.copy()
>>> 
 tea_varities
['Black', 'green', 'Masala', 'White']
>>> tea_varities_copy
['Black', 'green', 'Masala', 'White']
>>> tea_varities_copy.append("lemon")
>>> tea_varities_copy
['Black', 'green', 'Masala', 'White', 'lemon']
>>> tea_varities
['Black', 'green', 'Masala', 'White']9
```
## list comparision
```
>>> range(10)                              
range(0, 10)
>>> y=range(10)
>>> print(y)
range(0, 10)
>>> squared_num = [x**2 for x in range(10)]
>>> squared_num                            
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_num=[y**3 for y in range(5)]
>>> cube_num
[0, 1, 8, 27, 64]
>>> even_num=[x+2 for x in range(10)]
>>> even_num
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> even_num=[x/2 for x in range(10)] 
>>> even_num                          
[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
>>> 
>>> even_num=[x-2 for x in range(10)]
>>> even_num
[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
>>> 
```