"""
This function calcuates the amount of time it takes to burn a specified amount of calories. 
It takes in two arguments, which are calories and excercise. The calorie parameter is the 
amount of calories you want to calculate the time for. The excercise parameter determines 
the time it takes to burn X amount of calories according to the intesity of the excercise. 
The intesity of an excercise is measured by an MET score given to each excercise, this 
score is then plugged in to an equation which calculates the amount of calories you would
per minute based on weight and the MET score of the excercise. Then we divide the calories 
from the food by the calories burnt per minute and that gives us the time it would take to 
burn those calories from that food.

Resource:
https://www.hss.edu/conditions_burning-calories-with-exercise-calculating-estimated-energy-expenditure.asp
"""

def time2Burn(calFromFood, excercise):
    //Checks whether excercise is biking/swimming/running
    if excercise == "biking":
        MET = 4.0
        
    elif excercise == "swimming":
        MET = 6.0
       
    elif excercise == "running":
        MET = 8.0

    //Calculates the calories burned per minute
    energyExpenditure = .0175 * MET * 64.5
    
    //Calculates the time to burn the calories from food
    time = int(calFromFood) / energyExpenditure
    
    //rounds the time that was calculated
    roundTime = time - int(time)
    
    if roundTime > .49:
        roundTime = 1 - roundTime
        time += roundTime
        
    else:
    	time -= roundTime
    
    return time
