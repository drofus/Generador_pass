import random
contraseña = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long = int(input("Introduzca la longitud del password: "))

password = ""
for i in range(long):
    password += random.choice(contraseña)

print(password)