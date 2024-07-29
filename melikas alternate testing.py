#TESTING MY UNTESTABLE FUNCTIONS HERE

################################################################################################################################################################################
#GRAPHING CALCULATOR
################################################################################################################################################################################

####################### PRIMARY WINDOW FUNCTION TESTING #######################
# CANNOT BE TESTED WITH SPECIFIC EXAMPLES 
#Test 1: If function is ever called (primary_window()) the window should show up. It HAS TO HAVE its main label and seven buttons (most back buttons make the primary window re apear)

#Test 2: If the user selects graphing calculator, it should result in the quadratic_calculator function being called, and thus another window with three options appears (polynomial, trigonometric and logarithmic)

#Test 3: If the user selects the polygon button, it should result in the polygon_option_page function being called, and thus another window with all the shape options as buttons appears (square, triangle, square, etc)

#Test 4: If the user selects the LCM and GCF button, the lcm_gcf_window function should be called, which results in another window that allows the user to pick betwee lcm and gcf

#Test 5: If the user selects the random data set, the random_data_set function should be called resulting in another window wth three textboxes for the user to enter input

#Test 6: If the user selects the y intercept calculator, the y-int-calc function should be called resulting in another window with three textboxes for m, x and b

#Test 7: If the user selects the simulations button, the simulations function should be called resulting in another window with two options, dice and coin

####################### BACK TO HOME PAGE FUNCTION TESTING #######################
# CANNOT BE TESTED WITH SPECIFIC EXAMPLES
#Test 1: Anytime this function is called the main home page (tested above) should re apear

####################### QUADRATIC CALCULATOR FUNCTOIN, POLYNOMIAL AND TRIG FUNCTION TESTNG #######################
# CANNOT BE TESTED WITH SPECIFIC EXAMPLES
#Test 1: ALL of these functions should create a new window when called, with a label, three buttons, and a back button.         
      # A) Quadratic_calculator function results in the three options of polyatomic, trig and log when called. This function should be called when the user selects the graphing calculator in the home page. Polynomial button should redirect the user to the polynomial window (function is polynomial function) as shown below. Trigonometric button should redirect to the trigonometric window (function is trigonometric function) as shown below. Logarithmin button should result in another page with textboxes for the user to enter info, as the buttons command s logarithmic function

      # B) Polynomial function results in the three options of quadratic, cubic and quartic when called. This function should be called when the user the polynomial button in the quadratic calculator window (shown above). Selecting quadratic button results in the quadratic function being called, cubic results in the cubic function being called, and quartic results in the quartic function being called. 

      # C) Trigonometric function results in the three options of sin, cos and tan when called. This function should be called when the user the trigonometric button in the quadratic calculator window (shown above). Selecting the sin button results in the sin function being called, cos results in the cos function being called, and tan results in the tan function being called. 

#Test 2: Selecting the back button will result in the back_to_home_page function being called, meaning the home page window will re apear

####################### Quadratic, cubic, quartic, sin, cos, tan annd log functions #######################
#Text 1: When the functions are called, all of the functions should result in a new window being created. The window contans a back button, enter button, and a certain number of textboxes. They functions should all appear when the correspondinng button is clicked in the previous windows (ex. quadratic button runs quadratic function, cubic runs cubic, quartic runs quartic, so on.)
  # How many textboxes is every function expected to put on the window?
  # Quadratic - 3 (a, b c)
  # Cubic - 4 (a, b, c, d)
  # Quartic - 5 (a, b, c, d, e)
  # Sin, cos and tan - 4 (a, k, p, q)
  # Log - 4 (a, b, h, k)
#Test 2: Selecting the back button will result in the back_to_home_page function being called, meaning the home page window will re apear
#Test 3: Selecting the enter button will result in another function being called, depending on the mode, and it in the end graphs the users input
  # Quadratic - quadratic_entry_button
  # Cubic - cubic_entry_button
  # Quartic - quartic_entry_button
  # Sin - sin_entry_button
  # Cos - cos_entry_button
  # Tan - tan_entry_button
  # Log - log_entry_button
#Test 3: Inputting inproper values (such as non numbers) cann result in an error message popping up

