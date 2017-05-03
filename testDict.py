

nutritionInfo = ['Calories', 'Sodium', 'Carbohydrates', 'Total Sugar', 'Protein', 'Total Fat', 'Saturated Fat', 'Trans Fat', 'Cholestrol']
bkMedFryInfo = [380, '570mg', '53g', '0g', '5g', '150g', '3g', '0g', '0mg']
bkWhopperInfo = [630, '810mg', '49g', '11g', '26g', '38g' '11g', '1.5g', '85mg']
bkHtDogInfo = [310, '960mg', '32g', '10g', '11g', '16g', '6g', '1g' '30mg']
inOutDoubDoubInfo = [650, '1400mg', '38g', '9g', '35g', '40g', '18g', '1g', '120mg']
inOutFryInfo = [395, '245mg', '54g', '0g', '7g', '18g', '5g', '0g', '0mg']
mcDbigMacInfo = [540, '1040mg', '45g', '9g', '25g', '29g', '10g', '1.5g', '75mg']
mcDdoubleQPwChzInfo = [750, '1280mg', '42', '10g', '48g', '43g', '19g', '3g', '160mg']
mcDchzBurgerInfo = [300, '680mg', '33g', '7g', '15g', '12g', '6g', '1g', '40mg']

for row in zip('bkMedFry', 'bkHtDog', 'bkWhopper', 'inOutDoubDoub', 'inOutFry', 'mcDbigMac', 'mcDdoubleQPwChz', 'mcDchzBurger'):
    print' '.join(row)

'''for row in zip('bkMedFry', 'bkHtDog', 'bkWhopper', 'inOutDoubDoub', 'inOutFry', 'mcDbigMac', 'mcDdoubleQPwChz', 'mcDchzBurger'):
    print' '.join(row)

bkMedFry = {}    
for i in range(len(nutritionInfo)):
    bkMedFry[nutritionInfo[i]] = bkMedFryInfo[i]
print bkMedFry
# print "\n".join(bkMedFry)     //only lists nutritionInfo 



bkWhopper = {}
for i in range(len(bkWhopperInfo)):
    bkWhopper[nutritionInfo[i]] = bkWhopperInfo[i]
    
print bkWhopper

bkHtDog = {}
for i in range(len(bkHtDogInfo)):
    bkHtDog[nutritionInfo[i]] = bkHtDogInfo[i]
print bkHtDog

inOutDoubDoub = {}
for i in range(len(inOutDoubDoubInfo)):
    inOutDoubDoub[nutritionInfo[i]] = inOutDoubDoubInfo[i]
print inOutDoubDoub

inOutFry = {}
for i in range(len(inOutFryInfo)):
    inOutFry[nutritionInfo[i]] = inOutFryInfo[i]
print inOutFry

mcDbigMac = {}
for i in range(len(mcDbigMacInfo)):
    mcDbigMac[nutritionInfo[i]] = mcDbigMacInfo[i]
print mcDbigMac
      
mcDdoubleQPwChz = {}
for i in range(len(mcDdoubleQPwChzInfo)):
    mcDdoubleQPwChz[nutritionInfo[i]] = mcDdoubleQPwChzInfo[i]
print mcDdoubleQPwChz

mcDchzBurger = {}
for i in range(len(mcDchzBurgerInfo)):
    mcDchzBurger[nutritionInfo[i]] = mcDchzBurgerInfo[i]
print mcDchzBurger

'''