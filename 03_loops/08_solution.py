number = 1

its_prime = True

if number>1:
    for i in range(2,number):
        if (number%i)==0:
            its_prime=False
            break

if its_prime and number != 1:
    print("Your number is Prime")
else:
    print("Your number is not Prime")