#The complexity of this program is O(log n )

program_stays_on = "empty"
print("Welcome to a program that lets you convert base-10 numbers to base-8 or base-2")

while program_stays_on != "q": # Loop keeps the program on. Press x in the upper right console corner to exit.

    base2_or_base8 = input("Press k if you want binary and press l if you want octal number: ")
    divider = 0
    if base2_or_base8 == "k": #User decides does she/he want to convert base-10 number to base-2 or base-8
        divider = 2
    else:
        divider = 8

    base10_number = int(input("Input positive base-10 integer: ")) 

    if base10_number <= 0: #this if statement checks that was the users number a positive integer
        print(base10_number,"was not a positive integer!")
        base10_number = int(input("input positive integer: "))

    remainder = 0
    converter_number = [] #list where the converted base-2/base-8 number goes
    index = 0 

    while base10_number != 0:   #Loop that converts the base-10 number to base-2 or base-8 
         remainder = base10_number % divider
         converter_number.append(remainder)
         base10_number = base10_number // divider

    converter_number.reverse() #Reverses list, because the loop places the numbers in reversed order
    if base2_or_base8 == "k": #prints the base-2/base-8 number
        print("In Binary: ",converter_number,)
    else:
        print("In octal: ",converter_number,)
    print("")