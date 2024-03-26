# numbers or string ka immidate garbej collection nahi hota hai 
## 01 example
```
>> a=3             
>>> a='chaiaurcode'
>>> 
```
in this case not detroy 3 in memory  immidatary

### python me kabi bhi value store hoti hai tabi sabase pahile 3 ka ek object ye memory me store hota hai aur oh phir a ko point karata hai 

### jo bhi object ka type hota hai ho kabi bhi object ke andhar rahata hai names me nahi rahata

## 02 example

```
>>> a=5
>>> b=2
>>> a
5
>>> b
2
>>> a=a+2
>>> a
7
>>>
```
## 03 explain
a=5 <br><br>
in this case  a=5 sabase pahale  memory me 5 ka ek object bana hoga aur us obj ne a ko point karana start kiya hoga <br>
<br>
b=2
in this case b=2 sabase pahale memory me 2 ka ek object bana hoga aur us obj ne b ko point kiy hoga <br><br>
a=a+2 <br>
### python ke andar jaha ka bhi reference hota hai calculation se pahale sari refresence ki value autometaicaly oha par aa jati hai
<br>
that why 
in this case a= a+2  ke samay 'a' ke jaga par 5 ki value aa gai hogi <br> 5+2(a+2)
<br>
a=5+2
<br>

a=7
then 7 ka ek naya obj create hota hai aur a ab us 7 ke obj ko point karata hai

## 04 example 

### List me humne agar same value bhi diye to do alag alag variable ko to usake liye python do alag alag obj banata hai above example 

```
>>> myListOne = [1,2,3]   
>>> myListTwo = myListOne
>>> myListOne='chai'      
>>> myListTwo
[1, 2, 3]
>>> myListOne = [1,2,3]
>>> myListTwo
[1, 2, 3]
>>> myListOne[0]=33
>>> myListOne      
[33, 2, 3]
>>> myListTwo       
[1, 2, 3]
```
humne  myListOne = [1,2,3] aur myListTwo = myListOne karake dono ko ekhi list type ke obj se point karaya then <br>
myListOne='chai' me ab string type ke obj ne myListOne ko point kiya <br>
 myListOne = [1,2,3] jab humne ye kiya to ek naya obj memory me bana list type ka myListOne ab nay obj ko point kar raha hai <br>
 myListTwo ye apane purane obj ko hi point kara hai <br>
 isiliye jab
  <br> 
  myListOne[0]=33 
  <br>
   myListOne     ko print kiya to  
[33, 2, 3] ye result aya aur
 <br>
myListTwo ka ye result aya 
[1, 2, 3]
<br>
ye abhi bhi pahile obj ko point kar raha tha

## 04 exp

```
>>> l1=[1,2,3]
>>> l2=l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
>>> l1[0]=44
>>> l2
[44, 2, 3]
>>>
```

in this case <br>
l1=[1,2,3]<br>
create one obj list type ka [1,2,3] aur vo point karega 'l1' ko <br>
l2=l1<br>
l2 point kar raha hai same obj ko jo l1 ke liye bana hai<br>
l1[0]=44
in this time us obj me zero element pe se 1 ki value change hoke 44 hoi
<br>
agar hum l2 ko print karege to <br>
usaka output kya ayega?<br>
yes change huaa obj hi aye ga kyuki dono jan same obj ko poin kar rahe the
<br>
[44, 2, 3]

## 05 example 
### when we can do any slicing this time we create a copy of obj
```
>>> h1=[1,2,3]
>>> h2=h1[:]
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]
>>> h1[0]=33
>>> h2
[1, 2, 3]
```

```
>>> import copy
>>> h2=copy.copy(h1) 
>>> h2=copy.deepcopy(h1)
```
h2=copy.copy(h1)  is me h1 list type  obj ki ek copy banake us obj ko h2 point karega
 h2=copy.deepcopy(h1) is me list ke andhar bhi agar koi list hogo to usko bhi copy karake h2 ko assing karate hai obj ke andar ke obj ko bhi copy karate hai aur new obj banate hai

 ## 6 exapmle

 ```
 >>> n=[1,2,3]
>>> m=n
>>> n
[1, 2, 3]
>>> m
[1, 2, 3]
>>> m==n
True
>>> m is n
True
>>> m=[1,2,3]
>>> m==n
True
>>> m is n
False
>>>
 ```

  n=[1,2,3] <br>
 m=n<br>

 in this case memory me ek list type ka obj banaya aur m aur n ko usase point karaya

 m==n<br>
 True

 == is check value of are same or not <br>
 'is' check  location are same or not<br>


  m is n <br>
True<br>
location are same that's why out true
m=[1,2,3] <br>
this time create new obj in memory list type and assign m value of this
m==n <br> value is same
True <br>
m is n <br> memory location are diffrent
False <br>