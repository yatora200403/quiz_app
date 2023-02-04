from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk, Image
import question_and_answer_generator as qa


class FlagQuiz:
    def __init__(self, root) -> None:
        self.root = root
        self.path = "./flashcard_app/flag_images/"

        self.country_flags_image1 = ImageTk.PhotoImage(Image.open(self.path + "japan.png"))
        self.country_flags_image2 = ImageTk.PhotoImage(Image.open(self.path + "japan.png"))
        self.country_flags_image3 = ImageTk.PhotoImage(Image.open(self.path + "japan.png"))

        self.frame_flag_quiz = Frame(self.root, width=500, height=600, bg="white")
    
    def flag_country_quiz(self):
        #hide prev widget and destroy child inside that widget
        self.destroy_prev_frame()

        self.frame_flag_quiz.pack(fill="both", expand=True)
        lb_question = Label(self.frame_flag_quiz, text="Which is Flag Of this Country ? ", font=("Roboto", 25, BOLD), bg="white")
        lb_question.pack(pady=20)

        #generator
        question_and_answer = qa.random_answer_flag_quiz()
        self.answer = question_and_answer[1]
        lb_country_name = Label(self.frame_flag_quiz, text=question_and_answer[1].title(), font=("Roboto", 20, BOLD), bg="white")
        lb_country_name.pack(pady=5)

        #radio button
        frame_radio = Frame(self.frame_flag_quiz, bg="white")
        frame_radio.pack()

        self.answer_variable = StringVar()
        self.answer_variable.set(None)
        
        self.country_flags_image1 = ImageTk.PhotoImage(Image.open(self.path + question_and_answer[0][0] + ".png").resize(size=(100,70), resample=Image.LANCZOS))
        self.country_flags_image2 = ImageTk.PhotoImage(Image.open(self.path + question_and_answer[0][1] + ".png").resize(size=(100,70), resample=Image.LANCZOS))
        self.country_flags_image3 = ImageTk.PhotoImage(Image.open(self.path + question_and_answer[0][2] + ".png").resize(size=(100,70), resample=Image.LANCZOS))

        rb_country1 = Radiobutton(frame_radio, image=self.country_flags_image1, variable=self.answer_variable, value=question_and_answer[0][0], bg="light blue", indicatoron=0)
        rb_country2 = Radiobutton(frame_radio, image=self.country_flags_image2, variable=self.answer_variable, value=question_and_answer[0][1], bg="light blue", indicatoron=0)
        rb_country3 = Radiobutton(frame_radio, image=self.country_flags_image3, variable=self.answer_variable, value=question_and_answer[0][2], bg="light blue", indicatoron=0)
        
        rb_country1.grid(row=0, column=0, padx=5)
        rb_country2.grid(row=0, column=1, padx=5)
        rb_country3.grid(row=0, column=2, padx=5)
        
        #button
        self.btn_pass = Button(self.frame_flag_quiz, text="Pass", width=10, command=self.pass_answer_flag_quiz)
        self.btn_pass.pack(pady=10)
        self.btn_answer = Button(self.frame_flag_quiz, text="Answer",width=10,state="normal" ,command=self.answer_checker_flag_quiz)
        self.btn_answer.pack(pady=10)

        #checker
        self.lb_checker_flag = Label(self.frame_flag_quiz, font=("Roboto", 25, BOLD) , bg="white")
        self.lb_correction_flag = Label(self.frame_flag_quiz, font=("Roboto", 12, BOLD), bg="white")
        
        self.lb_checker_flag.pack()
        self.lb_correction_flag.pack()
    
    def answer_checker_flag_quiz(self):
        if self.answer_variable.get() == self.answer:
            self.lb_checker_flag['text'] = "Correct!"
            self.lb_checker_flag['fg'] = "green"
            self.lb_correction_flag['text'] = "that's the right flag"
            self.btn_pass['text'] = "Next"
            self.btn_answer['state'] = "disable"
        else:
            self.lb_checker_flag['text'] = "Incorrect!"
            self.lb_checker_flag['fg'] = "red"
            self.lb_correction_flag['text'] = "the rigth answer is " + self.answer.title()
            self.btn_pass['text'] = "Next"
            self.btn_answer['state'] = "disable"
    
    def pass_answer_flag_quiz(self):
        self.flag_country_quiz()

    def destroy_prev_frame(self):
        for widget in self.frame_flag_quiz.winfo_children():
            widget.destroy()
