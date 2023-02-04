from tkinter import *
from tkinter.font import BOLD
from country_name_quiz import CountryQuiz
from flags_country_quiz import FlagQuiz
from math_quiz import MathQuiz


root = Tk()
root.title("Quiz App")
icon = PhotoImage(file="./flashcard_app/favicon/quiz.png")
root.iconphoto(False, icon)
root.resizable(0,0)
root.geometry("500x600")
root.config(bg="white")

class Category:
    def __init__(self, root) -> None:

        self.cq = CountryQuiz(root=root)
        self.fq = FlagQuiz(root=root)
        self.mq = MathQuiz(root=root)

    def country_name_quiz(self):
        self.destroy_prev_widget()
        self.cq.country_name_quiz()

    def flag_country_quiz(self):
        self.destroy_prev_widget()
        self.fq.flag_country_quiz()

    def math_quiz(self, category_math):
        self.destroy_prev_widget()
        self.mq.math_quiz(category_math)

    def destroy_prev_widget(self):
        self.cq.frame_country_name.pack_forget()
        self.fq.frame_flag_quiz.pack_forget()
        self.mq.frame_math_quiz.pack_forget()

c = Category(root=root)


my_menu = Menu(root)
root.config(menu=my_menu) 

#category
geography_menu = Menu(my_menu)
math_menu = Menu(my_menu)

my_menu.add_cascade(label="Geography", menu=geography_menu)
my_menu.add_cascade(label="Math", menu=math_menu)
my_menu.add_cascade(label="Quit", command=root.quit)

#sub-category geography
geography_menu.add_command(label="Country Name Quiz", command=c.country_name_quiz)
geography_menu.add_command(label="Flag Country Quiz", command=c.flag_country_quiz)

#sub-category math
math_menu.add_command(label="Addition", command=lambda:c.math_quiz("+"))
math_menu.add_command(label="Subtraction", command=lambda:c.math_quiz("-"))
math_menu.add_command(label="Multiply", command=lambda:c.math_quiz("x"))
math_menu.add_command(label="Division", command=lambda:c.math_quiz(":"))
        

root.mainloop()
    