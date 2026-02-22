import json
#Some JSON string
x ='''{                        
        "name" : {
            "first name" : "John", 
             "second name" : "Vadic"
        }, 
       "age": 30 
}'''
new_json = json.loads(x)            #Formating to Python object

# back2 = json.dumps(new_json, indent=2, separators=(". ", " = "), sort_keys=True) #Formating PY -> JSON

with open('my.json', 'w') as file:
    json.dump(new_json, file, indent=2)
