
import csv
import datetime

#open guns.csv file and make each row into a list
with open('guns.csv') as infile:
    guns_reader = csv.reader(infile)
    data = list(guns_reader)
    header = data[0]
    data = data[1:]
#open census.csv and make each row into a list    

with open('census.csv') as infile2:
    census_reader = csv.reader(infile2)
    census = list(census_reader)
#print(census)

#looking at Homicide incidents

intents = [row[3] for row in data ]
races = [row[7] for row in data ]

homicide_race_counts = {}
suicide_race_counts = {}
for i,race in enumerate(races):
    if intents[i] == 'Homicide':
        if race not in homicide_race_counts:
            homicide_race_counts[race] = 1
        else:
            homicide_race_counts[race] += 1
    elif intents[i] == 'Suicide':
        if race not in suicide_race_counts:
            suicide_race_counts[race] = 1
        else:
            suicide_race_counts[race] += 1
print(suicide_race_counts)

#print(homicide_race_counts)
    

#counting sex and race
sex_counts = {}
race_counts = {}
for row in data:
   
    if row[5] not in sex_counts:
        sex_counts[row[5]] = 1
    elif row[5] in sex_counts:
        sex_counts[row[5]] += 1
    if row[7] not in race_counts:
        race_counts[row[7]] = 1
    elif row[7] in race_counts:
        race_counts[row[7]] += 1

#print(sex_counts)
#print(race_counts)

#getting rate per 100,000
mapping = {'Native American/Native Alaskan':3739506,'Black':40250635,
           'White':197318956,'Hispanic':44618105,
           'Asian/Pacific Islander':15834141
              }
race_per_hundredk = {}
for race in race_counts:
    race_per_hundredk[race] = (race_counts[race]/mapping[race])* 100000
    homicide_race_counts[race] = (homicide_race_counts[race]/mapping[race])*100000
    suicide_race_counts[race] = (suicide_race_counts[race]/mapping[race])* 100000

#print(homicide_race_counts)
#print(race_per_hundredk)
print(suicide_race_counts)
    
    
    


# most victims are men(85.6%). Once we look at it per 100,000 deaths, we see
# that African-Americans are effected more by gun deaths
# African-American are also effect more by homicide (gun violence). 48 per 100,000 African-American are
# victims of gun violence (homicide). African-Americans have the highest rate.
#28 out of every 100,000 White Americans commit suicide via gun. White Americans have the highest rate.
