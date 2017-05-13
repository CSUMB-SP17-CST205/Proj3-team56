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