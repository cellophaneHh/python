from lxml import etree

with open("./1559971901.5445068.html", 'r') as file:
    html_soruce = file.read()

parser = etree.HTML(html_soruce)
