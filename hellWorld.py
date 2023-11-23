"""
Your module description

print("hello world")

a = 1
#print(a)
#print(type(a))
#print("a che vale " + str(a) + " è una variabile di tipo"  + (str(type(a))))
#name = input("come ti chiami? ")
#anni = input("quanti anni hai? ")
#genere = input("cosa sei? ")
#print("ciao " + name)
#print ("ciao {} hai {} anni e sei {}" .format(name, anni, genere))

List = ["apple", "banana", "cherry"]
n = 0
for a in List:
    n += 1
    print(a, n)

import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

richiesta = input("Do you need to ship a package? (Enter yes or no) ")
if richiesta == "yes":
    print("ua fraaaaa")
elif richiesta == "no":
    print ("afammocc")
else:
    print ("ma cheriit?")
  
import random    

number = random.randint(1,10)

indovinato = False

while indovinato != True:
    guess = input("indovina il numero ")
    if int(guess) == number:
        indovinato = True
        print("bravoooo!!!")
    else:
        print("sbagliato")
    
"""
number = 7
for x in range(0,number+1):
    print(x)