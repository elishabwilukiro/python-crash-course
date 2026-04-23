def day_of_week(day):

     day = int(input("Enter value of x: "))

     if day==1:
          return "It's Sunday"
     elif day==2:
          return "It's Monday"
     elif day==3:
          return "It's Tuesday"
     elif day==4:
          return "It's Wednesday"
     elif day==5:
          return "It's Thursday"
     elif day ==6:
          return "It's Friday"
     else:
          return "Not a valid date"
     
print(day_of_week(2))

