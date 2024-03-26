# Tuples in Pythons

```
>>> tea_types=("Black","Green","Oolong")
>>> tea_types
('Black', 'Green', 'Oolong')
>>> tea_types(0)
Traceback (most recent call last):       
  File "<stdin>", line 1, in <module>    
TypeError: 'tuple' object is not callable
>>> tea_types[0]
'Black'
>>> tea_types[-1]
'Oolong'
>>> tea_types[0]="Lemon"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> tea_types=("Masala","Green","Oolong","Black")
>>> tea_types
('Masala', 'Green', 'Oolong', 'Black')
>>> more_tea=("Herbal","Earl Grey")
>>> all_tea = more_tea          
>>> all_tea
('Herbal', 'Earl Grey')
>>> all_tea = more_tea+more_tea
>>> all_tea
('Herbal', 'Earl Grey', 'Herbal', 'Earl Grey')
>>> all_tea = more_tea+tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Masala', 'Green', 'Oolong', 'Black')
>>> if "Green" in all_tea:
...     print("I have Green tea")
... 
I have Green tea
>>>
```

```
>>> more_tea=("Herbal","Earl Grey","Herbal")
>>> more_tea
('Herbal', 'Earl Grey', 'Herbal')
>>> more_tea.count("Herbal")
2
>>> more_tea.count("Herb")   
0
>>>
```

```
>>> tea_types
('Masala', 'Green', 'Oolong', 'Black')
>>> (masala,green,oolong,black)=tea_types
>>> masala
'Masala'
>>> oolong
'Oolong'
>>> type(masala)
<class 'str'>
>>> type(tea_types)
<class 'tuple'>
>>> type(tea_types[0])
<class 'str'>
>>>
```