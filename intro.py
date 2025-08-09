first = "Elisha"
last = "Bwilukiro"
full1 = first + last
full2 = F"{first} + {last}"
print(full1)
print(full2)

print("\nString Method")
print("----")
course = "  Python programming"
print(course)
print(course.lower())
print(course.upper())
print(course.title())
print(course.rstrip())
print(course.replace("Python","Java"))
print("pro" in course)
print("swift" not in course)

print("\nConditional Statement")
print("----")
temperature = 15
if(temperature > 30):
     print("It's warm")
print("Drink water now")
print("Done")
