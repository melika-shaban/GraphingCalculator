import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import random

# from __init__ import * 
from LIBRARY.SimpleFunctions import *
from LIBRARY.Polygons import *

import LIBRARY

############################

import math

#ALL EXAMPLES/TESTING CAN BE FOUND NEAR THE BOTTOM OF THIS FILE FOR THE FUNCTIONS ON THIS FILE

########################################################################################################################################################PRIMARY WINDOW #####################################################################################

#This first section is like the home page and is how the user selects the feature they wish

#primary_window is a function that remakes the entire home window everytime it is called, which includes the buttons that allow the user to use the graphing calculator, polygon function, lcm, and gcf function, random data set and quadratic calculator root finder. It is helpful because instead of having everything on the same window and having to keep deleting and brinning back buttons, everything re-appears everytime this function is called. It takes no parameters.
#The function takes no parameters, and it essentially outputs in tkinter window with a label and buttons

#EXAMPLE: If you this function were called and you clicked any button, it would take you to the respective window. For instance, selecting polygons would call the appropriate functoin and display all the polygon buttons
def primary_window():
  global window  #globalizing the window variable so it can be destroyed later
  
  window = Tk()  #creates window by creating an object in the Tk() class and assigning it to the variable window

  window.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  window.title("math") #using the built in title method on the window to change it's title to math

  window['bg'] = "pink" #making the window pink

  #below i create the first label by creating a label object in the Label class. In the parameters I specify which window it's going in, the text it should display, the font, colour. Then, essentially I use the pack and place methods which allows the label to be seen on the screen. In the place parameters I also specify where the label belongs on the x and y axis and it's anchor. 
  label1 = Label(window, text = "Select the mode", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #below I create all the buttons I need for this first window. The steps are pretty much the exact same as the label steps, and it's also essentially the same for most things placed on windows (checkbox, text, button, etc). For every button, I  first create an object in the button class and assign it to a variable. I specify the window, text, and colours in the parameters. The most important parameter is arguably the command one though, which allows the button to actually do something and calls another function. Then I pack and place them in the appropriate spot, specify the anchor, and this time I also give a width size so they look uniform. 

  #button 1
  first_button = Button(window, text = "Graphing calculator", bg = "pink", command = quadratic_calculator)
  first_button.pack()
  first_button.place(x = 100, y = 100, anchor = "center", width = 200)
  
  #button 2
  second_button = Button(window, text = "Polygons", bg = "pink", command = polygon_option_page)
  second_button.pack()
  second_button.place(x = 300, y = 100, anchor = "center", width = 200)

  #button 3
  third_button = Button(window, text = "LCM & GCF", bg = "pink", command = LCM_GCF_window)
  third_button.pack()
  third_button.place(x = 100, y = 150, anchor = "center", width = 200)

  #button 4
  fourth_button = Button(window, text = "Random data set", bg = "pink", command = random_data_set)
  fourth_button.pack()
  fourth_button.place(x = 300, y = 150, anchor = "center", width = 200)

  #button 5
  sixth_button = Button(window, text = "Quadratic calculator", bg = "pink", command = actual_quadratic_calculator)
  sixth_button.pack()
  sixth_button.place(x = 100, y = 200, anchor = "center", width = 200)

  #button 7
  eigth_button = Button(window, text = "Simulations", bg = "pink", command = simulations)
  eigth_button.pack()
  eigth_button.place(x = 300, y = 200, anchor = "center", width = 200)
  
  #Lastly, I also call the mainloop function so that the window keeps showing up. 
  mainloop()

#back_to_home_page is a function that essentially take the user back to the homepage, or in other words makes it appear again so they can select from the options. It does so by getting rid of some other windows with the destroy method and it also calls the primary window function to make the window show up again. For the majority of back buttons in this project, this function is the command for it (since it goes "back" (or recreates) the home page)
#Takes no parameters, output is basically the home page again

#EXAMPLE: If this button were to be called during any other window of this program, the home page would re apear. For instance, if I were to be on the polygons page, the main page with the options of the app (graphing calculator, polygons, random data set, etc) would re apear. 
def back_to_home_page(): 
  window.destroy() #I first detroy the main window using the destroy method
  primary_window() #Then I make the primary window again using the function I made that creates the primary window (function called primary_window)
  quads.destroy() #then I attempt to destroy the other window made, which is called quads, using the destroy method



################################################################################################################################################################################################
################################################################################################################################################################################################
################################################################################################################################################################################################
################### GRAPHING CALCULATOR BEGINS (Melika) ###################
################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################

#the graphing calculator allows the user to select the kind of graph theyre making and then enter their inputs, and then the program will graph it 


########################################################################################################################################################Quadratic Calculator #####################################################################################
  
  
#quadratic_calculator creates the window needed when the user selects the graphing calculator, where they can pick between the given options which leads the user to another window.  It creates a label, all the button options (polynomial, trigonometric, logarithmic) and also the back button. The user is then taken to the next window to input info based on which button they selected and the command it has.
#Once again the function takes no parameters, but it outputs the window described (buttons to select next window)

#EXAMPLE: Anytime this function is called the graphing calculator page with the different catagories (polynomial, trig, log) would re apear. Depending on the bottom selected, another window will appear. For instance, selecting polynomial will call another function and make the polynomial window visible with the polynommial options.

def quadratic_calculator():
  
  global quads #globalizing the window variable so it can be destroyed later
  
  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Quadratic Calculator") #using the built in title method on the window to change it's title

  quads['bg'] = "pink" #making the window pink

  #making the primary label that tells the user to select the mode. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Select the mode", font = ("Helvetica", "24"), bg = "pink") 
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #below I create all the buttons I need for this  window. Again, it's pretty much the exact same steps as everytime else. For every button, I  first create an object in the button class and assign it to a variable. I specify the window, text, and colours in the parameters. I also speicfy the command in the parameters, which allows the button to actually do something and calls another function. Then I pack and place them in the appropraite spot, specify the anchor, and specify width.

  #polynomial button (first button). This button calls the polynomial function (created later) so that the user can select between the options
  polynomial_button = Button(quads, text = "Polynomial Function", bg = "pink", command = polynomial_function)
  polynomial_button.pack()
  polynomial_button.place(x = 200, y = 100, anchor = "center", width = 200)

  #trigonometric button (second button). This button calls the function that shows the trigonometric options
  trigonometric_button = Button(quads, text = "Trigonometric Function", bg = "pink", command = trigonometric_function)
  trigonometric_button.pack()
  trigonometric_button.place(x = 200, y = 150, anchor = "center", width = 200)

  #logarithmic button (third button). This button calls the function that shows the logarithmic options
  logarithmic_button = Button(quads, text = "Logarithmic Function", bg = "pink", command= logarithmic_function)
  logarithmic_button.pack()
  logarithmic_button.place(x = 200, y = 200, anchor = "center", width = 200)

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page)
  back_button_one.pack()
  back_button_one.place(x = 200, y = 250, anchor = "center", width = 200)

########################################################################################################################################################Polynomial function #####################################################################################

#polynomial function is a function that creates the window needed when the user selects the polynomial option in the graphing calculator. In summary, what it does is create all the polynomial options (quadratic, cubic, quartic) and also the back button, that the user can select to input their info for those topics
#Once again takes no inputs, and the output is a window with the quadratic, cubic, quartic and back button, and also a label

#EXAMPLE: Anytime this function is called the output will switch to show this window and its options. Depending on the button selected, another function will be called. For example, selecting quadratic would bring the quadratic window that allows the user to enter their info

def polynomial_function():
  global quads #globalizing the window variable so it can be destroyed later
  
  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Polynomial Function") #using the built in title method on the window to change it's title

  quads['bg'] = "pink" #making the window pink

  #making the priamary label that tells the user to select the mode. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Select the mode", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #below I create all the buttons I need for this  window. Again, it's pretty much the exact same steps as everytime else. For every button, I  first create an object in the button class and assign it to a variable. I specify the window, text, and colours in the parameters. I also speicfy the command in the parameters, which allows the button to actually do something and calls another function. Then I pack and place them in the appropraite spot, specify the anchor, and specify width.

  #first button: quadratic_button, calls the quadratic function (created later on) so that the user can enter their input and the program will graph it
  quadratic_button = Button(quads, text = "Quadratic", bg = "pink", command= quadratic_function)
  quadratic_button.pack()
  quadratic_button.place(x = 200, y = 100, anchor = "center", width = 200)

  #second button: cubic_button, calls the cubic function (created later on) so that the user can enter their input and the program will graph it
  cubic_button = Button(quads, text = "Cubic", bg = "pink", command = cubic_function)
  cubic_button.pack()
  cubic_button.place(x = 200, y = 150, anchor = "center", width = 200)

  #third button: quartic_button, calls the quartic function (created later on) so that the user can enter their input and the program will graph it
  quartic_button = Button(quads, text = "Quartic", bg = "pink", command = quartic_function)
  quartic_button.pack()
  quartic_button.place(x = 200, y = 200, anchor = "center", width = 200)

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page)
  back_button_one.pack()
  back_button_one.place(x = 200, y = 250, anchor = "center", width = 200)

######################################################################################################################################################################################################################################################THE FOLLOWING CODE BELONGS TO JUSTIN####################################
###########################################################################################################################################################################################################################################################################################################################

#############################QUADRATIC FUNCTION##########################

import matplotlib.pyplot as plt
import numpy as np


def quadgraph(a,b,c): #quadratic function graph
  x = np.arange(-10, 10,0.1) #creates a evenly-spaced grid starting at 0 and ending at 10
  y = a*(x**2) + b*x + c #equation for a parabola. For every x point, apply these transformations to x in order to get y
  fig, ax = plt.subplots(figsize=(5, 5), constrained_layout=True) 
  #creates a figure with dimensions 5x5 inches. The constrained layout adjusts the subplot to the figure dimensions.
  ax.plot(x,y, color='pink')
  #Creates the lines on the axes. Sets the colour of the figure to pink
  ax.set_ylim(-10,10) #Constrains the y axis from -10,10
  ax.set_xlim(-10,10) #Same as above for x axis
  plt.grid() #Creates a grid on the graph
  plt.show(block=False) #Display the braph. "block=False" allows code following the function to run

def cubicgraph(a,b,c,d): #cubic graph function
  x = np.arange(-10, 10,0.1)
  #equation for a cubic. For every x point, apply these transformations to x in order to get y
  y = a*(x**3) + b*(x**2) + c*x + d
  fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
  ax.plot(x,y, color='pink')
  ax.set_ylim(-10,10)
  ax.set_xlim(-10,10)
  plt.grid()
  plt.show(block=False)


def quarticgraph(a,b,c,d,e): #quartic graph function
  x = np.arange(-10, 10,0.1) 
  y = a*(x**4) + b*(x**3) + c*(x**2) + d*x + e
  #equation for a cubic. For every x point, apply these transformations to x in order to get y
  fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
  ax.plot(x,y, color='pink')
  ax.set_ylim(-10,10)
  ax.set_xlim(-10,10)
  plt.grid()
  plt.show(block=False)


def singraph(a,k,p,q): #sin function graph where p is in degrees
  x = np.arange(-10,10*np.pi,0.1) #generates grid from 0 to 10*pi with step 0.1. We use pi because the sin function is graphed in radians. We use 10*pi to get a sufficient amount of cycles before the function stops.
  p = np.radians(p) #convert p to radians
  y = a*np.sin(k*(x-p))+q #formula for sin function using radians
  fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
  ax.plot(x,y, color='pink')
  ax.set_ylim(-10,10)
  ax.set_xlim(-2*np.pi, 2*np.pi)
  plt.grid()
  plt.show(block=False)


def cosgraph(a,k,p,q): #sin function graph where p is in degrees
  x = np.arange(-10,10*np.pi,0.1)
  p = np.radians(p)
  y = (a*np.cos(k*(x-p))+q) #equation for cosine function
  fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
  ax.plot(x,y, color='pink')
  ax.set_ylim(-10,10)
  ax.set_xlim(-2*np.pi, 2*np.pi)
  plt.grid()
  plt.show(block=False)


def tangraph(a,k,p,q): #sin function graph where p is in degrees
  x = np.arange(-10,10*np.pi,0.1)
  p = np.radians(p)
  y = (a*np.tan(k*(x-p))+q) #equation for tan function
  fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
  ax.plot(x,y, color='pink')
  ax.set_ylim(0,10)
  ax.set_xlim(-2*np.pi, 2*np.pi)
  plt.grid()
  plt.show(block=False)


def loggraph(a,b,h,k): #log function graph
  x = np.arange(-10, 10, 0.1)
  y = a*(np.log(x+h) / np.log(b)) + k 
  #equation for log graph. We use change of base formula to get log with a variable base
  fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
  ax.plot(x,y, color='pink')
  ax.set_ylim(-10,10)
  ax.set_xlim(-10,10)
  plt.grid()
  plt.show(block=False)

