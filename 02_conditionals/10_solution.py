pets_type="Dog"
pets_age=10


if pets_type=="Cat":
    if pets_age > 5:
        food="Senior cat food"
    else:
        food="Junior cat food"
elif pets_type=="Dog":
    if pets_age<2:
        food="Puppy food"
    else:
        food="adult food"

print("According your  pet type  {} and pet age  {} AI recommend you givi your pet {}".format(pets_type,pets_age,food))