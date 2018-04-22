my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append("a")
friend_foods.append("b")

for mf in my_foods:
    print(mf)

print("==============")
for ff in friend_foods:
    print(ff)
