def city_country(city, country, population=''):
    """返回格式化的国家城市名"""
    formatted_info = city + ", " + country + " - population " + str(population)
    return formatted_info.title()


