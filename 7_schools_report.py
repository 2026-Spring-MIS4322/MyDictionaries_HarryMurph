"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $60,000



"""

import json

# Helper function to safely convert values to numbers
def to_number(value):#safely convert a value to a number, returning None if the conversion fails
    if value is None:
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


# Load the JSON file
with open('school_data.json', 'r') as infile:
    schools = json.load(infile)


conference_schools = [372, 108, 107, 130]  # ACC, Big 12, Big Ten, SEC


print("Schools in ACC, Big 12, Big Ten, and SEC:\n")

found_conference = False#flag to track if any schools matched the conference criteria
for school in schools:#iterate through the list of schools
    ncaa = school.get('NCAA')#get the 'NCAA' key from the school dictionary, which is itself a dictionary containing various NCAA-related data
    if isinstance(ncaa, dict):#check if the 'NCAA' key is a dictionary (to avoid errors if it's missing or not in the expected format)
        conf = to_number(ncaa.get('NAIA conference number football (IC2020)'))#get the 'NAIA conference number football (IC2020)' key from the 'NCAA' dictionary and convert it to a number using the to_number helper function
        if conf is not None and int(conf) in conference_schools:#check if the conference number is not None and is in the list of conference schools
            print(school.get('instnm'))#print the name of the school (the 'instnm' key from the school dictionary)
            found_conference = True#set the flag to True if a school matched the conference criteria

if not found_conference:
    print("⚠️ No schools matched the conference criteria.")


print("\nSchools with Women's graduation rate over 75%:\n")

found_grad = False#flag to track if any schools matched the graduation rate criteria
for school in schools:
    grad = to_number(school.get('Graduation rate  women (DRVGR2020)'))
    if grad is not None and grad > 75:
        print(f"{school.get('instnm')} — {grad}%")
        found_grad = True

if not found_grad:
    print("⚠️ No schools matched the graduation rate criteria.")


print("\nSchools with total price for in-state students living off campus over $60,000:\n")#flag to track if any schools matched the cost criteria

found_cost = False#flag to track if any schools matched the cost criteria
for school in schools:
    cost = to_number(
        school.get(
            'Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'
        )
    )
    if cost is not None and cost > 60000:
        print(f"{school.get('instnm')} — ${cost:,.0f}")
        found_cost = True

if not found_cost:
    print("⚠️ No schools matched the cost criteria.")
