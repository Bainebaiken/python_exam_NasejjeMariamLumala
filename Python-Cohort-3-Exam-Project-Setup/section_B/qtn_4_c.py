
import math

def valueOfd():
    
    X1 = int(input('Enter the value of X1:\t')) 
    X2 = int(input('Enter the value of X2:\t'))
    Y1 = float(input('Enter the value of Y1:\t')) 
    Y2 = float(input('Enter the value of Y2:\t')) 

    simplifiedRoute = ((X1-X2) + (Y1-Y2) )
    d = math.sqrt(simplifiedRoute)
    
    print("The value of d is: %.2f " %d + " ")
   
valueOfd()










