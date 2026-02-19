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

import json  # lets us read JSON files

infile = open('school_data.json', 'r')  # open the file
schools = json.load(infile)  # load JSON into a Python list
infile.close()  # close the file

conference_schools = [372, 108, 107, 130]  # AAC, Big 12, Big Ten, SEC (based on your prompt)

print("\nSchools in ACC, Big 12, Big Ten, and SEC:\n")  # heading (your prompt wording)

for school in schools:  # loop through each school

    if "NCAA" in school:  # make sure NCAA section exists
        if "NAIA conference number football (IC2020)" in school["NCAA"]:  # make sure the key exists inside NCAA

            conference = school["NCAA"]["NAIA conference number football (IC2020)"]  # get the conference number

            if conference in conference_schools:  # check if it matches one of the conference numbers we want
                print("University:", school["instnm"])  # print the school name
                print()  # blank line


print("\nschools with Women's graduation rate over 75%:\n")  # heading

for school in schools:  # loop through each school

    if "Graduation rate  women (DRVGR2020)" in school:  # check if the key exists (note: two spaces)
        graduation_rate_women = school["Graduation rate  women (DRVGR2020)"]  # get the value

        if graduation_rate_women is not None:  # skip null values
            if graduation_rate_women > 75:  # check if over 75

                print("University:", school["instnm"])  # matches screenshot label
                print("Graduation Rate for Women:", graduation_rate_women, "%")  # matches screenshot label + %
                print()  # blank line


print("\nschools with total price for in-state students living off campus over $60,000:\n")  # heading

for school in schools:  # loop through each school

    key_name = "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"  # exact key from your JSON

    if key_name in school:  # check if the key exists
        total_price = school[key_name]  # get the value

        if total_price is not None:  # skip null values
            if total_price > 60000:  # check if over 60,000

                print("University:", school["instnm"])  # matches screenshot label
                print("Total price for in-state students living off campus: $"
                      + format(total_price, ",.2f"))  # formats like $66,750.00
                print()  # blank line

