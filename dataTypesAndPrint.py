# ~ ~ ~ Data's type & print function ~ ~ ~ #

"""
lesson Tools:
type(a) = the type fuction return the data type of a,
print(a) = print(a) to the console
"""

# Primitives
a = 15    # integer or int for sort a whole number
b = "a"   # str/char -!!! in python we called str or string type is a single character or a string of charicters
c = 15.4  # float a decimal point number
d = True  # boolean or bool for short is a binary type being either one for true or zero for false

#print function
""" print is the most common function in python
    we can use it if we want to print output from our program to the console bellow
    we can print numbers types or string values -- > if we want to print a string use """

print("~~~~~~~~~~~~~~~~~~~")
print(a, b, c, d)
print("~~~~~~~~~~~~~~~~~~~")
print(type(a), type(b), type(c), type(d))

for i in range(3):
   print("~~~~~~~~~~~~~~~~~~~")

# for several lines use 3 """ at the start & at the end
print("""
 __      __       .__  .__                             __                          
/  \    /  \ ____ |  | |  |   ____  ____   _____     _/  |_  ____                  
\   \/\/   // __ \|  | |  | _/ ___\/  _ \ /     \    \   __\/  _ \                 
 \        /\  ___/|  |_|  |_\  \__(  <_> )  Y Y  \    |  | (  <_> )                
  \__/\  /  \___  >____/____/\___  >____/|__|_|  /    |__|  \____/                 
       \/       \/               \/            \/                                  
__________          __  .__                             .__                        
\______   \___.__._/  |_|  |__   ____   ____       ____ |  | _____    ______ ______
 |     ___<   |  |\   __\  |  \ /  _ \ /    \    _/ ___\|  | \__  \  /  ___//  ___/
 |    |    \___  | |  | |   Y  (  <_> )   |  \   \  \___|  |__/ __ \_\___ \ \___ \ 
 |____|    / ____| |__| |___|  /\____/|___|  /    \___  >____(____  /____  >____  >
           \/                \/            \/         \/          \/     \/     \/ 


""")

