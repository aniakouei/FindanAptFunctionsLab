
#create a function that takes the parameters of city, max_rent, min_beds and pets_allowed
#print a message and create an if statement if pets are allowed to add to that message
#create another function with the same parameters but provide defult options for min beds and pets allowed
# use function to print statements for both min beds and pets allowed omitted
#use function to print statements for just min beds
#use function to print statements for just pets allowed

#create a lambda function that adds 100 to any givem number and print
#create a lambda function that squares any given mumber and print
#create a lambda function that concatenates - before any string and print
#create a lambda function that divides any number by 3 and print


def apt_search1(city, max_rent, min_beds, pets_allowed):
    message = f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} per month'
    if pets_allowed:
        message += ", pets allowed! "
    return message

result = apt_search1("San Francisco", max_rent=2000, min_beds=1, pets_allowed=True)
print(result)

def apt_search2(city, max_rent, min_beds=3, pets_allowed=False):
    message = f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} per month'
    if pets_allowed:
        message += ", pets allowed! "
    return message

result2 = apt_search2("San Francisco", max_rent=2000)
print(result2)

result3 = apt_search2("New York", max_rent=1500,min_beds=2)
print(result3)

result4 = apt_search2("Miami", max_rent=3000, pets_allowed=True)
print(result4)

plus_one_hundred = lambda x: x + 100
print(plus_one_hundred(30))

square_num = lambda x: x ** 2
print(square_num(4))

concatenate = lambda s: "- " + s
print(concatenate('hello'))

divide_by_three = lambda x: x / 3
print(divide_by_three(9))