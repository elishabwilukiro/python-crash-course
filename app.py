# == DataType
# int(x),
# float(x),
# bool(x),
# str(x)

# x = input("x: ")
# y = int(x) + 2
# print(f"x:{x}, y:{y}")
# print(type(x), type(y))

# age = 20
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

# === Operator
# (and, or, not)
high_income = False
good_credit = True
student = True

if (high_income or good_credit) and not student:
     print("Eligible")
else:
     print("Not eligible")