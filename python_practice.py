

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

    x = 0
while x <= 5:
    print(x)
    x = x + 1

for i in range(len(counties)):
    print(counties[i])

for county in counties:
    print(county)

for num in range(5):
    print("only num :",num)

for num in range(10):
    print("flaot srq :",float(num)**2)

for num in range(10):
    print("float num to the 1/2 :",float(num)**.5)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print("county :",county)

for county in counties_dict.keys():
    print("keys :",county)

for county in counties_dict.values():
    print("values :",county)

for key, values in counties_dict.items():
    print("maybe? ", values, key)

for key, values in counties_dict.items():
    print("getting wierd with it? ",key , values, float(values)*2 )


for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county,"County has", voters,"registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print("Value: ", value)

for county_dict in voting_data:
    for i in county_dict.values():
        print(i)

print("happy") 

print('days')

for county_dict in voting_data:

     print(county_dict['registered_voters'])

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")