# Author: IBN (AMDG) 1/26/2022

print('Enter the net sales for')

previous = float(input('- Prior period:'))
current = float(input('- Current period:'))

change = (current - previous) * 100 / previous

try:
    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'
except:
    result = "Please check your inputs"
finally:
    print("Thank you for using the program!")
