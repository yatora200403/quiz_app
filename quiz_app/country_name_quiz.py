from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk, Image
import question_and_answer_generator as qa

class CountryQuiz:
    def __init__(self, root) -> None:
        self.root = root
        self.path = "./flashcard_app/flag_images/"
        self.frame_country_name = Frame(self.root, width=500, height=600, bg="white")
        self.country_flags_image = ImageTk.PhotoImage(Image.open(self.path + "japan.png")) #if u call a function to open image u must be global it function first and then u can call the function where ever it is, if u not the image will not appear.

    def country_name_quiz(self):
        #hide prev widget and destroy child inside that widget
        self.destroy_prev_frame()

        # frame state
        self.frame_country_name.pack(fill="both", expand=True)
        
        #question
        Label(self.frame_country_name, text="This Flag belong to ?", font=("Roboto", 30, BOLD), bg="white").pack(pady=5)

        self.show_img = Label(self.frame_country_name)
        self.show_img.pack(pady=10)

        #entry answer
        self.entry_answer = Entry(self.frame_country_name, font=("Helvetica", 20), bd=2)
        self.entry_answer.focus()
        
        #button for random
        self.btn_pass_answer = Button(self.frame_country_name, text="Pass",width=10, command=self.pass_answer_country_name)
        self.btn_answer = Button(self.frame_country_name, text="Answer",width=10, command=self.answer_checker_country_name)

        #label correct or incorrect
        self.label_checker = Label(self.frame_country_name, font=("Roboto", 25, BOLD) , bg="white")
        self.label_correction = Label(self.frame_country_name, font=("Roboto", 12, BOLD), bg="white")
        
        self.entry_answer.pack(pady=5)
        self.btn_pass_answer.pack(pady=10)
        self.btn_answer.pack(pady=10)
        self.label_checker.pack()
        self.label_correction.pack()
        
        self.randomize_flags_country_name()


    def answer_checker_country_name(self):
        answer = self.entry_answer.get().replace(" ","").lower()
        if answer == self.generator_image:
            self.label_checker["text"] = "Correct!"
            self.label_checker["fg"] = "green"
            self.label_correction["text"] = "the answer is : " + self.entry_answer.get().title()
            self.btn_pass_answer["text"] = "Next"

            self.entry_answer['state'] = "disable"
            self.btn_answer['state'] = "disable"
        else:
            self.label_checker["text"] = "Incorrect!"
            self.label_checker["fg"] = "red"
            self.btn_pass_answer["text"] = "Next"
            self.label_correction["text"] = "the answer is : " + self.generator_image.title()

            self.entry_answer['state'] = "disable"
            self.btn_answer['state'] = "disable"
    
    def randomize_flags_country_name(self):
        self.entry_answer['state'] = "normal"
        self.entry_answer.delete(0,END)
        self.btn_answer['state'] = "normal"
        self.btn_pass_answer['state'] = "normal"
        self.label_checker['text'] = ""
        self.label_correction['text'] = ""
        self.btn_pass_answer['text'] = "Pass"

        #image
        self.generator_image = qa.random_answer_country_name()
        self.country_flags_image = ImageTk.PhotoImage(Image.open(self.path + self.generator_image + ".png").resize(size=(300,180), resample=Image.LANCZOS))
        self.show_img['image'] = self.country_flags_image
     
    def pass_answer_country_name(self):
        self.randomize_flags_country_name()

    def destroy_prev_frame(self):
        for widget in self.frame_country_name.winfo_children():
            widget.destroy()
