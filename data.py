#float adds a decimal point
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
print(f"hello {x}") """

""" temp = 30
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')  """

""" number = 10
if number % 2 == 0:
    print ("even")
else:
    print ("odd") """

""" def calculate_tip(bill, service):
    if service == "bad":
        tip_percentage = 0
    elif service == "ok":
        tip_percentage = 0.15
    elif service == "good":
        tip_percentage = 0.2
    elif service == "great":
        tip_percentage = 0.25
    else:
        return "Invalid service level. Please choose from 'bad', 'okay', 'good', or 'great'."
    
    tip = bill * tip_percentage
    return f"Tip for {service} service: ${tip:.2f}" #indicates an f string and make sure the tip is rounded to 2 decimal points.
bill = float(input("Enter the bill amount: $"))
service = input("Enter the service rating (bad, ok, good, great): ").strip()
tip = calculate_tip(bill, service)
print(tip) """

def find_factors(number):  
    factors = []  #Makes a list for the factors; where all the factors of the number would be
    for i in range(1, number + 1):  #starts a loop for all the numbers from 1 to the number
        if number % i == 0:  # checks if i divides number with no remainder, if 0 is a remainder, than i is a factor
            factors.append(i) # if i is a factor then it is added to the factors list
    return factors  
find_factors(6)