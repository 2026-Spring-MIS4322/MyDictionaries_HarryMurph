import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}


'''
print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)

print(len(phonebook))
mydictionary = dict(m=8, n=9)

print(mydictionary) #in a dictionary keys will always be a string. 

print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name= 'Chris'
if name in phonebook:     #the default for dictionaries is the key
    phone = phonebook[name]
    print(phone)
else:
    print(f"No phone number for {name}")

phone = phonebook['Chris']

print(phone)


print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Joe'] = '555-0123'#this will append to the phonebook dictionary 
phonebook['Chris'] = '555-4444'#this will update the value of the key 'Chris'
print(phonebook) #you cannot edit the key of a dictionary, you can only edit the value.



print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()
print(phonebook)
del phonebook['Chris']
print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:
    print(f"The key of the dictionary is {key}")
    print(f"The value of the key is {phonebook[key]}")

for v in phonebook.values():
    print(f"phone number: {v}")

for item in phonebook.items():
    print(item)

for k,v in phonebook.items():
    print(f"The key of the dictionary is {key}")
    print(f"The value of the key is {phonebook[key]}")

print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get('Chris',911)
print(phone)

print(phonebook)
phonebook.clear()
print(phonebook)



print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()


phone = phonebook.pop('Chris')
print(phone)
print(phonebook)



print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()


item = phonebook.popitem()
print(item)
print(phonebook)


print()
print('*****  end section 8 ********')
print()

'''

print()
print('*****  start section 9 - using random and converting to list ********')
print()


list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)
phone = phonebook[random_key]
print(phone)

print(phonebook[random.choice(list(phonebook))]) #this is a more concise way to do the same thing as above. 


print()
print('*****  end section 9 ********')
print()








