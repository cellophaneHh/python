customers = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for customer in customers:
    print("Hello," + customer)

print("=====================")
old_customer = 'b'
new_customer = 'h'

customers.remove(old_customer)
customers.append(new_customer)
for customer in customers:
    print("Hello," + customer)

print("a big desktop..")
customers.insert(0, 'i')
customers.insert(3, 'j')
customers.append('k')
for customer in customers:
    print("Hello," + customer)

print("oh.....")
old_customer = customers.pop();
old_customer = customers.pop();
old_customer = customers.pop();
old_customer = customers.pop();
old_customer = customers.pop();
old_customer = customers.pop();
old_customer = customers.pop();
old_customer = customers.pop();
for customer in customers:
    print(customer)

del customers[0]
del customers[0]
print(customers)


