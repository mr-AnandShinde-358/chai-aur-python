# Dictionary in Python
```
>>> chai_types = {"masala":"Spicy","Ginger":"Zesty","Green":"Mild"} 
>>> chai_types
{'masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["masala"]
'Spicy'
>>> chai_types.get("Ginger")
'Zesty'
>>> chai_types.get("Gingery") 
>>> chai_types.get("Masala")  
>>> chai_types.get("Masalaa") 
>>> chai_types.get("Ginger")  
'Zesty'
>>> chai_types.get("masala") 
'Spicy'
>>> chai_types.get("masalaa") 
>>> chai_types["masalaa"]     
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
KeyErr
```

```
for chai in chai_types:
...     print(chai,chai_types[chai])
...
masala Spicy
Ginger Zesty
Green Fresh
>>>
```

```
>>> chai_types = {"masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
>>> for key,value in chai_types.items():
...  print(key,value)
... 
masala Spicy
Ginger Zesty
Green Mild  
>>>
```

```
>>> if "masala" in chai_types:
...     print("I have masala chai")
... 
I have masala chai
>>> print(len(chai_types))
3   
>>> 
```

```
>>> chai_types["Earl Grey"]="Citrus"
>>> chai_types
{'masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild', 'Earl Grey': 'Citrus'}
>>> chai_types.pop("Ginger")
'Zesty'
>>> chai_types
{'masala': 'Spicy', 'Green': 'Mild', 'Earl Grey': 'Citrus'}
>>>
>>> chai_types.popitem()
('Earl Grey', 'Citrus')
>>> chai_types
{'masala': 'Spicy', 'Green': 'Mild'}
>>>
```

```
 del chai_types["Green"]
>>> chai_types
{'masala': 'Spicy'}
>>> chai_types_copy=chai_types.copy()
>>> chai_types_copy
{'masala': 'Spicy'}
>>> tea_shop = {
... "chai":{"Masala":"Spicy","Ginger":"Zesty"},
... "Tea":{"Green":"Mild","Black":"Strong"} 
... }
>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> print(tea_shop)
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"]
'Zesty'
>>> tea_shop["chai"]["Masala"] 
'Spicy'
>>> tea_shop["Tea"]["Black"]
'Strong'
>>>
```

```
>>> squared_num = {x:x**2 for x in range(5)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
>>> squared_num.clear()
>>> squared_num
{}
>>>
```

```
>>> keys=["Masala","Ginger","Lemon"]
>>> keys
['Masala', 'Ginger', 'Lemon']
>>> default_value="Delicious"
>>> new_dict=dict.fromkeys(keys,default_value)
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> new_dict=dict.fromkeys(keys,keys)          
>>> new_dict
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
>>>
``
