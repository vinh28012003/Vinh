class_info= [
    {
        "name": "Nam Khanh",
        "age": 16,
        "sex": "Male"
    },
    {
        "name": "Long",
        "age": 15,
        "sex": "Male"
    },
    {
        "name": "Linh",
        "age": 17,
        "sex": "Female"
    },        
]

for i in class_info:
    if "Female" in i["sex"]:
        print(i)