#Example:
#Inputs that would allow the program to create a graph (random examples)
#Quadratic - 1, 2, 3 -- 5, 20, 4 -- 5, 5, -2 -- 0, 2, 1 
#Log, sin, cos, tan, cubic - 1, 2, 3, 4 -- 0.5, 2, 3, 5 -- 0, 4, 0, 6
#Quartic - 1, 2, 3, 4, 5 -- 0, 0, 0, 0, 0 --, -15, 0.5, 18, 0, 2

#Inputs that would ultimately result in the error message (an error would be caused regardless of which graphing section you input this into):
#hi
#13f
#1/2
#yolo
#sweet_apples
#arrrr
#im so tired
#and overall anything that isn't actually a numeric value (negatives and decimals work)



####################### COLLECTING INFO FUNCTIONS #######################
#Most collecting info functions in this program are essentially expected to store the float version of the users input in a variable, and also uses a try and except to catch any errors. If the users input for any reason had any errors, it causes an error label

#Different modes use different collecting info functions. Quadratic, with three textboxes, uses collecting_info, ones with four use once_again_collecting_info, and so on

#Exmaple:
#strings 1, 2 and 3 would end up being floats and stored in variables a, b and c
#strings 5, 6, -7, 0 would end up being floats and stored in variables a, b, c and d
#strings like hi, sweet_apples, 1/2, etc, could not be turned to floats and therefore the except will catch the error and display the error message

####################### ENTRY FUNCTIONS #######################
#Test 1: Entry functions (ex. cubic_entry_button) either result in the users info ulltiamtely being graphed using the appropraite function Justin made (ex. quadratic_entry_button uses the quadgraph function ONLY), OR if the entry function encountered an error with using the collecting info functions to convert the users info to floats stored in variables, the display error will be displayed on the window

#Test 2: Every graph has a mini back button at the bottom, and when clicked the back button should return the user to the previous window (ex. if the user is looking at a cubic graph, it means they were previously on the cubic info entry window, so they will be returned there)

#Technically this function is what actually calls the collecting info function, therefore if the inputs are valid the output is a matplotlib graph, but otherwise the collecting info function displays the error message. Examples of acceptable/invalid inputs are shown above.

####################### CLOSE BACK BUTTON FUNCTION #######################
# CANNOT BE TESTED WITH SPECIFIC EXAMPLES
#Test 1: Should be called when the user selects the back button of a graph
#Test 2: Makes the graph and back button dissapear so the user can actually see the previous window again


################################################################################################################################################################################
#POLYGONS
################################################################################################################################################################################

####################### POLYGON OPTON PAGE FUNCTION #######################
# CANNOT BE TESTED WITH SPECIFIC EXAMPLES
#Test 1: Running this function should result in a window with 6 shape buttons of different polygons and a back button. This function is the command of the polygon button on the home page

#Test 2: Depending on the button selected, a different function will be executed
  #square - square_polygon
  #triangle - triangle_polygon
  #rectangle - rectannglge_polygon
  #octagonn - octagon_polygon
  #hexagon - hexagon_polygon
  #parallelogram - parallelogram_polygon

#Test 3: Clicking back button takes user back to home page

####################### BOXES FOR COORDS FUNCTION #######################
#Test 1: When this function is called, a window is created and depending on the shape the user selected (and the number of points/sides the shape has), a certain number of textboxes will be created

#Test 2: This function is usually called in the (shape_name)_polygon functions (shown above)

#Test 3: It has an enter button that calls the obtaining_info_for_coords function, which simply redirects to another function depending on the selected shape (tested later), and to sum things up it either prints the perim and area OR if inputs are invalid displays an error message

#Test 4: Clicking back button returns user to home page

#Test 5 (aka examples): Depending selected shape, there should be blank number of textboxes:
  #square - 4
  #triangle - 3
  #rectangle - 4
  #octagon - 8
  #hexagon - 6
  #parallelogram - 4

#EXAMPLES OF APPROVABLE INPUT:
#(1,2)
#(-2,3)
#(-2,-2)
#(6,-7)
#(0,1)
#(10,0)
#(0,0)

#ANYTHING NOT FORMATTED LIKE THAT COULD POTENTIALLY RESULT IN AN ERROR MESSAGE.
#ERROR EXAMPLES INCLUDE:
#hi
#sweet_apples
#3,4
#132
#-34
#00
#(3,
#etc




####################### OBTAINING INFO FOR POLYGON FUNCTION #######################
# CANNOT BE TESTED WITH SPECIFIC EXAMPLES

