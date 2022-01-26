# Author: IBN (AMDG) 1/13/2022

try:
    temp = float(input("Input a temperature. "))
    scale = input("Input the temperature's scale. ")
    if scale == "F":
        fahrenheit = (temp - 32) * (5/9)
        print(fahrenheit)
    elif scale == "C":
        celcius = (temp * (9/5)) + 32
        print(celcius)
    else:
        print("Please enter either F or C.")
except ValueError:
    print("Please enter a valid number.")
finally:
    print("Try another conversion!")