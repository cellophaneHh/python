count = 0
count_allow = 0
count_not_allow = 0

time_str = []
for i in range(20, 30):
    time_str.append('22:49:{}'.format(i))

with open('log/rate_limit.log') as f:
    for line in f.readlines():
        for time_s in time_str:
            if time_s in line:
                count += 1
                if 'INFO' in line:
                    count_allow += 1
                if 'WARNING' in line:
                    count_not_allow += 1

print(count)
print(count_allow)
print(count_not_allow)
