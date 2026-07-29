students = [
    {"name": "harmioner" , "house" : "gryfflinder" , "patronus" : "otter" },
    {"name": "harry" , "house" : "gryfflinder" , "patronus" : "stag" },
    {"name": "row" , "house" : "gryfflinder" , "patronus" : "jack russell terrier" },
    {"name": "draco" , "house" : "slythrim" , "patronus" : None },
]
for student in students:
    print(student["name"], student["house"], student["patronus"],sep=" , ")