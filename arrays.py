
courses = ["MIT","Cybersecurity","Datascience"]
print(courses)

#Accessing an element
print(courses[2])


#Looping through an array
for a in courses:
    print("Course is",a)

    #Adding a new element into an array
    courses.append("Laravel")
    print(courses)

    #Deleting an element from an array
    courses.remove("Cybersecurity")
    print(courses)