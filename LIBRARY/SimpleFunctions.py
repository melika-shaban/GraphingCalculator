######MARYAM
import math
import cmath
###Quadrtic Caluclator




def Quadratic_Formula_Calculator(a,b,c):#purpose is to find the 2 roots of a parabala
  value_squared = (b**2) - (4*a*c) #the value that will be rooted in the quadratic formula
#there will be a positive solution and negtive solution, so the formula is used twice using addtion and subtration to output 2 answers
  try: #This will try doing it usign normal math
    first_solution = (-b-math.sqrt(value_squared)) / (2*a)
    second_solution = (-b+math.sqrt(value_squared)) / (2*a)
    #print("The two answers are {0} and {1}".format(first_solution, second_solution))#prints the 2 answers, using format() to insert the first_solution({0}) and the second_solution ({1}) into the string
    coor = (first_solution, second_solution)
    return coor

  except:#it will go here if the answer is a complex number
    # print("You have entered an imaginary root(s)")
    return "You have entered an imaginary root(s)"#It will return this statement if the roots are imaginary


Quadratic_Formula_Calculator(2, 5, -7)

###############################################################################################
#MARYAM
#Random DataSet Generator
import random


def Rand_Data_Set(Amount_of_Numbers, Higest_Number, Lowest_Number):#purpose is to compose a random list of numbers based on the user's parameters
  List = [] #creates an empty list
  number = 0
  while number < Amount_of_Numbers: #as long at the counter is less than the amount of numbers the user wants
   X = random.randint(Lowest_Number, Higest_Number)#finds a random number for the user in the range they want
   List.append(X)#appends the random number
   number += 1#Adds to counter
  print(List)
  return List



###############################################################################################GCF

##ELLLIEE
def Factors(N): #takes the factors of number 'N' and puts them into a list
  Factors_List=[] #creates an empty list to add the factors to 
  N=int(N) #turns N into an integer just in case
  for i in range(1, (N+1)): #N+1 because the range isn't inclusive of the last number and every number is divisible by itself 
    D=i
    remainder=(N%D) 
    if remainder==0: #if there is no remainder then the number is a factor
      Factors_List.append(D)
  return(Factors_List)

def Common_Factors(N1, N2): #finds common factors between 2 numbers and puts them in a list
  N1=int(N1) # making the numbers integers just in case
  N2=int(N2)
  common_factors=[] #creates an empty list to add the common factors to 
  first=Factors(N1) 
  second=Factors(N2)
  for i in first: #for every number in the list of factors of the first number...
    for j in second: #and for every number in the list of factors of the second number...
      if i==j: #...if those two are equal add them to the list of common factors
        common_factors.append(i)
  return(common_factors)

def GCF(N1, N2): #prints the greatest common factor between 2 numbers
  CF=Common_Factors(N1, N2)
  CF.reverse() #since common factors are automatically in order, reverse them
  
  return(CF[0])
  #print(CF[0])


# tests
GCF(6, 3)

###############################################################################################
#Maryam
#Dice Roller

import tkinter as tk
import random

def image():#function updates image
      roll = random.randint(1, 6) #gets a random number

      #Unicade charters representing dice faces  
      dice_image = {
        1: '⚀', #The unicode images for the dice faces
        2: '⚁',
        3: '⚂',
        4: '⚃',
        5: '⚄',
        6: '⚅'
      }
      label.config(text=dice_image[roll])#updaes label to show the dice face/number

def dice():
  root = tk.Tk()#makes the window
  root.title("Dice Roller")#gives the window a title

  dice = tk.Frame(root)#makes frame to hold the dice label
  dice.pack(padx=20, pady=20)

  global label#makes label a global variable
  label = tk.Label(dice, font=("Arial", 100))#label for dice face
  label.pack()#packs label into frame

  button = tk.Button(root, text="ROLL", command = image)#makes button that is clicked when the user wants to roll the dice
  button.pack(pady = 10)
  root.mainloop()#starts the main loop

#makes sure it is not being important as a moduole and used
if __name__ == "__main__":
  dice()#calls main function to start application

##############################################################################################
#MARYAM
#Coin Flipper

import tkinter as tk
import random

def image2():#function updates image
      flip = random.randint(1, 2) #gets a random number

      #Unicode charters representing dice faces 
      coin_image = {
        1: '⊕', #The unicode images for the dice faces
        2: '⊖'

      }
      label.config(text=coin_image[flip])#updaes label to show the coin face

def coin():
  root = tk.Tk()#makes the window
  root.title("Coin Flipper")#gives the window a title

  coin = tk.Frame(root)#makes frame to hold the coin label
  coin.pack(padx=20, pady=20)

  global label#makes label a global variable
  label = tk.Label(coin, font=("Arial", 100))#label for coin face
  label.pack()#packs label into frame

  button = tk.Button(root, text="FLIP", command = image2)#makes button that is clicked when the user wants to flip the coin
  button.pack(pady = 10)
  root.mainloop()#starts the main loop

#makes sure it is not being important as a moduole and used
if __name__ == "__main__":
  coin()#calls main function to start application

##############################################################################################

#MARYAMM 
#Lowest Common Multiple Finder



# def GCF(Num1, Num2):#Using previously created function
#   while Num2:
#     #finds remainder od Number divided by Num2
#     #and then assigns Num1 the last value Num2 held
#     Num1, Num2 = Num2, Num1 % Num2
#   return Num1

def LCM(a, b):# purpose is to find the lowest common multiple of to integers
  return (a * b) // GCF(a, b)#the formula for finding the GCM
  print((a * b) // GCF(a, b))
  #it is calculated usign the relasionship between the LCM and GCF

LCM(5, 10)


############################################################################################

#MARYAM
#The y -coorcinate of the Y-Intercept Finder
#Note, the X-coordinate will alays be 0

def y(x, y, m):#purpose is to find the x-coordinate fo the y-int

  num = y - m * x
  #print("the y-ccordinate of the y-int is num")
  return num#solves for b using the linear eqations
  print(num)
y(4, 3, 5)
############################################################################################


