# Counter() in python

from collections import Counter

breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)

print(breakfast_counter)
#---
b1 = breakfast_counter.most_common()
b2 = breakfast_counter.most_common(1)
print(b1,"\n",b2)
#---
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print("-------------------------")
combine = breakfast_counter + lunch_counter

difference_breakfast = breakfast_counter - lunch_counter

difference_lunch = lunch_counter - breakfast_counter

intersection = lunch_counter & breakfast_counter

union = lunch_counter | breakfast_counter

total = [combine, difference_breakfast, difference_lunch, intersection, union]

a=0
for x in total:
    if a==0:
        print("breakfast_counter + lunch_counter: ",x) 
    elif a==1:
        print("breakfast_counter - lunch_counter: ",x)
    elif a==2:
        print("lunch_counter - breakfast_counter: ",x)
    elif a==3:
        print("lunch_counter & breakfast_counter: ",x)
    elif a==4:
        print("lunch_counter | breakfast_counter: ",x)
    a+=1

