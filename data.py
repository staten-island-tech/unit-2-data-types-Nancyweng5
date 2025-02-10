
""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6]) """

"test"
["t","e","s","t"]

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """





""" day_of_week = input("what day is it?")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")
 """

""" x = "test"
print(f"hello {x}")

temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" number = 10
if number % 2 == 0:
    print ("even")
else:
    print ("odd") """

service = ("ok")
bill = 100

def calculate_tip(bill, service):
    if service == ("bad") :
        tip_percentage = 0
    elif service == ("ok") : 
        tip_percentage = 0.15
    elif service == ("good") :
        tip_percentage = 0.2
    elif service == ("great") :
        tip_percentage = 0.25
    else : 
        return  ("Invalid service level. Please choose from 'bad', 'okay', 'good', or 'great'.")


