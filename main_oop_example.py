from tkinter import *
from tkinter import messagebox
import time
import random

prompt = ['Twas the night before Christmas....',
          "It was a cold and rainy night at the local pub, when suddenly a shadowy figure burst through the door...",
          "What is it they say about the dead and sleep? I forget. Anyways, so there I was. Down to my last bit of strength...",
          "Ain't no rest for the wicked, but you've been living peacefully the past few years..."
          ]

old_passage_length = 0
new_passage_length = 0

def check_length():
    global old_passage_length
    global new_passage_length
    new_passage_length = len(entry_field.get(0.0, 'end'))
    difference = new_passage_length - old_passage_length
    old_passage_length = new_passage_length
    if difference < 1:
        entry_field.delete("1.0", 'end')
        if messagebox.askyesno(title='Do you wish to try again?', message='Yes to start over. No to close program.'):
            return False
        else:
            window.destroy()
    window.after(60000, check_length)


# gotta figure this one out soon
def choose_prompt():
    global prompt
    # pull random prompt and reassign to prompt
    writing_prompt.config(text=random.choice(prompt))





window = Tk()
window.title('Think On Your Feet')
window.config(height=600, width=600, padx=50, pady=50)

title_label = Label(text="Test your writing skills. Don't stop for more than a minute or else your progress will be lost!")
title_label.grid(row=0,column=1)
writing_prompt = Label(text='Import writing here')
writing_prompt.grid(row=1,column=1)

generate_prompt_button = Button(text='Generate Prompt', command=choose_prompt)
generate_prompt_button.grid(row=2, column=0)

start_writing_button = Button(text='Start Writing!', command=check_length)
start_writing_button.grid(row=2, column=1)

entry_field = Text(height=100, width=100, padx=50, pady=50)
entry_field.grid(row=3,column=1)




window.mainloop()