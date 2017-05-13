import os
from flask import Flask, render_template, request, url_for, redirect
from flask_uploads import UploadSet, configure_uploads, IMAGES
from ml import image_accuracy
import food
import exercise 

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	# Saves photo from user upload
    if request.method == 'POST' and 'photo' in request.files:
    	if request.files['photo'].filename == '':
    		return render_template('index.html')
    	else:
        	photos.save(request.files['photo'])

    # Creates image path from user image    
	picture = "static/img/" + str(request.files['photo'])[16:-17]
	# Item name and score percentage
	item, score = image_accuracy(picture)
	cal = food.food[item]['Calories']
	
	# remove underscore and Makes all first char of every word to upper
	name = item.replace('_',' ').title()
	
	# Accesses all nutrient info from database
	sodium = food.food[item]['Sodium']
	carbs = food.food[item]['Carbohydrates']
	sugar = food.food[item]['Total Sugar']
	protein = food.food[item]['Protein']
	fat = food.food[item]['Total Fat']
	s_fat = food.food[item]['Saturated Fat']
	t_fat = food.food[item]['Trans Fat']
	chol = food.food[item]['Cholesterol']
	
	runningCal = exercise.time2Burn(cal, "running")
	swimmingCal = exercise.time2Burn(cal, "swimming")
	bikingCal = exercise.time2Burn(cal, "biking")
	
	#returns if item accuracy percent is above 90
	if score > .9:
		return render_template("food.html", item=item, cal=cal, name=name, sodium=sodium, 
    							carbs=carbs, sugar=sugar, protein=protein, fat=fat, 
    							s_fat=s_fat, t_fat=t_fat, chol=chol, picture=picture, runningCal=runningCal,swimmingCal=swimmingCal, bikingCal=bikingCal)
    return render_template("item_not_found.html")
    							
    							
@app.route('/')
def login():
	return render_template('index.html')

@app.route('/about')	
def about():
	return render_template('about.html')
	
@app.route('/picture')
def pictue():
	return render_template('picture.html')
	
if __name__ == '__main__':
    app.run(
        debug=True,
        port = int(os.getenv('PORT', 8080)),
        host = os.getenv('IP', '0.0.0.0')
    )
