motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#update
motorcycles[0] = 'ducati'
print(motorcycles)

#add
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

#delete
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#pop从末尾删除
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#默认的pop()函数会把list当做stack使用，后进先出，因此弹出的是末尾元素
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
first_owned = motorcycles.pop(0)
print(first_owned.title())

#不知道索引删除某个值，remove
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

