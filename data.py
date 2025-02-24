
""" x = 3
y = float(3)
print(x,y) 
#float adds a decimal point """


""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
#strings lists values """


"""print(values[0])
print(values[6]) 
#allows us to access first and last elements """


""""test"
["t","e","s","t"]
#shows a string which is a list with letters to create a word """


""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) 
#splits te string into a new list """


""" sentence = input("enter a sentence: ")
def count_words(sentence):
    words = sentence.split()  # Split the sentence into a list of words
    return len(words)
word_count = count_words(sentence)
print("The number of words in your sentence is:", word_count) """


""" day_of_week = input("what day is it?")
if day_of_week == "Friday": 
    print("correct") #if the day is friday it would be marked as correct
else:
    print("incorrect") #if it isn't friday it would be marked as incorrect
#booleans help confirm if things are true of false. This code helps shows what day it is, if its not friday than it buts false.  """


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
if number % 2 == 0: #if a number is divided by 2 ends up with a 0, the number is even
    print ("even")
else:
    print ("odd")
      """ 

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

""" def find_factors(number):  
    factors = []  #Makes a list for the factors; where all the factors of the number would be
    for i in range(1, number + 1):  #starts a loop for all the numbers from 1 to the number
        if number % i == 0:  # checks if i divides number with no remainder, if 0 is a remainder, than i is a factor
            factors.append(i) # if i is a factor then it is added to the factors list
    return factors  
print(find_factors(2525)) # prints the factors of the number """

