#food = {
bkMedFry = {'Calories': 380, 'Sodium': '570 mg', 'Carbohydrates':'53 g', 'Total Sugar':'0 g', 'Protein':'5 g', 'Total Fat':'150 g', 'Saturated Fat': '3 g', 'Trans Fat': '0 g', 'Cholesterol': '0 mg'}
    
bkHtDog = {'Calories': 310, 'Sodium': '960 mg', 'Carbohydrates':'32 g', 'Total Sugar':'10 g', 'Protein':'11 g', 'Total Fat':'16 g', 'Saturated Fat': '6 g', 'Trans Fat': '1 g', 'Cholesterol': '30 mg'}

bkWhopper = {'Calories': 630, 'Sodium': '810 mg', 'Carbohydrates':'49 g', 'Total Sugar':'11 g', 'Protein':'26 g', 'Total Fat':'38 g', 'Saturated Fat': '11 g', 'Trans Fat': '1.5 g', 'Cholesterol': '85 mg'}

inOutDoubDoub = {'Calories': 650, 'Sodium': '1400 mg', 'Carbohydrates':'38 g', 'Total Sugar':'9 g', 'Protein':'35 g', 'Total Fat':'40 g', 'Saturated Fat': '18 g', 'Trans Fat': '1 g', 'Cholesterol': '120 mg'}

inOutFry = {'Calories': 395, 'Sodium': '245 mg', 'Carbohydrates':'54 g', 'Total Sugar':'0 g', 'Protein':'7 g', 'Total Fat':'18 g', 'Saturated Fat': '5 g', 'Trans Fat': '0 g', 'Cholesterol': '0 mg'}
#}
#print info
for i in bkMedFry:
    print (i, bkMedFry[i])

#write info onto file
with open("dictionaries.txt", "w") as dictionaries:
    dictionaries.write(str(bkHtDog))
