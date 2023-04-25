# setdefault() & defaultdict()

periodic_table = { 'Hydrogen' : 1, 'Helium' : 2}

#k=periodic_table.keys()
#k=periodic_table.values()

carbon = periodic_table.setdefault('Carbon', 12)

print(periodic_table)

print(periodic_table.get("Carbon")) # reasch The "Carbon"'s value.
#------------------------------------------------------------------

from collections import defaultdict

# if used the int(), list(), dict() , return value is 0, [], {} or None
periodic_table=defaultdict(int)
periodic_table["Hydrogen"] = 10
periodic_table["Lead"]
print(periodic_table)

#For next example:
def no_idea():
    return "Huh!"

bestiary = defaultdict(no_idea)
bestiary['a']=100
bestiary['b']="Basilisk"
bestiary['c']

print(bestiary)

#For next example of the Counter:

food_counter = defaultdict(int)
lits=['spam', 'spam','eggs','vegerable']
for food in lits:
    food_counter[food] +=1

for food, count in food_counter.items():
    print(food, count)

#if dict:
dict_counter={}
for food in lits:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1

for food, count in dict_counter.items():
    print(food, count)