##################################END OF JUSTIN'S GRAPHING FUNCTIONS###################

######################################################################################################################################################################################################################################################THE FOLLOWING CODE BELONGS TO MELIKA####################################
###########################################################################################################################################################################################################################################################################################################################

########################################################################################################################################################Quadratic Function #####################################################################################

#quadratic_function is a function that creates the window needed when the user selects the quadratic option in the graphing calculator. The ultimate purpose is to obtain the information (variable values) needed from the user to actually do this type of graph. This function has nothing to do with actually making the graph; it is solely for obtaining info. It creates the textboxes for the user to enter their info, as well as the labels specifying the different values, the enter button which calls another function that actually does the graphing, and a back button that takes the user bake to the home page (or in other words makes it reapear)
#Again, it takes no parameters and has no inputs, and the output is the window where the user inputs their info for the graph

#EXAMPLE: Anytime this function is called the quadratc info entering page with the textboxes will apear. If the user were to input 3, 4 and 5, the function would call on Justin's function to create the matplotlib window of a quadratic graph with those values.

def quadratic_function():
  global quads, a_textbox, b_textbox, c_textbox #I globalize the window as well as the textboxes variable so that I can use the other methods on them in a later function (such as the get method with the textboxes)
  
  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Quadratic Function") #using the built in title method on the window to change it's title

  quads['bg'] = "pink" #making the window pink

  #below i make the primary label that tells the user to enter the values. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen. You may notice that a lot of things in this file are named the exact same thing, such as the way the majority of textboxes are stored in the variable label2. The reason being is that after they are placed on the screen they aren't needed for anythin so this way I could reuse code more. HOWEVER, most title labels have a special variable of label1, because if the error inputs inproper info later I change the title name so it has its own special name so i don't replace another label.
  label1 = Label(quads, text = "Enter the values", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #i start off by making my three labels "a value", "b value", and "c value". I create objects of the label class, assign them to variables, and in the parameters I specify the window (quads), text, font and colour. Then I pack and place them where I wish by specifying the x and y numbers and the anchor. 

  #A value label
  label2 = Label(quads, text = "A Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 100, anchor = "center")

  #B value label, underneath a value label
  label2 = Label(quads, text = "B Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 150, anchor = "center")

  #C value label, underneath b value label
  label2 = Label(quads, text = "C Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 200, anchor = "center")

   #i then make my three textboxes beside the three labels (a value, b value and c value). I create objects of the Entry class (which is a textbox, assign them to variables, and in the parameters I specify the window (quads). Then I pack and place them where I wish by specifying the x and y numbers and the anchor. 

  #first textbox for the a value
  a_textbox = Entry(quads)
  a_textbox.place()
  a_textbox.place(x=250, y = 100, anchor = "center")

  #second textbox for the b value
  b_textbox = Entry(quads)
  b_textbox.place()
  b_textbox.place(x=250, y = 150, anchor = "center")

  #third textbox for the c value
  c_textbox = Entry(quads)
  c_textbox.place()
  c_textbox.place(x=250, y = 200, anchor = "center")

  #i make the enter button below. It is essential because its how the user is able to let the program know that the user has entered their info into the textboxes, then it runs another function that which essentially  ends up graphing everything by callling on the quadratic_entry_button when clicked (created and explained later on).
  enter_button = Button(quads, text = "Enter", bg = "pink", command = quadratic_entry_button) #making an object of the Button class  and assiging it to the variable enter_button. In the parameters I specify the window, text,  colour and command.
  enter_button.place()
  enter_button.place(x = 200, y = 235, anchor = "center") #i use the place and pack methods and in the place parameters I specify when the button should go with x and y and the anchor

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again when clicked
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page, width = 65)
  back_button_one.pack()
  back_button_one.place(x = 200, y = 275, anchor = "center", width = 65)

########################################################################################################################################################Collecting Info #####################################################################################

#collcting_info is a function that is different from most of the other functions in this program. It is essential when trying to graph the input of the user for the quadratic function because the users input starts off as a string, so by turning it to a float it can be used later. It's also crucial because if its unable to turn the input to a float, it means the user entered incorrect info therefore it'll display the appropriate error message. To sum things off, it obtains the text typed into textboxes made in previous functiono, and stores them in variables and turns them to a float. This function is only used when there are THREE TEXTBOXES.  
#EXAMPLE: If the first textbox has 5, the second had 8, and the third has 9, after this function is called the three values would be stored as floats in the variables a, b and c. Let's say the first textbox had the string "sweet_apples" though, then the error statement would appear on the window instead

def collecting_info():
  global a, b, c #globalizing a, b, and c variables that stores the input of the textboxes

  #For all the variables with textboxes I previusly made (and globalized), I use the get method with the entry objects, and store the value in variables a, b and c
  a = a_textbox.get() #textbox a value stored in variable a
  b = b_textbox.get() #textbox b value stored in variable b
  c = c_textbox.get() #textbox c value stored in variable c

  #Because we can't gaurantee the user to  enter  a  numeric  value, instead of simply turning all the textbox value to a float/integer, I  put  it  all in a try and except  so that if they are not numeric values, it doesn't stop the entire program. It trys to turn a, b and c to a float, but if it doesn't work it changes the main, big label to tell the user to try again. 
  try: 
    a = float(a) #replacing the value of variable a to a float
    b = float(b) #replacing the value of variable b to a float
    c = float(c) #replacing the value of variable c to a float
  except: #except block, so  if an error occured this block of code will run instead
    #I make a label in the variable label1, and this time it displays the error message at the top of the screen
    label1 = Label(quads, text = "Please try again with appropriate values", font =   ("Helvetica", "15"), bg = "pink")   #new label object in variable label1
    label1.pack()
    label1.place(x = 200, y = 50, anchor = "center") #pack and place it to where I wish on the screen

########################################################################################################################################################Close back button function #####################################################################################

#close_back_button is a function that closes the matplotlib window and destroys the back button, so that the user can see the windows underneath again. It has no parameters/inputs, and all it does is close already created stuff

#EXAMPLE: Whenever there is a matplotlib graph open with a back button, this function should make them dissapear. For instance, if the quadratic graph is open and the user clicked the back button who's command is this function, the graph and button would dissapear and we would once again see the previous window 

def close_back_button():
  plt.close() #closes matplotlib window (uses close method)
  bob.destroy() #gets rid of the back button so it doesn't cover the window (uses destroy method)

########################################################################################################################################################Quadratic Entry Button #####################################################################################

 #quadratic_entry_button is the function that actually graphs the users. It works by first using the collecting_info() function to turn the users input to numerical values and checks for errorss. Then, it uses Justin's quadragraph function. Afterwards, it also makes the window and button neccessary for the back button by creating a new window. The back button takes the user back to the quadratic textbox page.
#Once again, it takes no inputs and the output is the matplotlib window with the graph and also a tiny back button

#EXAMPLE: This function will always use the collecting info to turn the values to floats, use Justin's functions to generate the matplotlib graph and create the back button. If somebody has inputted 1, 2 and 4, this function essentially turns the stings to floats, makes the quadratic graph and creates the back button. When the back button it clicked the previous window is shown again.

def quadratic_entry_button(): 
  global bob #making the window of the button global so we can delete it later
  
  collecting_info() #Calling the collecting info function so that the users input in the textboxes is actually stored to proper variables to be used

  quadgraph(a, b, c) #calling  the quadgraph function that Justin made and suppplying the users input (a, b and c) in the parameters so that it graphs the values
  
  bob = Tk() #making a new Tk class object and storing in the variable bob
  bob.geometry("60x570") #changing the dimensions of bob so that it's a thin window and doesn't take up extra space, but is very tall so we can see it underneath the matplotlib window
  back_button_one = Button(bob, text = "Back", bg = "pink", width = 60, command = close_back_button)

  back_button_one.pack()
  back_button_one.place(x = 30, y = 555, anchor = "center", width = 60, height = 30) #packing and placing the button on the desired spot on the window (the width of the button is the same as the window and it is placed very low on the y axis so that it pokes out underneath the matplotlib window)

### THE REMAINING FUNCTIONS DO NOT HAVE EXAMPLES BECAUSE THEY PRETTY MUCH DO THE EXACT SAME THING
## EX. polynomial, trigonometric both lead to other pages full of options depending on the button clicked, cubic, quartic, sin, cos tan and log will all take the user to window to input info, the collecting functions all turn the values to floats and the entry functions actually make the graph and back button
########################################################################################################################################################Cubic Function
#####################################################################################

#cubic_function is a function that makes the window needed when the user selects the cubic option in the graphing calculator. The ultimate purpose is to obtain the information (variable values) needed from the user to actually do this type of graph. This function has nothing to do with actually making the graph; it is solely for obtaining info. It creates the textboxes for the user to enter their info, as well as the labels specifying the different values and the enter button, the enter button which calls another function that actually does the graphing, and a back button that takes the user bake to the home page (or in other words makes it reapear)

#Again, it takes no parameters and has no inputs, and the output is the window where the user inputs their info for the graph

def cubic_function():
  global quads, a_textbox, b_textbox, c_textbox, d_textbox, enter_button #I globalize the window as well as the textboxes variable so that I can use the get method on them in a later function 
  
  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Cubic Function") #using the built in title method on the window to change it's title 

  quads['bg'] = "pink" #making the window pink

  #below  i make the primary label that tells the user to enter the values. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Enter the values", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #i start off by making my four labels "a value", "b value", "c value"  and "d value". I create objects of the label class, assign them to variables, and in the parameters I specify the window (quads), text, font and colour. Then I pack and place them where I wish by specifying the x and y numbers and the anchor.

  #A value label
  label2 = Label(quads, text = "A Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 100, anchor = "center")

  #B value label
  label2 = Label(quads, text = "B Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 150, anchor = "center")

  #C value label
  label2 = Label(quads, text = "C Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 200, anchor = "center")

  #D value label
  label2 = Label(quads, text = "D Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 250, anchor = "center")

  #i then make my four textboxes beside the four labels (a value, b value, c value and d value). I create objects of the Entry class (which is a textbox, assign them to variables, and in the parameters I specify the window (quads). Then I pack and place them where I wish by specifying the x and y numbers and the anchor. 

  #first textbox for the a value
  a_textbox = Entry(quads)
  a_textbox.place()
  a_textbox.place(x=250, y = 100, anchor = "center")

  #second textbox for the b value
  b_textbox = Entry(quads)
  b_textbox.place()
  b_textbox.place(x=250, y = 150, anchor = "center")

  #third textbox for the c value
  c_textbox = Entry(quads)
  c_textbox.place()
  c_textbox.place(x=250, y = 200, anchor = "center")

  #fourth textbox for the d value
  d_textbox = Entry(quads)
  d_textbox.place()
  d_textbox.place(x=250, y = 250, anchor = "center")
  
  #i make the enter button below which essentially  graphs everything by callling on the quadratic_entry_button when clicked (created and explained later on)
  enter_button = Button(quads, text = "Enter", bg = "pink", command = cubic_entry_button) #making an object of the Button class  and assiging it to the variable enter_button. In the parameters I specify the window, text,  colour and command.
  enter_button.place()
  enter_button.place(x = 150, y = 280, anchor = "center") #i use the place and pack methods and in the place parameters I specify when the b

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again when clicked
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page, width = 65)
  back_button_one.pack()
  back_button_one.place(x = 250, y = 280, anchor = "center", width = 65)

########################################################################################################################################################Once again collecting info function #####################################################################################

#once_again_collcting_info is a function that obtains the text typed into textboxes made in previous function(cubic_function), and stores them in variables and turns them to a float, and uses a try and except to catch any errors. This function is used with FOUR textboxes
def once_again_collecting_info():
  global a, b, c, d #globalizing a, b, c and d variables that stores the input of the textboxes
  
  #For all the variables with textboxes I previusly made (and globalized), I use the get method with the entry objects, and store the value in variables a, b, c and d
  a = a_textbox.get() #textbox a value stored in variable a
  b = b_textbox.get() #textbox b value stored in variable b
  c = c_textbox.get() #textbox c value stored in variable c
  d = d_textbox.get() #textbox d value stored in variable d
  
  #Because we can't gaurantee the user to  enter  a  numeric  value, instead of simply turning all the textbox value to a float/integer, I  put  it  all in a try and except  so that if they are not numeric values, it doesn't stop the entire program. It trys to turn a, b,c and d to a float, but if it doesn't work it changes the main, big label to tell the user to try again. 
  try:
    a = float(a) #replacing the value of variable a to a float
    b = float(b) #replacing the value of variable b to a float
    c = float(c) #replacing the value of variable c to a float
    d = float(d) #replacing the value of variable d to a float
  except: #except block, so  if an error occured this block of code will run instead
    #I make a new label in the variable label1, and this time it displays the error message at the top of the screen
    label1 = Label(quads, text = "Please try again with appropriate values", font =   ("Helvetica", "15"), bg = "pink") #new label object in variable label1
    label1.pack()
    label1.place(x = 200, y = 50, anchor = "center")  #pack and place it to where I wish on the screen

######################################################################################################################################################## Cubic entry button
#####################################################################################

#cubic_entry_button is a function that actually graphs the users input by using Justin's cubigraph function, and makes the back button by creating a new window. It works by first using the past function to turn the users input to numerical values and checks for errors. Then it uses the cubic graphing function. Afterwards, it also makes the window and button neccessary for the back button by creating a new window. The back button takes the user back to the cubic entry page.
#Once again, it takes no inputs and the output is the matplotlib window with the graph and also a tiny back button

def cubic_entry_button():
  global bob #making the window of the button global so we can delete it later
  
  once_again_collecting_info() #Calling the once again collecting info function so that the users input in the textboxes is actually stored to proper variables to be used

  cubicgraph(a, b, c, d) #calling  the cubic graph function that Justin made and suppplying the users input (a, b, c and d) in the parameters so that it graphs the values

  bob = Tk() #making a new Tk class object and storing in the variable bob
  bob.geometry("60x570") #changing the dimensions of bob so that it's a thin window and doesn't take up extra space, but is very tall so we can see it underneath the matplotlib window
  back_button_one = Button(bob, text = "Back", bg = "pink", width = 60, command = close_back_button)

  back_button_one.pack()
  back_button_one.place(x = 30, y = 555, anchor = "center", width = 60, height = 30) #packing and placing the button on the desired spot on the window (the width of the button is the same as the window and it is placed very low on the y axis so that it pokes out underneath the matplotlib window)

######################################################################################################################################################## Quartic Function #####################################################################################

  
#quartic_function creates the window needed when the user selects the quartic option in the graphing calculator. It creates the textboxes for the user to enter their info, as well as the labels specifying the different values and the enter button. This is very similar to the quadratic function and cubic one, with the some differences being how there's an extra label and textbox for the extra variable.
def quartic_function():
  global quads, label1, label2, a_textbox, b_textbox, c_textbox, d_textbox, e_textbox, enter_button
  quads = Tk()

  quads.geometry("400x300")

  quads.title("Quadratic Function")

  quads['bg'] = "pink"

  #labels
  
  label1 = Label(quads, text = "Enter the values", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 25, anchor = "center")

  label2 = Label(quads, text = "A Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 75, anchor = "center")

  label2 = Label(quads, text = "B Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 115, anchor = "center")

  label2 = Label(quads, text = "C Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 155, anchor = "center")

  label2 = Label(quads, text = "D Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 195, anchor = "center")

  label2 = Label(quads, text = "E Value", font = ("Helvetica", "15"), bg = "pink") #this is added so that there is an extra label the extra needed variable
  label2.pack()
  label2.place(x = 100, y = 235, anchor = "center")

  #textboxes
  
  a_textbox = Entry(quads)
  a_textbox.place()
  a_textbox.place(x= 250, y = 75, anchor = "center")

  b_textbox = Entry(quads)
  b_textbox.place()
  b_textbox.place(x=250, y = 115, anchor = "center")

  c_textbox = Entry(quads)
  c_textbox.place()
  c_textbox.place(x=250, y = 155, anchor = "center")

  d_textbox = Entry(quads)
  d_textbox.place()
  d_textbox.place(x=250, y = 195, anchor = "center")

  e_textbox = Entry(quads) #this is added so that there is an extra text box for the extra needed variable
  e_textbox.place()
  e_textbox.place(x=250, y = 235, anchor = "center")

  #back and enter button

  enter_button = Button(quads, text = "Enter", bg = "pink", command = quartic_entry_button)
  enter_button.place()
  enter_button.place(x = 150, y = 280, anchor = "center")

  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page, width = 65)

  back_button_one.pack()
  back_button_one.place(x = 250, y = 280, anchor = "center", width = 65)

######################################################################################################################################################## Collecting info for quartic function
#####################################################################################

#collcting_info is a function that works similarly to collecting_info and once_again_collecting_info. It obtains the text typed into textboxes made in previous function, and stores them in variables and turns them to a float. The reason this is different than the other functions is that it works with five textboxes. 
def collecting_info_for_quartic():
  global a, b, c, d, e 

  #putting value inputted in textboxes to variables
  a = a_textbox.get() 
  b = b_textbox.get() 
  c = c_textbox.get()
  d = d_textbox.get()
  e = e_textbox.get()
  try: 
    a = float(a) #trying to turn values to floats 
    b = float(b) 
    c = float(c) 
    d = float(d)
    e = float(e)
  except: #except just in case anything crashes
    label1 = Label(quads, text = "Please try again with appropriate values", font =   ("Helvetica", "15"), bg = "pink")   #new label object in variable label1
    label1.pack()
    label1.place(x = 200, y = 50, anchor = "center") #pack and place it to where I wish on the screen

######################################################################################################################################################## Quartic entry button function
#####################################################################################

#quartic_entry_button is a function that actually graphs the users input by using Justin's quarticgraph function, and makes the back button by creating a new window. It works by first using the past function to turn the users input to numerical values and checks for errors. Then it uses the quartic graphing function. Afterwards, it also makes the window and button neccessary for the back button by creating a new window. The back button takes the user back to the quartic entry page.
#Once again, it takes no inputs and the output is the matplotlib window with the graph and also a tiny back button
def quartic_entry_button():
  global bob
  collecting_info_for_quartic() #making input floats and checking errors with functions

  quarticgraph(a, b, c, d, e) #making graph

  bob = Tk() #making window and button below for back button
  bob.geometry("60x570")
  back_button_one = Button(bob, text = "Back", bg = "pink", width = 60, command = close_back_button)

  back_button_one.pack()
  back_button_one.place(x = 30, y = 555, anchor = "center", width = 60, height = 30)
  
######################################################################################################################################################## Trig function
#####################################################################################

  #trigonometric_function is a function that creates the window needed when the user selects the trig option in the graphing calculator. In summary, what it does is create all the trig options (sin, cos, tan) and also the back button, that the user can select to input their info for those topics
  #Once again takes no inputs, and the output is a window with the sin, cos, tan and back button, and also a label

def trigonometric_function():
  global quads #globalizing the window variable so it can be destroyed later

  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Trigonometric Function") #using the built in title method on the window to change it's title

  quads['bg'] = "pink" #making the window pink

  #making the priamary label that tells the user to select the mode. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Select the mode", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #below I create all the buttons I need for this  window. Again, it's pretty much the exact same steps as everytime else. For every button, I  first create an object in the button class and assign it to a variable. I specify the window, text, and colours in the parameters. I also speicfy the command in the parameters, which allows the button to actually do something and calls another function. Then I pack and place them in the appropraite spot, specify the anchor, and specify width.

  #first button: sin_button, calls the sin function (created later on) so that the user can enter their input (thats a different function though(sin_function))
  sin_button = Button(quads, text = "Sin", bg = "pink", command = sin_function)
  sin_button.pack()
  sin_button.place(x = 200, y = 100, anchor = "center", width = 200)

  #second button: Cos_button, calls the cos function (created later on) so that the user can enter their input (thats a different function though(cos_function))
  cos_button = Button(quads, text = "Cos", bg = "pink", command = cos_function)
  cos_button.pack()
  cos_button.place(x = 200, y = 150, anchor = "center", width = 200)

  #third button: tan_button, calls the tan function (created later on) so that the user can enter their input (thats a different function though(tan_function))
  tan_button = Button(quads, text = "Tan", bg = "pink", command = tan_function)
  tan_button.pack()
  tan_button.place(x = 200, y = 200, anchor = "center", width = 200)

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page)
  back_button_one.pack()
  back_button_one.place(x = 200, y = 250, anchor = "center", width = 200)

###############################################SIN FUNCTION
#####################################################################################################################################################################

#sin_function creates the window needed when the user selects the sin option in the graphing calculator. The ultimate purpose is to obtain the information (variable values) needed from the user to actually do this type of graph. This function has nothing to do with actually making the graph; it is solely for obtaining info. It creates the textboxes for the user to enter their info, as well as the labels specifying the different values, the enter button which calls another function that actually does the graphing, and a back button that takes the user back to the home page (or in other words makes it reapear)
#Again, it takes no parameters and has no inputs, and the output is the window where the user inputs their info for the graph
def sin_function():
  global quads, a_textbox, b_textbox, c_textbox, d_textbox #I globalize the window as well as the textboxes variable so that I can use the get method on them in a later function 

  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Sin Function") #using the built in title method on the window to change it's title

  quads['bg'] = "pink" #making the window pink

  #below i make the primary label that tells the user to enter the values. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Enter the values", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #i start off by making my 4 labels "a value", "k value", "p value"  and "q value". I create objects of the label class, assign them to variables, and in the parameters I specify the window (quads), text, font and colour. Then I pack and place them where I wish by specifying the x and y numbers and the anchor.

  #A value label
  label2 = Label(quads, text = "A Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 100, anchor = "center")

  #k value label
  label2 = Label(quads, text = "K Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 150, anchor = "center")

  #p value label
  label2 = Label(quads, text = "P Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 200, anchor = "center")

  #q value label
  label2 = Label(quads, text = "Q Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 250, anchor = "center")

  #I then make my four textboxes beside the four labels (a value, k value, p value and q value). I create objects of the Entry class (which is a textbox, assign them to variables, and in the parameters I specify the window (quads). Then I pack and place them where I wish by specifying the x and y numbers and the anchor. 

  #first textbox for the a value
  a_textbox = Entry(quads)
  a_textbox.place()
  a_textbox.place(x=250, y = 100, anchor = "center")

  #second textbox for the k value
  b_textbox = Entry(quads)
  b_textbox.place()
  b_textbox.place(x=250, y = 150, anchor = "center")

  #third textbox for the p value
  c_textbox = Entry(quads)
  c_textbox.place()
  c_textbox.place(x=250, y = 200, anchor = "center")

  #fourth textbox for the q value
  d_textbox = Entry(quads)
  d_textbox.place()
  d_textbox.place(x=250, y = 250, anchor = "center")

  #i make the enter button below which essentially  graphs everything by callling on the sin_entry_button when clicked (created and explained later on)
  enter_button = Button(quads, text = "Enter", bg = "pink", command = sin_entry_button) #making an object of the Button class  and assiging it to the variable enter_button. In the parameters I specify the window, text,  colour and command.
  enter_button.place()
  enter_button.place(x = 150, y = 280, anchor = "center") #i use the place and pack methods and in the place parameters I specify when the button should go with x and y and the anchor

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again when clicked
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page, width = 65)
  back_button_one.pack()
  back_button_one.place(x = 250, y = 280, anchor = "center", width = 65)

######################################################################################################################################################## sin entry button
#####################################################################################

 #sin_entry_button is a function that actually graphs the users input by using Justin's quadragraph function, and makes the back button by creating a new window. It works by first using the function that turns input to floats to turn the users input to numerical values and checks for errors. Then it uses the sin graphing function. Afterwards, it also makes the window and button neccessary for the back button by creating a new window. The back button takes the user back to the quartic entry page.
#Once again, it takes no inputs and the output is the matplotlib window with the graph and also a tiny back button

def sin_entry_button(): 
  global bob #making the window of the button global so we can delete it later

  once_again_collecting_info() #Calling the once again collecting info function so that the users input in the textboxes is actually stored to proper variables to be used

  singraph(a, b, c, d) #calling  the sin function that Justin made and suppplying the users input in the parameters so that it graphs the values

  bob = Tk() #making a new Tk class object and storing in the variable bob
  
  bob.geometry("60x570") #changing the dimensions of bob so that it's a thin window and doesn't take up extra space, but is very tall so we can see it underneath the matplotlib window
  
  back_button_one = Button(bob, text = "Back", bg = "pink", width = 60, command = close_back_button)

  back_button_one.pack()
  back_button_one.place(x = 30, y = 555, anchor = "center", width = 60, height = 30) #packing and placing the button on the desired spot on the window (the width of the button is the same as the window and it is placed very low on the y axis so that it pokes out underneath the matplotlib window)

####################################################################################################################################################### Cos Function
#####################################################################################


#cos_function creates the window needed when the user selects the cos option in the graphing calculator. The ultimate purpose is to obtain the information (variable values) needed from the user to actually do this type of graph. This function has nothing to do with actually making the graph; it is solely for obtaining info. It creates the textboxes for the user to enter their info, as well as the labels specifying the different values, the enter button which calls another function that actually does the graphing, and a back button that takes the user bake to the home page (or in other words makes it reapear)
#Again, it takes no parameters and has no inputs, and the output is the window where the user inputs their info for the graph

def cos_function():
  global quads, a_textbox, b_textbox, c_textbox, d_textbox, enter_button #I globalize the window as well as the textboxes variable so that I can use the get method on them in a later function 

  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Cos Function") #using the built in title method on the window to change it's title

  quads['bg'] = "pink" #making the window pink

  #below  i make the primary label that tells the user to enter the values. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Enter the values", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #i start off by making my 4 labels "a value", "k value", "p value"  and "q value". I create objects of the label class, assign them to variables, and in the parameters I specify the window (quads), text, font and colour. Then I pack and place them where I wish by specifying the x and y numbers and the anchor.

  #A value label
  label2 = Label(quads, text = "A Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 100, anchor = "center")

  #k value label
  label2 = Label(quads, text = "K Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 150, anchor = "center")

  #p value label
  label2 = Label(quads, text = "P Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 200, anchor = "center")

  #q value label
  label2 = Label(quads, text = "Q Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 250, anchor = "center")

  #I then make my four textboxes beside the four labels (a value, b value, c value and d value). I create objects of the Entry class (which is a textbox, assign them to variables, and in the parameters I specify the window (quads). Then I pack and place them where I wish by specifying the x and y numbers and the anchor. 

  #first textbox for the a value
  a_textbox = Entry(quads)
  a_textbox.place()
  a_textbox.place(x=250, y = 100, anchor = "center")

  #second textbox for the k value
  b_textbox = Entry(quads)
  b_textbox.place()
  b_textbox.place(x=250, y = 150, anchor = "center")

  #third textbox for the p value
  c_textbox = Entry(quads)
  c_textbox.place()
  c_textbox.place(x=250, y = 200, anchor = "center")

  #fourth textbox for the q value
  d_textbox = Entry(quads)
  d_textbox.place()
  d_textbox.place(x=250, y = 250, anchor = "center")

  #I make the enter button below which essentially  graphs everything by callling on the cos_entry_button when clicked (created and explained later on)
  enter_button = Button(quads, text = "Enter", bg = "pink", command = cos_entry_button) #making an object of the Button class  and assiging it to the variable enter_button. In the parameters I specify the window, text,  colour and command.
  enter_button.place()
  enter_button.place(x = 150, y = 280, anchor = "center") #i use the place and pack methods and in the place parameters I specify when the button should go with x and y and the anchor

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again when clicked
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page, width = 65)
  back_button_one.pack()
  back_button_one.place(x = 250, y = 280, anchor = "center", width = 65)

########################################################################################################################################################Cos entry button
#####################################################################################

#cos_entry_button is a function that actually graphs the users input by using Justin's cosgraph function, and makes the back button by creating a new window. The back button takes the user back to the cos textbox page. It works by firstly turning the users input to numerical values and checks for errors using other functions made. Then, it uses Justin's cosgraph function. Afterwards, it also makes the window and button neccessary for the back button by creating a new window. The back button takes the user back to the quadratic textbox page.
#Once again, it takes no inputs and the output is the matplotlib window with the graph and also a tiny back button.

def cos_entry_button():
  global bob #making the window of the button global so we can delete it later

  once_again_collecting_info() #Calling the once again collecting info function so that the users input in the textboxes is actually stored to proper variables to be used

  cosgraph(a, b, c, d) #calling  the quadgraph function that Justin made and suppplying the users input in the parameters so that it graphs the values

  bob = Tk() #making a new Tk class object and storing in the variable bob
  bob.geometry("60x570") #changing the dimensions of bob so that it's a thin window and doesn't take up extra space, but is very tall so we can see it underneath the matplotlib window
  back_button_one = Button(bob, text = "Back", bg = "pink", width = 60, command = close_back_button)

  back_button_one.pack()
  back_button_one.place(x = 30, y = 555, anchor = "center", width = 60, height = 30) #packing and placing the button on the desired spot on the window (the width of the button is the same as the window and it is placed very low on the y axis so that it pokes out underneath the matplotlib window)

##########################################################################################################
############################################TAN FUNTION
#######################################################################################################

#tan_function creates the window needed when the user selects the tan option in the graphing calculator. It creates the textboxes for the user to enter their info, as well as the labels specifying the different values and the enter button. It's pretty much the exact same thing as that past ones, except this time the enter button uses the tangraph function intead.

def tan_function():
  global quads, a_textbox, b_textbox, c_textbox, d_textbox, enter_button #I globalize the window as well as the textboxes variable so that I can use the get method on them in a later function 

  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Tan Function") #using the built in title method on the window to change it's title

  quads['bg'] = "pink" #making the window pink

  #below I make the primary label that tells the user to enter the values. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Enter the values", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #I start off by making my 4 labels "a value", "k value", "p value"  and "q value". I create objects of the label class, assign them to variables, and in the parameters I specify the window (quads), text, font and colour. Then I pack and place them where I wish by specifying the x and y numbers and the anchor.

  #A value label
  label2 = Label(quads, text = "A Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 100, anchor = "center")

  #k value label
  label2 = Label(quads, text = "K Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 150, anchor = "center")

  #p value label
  label2 = Label(quads, text = "P Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 200, anchor = "center")

  #q value label
  label2 = Label(quads, text = "Q Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 250, anchor = "center")

  #I then make my four textboxes beside the four labels (a value, b value, c value and d value). I create objects of the Entry class (which is a textbox, assign them to variables, and in the parameters I specify the window (quads). Then I pack and place them where I wish by specifying the x and y numbers and the anchor. 

  #first textbox for the a value
  a_textbox = Entry(quads)
  a_textbox.place()
  a_textbox.place(x=250, y = 100, anchor = "center")

  #second textbox for the k value
  b_textbox = Entry(quads)
  b_textbox.place()
  b_textbox.place(x=250, y = 150, anchor = "center")

  #third textbox for the p value
  c_textbox = Entry(quads)
  c_textbox.place()
  c_textbox.place(x=250, y = 200, anchor = "center")

  #fourth textbox for the q value
  d_textbox = Entry(quads)
  d_textbox.place()
  d_textbox.place(x=250, y = 250, anchor = "center")

  #I make the enter button below which essentially  graphs everything by callling on the quadratic_entry_button when clicked (created and explained later on)
  #this is the sole difference with some of the other functions; the enter button will use the input to call the tan_entry_button instead, which eventually graphs the inputs
  enter_button = Button(quads, text = "Enter", bg = "pink", command = tan_entry_button) #making an object of the Button class  and assiging it to the variable enter_button. In the parameters I specify the window, text,  colour and command.
  enter_button.place()
  enter_button.place(x = 150, y = 280, anchor = "center") #i use the place and pack methods and in the place parameters I specify when the button should go with x and y and the anchor

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again when clicked
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page, width = 65)
  back_button_one.pack()
  back_button_one.place(x = 250, y = 280, anchor = "center", width = 65)

####################################################################################################################################################################################################################
########################### Tan Entry Button
####################################################################################################################################################################################################################

#like the other entry buttons, tan_entry_button is a function that actually graphs the users input by using Justin's tan function, and makes the back button by creating a new window. The back button takes the user back to the tan textbox page.
#takes no inputs, output is basically the matplotlib window and a mini back button
def tan_entry_button():
  global bob #making the window of the button global so we can delete it later

  once_again_collecting_info() #Calling the once again collecting info function so that the users input in the textboxes is actually stored to proper variables to be used

  tangraph(a, b, c, d) #calling  the quadgraph function that Justin made and suppplying the users input in the parameters so that it graphs the values

  bob = Tk() #making a new Tk class object and storing in the variable bob
  bob.geometry("60x570") #changing the dimensions of bob so that it's a thin window and doesn't take up extra space, but is very tall so we can see it underneath the matplotlib window
  back_button_one = Button(bob, text = "Back", bg = "pink", width = 60, command = close_back_button)

  back_button_one.pack()
  back_button_one.place(x = 30, y = 555, anchor = "center", width = 60, height = 30) #packing and placing the button on the desired spot on the window (the width of the button is the same as the window and it is placed very low on the y axis so that it pokes out underneath the matplotlib window)

###############################################################################################################################################LOGARITHMIC FUNCTION THING
##############################################################################################

  
#logarithmic_function creates the window needed when the user selects the logarithmic option in the graphing calculator. It creates the textboxes for the user to enter their info, as well as the labels specifying the different values and the enter button. It doesn't actually graph anything; its purpose is to obtain info from user
def logarithmic_function():
  global quads, a_textbox, b_textbox, c_textbox, d_textbox, enter_button #I globalize the window as well as the textboxes variable so that I can use the get method on them in a later function 

  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Logarithmic Function") #using the built in title method on the window to change it's title 

  quads['bg'] = "pink" #making the window pink

  #below  i make the primary label that tells the user to enter the values. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Enter the values", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #i start off by making my 4 labels "a value", "b value", "h value"  and "k value". I create objects of the label class, assign them to variables, and in the parameters I specify the window (quads), text, font and colour. Then I pack and place them where I wish by specifying the x and y numbers and the anchor.

  #A value label
  label2 = Label(quads, text = "A Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 100, anchor = "center")

  #b value label
  label2 = Label(quads, text = "B Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 150, anchor = "center")

  #h value label
  label2 = Label(quads, text = "H Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 200, anchor = "center")

  #k value label
  label2 = Label(quads, text = "K Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 250, anchor = "center")

  #i then make my four textboxes beside the four labels (a value, b value, c value and d value). I create objects of the Entry class (which is a textbox, assign them to variables, and in the parameters I specify the window (quads). Then I pack and place them where I wish by specifying the x and y numbers and the anchor. 

  #first textbox for the a value
  a_textbox = Entry(quads)
  a_textbox.place()
  a_textbox.place(x=250, y = 100, anchor = "center")

  #second textbox for the B value
  b_textbox = Entry(quads)
  b_textbox.place()
  b_textbox.place(x=250, y = 150, anchor = "center")

  #third textbox for the H value
  c_textbox = Entry(quads)
  c_textbox.place()
  c_textbox.place(x=250, y = 200, anchor = "center")

  #fourth textbox for the K value
  d_textbox = Entry(quads)
  d_textbox.place()
  d_textbox.place(x=250, y = 250, anchor = "center")

  #i make the enter button below which essentially  graphs everything by callling on the logarithmic_entry_button when clicked (created and explained later on)
  #the enter button is super important because it goes to the function that ends up obtaining the users info and graphs the input 
  enter_button = Button(quads, text = "Enter", bg = "pink", command = logarithmic_entry_button) #making an object of the Button class  and assiging it to the variable enter_button. In the parameters I specify the window, text,  colour and command.
  enter_button.place()
  enter_button.place(x = 150, y = 280, anchor = "center") #i use the place and pack methods and in the place parameters I specify when the button should go with x and y and the anchor

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again when clicked
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page)
  back_button_one.pack()
  back_button_one.place(x = 250, y = 280, anchor = "center", width = 65)

####################################################################################################################################### Logarithmic Entry Button ##################################################################################################

#logarithmic_entry_button is a function that actually graphs the users input by using Justin's logarithmic function, and makes the back button by creating a new window. The back button takes the user back to the logarithmic textbox page. It does a similar thing in comparison to the other entry buttons, other than the fact that it calls loggraph instead to work with the log input. 
def logarithmic_entry_button():
  global bob #making the window of the button global so we can delete it later

  once_again_collecting_info() #Calling the once again collecting info function so that the users input in the textboxes is actually stored to proper variables to be used

  loggraph(a, b, c, d) #calling  the quadgraph function that Justin made and suppplying the users input (a, b, c and d) in the parameters so that it graphs the values

  bob = Tk() #making a new Tk class object and storing in the variable bob
  bob.geometry("60x570") #changing the dimensions of bob so that it's a thin window and doesn't take up extra space, but is very tall so we can see it underneath the matplotlib window
  back_button_one = Button(bob, text = "Back", bg = "pink", width = 60, command = close_back_button)

  back_button_one.pack()
  back_button_one.place(x = 30, y = 555, anchor = "center", width = 60, height = 30) #packing and placing the button on the desired spot on the window (the width of the button is the same as the window and it is placed very low on the y axis so that it pokes out underneath the matplotlib window)

################################################################################################################################################################################################
################################################################################################################################################################################################
################################################################################################################################################################################################
###################  END OF GRAPHING CALCULATOR  ###################
################################################################################################################################################################################################
##########################################################################################################################################################################################

################################################################################################################################################################################################
################################################################################################################################################################################################
################################################################################################################################################################################################
###################  POLYGON SECTIOIN BEGNS (Melika)  ###################
################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################

#this section has the user select a shape, input coordinates, and then depending on the shape and coordiantes it will print the area and perimeter to the console

####################################################################################################################################### Polygon option page function
##################################################################################################

#polygon_option_page creates the window needed when the user selects the polygon button. It shows all the shape options as buttons (such as square, rectangle, triangle, etc) as well as a back button if the user wishes to return. The objective is so that the user can reach the approriate window to enter the informatin of their polygon depending on the shape. This specific window doesn't actually run any of my peers functions, it simply takess the user to where they can enter their info depending on the shape they selected. 

#takes no inputs, output is a window with a bunch of various buttons for the polygons and then a back button (and also label). 

#EXAMPLE: if the user selected the square button, the command of the square button would be executed, which is the square_polygon function, which helps later on make the page for the user to enter their coords
def polygon_option_page():

  global quads #globalizing the window variable so it can be destroyed later

  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Polygon Feature") #using the built in title method on the window to change it's title to Polygon Feature

  quads['bg'] = "pink" #making the window pink

  #making the primary label that tells the user to select the mode. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Select the Polygon", font = ("Helvetica", "24"), bg = "pink") 
  label1.pack()
  label1.place(x = 200, y = 25, anchor = "center")

  #SQUARE BUTTON - calls on square polygon function later on that actually creates the textboxes for the info to be entered in
  square_button = Button(quads, text = "Square", bg = "pink", command = square_polygon)
  square_button.pack()
  square_button.place(x = 200, y = 60, anchor = "center", width = 200)

  #RECTANGLE BUTTON - calls on rectangle polygon function later on that actually creates the textboxes for the info to be entered in
  rectangle_button = Button(quads, text = "Rectangle", bg = "pink", command = rectangle_polygon)
  rectangle_button.pack()
  rectangle_button.place(x = 200, y = 90, anchor = "center", width = 200)

  #TRIANGLE BUTTON - calls on triangle polygon function later on that actually creates the textboxes for the info to be entered in
  triangle_button = Button(quads, text = "Triangle", bg = "pink", command = triangle_polygon)
  triangle_button.pack()
  triangle_button.place(x = 200, y = 120, anchor = "center", width = 200)

  #OCTAGON BUTTON - calls on octagon polygon function later on that actually creates the textboxes for the info to be entered in
  octagon_button = Button(quads, text = "Octagon", bg = "pink", command = octagon_polygon)
  octagon_button.pack()
  octagon_button.place(x = 200, y = 150, anchor = "center", width = 200)

  #HEXAGON BUTTON - calls on hexagon polygon function later on that actually creates the textboxes for the info to be entered in
  hexagon_button = Button(quads, text = "Hexagon", bg = "pink", command = hexagon_polygon)
  hexagon_button.pack()
  hexagon_button.place(x = 200, y = 180, anchor = "center", width = 200)

  #Parallelogram BUTTON - calls on parallelogra polygon function later on that actually creates the textboxes for the info to be entered in
  Parallelogram_button = Button(quads, text = "Parallelogram", bg = "pink", command = parallelogram_polygon)
  Parallelogram_button.pack()
  Parallelogram_button.place(x = 200, y = 210, anchor = "center", width = 200)

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again when clicked
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page, width = 65)
  back_button_one.pack()
  back_button_one.place(x = 200, y = 250, anchor = "center", width = 65)

####################################################################################################################################### Boxes for coords function
##################################################################################################


#boxes_for_coords is a function for creating the textboxes for the user to enter their input so that they can find the perimiter and area of the shape they previously selected. Basically, when the shape buttons are clicked in the previous function, it leads to another function created later on that assigns the variable x with a certain number depending on how many sides the polygon has. This function uses the number of shapes to determine how any textboxes should be created. It checks for most numbers using conditional systems, and then if the conditional statement is true, depending on the number in the conditional statement, a certain number of textboxes will be created. There's also an enter button so the user can enter their info and a back button to go back to the home page.

#EXAMPLE: If the user selected triangle, x would be equal to three (x is assigned it's value in later functions), and therefore three textboxes would should up on the window, NO MORE THAN THREE THOUGH

#It takes no inputs and the output is a window with buttons, and enter and back button (and also a label)
def boxes_for_coords():
  global quads, a_textbox, b_textbox, c_textbox, d_textbox, e_textbox, f_textbox, g_textbox, h_textbox #globalizing the window variable so it can be destroyed later, and the textboxes so i can obtain the information later

  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Input Info") #using the built in title method on the window to change it's title to Input Info

  quads['bg'] = "pink" #making the window pink
  
  #making the primary label that tells the user to select the mode. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Enter the X and Y coordinates in the format of '(x,y)'", font = ("Helvetica", "10"), bg = "pink") 
  label1.pack()
  label1.place(x = 200, y = 25, anchor = "center")
  
  if x >= 3: #we first check if x (the number of sides the shape has) is more than or equal to three to make the first three textboxes (three is the minimum because the lowest number of sides a shape has is 3 (triangle)). Technically every shape is going to create these three textboxes.
  #i use the same textbox creating method as before
    a_textbox = Entry(quads)
    a_textbox.place()
    a_textbox.place(x=200, y = 50, anchor = "center")

    b_textbox = Entry(quads)
    b_textbox.place()
    b_textbox.place(x=200, y = 80, anchor = "center")

    c_textbox = Entry(quads)
    c_textbox.place()
    c_textbox.place(x=200, y = 110, anchor = "center")
  
    
  if x >= 4: #next i check if the shape has four sides, and if it does I create an additional textbox to have four for the four sides.
    d_textbox = Entry(quads)
    d_textbox.place()
    d_textbox.place(x=200, y = 140, anchor = "center")
    
  if x >= 5: #next i check if the shape has five sides, and if it does I create an additional textbox to have five for the five sides
    e_textbox = Entry(quads)
    e_textbox.place()
    e_textbox.place(x=200, y = 170, anchor = "center")
    
  if x >= 6: #next i check if the shape has six sides, and if it does I create an additional textbox to have six for the six sides.
    f_textbox = Entry(quads)
    f_textbox.place()
    f_textbox.place(x=200, y = 200, anchor = "center")

    
  if x >= 8: #finally i check if the shape has eight sides, and if it does I create two additional textboxes to have eight for the eight sides. The reason why this conditional checks for eight and we skipped seven is because none of our polynomial options have seven sides
    g_textbox = Entry(quads)
    g_textbox.place()
    g_textbox.place(x=200, y = 230, anchor = "center")

    h_textbox = Entry(quads)
    h_textbox.place()
    h_textbox.place(x=200, y = 260, anchor = "center")



  #i make the enter button below which essentially  graphs everything by callling on the obtaining_info_for_polygons when clicked (created and explained later on)
  enter_button = Button(quads, text = "Enter", bg = "pink", command = obtaining_info_for_polygons) #making an object of the Button class  and assiging it to the variable enter_button. In the parameters I specify the window, text,  colour and command.
  enter_button.place()
  enter_button.place(x = 330, y = 150, anchor = "center") #i use the place and pack methods and in the place parameters I specify when the button should go with x and y and the anchor

  back_button_one = Button(quads, text = "Back", bg = "pink", width = 60, command = back_to_home_page)
  back_button_one.pack()
  back_button_one.place(x = 330, y = 190, anchor = "center", width = 60, height = 30) #packing and placing the button on the desired spot on the window (the width of the button is the same as the window and it is placed very low on the y axis so that it pokes out underneath the matplotlib window)

####################################################################################################################################### Obtaining info for polygons function
##################################################################################################
  
#obtaining_info_for_polygons is a function that goes to the specific function that finds the area and perimemter of the user depending on which shape they selected. It is called with the enter button of the previous function. Essentially, when a certain polygon button is clicked the variable "shape" is assigned with the selected shape name (this is all coded later), so this function checks which shape was selected and runs the appropraite code depedning on the shape using conditionals. It is an important function because since I only use one function to make all of my textboxes above, this function then goes to the appropraite function to find the area and perimeter 

#It takes no inputs and what it ends up doing is call another function

#EXAMPLE: When the user selects the enter button of the previous function, this function is called. An example is if the person selected the square button, later on the variable square would be given the appropraite name (square) and thus in this function the conditional of shape = "sqare" would be condiered true and the indented block would be executed, which in this case is the obtaining_nfo_for_square function
def obtaining_info_for_polygons():
  if shape == "square": #checks for shape name
    obtaining_info_for_square() #runs appropraite function
  if shape == "triangle": #the same things is repeated for all polygons
    obtaining_info_for_triangle()
  if shape == "rectangle":
    obtaining_info_for_rectangle()
  if shape == "octagon":
    obtaining_info_for_octagon()
  if shape == "hexagon":
    obtaining_info_for_hexagon()
  if shape == "parallelogram":
    obtaining_info_for_parallelogram()

#turning_coords_to_tuple turns the users string input to a tuple. It works by takig the users string that is inputted like (x,y), removing the brackets, and then I make all the input on one side of the comma on tuple item, and all the input on the other side of the comma another tuple item

#This is one of the only functions in this entire code that has an inpute. The input is a string formatted like the following: (x,y), so a round bracket enclosing two numeric values seperated by a comma.
#The output technically looks the exact same, other than the fact that it is actually considered a tuple to python and doesn't only look like one

#EXAMPLE: If you were to input a string that is formatted just like a tuple (ex. (3,4), (-5,60), (0,14), etc) the function will return the actual tuple version, so for the given example the function would return (3,4), (-5,60), (0,14) respectively, with the difference being that they are now tuples.
    
def turning_coords_to_tuple(a):
  a = a[1:] #I tell the user to input their input like so (x,y), but python simply considers that a string, so in order to turn it to a tuple I begin by removing the first bracket by assigning a the value of a without the first index by doing a[1:], meaning the first string index (hence the 1) all the way to the end of the string (hence the blank)
  a = a[:-1] #To get rid of the last bracket I do the same thing except I leave everything in the begining all the way to the last index. 
  comma = a.index(',') #I find the index of the comma and store it in variable comma
  x_coord = float(a[:comma]) #I make a variable with everything in the string a up to the index of the value in comma, which in this case is the x coordinate
  y_coord = float(a[comma+1:]) #I add everything after the comma to a variable which is my y coordiate
  a = (x_coord,y_coord) #fially i make the tuple of x and y
  return a

#


####################################################################################################################################### Obtaining info functions (includes all polygons including squares, triangles, etc)
##################################################################################################

#obtaining_info_for_square obtains the info from the textboxes, and ues the turning_coords_to_tuple to turn the string input to a tuple and stores it in a variable. It adds the coordinates to a list, and then using Ellie's code, it makes an object of the square class and adds the list of coordinates in the parameters, and then uses the perimeter and area method to obtain the area and perimeter and print it. It has everything in a try and except so that if for some reason there's an error (such as the user inputing info that can't be turned to a tuple), it doesn't crash the entire program

#ALL obtaining_info_for_shapename functions below pretty much work the exact same way, with the sole difference being that sometimes there are more variables/more items being added to the list, because the shape may vary and have more sides therefore more coords. The only other difference is that obviously a different class is going to have an object be created because the shapes are different, but it still uses the area and perimeter methos

#These functions get called in the obtaining_info_for_polygons function depending on the shape the user selected.

#EXAMPLE: If the user has selected square, the obtaining_info_for_polygon function would redirect the code to the obtaining_info_for_square function. Here, the users coordinates would be converted to tuples with the above function, added to a list, and then a square object would be created with the list as the attribute, and then we print the perimeter and area of the square object. If the coordinates are incorrect for some reason, the except catches the error and displays the error message

#SQUARE FUNCTION 
def obtaining_info_for_square():
  global list_for_coords 
  list_for_coords = [] #making empty list
  try: #using try and except to catch errors
    a = turning_coords_to_tuple(a_textbox.get()) #using get method to obtain info user unputted to textboxes then using my turning_coords_to_tuple function to turn it to a tuple then storing that into a variable. I do this for every textbox
    b = turning_coords_to_tuple(b_textbox.get())
    c = turning_coords_to_tuple(c_textbox.get())
    d = turning_coords_to_tuple(d_textbox.get())
    list_for_coords.append(a) #I append every variable with a tuple to the empty list
    list_for_coords.append(b)
    list_for_coords.append(c)
    list_for_coords.append(d)
    square_object = square(list_for_coords) #making square class obejcts with the list of coordinates as a parameter
    print("Perimeter:", square_object.perimeter) #printing perimeter with perimeter method
    print("Area:", square_object.area) #printing area with area method
  except: #except block, so  if an error occured this block of code will run instead
  #I make a new label in the variable label1, and this time it displays the error message at the top of the screen
    label1 = Label(quads, text = "Please try again with appropriate values", font =   ("Helvetica", "10"), bg = "pink") #new label object in variable label1
    label1.pack()
    label1.place(x = 200, y = 25, anchor = "center")  #pack and place it to where I wish on the screen

#all of the obtaining info functions below do the exact same things but with different numbers of variables and with different shape classes depending on the selected polygon

#PARALLELOGRAM FUNCTION
def obtaining_info_for_parallelogram():
  global list_for_coords, x
  list_for_coords = []
  try:
    a = turning_coords_to_tuple(a_textbox.get())
    b = turning_coords_to_tuple(b_textbox.get())
    c = turning_coords_to_tuple(c_textbox.get())
    d = turning_coords_to_tuple(d_textbox.get())
    list_for_coords.append(a)
    list_for_coords.append(b)
    list_for_coords.append(c)
    list_for_coords.append(d)
    parallelogram_object = parallelogram(list_for_coords)
    print("Perimeter:", parallelogram_object.perimeter)
    print("Area:", parallelogram_object.area)
  except: #except block, so  if an error occured this block of code will run instead
  #I make a new label in the variable label1, and this time it displays the error message at the top of the screen
    label1 = Label(quads, text = "Please try again with appropriate values", font =   ("Helvetica", "10"), bg = "pink") #new label object in variable label1
    label1.pack()
    label1.place(x = 200, y = 25, anchor = "center")  #pack and place it to where I wish on the screen

#TRIANGLE FUNCTION
def obtaining_info_for_triangle():
  global list_for_coords, x
  list_for_coords = []
  try:
    a = turning_coords_to_tuple(a_textbox.get())
    b = turning_coords_to_tuple(b_textbox.get())
    c = turning_coords_to_tuple(c_textbox.get())
    list_for_coords.append(a)
    list_for_coords.append(b)
    list_for_coords.append(c)
    triangle_object = triangle(list_for_coords)
    print("Perimeter:", triangle_object.perimeter)
    print("Area:", triangle_object.area)
  except: #except block, so  if an error occured this block of code will run instead
  #I make a new label in the variable label1, and this time it displays the error message at the top of the screen
    label1 = Label(quads, text = "Please try again with appropriate values", font =   ("Helvetica", "10"), bg = "pink") #new label object in variable label1
    label1.pack()
    label1.place(x = 200, y = 25, anchor = "center")  #pack and place it to where I wish on the screen

    #RECTANGLE FUNCTION
def obtaining_info_for_rectangle():
  global list_for_coords, x
  list_for_coords = []
  try:
    a = turning_coords_to_tuple(a_textbox.get())
    b = turning_coords_to_tuple(b_textbox.get())
    c = turning_coords_to_tuple(c_textbox.get())
    d = turning_coords_to_tuple(d_textbox.get())
    list_for_coords.append(a)
    list_for_coords.append(b)
    list_for_coords.append(c)
    list_for_coords.append(d)
    rectangle_object = rectangle(list_for_coords)
    print("Perimeter:", rectangle_object.perimeter)
    print("Area:", rectangle_object.area)
  except: #except block, so  if an error occured this block of code will run instead
  #I make a new label in the variable label1, and this time it displays the error message at the top of the screen
    label1 = Label(quads, text = "Please try again with appropriate values", font =   ("Helvetica", "10"), bg = "pink") #new label object in variable label1
    label1.pack()
    label1.place(x = 200, y = 25, anchor = "center")  #pack and place it to where I wish on the screen

    #OCTAGON FUNCTION
def obtaining_info_for_octagon():
  global list_for_coords, x
  list_for_coords = []
  try:
    a = turning_coords_to_tuple(a_textbox.get())
    b = turning_coords_to_tuple(b_textbox.get())
    c = turning_coords_to_tuple(c_textbox.get())
    d = turning_coords_to_tuple(d_textbox.get())
    e = turning_coords_to_tuple(e_textbox.get())
    f = turning_coords_to_tuple(f_textbox.get())
    g = turning_coords_to_tuple(g_textbox.get())
    h = turning_coords_to_tuple(h_textbox.get())
    list_for_coords.append(a)
    list_for_coords.append(b)
    list_for_coords.append(c)
    list_for_coords.append(d)
    list_for_coords.append(e)
    list_for_coords.append(f)
    list_for_coords.append(g)
    list_for_coords.append(h)
    
    octagon_object = octagon(list_for_coords)
    print("Perimeter:", octagon_object.perimeter)
    print("Area:", octagon_object.area)
  except: #except block, so  if an error occured this block of code will run instead
  #I make a new label in the variable label1, and this time it displays the error message at the top of the screen
    label1 = Label(quads, text = "Please try again with appropriate values", font =   ("Helvetica", "10"), bg = "pink") #new label object in variable label1
    label1.pack()
    label1.place(x = 200, y = 25, anchor = "center")  #pack and place it to where I wish on the screen

#HEXAGON FUNCTION
def obtaining_info_for_hexagon():
  global list_for_coords, x
  list_for_coords = []
  try:
    a = turning_coords_to_tuple(a_textbox.get())
    b = turning_coords_to_tuple(b_textbox.get())
    c = turning_coords_to_tuple(c_textbox.get())
    d = turning_coords_to_tuple(d_textbox.get())
    e = turning_coords_to_tuple(e_textbox.get())
    f = turning_coords_to_tuple(f_textbox.get())
    list_for_coords.append(a)
    list_for_coords.append(b)
    list_for_coords.append(c)
    list_for_coords.append(d)
    list_for_coords.append(e)
    list_for_coords.append(f)

    hexagon_object = hexagon(list_for_coords)
    print("Perimeter:", hexagon_object.perimeter)
    print("Area:", hexagon_object.area)
  except: #except block, so  if an error occured this block of code will run instead
  #I make a new label in the variable label1, and this time it displays the error message at the top of the screen
    label1 = Label(quads, text = "Please try again with appropriate values", font =   ("Helvetica", "10"), bg = "pink") #new label object in variable label1
    label1.pack()
    label1.place(x = 200, y = 25, anchor = "center")  #pack and place it to where I wish on the screen


####################################################################################################################################### Shape function
##################################################################################################
  
#The following functions are the functions that are called when the user selects their polygon button. Essentially, it assigns the variable x with the number of sides the shape has so that the function "boxes_for_coords" can make the appropraite number of textboxes, then it assigns the variable shape with the name of the shape for the obtaining_info_for_polygons function so the appropraite function gets called depending on the shape, then calls the actual boxes_for_coords function so the user can begin inputting info

#Essentially, these functions are what make the button actually work

#EXAMPLE: If the user first clicked the square button in the original polygon window, the square_polygon function would be called, and thus x would be assigned the value of 4 so that the boxes_for_coords function works out, and square would be assigned "square" for the obtaining_info_for_polygon function from earlier. Then, the boxes_for_coords function is called which will result in the perimmeter and area of the square being printed to the console. 
#SQUARE
def square_polygon(): 
  global x, shape #for all the functions i globalize x (number of sides) and shape so that I can actually use the value in the other functions
  x = 4 #set x to number of sides
  shape = "square" #set shape to shape name
  boxes_for_coords() #call boxes_for_coords to make the text boxes

#TRIANGLE
def triangle_polygon():
  global x, shape
  x = 3
  shape = "triangle"
  boxes_for_coords()

#RECTANGLE
def rectangle_polygon():
  global x, shape
  x = 4
  shape = "rectangle"
  boxes_for_coords()

#OCTAGON
def octagon_polygon():
  global x, shape
  x = 8
  shape = "octagon"
  boxes_for_coords()

#HEXAGON
def hexagon_polygon():
  global x, shape
  x = 6
  shape = "hexagon"
  boxes_for_coords()

#PARALLEOGRAM
def parallelogram_polygon():
  global x, shape
  x = 4
  shape = "parallelogram"
  boxes_for_coords()


################################################################################################################################################################################################
###################  POLYGON SECTIOIN ENDS 
######################################################################################################################################
    
################################################################################################################################################################################################
###################  RANDOM DATA SET BEGINS (Melika) 
######################################################################################################################################

####################################################################################################################################### random data set
####################################################################

#random_data_set is a function that creates the window for the user to enter their input when the user selects ths random_data_sest option on the home page. It has a number of number, highest number and lowest number textbox, some labells, the back button, and the enter button which calls on another functioin that obtains the info from the textboxes to prnt the random data set to the console.

#There are no inputs, the output/resultl is the window with labels, textboxes and the enter/back buttons

#EXAMPLE: Anytime this function is called, a window would be created with three textboxes (number of numbers, highest/lowest number), with the enter and back button, and labels. The enter button will ALWAYS print rand data set function below

def random_data_set():
  global quads, a_textbox, b_textbox, c_textbox
  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Random Data Set") #using the built in title method on the window to change it's title to Random Data Set

  quads['bg'] = "pink" #making the window pink

  #making the primary label that tells the user to enter the information. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Enter the information", font = ("Helvetica", "24"), bg = "pink") 
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #i start off by making my three labels "Amount of Numbers", "Highest Number", and "Lowest Number". I create objects of the label class, assign them to variables, and in the parameters I specify the window (quads), text, font and colour. Then I pack and place them where I wish by specifying the x and y numbers and the anchor. 

  #Amount of Numbers Label
  label2 = Label(quads, text = "Amount of Numbers", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 100, anchor = "center")

  #Highest Number, underneath a value label
  label2 = Label(quads, text = "Highest Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 150, anchor = "center")

  #Lowest Number, underneath b value label
  label2 = Label(quads, text = "Lowest Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 200, anchor = "center")

   #i then make my three textboxes beside the three labels. I create objects of the Entry class (which is a textbox, assign them to variables, and in the parameters I specify the window (quads). Then I pack and place them where I wish by specifying the x and y numbers and the anchor. 

  #first textbox for the amount of numbers
  a_textbox = Entry(quads)
  a_textbox.place()
  a_textbox.place(x=300, y = 100, anchor = "center")

  #second textbox for the highest number
  b_textbox = Entry(quads)
  b_textbox.place()
  b_textbox.place(x=300, y = 150, anchor = "center")

  #third textbox for the lowest value
  c_textbox = Entry(quads)
  c_textbox.place()
  c_textbox.place(x=300, y = 200, anchor = "center")

  #i make the enter button below which runs Maryams program to prit the list to the screen
  enter_button = Button(quads, text = "Enter", bg = "pink", command = print_rand_data_set) #making an object of the Button class  and assiging it to the variable enter_button. In the parameters I specify the window, text,  colour and command.
  enter_button.place()
  enter_button.place(x = 200, y = 250, anchor = "center") #i use the place and pack methods and in the place parameters I specify when the button should go with x and y and the anchor

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again when clicked
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page, width = 65)
  back_button_one.pack()
  back_button_one.place(x = 200, y = 280, anchor = "center", width = 65)

####################################################################################################################################### print rand data set function
####################################################################

#This functions overall purpose is to generate the random data set using the users input and print it to the console. It first uses the get method on the textboxes to obtain the users input then stores it to a variable. Then, it attempts to turn the input to an integer and then calls the random_data_set function (made by peers) and supplies the users input as the parameters. The whole thing is in a try and except so issues are caught if the user inputs incorrect info

#takes no inputs, it results in printing the random data set list in the console (if user enters proper info)

#EXAMPLE: If the amount of numbers was 4, the highest was 7, and the lowest was 0, the random data set could look something like this [4, 2, 1, 6] and that will be printed to the console. If one of the values was something like asdlfjaldksfja (or any non numerical value), the except would catch the error and print the error message.

def print_rand_data_set():
  #For all the variables with textboxes I previusly made, I use the get method with the entry objects, and store the value in variables a, b and c
  a = a_textbox.get() #textbox a value of total amount of numbers stored in variable a
  b = b_textbox.get() #textbox b value of highest number stored in variable b
  c = c_textbox.get() #textbox c value of lowest number stored in variable c

  #I need to convnert what the user entered to an integer or float so it works with maryams code, but because we can't gaurantee the user to  enter  a  numeric  value, instead of simply turning all the textbox value to a float/integer, I  put  it  all in a try and except  so that if they are not numeric values it doesn't stop the entire program. If it doesn't work it changes the main, big label to tell the user to try again. 
  # try: 
  a = int(a)
  b = int(b)
  c = int(c)
  Rand_Data_Set(a, b, c)
  # except: #except block, so  if an error occured this block of code will run instead
  #   #I make a new label in the variable label1, and this time it displays the error message at the top of the screen
  #   label1 = Label(quads, text = "Please try again with appropriate numbers", font =   ("Helvetica", "14"), bg = "pink")   #new label object in variable label1
  #   label1.pack()
  #   label1.place(x = 200, y = 50, anchor = "center") #pack and place it to where I wish on the screen

################################################################################################################################################################################################
###################  RANDOM DATA SET SECTIOIN ENDS 
######################################################################################################################################

################################################################################################################################################################################################
###################  QUADRATIC CALCULATOR SECTION BEGINS (Melika) 
######################################################################################################################################


####################################################################################################################################### actual quadratic calculator function
####################################################################

#actual QUADRATIC calculator is the function that is called when the user selects the quadratic calcualtor option and the main home page. Essentially, all it does is create the textboxes for the user to enter their information, and then when the user selects the enter button another function is called that uses the input. It also have a main label, and buttons (back and enter button). This function doesn't actually call Maryam's function to find info, it simply gathers input

#Takes no parameters, output is a window with textboxes, label and buttons

#EXAMPLE: Any time this function is called, it will always result in the exact same textboxes, buttons and labels. The enter button will always have the command of quadratic_calculator_entry_button

def actual_quadratic_calculator():
  global quads, a_textbox, b_textbox, c_textbox #I globalize the window as well as the textboxes variable so that I can use the get method on them in a later function 

  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Quadratic Calculator") #using the built in title method on the window to change it's title

  quads['bg'] = "pink" #making the window pink

  #below i make the primary label that tells the user to enter the values. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Enter the values", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #i start off by making my three labels "a value", "b value", and "c value". I create objects of the label class, assign them to variables, and in the parameters I specify the window (quads), text, font and colour. Then I pack and place them where I wish by specifying the x and y numbers and the anchor. 

  #A value label
  label2 = Label(quads, text = "A Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 100, anchor = "center")

  #B value label, underneath a value label
  label2 = Label(quads, text = "B Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 150, anchor = "center")

  #C value label, underneath b value label
  label2 = Label(quads, text = "C Value", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 200, anchor = "center")

   #I then make my three textboxes beside the three labels (a value, b value and c value). I create objects of the Entry class (which is a textbox, assign them to variables, and in the parameters I specify the window (quads). Then I pack and place them where I wish by specifying the x and y numbers and the anchor. 

  #first textbox for the a value
  a_textbox = Entry(quads)
  a_textbox.place()
  a_textbox.place(x=250, y = 100, anchor = "center")

  #second textbox for the b value
  b_textbox = Entry(quads)
  b_textbox.place()
  b_textbox.place(x=250, y = 150, anchor = "center")

  #third textbox for the c value
  c_textbox = Entry(quads)
  c_textbox.place()
  c_textbox.place(x=250, y = 200, anchor = "center")

  #i make the enter button below which essentially  graphs everything by callling on the quadratic_calculator_entry_button when clicked (created and explained later on)
  enter_button = Button(quads, text = "Enter", bg = "pink", command = quadratic_calculator_entry_button) #making an object of the Button class  and assiging it to the variable enter_button. In the parameters I specify the window, text,  colour and command.
  enter_button.place()
  enter_button.place(x = 200, y = 235, anchor = "center") #i use the place and pack methods and in the place parameters I specify when the button should go with x and y and the anchor

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again when clicked
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page, width = 65)
  back_button_one.pack()
  back_button_one.place(x = 200, y = 275, anchor = "center", width = 65)


####################################################################################################################################### collecting info function
####################################################################

#collcting_info is a function that is different from most of the other functions in this program. It obtains the text typed into textboxes made in previous functiono, and stores them in variables and turns them to a float. This function works with three text boxes. 

#takes no input, result of function is variables with users input stored in it 

#EXAMPLE: If the user had inputted 5, 7 and 8, after this function has run variables a, b and c would contain the float value of 5, 7 and 8. If the user inputs any incorrect info, the except will catch it and print the error message
def collecting_info():
  global a, b, c #globalizing a, b, and c variables that stores the input of the textboxes

  #For all the variables with textboxes I previusly made (and globalized), I use the get method with the entry objects, and store the value in variables a, b and c
  a = a_textbox.get() #textbox a value stored in variable a
  b = b_textbox.get() #textbox b value stored in variable b
  c = c_textbox.get() #textbox c value stored in variable c

  #Because we can't gaurantee the user to  enter  a  numeric  value, instead of simply turning all the textbox value to a float/integer, I  put  it  all in a try and except  so that if they are not numeric values, it doesn't stop the entire program. It trys to turn a, b and c to a float, but if it doesn't work it changes the main, big label to tell the user to try again. 
  try: 
    a = float(a) #replacing the value of variable a to a float
    b = float(b) #replacing the value of variable b to a float
    c = float(c) #replacing the value of variable c to a float
  except: #except block, so  if an error occured this block of code will run instead
    #I make a label in the variable label1, and this time it displays the error message at the top of the screen
    label1 = Label(quads, text = "Please try again with appropriate values", font =   ("Helvetica", "15"), bg = "pink")   #new label object in variable label1
    label1.pack()
    label1.place(x = 200, y = 50, anchor = "center") #pack and place it to where I wish on the screen


####################################################################################################################################### quadratic calculator entry button
####################################################################

 #quadratic_calculator_entry_button is a function that actually graphs the users input by using Maryam's quadratic formula calculator function, and makes the back button by creating a new window. The back button takes the user back to the quadratic textbox page. In summary is uses the collecting info function to put the input in the textboxes to variables and then uses Maryams function to find the roots and prints it.

#EXAMPLE: If the input is valid then a graph will be created but if they are invalid the error from collectng info with be caught in the except and the error will be displayed

def quadratic_calculator_entry_button(): 

  try: 
    collecting_info() #Calling the collecting info function so that the users input in the textboxes is actually stored to proper variables to be used
    print(Quadratic_Formula_Calculator(a, b, c))#calling  the quadratic formula calculator function that Maryam made and suppplying the users input (a, b and c) in the parameters so that it graphs the values
  except:
    pass

################################################################################################################################################################################################
###################  QUADRATIC CALCULATOR SECTION ENDS
######################################################################################################################################

################################################################################################################################################################################################
###################  LCM AND GCF SECTION BEGINS (Melika) 
######################################################################################################################################


####################################################################################################################################### lcm_gcf window function
####################################################################

#the lcm_gcf_window is the function that makes the window selected when the user selects the lcm and gcf function on the main home page. Essentially, it has buttons for the user to select wheather they want gcf or lcm, and then also has a label and back button. When the user selects their button, the buttons command is called which is another function that makes the textboxes appear. This sspecific function though has ntohing with finding the lcm and gcf, it simply guides the user to another window .

#It takes no inputs and the output is the window which the lcm and gcf window

#EXAMPLE: This function will always make a window with a lcm button that opens another window to input info, a gcf button that opens another window to input window and a back button to go back.

def LCM_GCF_window():
  global quads #globalizing the window variable so it can be destroyed later

  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("LCM and GCF") #using the built in title method on the window to change it's name to lcm and gcf

  quads['bg'] = "pink" #making the window pink

  #making the priamary label that tells the user to select the mode. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Select the mode", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #below I create all the buttons I need for this  window. Again, it's pretty much the exact same steps as everytime else. For every button, I  first create an object in the button class and assign it to a variable. I specify the window, text, and colours in the parameters. I also speicfy the command in the parameters, which allows the button to actually do something and calls another function. Then I pack and place them in the appropraite spot, specify the anchor, and specify width.

  #first button: LCM, calls the LCM function (created later on) so that the user can enter their input and the program will find the lcm
  LCM_button = Button(quads, text = "LCM", bg = "pink", command= LCM_window)
  LCM_button.pack()
  LCM_button.place(x = 200, y = 100, anchor = "center", width = 200)

  #second button: GCF, calls the GCF function (created later on) so that the user can enter their input and the program will find the gcf
  GCF_button = Button(quads, text = "GCF", bg = "pink", command = GCF_window)
  GCF_button.pack()
  GCF_button.place(x = 200, y = 170, anchor = "center", width = 200)

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page)
  back_button_one.pack()
  back_button_one.place(x = 200, y = 250, anchor = "center", width = 240)



####################################################################################################################################### lcm window function
####################################################################
#LCM_window is the function that is called when the user selects the lcm button with the previous function. It creates the textboxes for the user to input their info, including the first and second nubers, and then also the labels and enter/back button. This function doesn't actually find the lcm, instead it simply gathers info so that when the user presses the enter button there is input from the user to use. 

#It again takes no inputs, and the output is a window with some labels, buttons and two textboxes for the numbers

#EXAMPLE: LCM window makes the window for the user to input their info in textboxes. It will do the same thing every single time. The enter button runs the lcm results function using the users input


def LCM_window():
    global quads, a_textbox, b_textbox 

    quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

    quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

    quads.title("LCM") #using the built in title method on the window to change it's title to lcm

    quads['bg'] = "pink" #making the window pink

    #below  i make the primary label that tells the user to enter the values. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
    label1 = Label(quads, text = "Enter the values", font = ("Helvetica", "24"), bg = "pink")
    label1.pack()
    label1.place(x = 200, y = 50, anchor = "center")

    #i start off by making my 2 labels "First number", and "Second number". I create objects of the label class, assign them to variables, and in the parameters I specify the window (quads), text, font and colour. Then I pack and place them where I wish by specifying the x and y numbers and the anchor.

    #first number label
    label2 = Label(quads, text = "First Number", font = ("Helvetica", "15"), bg = "pink")
    label2.pack()
    label2.place(x = 100, y = 100, anchor = "center")

    #second number labela
    label2 = Label(quads, text = "Second Number", font = ("Helvetica", "15"), bg = "pink")
    label2.pack()
    label2.place(x = 100, y = 175, anchor = "center")



    #I then make my 2 textboxes beside the 2 labels (a value, b value). I create objects of the Entry class (which is a textbox, assign them to variables, and in the parameters I specify the window (quads). Then I pack and place them where I wish by specifying the x and y numbers and the anchor. 

    #first textbox for the a value
    a_textbox = Entry(quads)
    a_textbox.place()
    a_textbox.place(x=300, y = 100, anchor = "center")

    #second textbox for the b value
    b_textbox = Entry(quads)
    b_textbox.place()
    b_textbox.place(x=300, y = 175, anchor = "center")

    #I make the enter button below which essentially  graphs everything by callling on the logarithmic_entry_button when clicked (created and explained later on)
    enter_button = Button(quads, text = "Enter", bg = "pink", command = lcm_results) #making an object of the Button class  and assiging it to the variable enter_button. In the parameters I specify the window, text,  colour and command.
    enter_button.place()
    enter_button.place(x = 200, y = 230, anchor = "center") #i use the place and pack methods and in the place parameters I specify when the button should go with x and y and the anchor

    #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again when clicked
    back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page, width = 65)
    back_button_one.pack()
    back_button_one.place(x = 200, y = 280, anchor = "center", width = 65)

####################################################################################################################################### lcm results function
####################################################################

#lcm_results is the function that is the command of the enter button for the lcm window that uses the users input to diplay the lcm in the console. Essentially, it gets the input in the textboxes with the get method, stores it in a variable, then in a try and except trys to turn the values to a float. It calls the LCM function (created by peers, not me), with the users input as the parameters, and prints it. If any errors arise such as the users input is not a number, the except will catch the error and display the error message.  

#it takes no input, and the output is lcm printed to the console

#EXAMPLE: If the user inputted 5 and 10, this function would try to turn the values the floats, store them to variables and using the lcm function with the users input to find the lcm and then would prints it to the console, so in this case it would be 10. If the user had entered something that's not numerical or correct, the except would catch the error and display the error message 

def lcm_results():
  #For all the variables with textboxes I previusly made (and globalized), I use the get method with the entry objects, and store the value in variables a, b
    a = a_textbox.get() #textbox a value stored in variable a
    b = b_textbox.get() #textbox b value stored in variable b

    #Because we can't gaurantee the user to  enter  a  numeric  value, instead of simply turning all the textbox value to a float/integer, I  put  it  all in a try and except  so that if they are not numeric values, it doesn't stop the entire program. It trys to turn a, b,c and d to a float, but if it doesn't work it changes the main, big label to tell the user to try again. 
    try:
      a = float(a) #replacing the value of variable a to a float
      b = float(b) #replacing the value of variable b to a float
      print(LCM(a,b))

    except: #except block, so  if an error occured this block of code will run instead
      #I make a new label in the variable label1, and this time it displays the error message at the top of the screen
      label1 = Label(quads, text = "Please try again with appropriate values", font =   ("Helvetica", "15"), bg = "pink") #new label object in variable label1
      label1.pack()
      label1.place(x = 200, y = 50, anchor = "center")  #pack and place it to where I wish on the screen

####################################################################################################################################### gcf window function
####################################################################

#GCF_window is the function that is called when the user selects the gcm button on the lcm and gcf window. It creates the textboxes for the user to input their info, including the first and second nubers, and then also the labels and enter/back button. This function doesn't actually find the gcf, instead it simply gathers info so that when the user presses the enter button there is input from the user to use. 

#It again takes no inputs, and the output is a window with some labels, buttons and two textboxes for the numbers

#EXAMPLE: GCF window makes the window for the user to input their info in textboxes. It will do the same thing every single time. The enter button runs the gcf results function using the users input


def GCF_window():
  global quads, a_textbox, b_textbox 

  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("GCF") #using the built in title method on the window to change it's title to GCF

  quads['bg'] = "pink" #making the window pink

  #below I make the primary label that tells the user to enter the values. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Enter the values", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #I start off by making my 2 labels "First number", and "Second number". I create objects of the label class, assign them to variables, and in the parameters I specify the window (quads), text, font and colour. Then I pack and place them where I wish by specifying the x and y numbers and the anchor.

  #first number label
  label2 = Label(quads, text = "First Number", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 100, anchor = "center")

  #second number label
  label2 = Label(quads, text = "Second Number", font = ("Helvetica", "15"), bg = "pink")
  label2.pack()
  label2.place(x = 100, y = 175, anchor = "center")



  #I then make my 2 textboxes beside the 2 labels (a value, b value). I create objects of the Entry class (which is a textbox, assign them to variables, and in the parameters I specify the window (quads). Then I pack and place them where I wish by specifying the x and y numbers and the anchor. 

  #first textbox for the first number
  a_textbox = Entry(quads)
  a_textbox.place()
  a_textbox.place(x=300, y = 100, anchor = "center")

  #second textbox for the second number
  b_textbox = Entry(quads)
  b_textbox.place()
  b_textbox.place(x=300, y = 175, anchor = "center")

  #I make the enter button below. The command of the command is gcf_results, so that when the user is done inputting inputting the info, they can press the enter button whhich run another button so that the gcf can be printed to the conosle
  enter_button = Button(quads, text = "Enter", bg = "pink", command = gcf_results) #making an object of the Button class  and assiging it to the variable enter_button. In the parameters I specify the window, text,  colour and command.
  enter_button.place()
  enter_button.place(x = 200, y = 230, anchor = "center") #i use the place and pack methods and in the place parameters I specify when the button should go with x and y and the anchor

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again when clicked
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page, width = 65)
  back_button_one.pack()
  back_button_one.place(x = 200, y = 280, anchor = "center", width = 65)

####################################################################################################################################### gcf results function
####################################################################

#gcf_results is the function that is the command of the enter button for the gcf window that uses the users input to diplay the gcf in the console. Essentially, it gets the input in the textboxes with the get method, stores it in a variable, then in a try and except trys to turn the values to a float. It calls the GCF function (created by peers, not me), with the users input as the parameters, and prints it. If any errors arise such as the users input is not a number, the except will catch the error and display the error message.  

#it takes no input, and the output is lcm printed to the console

#EXAMPLE: If the user inputted 5 and 10, this function would try to turn the values the floats, store them to variables and using the gcf function with the users input to find the gcf and then would prints it to the console, so in this case it would be 5. If the user had entered something that's not numerical or correct, the except would catch the error and display the error message 

def gcf_results():
#For all the variables with textboxes I previusly made (and globalized), I use the get method with the entry objects, and store the value in variables a, b
  a = a_textbox.get() #textbox a value stored in variable a
  b = b_textbox.get() #textbox b value stored in variable b

  #Because we can't gaurantee the user to  enter  a  numeric  value, instead of simply turning all the textbox value to a float/integer, I  put  it  all in a try and except  so that if they are not numeric values, it doesn't stop the entire program. It trys to turn a, b,c and d to a float, but if it doesn't work it changes the main, big label to tell the user to try again. 
  try:
    a = float(a) #replacing the value of variable a to a float
    b = float(b) #replacing the value of variable b to a float
    print(GCF(a,b))

  except: #except block, so  if an error occured this block of code will run instead
    #I make a new label in the variable label1, and this time it displays the error message at the top of the screen
    label1 = Label(quads, text = "Please try again with appropriate values", font =   ("Helvetica", "15"), bg = "pink") #new label object in variable label1
    label1.pack()
    label1.place(x = 200, y = 50, anchor = "center")  #pack and place it to where I wish on the screen

################################################################################################################################################################################################
###################  LCM AND GCF SECTION ENDS
######################################################################################################################################


################################################################################################################################################################################################
###################  SIMULATIONS  SECTION BEGINS (Melika) 
######################################################################################################################################

#simulations and is the function that makes the window for the user to select the simulation they wish to run (dice and coin), and it appears when the user selects the simulations option on the home page. It has a label, two buttons (coin and dice that run the coin and dice functinos that maryam made) and a back button

#EXAMPLE: will always create a window with the coin and dice functions. Depending on the button selected, the command will either be the dice or coin function. If they select the coin button, the coin function will be run and the mini coin window will appear. If the dice butto is selected, the mini dice window will apear as the dice dunction is called
  
def simulations():
  global quads #globalizing the window variable so it can be destroyed later

  quads = Tk() #creates window by creating an object in the Tk() class and assigning it to the variable "quads"

  quads.geometry("400x300") #using the built in geometry method on the window created to change the dimensions of the window

  quads.title("Coin and Dice") #using the built in title method on the window to change it's title

  quads['bg'] = "pink" #making the window pink

  #making the priamary label that tells the user to select the mode. I make an object in the label class and assigning it to the variable label1 (and in the parameters I specify the window, text, font and colour). Then, I pack and place it to where I wish on the screen.
  label1 = Label(quads, text = "Select the mode", font = ("Helvetica", "24"), bg = "pink")
  label1.pack()
  label1.place(x = 200, y = 50, anchor = "center")

  #below I create all the buttons I need for this  window. Again, it's pretty much the exact same steps as everytime else. For every button, I  first create an object in the button class and assign it to a variable. I specify the window, text, and colours in the parameters. I also speicfy the command in the parameters, which allows the button to actually do something and calls another function. Then I pack and place them in the appropraite spot, specify the anchor, and specify width.

  #first button: Coin, calls the coin function (created by Maryam) so that the user can see the coin simulation. When the button is clicked maryams coin graphic will show up on the screen
  coin_button = Button(quads, text = "Coin", bg = "pink", command= coin)
  coin_button.pack()
  coin_button.place(x = 200, y = 100, anchor = "center", width = 200)

  #second button: Dice, calls the dice function (created by Maryam) so that the user can see the dice simulation. When the button is clicked maryams dice graphic will show up on the screen
  dice_button = Button(quads, text = "Dice", bg = "pink", command = dice)
  dice_button.pack()
  dice_button.place(x = 200, y = 170, anchor = "center", width = 200)

  #Back button (last button). This button calls the back_to_home_page which lets the user see the home page again
  back_button_one = Button(quads, text = "Back", bg = "pink", command = back_to_home_page)
  back_button_one.pack()
  back_button_one.place(x = 200, y = 250, anchor = "center", width = 240)

#############################################################
###################testing###################################################################################################################

# ##################MARYAMMMMM#####################
testCount = 1
def test(actual, expected): #creats funtion to test answers
  global testCount
  if actual == expected: #if the answer is correct/expected
    print("Test ", testCount, "passed")#it will print that the test has passed
  else:#if the answer was not expected
    print("Test ", testCount, "failed")#it will print that the test failed
  testCount+=1#adds to the counter

##############tests for quadratic calculator #################
test(LIBRARY.SimpleFunctions.Quadratic_Formula_Calculator(2, 5, -7), (-3.5, 1.0)) #a negative integer in case a negative number messes with things somehow
test(LIBRARY.SimpleFunctions.Quadratic_Formula_Calculator(2, -5, -7), (-1.0, 3.5))#makes sure it works with 2 negative values
test(LIBRARY.SimpleFunctions.Quadratic_Formula_Calculator(2, 6, 7), ("You have entered an imaginary root(s)"))#tests in case the roots aren't real
########################tets of GCF ###########################
test(LIBRARY.SimpleFunctions.GCF(6, 3), 3) #makes sure it works if 2 numbers are multiples
test(LIBRARY.SimpleFunctions.GCF(1, 7), 1)#Makes sure it works with 2 prime number (must equal 1)
test(LIBRARY.SimpleFunctions.GCF(423, 15), 3)#Ensures it works if the numbers have a large difference
test(LIBRARY.SimpleFunctions.GCF(24, 13), 1)#It works if one of the numbers are prime
########testing for random data set, simulations for dice and coin###########
#All of these tests are provided in the spec sheet
#######################tests for LCM #########################
test(LIBRARY.SimpleFunctions.LCM(5, 10), 10) #makes sure it worksif the 2 numbers are multiples
test(LIBRARY.SimpleFunctions.LCM(9, 13), 117) #Ensures it works if one number is prime
test(LIBRARY.SimpleFunctions.LCM(3, 13), 39) #Ensures it works if both numbers are prime
test(LIBRARY.SimpleFunctions.LCM(3, 3), 3) #Ensures it works if both numbers are the same
######################tests for y #############################
test(LIBRARY.SimpleFunctions.y(4, 3, 5), -17) #a larger prime number that will cause it to loop a few times to make sure it still returns "Prime"
test(LIBRARY.SimpleFunctions.y(6, 3, 2), -9) #makes sure it works if all the numbers are multiples
test(LIBRARY.SimpleFunctions.y(-2, 3, 4), 11)#if one number is negative
test(LIBRARY.SimpleFunctions.y(-5, -2, 10), 48)#if 2 numbers are negative
test(LIBRARY.SimpleFunctions.y(-6, -3, -2), -15)#ensures it works if 3 numbers are negative



#MELIKAAAA
####################################################################
#ACTUAL TESTABLE FUNCTION
################ Tests turning coords to tuple######################
test(turning_coords_to_tuple("(3,5)"), (3,5))
test(turning_coords_to_tuple("(-89,-8)"), (-89,-8))
test(turning_coords_to_tuple("(-70,12)"), (-70,12))
test(turning_coords_to_tuple("(12,-70)"), (12,-70))
test(turning_coords_to_tuple("(0,15)"), (0,15))
test(turning_coords_to_tuple("(0,-3)"), (0,-3))
test(turning_coords_to_tuple("(15,0)"), (15,0))
test(turning_coords_to_tuple("(-15,0)"), (-15,0))

#  the rest of my tests don't actually return values, they either make another window/use other functions to make a graph, and regardless they are highly dependant on most of the other functions in the program therefore they are written in a seperate py (melikas alternate testing)


# ELLLIEEE

def class_checker(Answer, expected, test_num): #checks if the answer is equal to the expected value 
  if Answer == expected: #if the two are equal
    print("Test ", test_num, "Passed") #the test is passed
  else: #if they aren't
    print("Test ", test_num, "Failed") #the test is failed

######################Tests SideLengths#######################

test(LIBRARY.Polygons.SideLengths([(0, 1), (3, 1), (3, 3), (0, 3)]), [3.0, 2.0, 3.0, 2.0]) #tests for points that give integer values
test(LIBRARY.Polygons.SideLengths([(0, 2), (3, 5), (3, 12), (0, 16)]), [4.2426, 7.0, 5.0, 14.0]) #tests for points that give float values
test(LIBRARY.Polygons.SideLengths([(0), (3, 5), (3, 12), (0, 16)]), "please enter appropriate coordinates") #tests for coordinates entered that aren't real coordinates

######################Tests Perimeter#########################

test(LIBRARY.Polygons.Perimeter([(0, 1), (3, 1), (3, 3), (0, 3)]), 10) #tests for points that give integer values
test(LIBRARY.Polygons.Perimeter([(0, 2), (3, 5), (3, 12), (0, 16)]), 30.2426) #tests for points that give float values

################Tests Regular_Polygon_Checker##################

test(LIBRARY.Polygons.Regular_Polygon_Checker([(0, 0), (0, 2), (2, 2), (2, 0)]), True) #tests for points that do not have equal sides
test(LIBRARY.Polygons.Regular_Polygon_Checker([(0, 2), (3, 5), (3, 12), (0, 16)]), False) #tests for points that do not have equal sides

######################Tests class_checker######################
rectangle1=rectangle([(0, 0), (0, 2), (2, 2), (2, 0)]) 


# test(class_checker(rectangle1.area, 4.0, 34), "Test 34 Passed")

######################Tests Square Class######################
square1=square([(0, 0), (0, 2), (2, 2), (2, 0)])
class_checker(square1.area, 4.0, 32)
square2=square([(0, 0), (0, 2), (2, 0), (2, 2)]) 
class_checker(square2.area, "This is not a square, please enter points in order or select correct shape.", 33)

####################Tests Rectangle Class#####################

rectangle1=rectangle([(0, 0), (0, 2), (2, 2), (2, 0)]) 
class_checker(rectangle1.area, 4.0, 34)
rectangle2=rectangle([(0, 7), (1, 3), (2, 2), (5, 6)]) 
class_checker(rectangle2.area, "This is not a rectangle, please enter points in order or select correct shape.", 35)

####################Tests Triangle Class#####################

triangle1=triangle([(0, 0), (4, 0), (0, 4)])
class_checker(triangle1.area, 8.0, 36)
triangle2=triangle([(0, 0), (0, 3), (1, 1)])
class_checker(triangle2.area, 1.5, 37)

###################Tests Parallelogram Class###################

parallelogram1a=parallelogram([(0, 0), (4, 0), (5, 3), (1, 3)])
# class_checker(t1.area, 8.0, 36)
#print(parallelogram1a.area)
parallelogram1b=parallelogram([(4, 0), (5, 3), (1, 3), (0, 0)])
#print(parallelogram1b.area)
parallelogram1c=parallelogram([(5, 3), (1, 3), (0, 0), (4, 0)])
#print(parallelogram1c.area)
parallelogram1d=parallelogram([(1, 3), (0, 0), (4, 0), (5, 3)])
#print(parallelogram1d.area)





# test(LIBRARY.FOLDER.FUNCTION(FUNCTION ARGUMENTS), ANSWER)







primary_window()

