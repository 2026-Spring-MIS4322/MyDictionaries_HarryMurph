person = {}#creating dictionary
person["fname"] = "Joe"#appending to the dictionary
person["lname"] = "Fonebone"#appending to the dict
person["age"] = 51
person["spouse"] = "Edna"#still appending
person["children"] = ["Ralph", "Betty", "Joey"]#the key is children and the value is a list of the names of the children 
person["pets"] = {"dog": "Fido", "cat": "Sox"}#dictionary within a dictionary, the key is pets and the value is another dictionary with the type of pet as the key and the name of the pet as the value.

print(person)

# print out the name of the second child
list_of_children = person['children']
print(list_of_children[1])
#it is prefered to use without using a variable 

# print out the name of the cat
dict_of_pets = person['pets']
print(dict_of_pets['cat'])
#without using a variable
print(person['pets']['cat'])

# use a loop to print out the names of each child
for child in person['children']:
    print(child)



# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for pet, name in person['pets'].items():#this is a tuple
    print(f"the type of pet is: {pet} and the name of the pet is:{name}")
