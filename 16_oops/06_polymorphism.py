# First we will learn what polymorphism means
# poly = many
# morph = forms
# so polymorphism means one thing but many forms

# we will try to learn with the help of real life example

# suppose a person :  father so he is someones child and he is husband of someone and he is father of his child also he his someones brother so he is a single person with multiple roles and this is polymorphism

# now we will learn using a program

class dog :
    def speak(self):
        print("bhaw bhaw")

class cat :
    def speak(self):
        print("meow meow")

class cow :
    def speak(self):
        print("moo moo")

dog_1= dog()
cat_1 =cat()
cow_1 = cow()

dog_1.speak()
cat_1.speak()
cow_1.speak()

"""
 so here every class has same named method (speak) but they have different behavior so this is a polymorphism

 every class using same method but they each have different behavior this is called polymorphism
 but method overriding is also same

 Method Overriding is one way to achieve Polymorphism.

 """


# we will now practice some questions on polymorphism


"""
QUESTION 1

Create a parent class named Animal.

Method:
- sound()

Print:
"Animal makes sound."

Create three child classes:

Dog
Cat
Cow

Override sound() in every child class.

Dog:
"Dog says Woof!"

Cat:
"Cat says Meow!"

Cow:
"Cow says Moo!"

Create one object of each class.

Call sound() using every object.
"""


class animal :

    def sound(self):
        print("Animal makes sound")

class dog :
    def sound(self):
        print("Dog says woof ".title())

class cat :
    def sound(self):
        print("cat says meow ".title())

class cow :
    def sound(self):
        print("cow says moo ".title())


dog_1 = dog()
cat_1 = cat()
cow_1 = cow()

dog_1.sound()
cat_1.sound()
cow_1.sound()


"""
Create a parent class named Shape.

Method:
- draw()

Print:
"Drawing Shape."

Create child classes:

Circle
Rectangle
Triangle

Override draw() in each child class.

Print suitable messages.

Create one object of each class.

Call draw().
"""

class Shape :
    def draw(self):
        print("Drawing shape".title())

class Circle :
    def draw(self):
        print("Drawing the circle".title())

class Rectangle :
    def draw(self):
        print("Drawing the rectangle".title())

class Triangle :
    def draw(self):
        print("Drawing the Triangle".title())


circle_1 = Circle()
rectangle_1 = Rectangle()
triangle_1 = Triangle()

circle_1.draw()
rectangle_1.draw()
triangle_1.draw()


