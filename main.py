#sw2 - Grade 10 Classmates System
from pyscript import display, document

# Classmate class
class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hello! I am {self.name} from {self.section} and my favorite subject is {self.favorite_subject}!"



# list to store classmates
classmates = [
    Classmate("Catimbang", "Topaz", "Math"),
    Classmate("Gano", "Topaz", "Science"),
    Classmate("Garcia", "Topaz", "English"),
    Classmate("Kaur", "Topaz", "Math"),
    Classmate("Tan", "Topaz", "PE"),
]


# function to display list
def show_list(event=None):
    document.getElementById("output").innerHTML = ""
    for c in classmates:
        display(c.introduce(), target="output")


# function to add classmate
def add_classmate(event):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    new_classmate = Classmate(name, section, subject)
    classmates.append(new_classmate)

    # clear inputs
    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("subject").value = ""

    # refresh list
    show_list()

