def make_car(maker, type_car, **otherInfo):
    car_info = {}
    car_info['maker'] = maker
    car_info['type_car'] = type_car
    for key in otherInfo.keys():
        car_info[key] = otherInfo.get(key)
    return car_info

print(make_car('1', '2', s=2))
