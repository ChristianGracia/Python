#very basic, just started learning python today

#basic variables
cucumbers = 3
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber
print(total_cost)


#float
cucumbers = 100
num_people = 6
float_cucumbers_per_person = float(cucumbers)/num_people
print(float_cucumbers_per_person)

#multiline strings with triple quotes """"""
haiku ="""The old pond,
A frog jumps in:
Plop!"""

#Booleans, False, True
age_is_12 = False
name_is_maria = True

#using str() and int() to convert data types
float_1 = 0.25
float_2 = 40.0
product = float_1 * float_2

big_string = "The product was " + str(product)

#Review
skill_completed = "Python Syntax"
exercises_completed = 13

points_per_exercise = 5
point_total = 100
point_total += exercises_completed * points_per_exercise

print("I got " + str(point_total) + " points!")

