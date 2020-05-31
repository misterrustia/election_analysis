#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for counties,voters  in counties_dict.items():
   # print(f'{counties} has {voters} registered voters' )

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]

for counties in voting_data:
    for county, voters  in counties.items():
        print("#1: ",county, voters )

# for all the dictionarys in the list
for counties_dic in voting_data:

# get the values from each key value pair - actually doesnt work - double loop writes first value twice
    for values in counties_dic.values():
        print(f'{values} has {values} registered voters')

#below is close but no f value

for counties_dic in voting_data:
    # didnt workt with fprint(f'{counties_dic['county']} "has" {counties_dic['registered_voters']} "registered voters"')
   # nope print(f'{(counties_dic['county'])} "has" {(counties_dic['registered_voters'])} "registered voters"')
   
   # final one works ish 
   # call key1 for value 1 then key 2 for value two in each dictionary- no nested loop
   print(counties_dic['county'], "has",counties_dic['registered_voters'] ,"registered voters")

  # When do you need to nest a second loop when using dictionarys in list?
  