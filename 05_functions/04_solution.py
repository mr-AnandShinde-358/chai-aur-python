import math
def circle_stats(redius):
   area= math.pi* redius**2
   circumference = 2* math.pi*redius
   return round(area,2),round(circumference,2)

a,c = circle_stats(3)
print("Area: ",a,"circumference: ",c)