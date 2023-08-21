
people = [
    {"name" : "kittunni", "address" : "payyanur"},
    {"name" : "kothandan", "address" : "kannur"},
    {"name" : "kindanan", "address"  : "kochi"},
    {"name" : "Ittunnan", "address"  : "kottyam"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print (people)