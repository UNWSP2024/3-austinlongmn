# Programmer: Austin Long
# Date: 2/4/2025
# Shipping Charge Calculator
# Programming Excersize 3-13

# The Fast Freight Shipping Company charges the following rates:

# Weight    	Price Per Pound
# 2 pounds or less   	$1.50
# Over 2 pounds but not more than 6 pounds  	$3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	$4.75
# Write a program which calculates the shipping charge and displays the total.

def weight_conversion(weight):
    # Calculate the shipping charge.
    shippingCost = 0.0
    ######################
    # WRITE YOUR CODE HERE
    ######################

    # Determine price per pound based on the weight
    if weight <= 2.0:
        shippingCost = 1.5
    elif weight <= 6.0:
        shippingCost = 3.0
    elif weight <= 10:
        shippingCost = 4.0
    else:
        shippingCost = 4.75

    # Return price per pound to caller
    return shippingCost

#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))