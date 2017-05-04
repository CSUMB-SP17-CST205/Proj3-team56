import os
from flask import Flask, render_template, request, url_for, redirect
from flask_uploads import UploadSet, configure_uploads, IMAGES
from ml import image_accuracy
import food


app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route('/upload', methods=['GET', 'POST'])
@app.route('/upload/<item>')
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        photos.save(request.files['photo'])
	picture = "static/img/" + str(request.files['photo'])[16:-17]
	item = image_accuracy(picture)
	cal = str(food.food[item]['Calories'])
	name = item.replace('_',' ').title()
	sodium = food.food[item]['Sodium']
	carbs = food.food[item]['Carbohydrates']
	sugar = food.food[item]['Total Sugar']
	protein = food.food[item]['Protein']
	fat = food.food[item]['Total Fat']
	s_fat = food.food[item]['Saturated Fat']
	t_fat = food.food[item]['Trans Fat']
	chol = food.food[item]['Cholesterol']
    return render_template("food.html", item=item, cal=cal, name=name, sodium=sodium, 
    						carbs=carbs, sugar=sugar, protein=protein, fat=fat, 
    						s_fat=s_fat, t_fat=t_fat, chol=chol, picture=picture)
@app.route('/')
def login():
	return render_template('index.html')
	

if __name__ == '__main__':
    app.run(
        debug=True,
        port = int(os.getenv('PORT', 8080)),
        host = os.getenv('IP', '0.0.0.0')
    )
