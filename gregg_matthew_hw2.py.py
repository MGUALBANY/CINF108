# 4-1
pizzas = ['cheese', 'chicken_bacon_ranch', 'pepperoni']
for pizza in pizzas:
    print(f" I like {pizza.title()} pizza \n")
print("chicken_bacon_ranch pizza is my favorite pizza")
print("pepperoni pizza is another top choice of mine")
print("cheese pizza is my least favorite")
print("i really love pizza")

# 4-2
print("\n")
water_animals = ['shark', 'sting_ray', 'puffer_fish']
for animal in water_animals:
    print(animal)
print(f"a {water_animals[0]} would make huge pet")
print(f"a {water_animals[1]} would make terrible pet")
print(f"a {water_animals[2]} would make cute pet")
print("All of these animals must have a source of water to survive and they all can be dangerous!")

# 4-3
print("\n")
numbers = list(range(1,21))
print(numbers)

# 8-1
def display_message():
    print("In this chapter we are learning about functions in general and what you can pass though them")
display_message()

# 8-2
def favorite_book(book):
    print(f"My favorite book is called {book.title()}")
favorite_book('A perfect marrige')

print("\n")

# 8-3
def make_shirt(shirt):
    print(f"I would like a shirt in a {shirt.title()}")
make_shirt('extra small that says, I <3 NY on it')

# positional argument for shirt
print(make_shirt)

# keyword argument
def keyword_shirt(size_of_shirt, message_on_shirt):
    print("I would like a {size_of_shirt}.")
    print("with the message {message_on_shirt} on it")
print(keyword_shirt)

# 8-4
def make_shirt(shirt):
    print(f"I would like a shirt in a {shirt.title()}")
make_shirt('large that says, I love python on it')

def make_shirt(shirt):
    print(f"I would like a shirt in a {shirt.title()}")
make_shirt('medium and a extra large that says, I <3 NY on it')

def make_shirt(shirt):
    print(f"I would like a shirt in a {shirt.title()}")
make_shirt('double extra large that says, python is confusing')

# 8-5
def describe_city1(city_country1):
    print('I want to visit' , city_country1.title())
describe_city1('paris france')

def describe_city2(city_country2):
    print('I want to visit' , city_country2.title())
describe_city1('munich germany')

def describe_city3(city_country3):
    print('I want to visit' , city_country3.title())
describe_city1('montreal canada')

# 8-6
def city_country(tulum, mexico):
    travel = f"{tulum} {mexico}"
    return travel.title()
travel12 = city_country('tulum,', 'mexico')
print(travel12),