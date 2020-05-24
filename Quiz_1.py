from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Simple 5 Question Quiz")
root.geometry("430x750")

# Create a Frame to Display Images for Quiz
image_frame = LabelFrame(root, padx=10, pady=10)
image_frame.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

# Create a Frame to Display Questions and Answers.
q_frame = LabelFrame(root, padx=20, pady=20)
q_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

# Create an Image List
my_img1 = ImageTk.PhotoImage(Image.open("pictures/Winston.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("pictures/Jan.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("pictures/Socrates.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("pictures/Chile.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("pictures/sage.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# Create a Question List
question1 = "Q1. Who is this historical figure pictured above?"
question2 = "Q2. Who is the painter for this famous painting?"
question3 = "Q3. Who is this famous football player from Brazil?"
question4 = "Q4. Where is this place located?"
question5 = "Q5. From which game is this character from?"

question_list = [question1, question2, question3, question4, question5]

# Create a Choice List
q1_choice = ["Prince Philip, Duke of Edinburgh", "Sir Winston Churchill", "Franklin D. Roosevelt", "Charles de Gaulle"]
q2_choice = ["Van Gough", "Jan Vermeer", "Auguste Renoir", "Paul Cezanne"]
q3_choice = ["Pele", "Ronaldo", "Socrates", "Garrincha"]
q4_choice = ["Peru", "Chile", "Tanzania", "New Zealand"]
q5_choice = ["Apex Legends", "OverWatch", "Far Cry", "Valorant"]

choice_list = [q1_choice, q2_choice, q3_choice, q4_choice, q5_choice]

# Put the Question Image in the image_frame
my_label = Label(image_frame, image=my_img1)

# Create a Label For The Question
q_label = Label(q_frame, text=question1)

# Create a variable r
r = StringVar()
r.set(NONE)

# Create the Radio Button for The Choices
r1 = Radiobutton(q_frame, text=q1_choice[0], variable=r, value=q1_choice[0])
r2 = Radiobutton(q_frame, text=q1_choice[1], variable=r, value=q1_choice[1])
r3 = Radiobutton(q_frame, text=q1_choice[2], variable=r, value=q1_choice[2])
r4 = Radiobutton(q_frame, text=q1_choice[3], variable=r, value=q1_choice[3])

# Create an Answer List.
ans = ["Sir Winston Churchill", "Jan Vermeer", "Socrates", "Chile", "Valorant"]
response = r.get()

# Create an Answer Label.
answer_label = Label(q_frame, text="The answer is " + str(ans[0]), padx=5, pady=5)

# Create a Function to Check Whether the Answer is Right or Not
def answer():
    global ans
    global response
    global answer_label

    response = r.get()

    # Create an if statement for the Right and Wrong Answer
    if response in ans:
        messagebox.showinfo(None, "You have guessed correctly")
    else:
        messagebox.showinfo(None, "You have guessed incorrectly")
        answer_label.grid(row=5, column=0, sticky=W)

    # Create an if Statement To Disable the RadioButton
    if response != NONE:
        r1.configure(state=DISABLED)
        r2.configure(state=DISABLED)
        r3.configure(state=DISABLED)
        r4.configure(state=DISABLED)

# Create a Function for Next Button
def next(image_number, question_number, choice_number, answer_number):
    global my_label
    global next_button
    global q_label
    global r1, r2, r3, r4
    global answer_label

    my_label.grid_forget()
    q_label.grid_forget()
    r1.grid_forget()
    r2.grid_forget()
    r3.grid_forget()
    r4.grid_forget()
    answer_label.grid_forget()

    my_label = Label(image=image_list[image_number-1])
    q_label = Label(q_frame, text=question_list[question_number-1])
    answer_label = Label(q_frame, text="The answer is " + str(ans[answer_number - 1]), padx=5, pady=5)
    next_button = Button(root, text="Next", state=DISABLED, command=lambda: next(image_number+1, question_number+1, choice_number+1, answer_number+1))

   # function that is called when you select a certain radio button
    def selected():
        if r.get() is not None and image_number != 5:
            next_button['state'] = 'normal'

    # Update the Radio Button
    r1 = Radiobutton(q_frame, text=choice_list[choice_number-1][0], variable=r, value=choice_list[choice_number-1][0], command=selected)
    r2 = Radiobutton(q_frame, text=choice_list[choice_number-1][1], variable=r, value=choice_list[choice_number-1][1], command=selected)
    r3 = Radiobutton(q_frame, text=choice_list[choice_number-1][2], variable=r, value=choice_list[choice_number-1][2], command=selected)
    r4 = Radiobutton(q_frame, text=choice_list[choice_number-1][3], variable=r, value=choice_list[choice_number-1][3], command=selected)

    if image_number == 5:
        next_button = Button(root, text="Next", state=DISABLED)
        # Create Button For Submit, Next and Close Window.
        submit_button = Button(root, text="Submit Answer", command=answer)
        submit_button.grid(row=2, column=1)

    my_label.grid(row=0, column=0, columnspan=3)
    q_label.grid(row=0, column=0)
    next_button.grid(row=2, column=2)

    r1.grid(row=1, column=0, sticky=W)
    r2.grid(row=2, column=0, sticky=W)
    r3.grid(row=3, column=0, sticky=W)
    r4.grid(row=4, column=0, sticky=W)

# Create a Function to Close The Window
def close():
    root.destroy()

next_button = Button(root, text="Play", command=lambda: next(1, 1, 1, 1))
next_button.grid(row=2, column=2)

close_button = Button(root, text="Close", command=close)
close_button.grid(row=2, column=0)

root.mainloop()