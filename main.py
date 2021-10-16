import tkinter
from tkinter import *
from time import sleep
from words import words
import random

random_num = random.randint(0, 430)


class GUI:
    def __init__(self, window):
        self.words = words[random_num:(random_num + 30)]
        # self.list_sentence =
        self.word_number = 0
        self.points = 0
        self.seconds = 0
        self.score = 0
        self.user_input = StringVar()

        # Bind Spacebar to the check_entry function so everytime you press space it runs it
        window.bind("<space>", self.check_entry)
        window.title("Typing Test")
        window.config(padx=50, pady=50)

        # Create Canvas to display the text
        self.canvas = Canvas(width=500, height=300, background='white')
        self.canvas.create_text(250, 150, text=self.words, justify=tkinter.CENTER, width=400, font="Arial 15")
        self.canvas.grid(column=0, row=0)

        # Create entry to write the text, set textvariable as the self.user_input to save it
        self.user_entry = Entry(textvariable=self.user_input)
        self.user_entry.grid(column=0, row=1, pady=10)

    def check_entry(self, event):
        """Checks if spacebar is pressed, gets the text of the entry, checks if the word is ok and deletes the
         word from the entry"""
        if event.char == " ":
            text = self.user_input.get().split(" ")[0].lower()
            word = self.words[self.word_number].lower()

            if text == word:
                self.points += 1

        self.user_entry.delete(0, 'end')
        self.word_number += 1
        window.after(1000, self.timer)
        if self.word_number == len(self.words):
            """Checks when you are done and calculate the score"""
            mins = self.seconds / 60
            self.score = round(self.points / mins, 0)
            sleep(1)
            Label(text=f"You scored {self.score} words per minute!", font="Arial 15").grid(column=0, row=2, pady=10)

    def timer(self):
        self.seconds += 1


if __name__ == "__main__":
    window = Tk()
    gui = GUI(window)
    window.mainloop()
    print(f"You scored {gui.score} words per minute!")
