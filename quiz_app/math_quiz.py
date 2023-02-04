from tkinter import *
from tkinter.font import BOLD
import question_and_answer_generator as qa


class MathQuiz:
    def __init__(self, root) -> None:
        self.root = root

        self.additon = "+"
        self.subtraction = "-"
        self.division = ":"
        self.multiplication = "x"

        self.frame_math_quiz = Frame(self.root,width=500, height=600, bg="white")
        

    def math_quiz(self, category_math):
        #destroy previous frame
        self.destroy_prev_frame()

        self.frame_math_quiz.pack(fill="both", expand=True, pady=10)

        self.category_math = category_math
        self.num1 = qa.random_answer_math_quiz()[0]
        self.num2 = qa.random_answer_math_quiz()[1]

        #category title (addition, subtraction, multiplication, division)
        self.lb_category_title = Label(self.frame_math_quiz, font=("Roboto", 25, BOLD), bg="white")
        self.lb_category_title.pack()

        #question
        self.frame_question = Frame(self.frame_math_quiz, bg="white")
        self.frame_question.pack()
        
        lb_num1 = Label(self.frame_question, text=self.num1, font=("Verdana", 30, BOLD), bg="white")
        lb_num1.grid(row=0, column=0)
        self.lb_operator = Label(self.frame_question, font=("Verdana", 30, BOLD), bg="white")
        self.lb_operator.grid(row=0,column=1)
        lb_num2 = Label(self.frame_question, text=self.num2, font=("Verdana", 30, BOLD), bg="white")
        lb_num2.grid(row=0,column=2)

        #answer label
        lb_answer_text = Label(self.frame_math_quiz, text="Answer : ", font=("Roboto", 15), bg="white")
        lb_answer_text.pack()
        
        #entry answer
        self.entry_answer = Entry(self.frame_math_quiz, state="normal", justify="center", font=("Verdana", 15), width=20, bd=2)
        self.entry_answer.pack()
        
        #button
        self.btn_pass = Button(self.frame_math_quiz, text="Pass", width=10, command=self.next_question)
        self.btn_pass.pack(pady=(10,5))
        self.btn_answer = Button(self.frame_math_quiz, text="Answer", width=10, command=self.checker_math_quiz)
        self.btn_answer.pack(pady=5)
        
        #label correction
        self.lb_checker = Label(self.frame_math_quiz,font=("Helvetica", 20, BOLD), bg="white")
        self.lb_checker.pack(pady=(10,5))
        self.lb_correction = Label(self.frame_math_quiz, font=("Helvetica", 15), bg="white")
        self.lb_correction.pack(pady=5)



        match self.category_math:
            case self.additon:
                self.lb_category_title['text'] = "Quiz Addition"
                self.lb_operator['text'] = self.additon
                self.result = self.num1 + self.num2

            case self.subtraction:
                self.lb_category_title['text'] = "Quiz Subtraction"
                self.lb_operator['text'] = self.subtraction
                self.result = self.num1 - self.num2

            case self.multiplication:
                self.lb_category_title['text'] = "Quiz Multiplication"
                self.lb_operator['text'] = self.multiplication
                self.result = self.num1 * self.num2
            
            case self.division:
                self.lb_category_title['text'] = "Quiz Division"
                self.lb_operator['text'] = self.division
                self.result = round(self.num1 / self.num2, 2)

  
    def checker_math_quiz(self):
        #correct or incorrect
        if float(self.entry_answer.get()) != self.result:
            self.entry_answer['state'] = "disable"
            self.lb_checker['text'] = "Incorrect!"
            self.lb_checker['fg'] = "red"
            self.lb_correction['text'] = f"the correct answer is : {self.result}"
            self.btn_pass['text'] = "Next"
            self.btn_answer['state'] = "disable"
        else:
            self.entry_answer['state'] = "disable"
            self.lb_checker['text'] = "Correct!"
            self.lb_checker['fg'] = "green"
            self.btn_pass['text'] = "Next"
            self.btn_answer['state'] = "disable"
            
    def next_question(self):
        self.math_quiz(self.category_math)

    def destroy_prev_frame(self):
        for widget in self.frame_math_quiz.winfo_children():
            widget.destroy()
