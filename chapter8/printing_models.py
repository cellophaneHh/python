def print_models(unprinted_designs,completed_models):
    """打印"""
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_complete(completed_models):
    print("\nThe folloowing models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robotpendant', 'dodecaheron']
completed_models = []

#不修改原列表，新建一个就行了
print_models(unprinted_designs[:], completed_models)

#print_models(unprinted_designs[:], completed_models)

print(unprinted_designs)
show_complete(completed_models)





