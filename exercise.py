"""
This function calcuates the amount of time it takes to burn a specified amount of calories. 
It takes in two arguments, which are the amounts of calories you want to calculate the time for

Resource:
https://www.hss.edu/conditions_burning-calories-with-exercise-calculating-estimated-energy-expenditure.asp
"""

def time2Burn(calFromFood, excercise):
    if excercise == "biking":
        MET = 4.0
        
    elif excercise == "swimming":
        MET = 6.0
       
    elif excercise == "running":
        MET = 8.0

    energyExpenditure = .0175 * MET * 64.5
    
    time = int(calFromFood) / energyExpenditure
    
    roundTime = time - int(time)
    
    if roundTime > .49:
        roundTime = 1 - roundTime
        time += roundTime
        
    else:
    	time -= roundTime
    
    return time