#Test 1: Regardless of which shape chosen, this functon essentially redirects to another code that results in the perimeter and area being printed. Depending on which shape is selected, it should redirect to a specific function to calculate the area and perimeter. Each shape causes the function to redirect to the blank function:
  #square - obtaining_info_for_square
  #triangle - obtaining_info_for_triangle
  #rectangle - obtaining_info_for_rectangle
  #octagon - obtaining_info_for_octagon
  #hexagon - obtaining_info_for_hexagon
  #parallelogram - obtaining_info_for_parallelogram

####################### OBTAINING INFO FOR _________ FUNCTIONS #######################
#Test 1: This function should print the area and perimeter to the console
#Test 2: If the user inputted incorect input (like words) an error mesasge will be displayed in the output

# All my function does it supply the valid input to Ellie's functions. Examples of valid input can be seen in her section

####################### _________ _ polygon FUNCTIONS #######################
#Test 1: The x coordinate of the blank (shape name) polygon functions should always be equal to the number of sides the shape has
#Test 2: The shape variable should always be assigned the name of the shape the user selected
#Test 3: The function should always result in the boxes_for_coords window being created

#Examples:
#square - 4, shape
#triangle - 3, triangle
#hexagon - 6, hexagon

####################### RANDOM DATA SET FUNCTION #######################
#Will always result in a new window with 3 textboxes for amount of numbers, lowest number and highest number
#This function is called (the window is created) when the user clicks the random data set button in the home page
#The back button takes the user back to the home bage
#The enter button prints the random data set to the console, OR will display an error message if the user inputted incorrect information

#valid and invalid input can be shown below, as well as examples of the random data set

####################### PRINT RAND DATA SET FUNCTION #######################
#using users input that has been converted to an integer, it prints the random data set to the console, OR will display an error message if the user inputted incorrect information

#Good examples:
#7, 1, 1 - [1, 1, 1, 1, 1, 1, 1]
#5, 3, 9 - [7, 8, 4, 6, 8]

# improper input - sweet_apples, yolo, entering values that don't make sense (such as the highest number being less than the lowest number)

####################### ACTUAL QUADRATIC CALCULATOR FUNCTION #######################
#Will always result in a new window with 2 textboxes for A and B values
#This function is called (the window is created) when the user clicks the quadratic calculator button in the home page
#The back button takes the user back to the home bage
#The enter button results in another function being called that prints the roots to the console or displays an error message if the input is invalid

####################### QUADRATIC CALCULATOR ENTRY BUTTON FUNCTION #######################
#Either prints roots (or whatever else the quadratic calculator function returns) or displays error message for invalid input

#successful examples can be found in maryams section
#improper examples is once again stuff like hi, sweet_apples, other non numeric values

####################### LCM, GCF WINDOW FUNCTION #######################
# Will always result in a new window with 3 buttons for lcm, gcf and back button
#This function is called (the window is created) when the user clicks the lcm and gcf button in the home page
#The back button takes the user back to the home bage
#LCM button redirects user to another window for user to input their numbers that they are trying to find the lcm of 
#GCF button redirects user to another window for user to input their numbers that they are trying to find the gcf of 

####################### LCM WINDOW FUNCTION #######################
#New window with two textboxes for user to enter info in
#Back button to return to home pages
#Enter button calls another function that obtains info from textbox and prints lcm to console OR displays error message


####################### GCF WINDOW FUNCTION #######################
#New window with two textboxes for user to enter info in
#Back button to return to home pages
#Enter button calls another function that obtains info from textbox and prints gcf to console OR displays error message

####################### lcm results and gcf results function #######################
# LCM window enter button calls lcm results, which gathers the users info and uses my peers LCM function and prints to the console or displays error message if user inputted invalid info 

# GCF window enter button calls gcf results, which gathers the users info and uses my peers GCF function and prints to the console or displays error message if user inputted invalid info 

#valid input - any numeric values (1, 2, 3, 4, 900, etc)
#invalid - non numeric values, or any input that in general contains characters that cannot be apart of a float (six, q434, etc)
#evidently actual tests are found in my group members testing section

####################### SIMULATIONS #######################
#Will always result in a new window with 3 buttons (coin, dice and back)
#This function is called (the window is created) when the user clicks the simulations button in the home page
#Coin button runs maryams coin function that displays a mini window with the coin simulation
#dice button runs maryams coin function that displays a mini window with the dice simulation





