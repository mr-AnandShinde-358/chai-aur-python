""" password = "4512d41"
if len(password)<6:
    strength="Week"
elif len(password)<10:
    strength="Medium"
else:
    strength="Strong"
print("Your password strange is",strength) """

password = "4512d41"

password_length=len(password)


if password_length < 6:
    strength="Week"
elif password_length < 10:
    strength="Medium"
else:
    strength="Strong"



print("Your password strange is",strength)