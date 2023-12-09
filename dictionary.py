students = {
    "s1": {"name":'Abhishek', '''surname''':"Bairagi", "address":'Ratlam'},
    '''s2''': {"name":'Pawan', '''surname''':"Pawar", "address":'Mandsaur'},
    's3': {"name":'Rajeev', '''surname''':"Singh", "address":'Jeeran'},
    
}

for student in students:
    print(f'{students[student]["name"]} {students[student]["surname"]} From  {students[student]["address"]} ')