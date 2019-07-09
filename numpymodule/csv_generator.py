import random

with open("./data.csv", 'w+') as file:
    for linenumber in range(10001):
        a = ''
        for i in range(5):
            a += ",{}".format(random.randint(0, 10001))
        file.writelines(a[1:] + "\n")
print('finished...')
