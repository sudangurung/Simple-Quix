from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Simple 5 Question Quiz")
root.geometry("390x400")

# Create a Frame to Display Images for Quiz
image_frame = LabelFrame(root, padx=10, pady=10)
image_frame.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

# Create a Frame to Display Questions and Answers.
q_frame = LabelFrame(root, padx=20, pady=20)
q_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

# Put the Quiz Image on the Start Page
my_img6 = ImageTk.PhotoImage(Image.open("pictures/Quiz.jpg"))
my_label1 = Label(root, image=my_img6, padx=10)
my_label1.grid(row=10, column=1, sticky=E+W)

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

# Create a variable r
r = StringVar()
r.set(NONE)

# Create an Answer List.
ans = ["Sir Winston Churchill", "Jan Vermeer", "Socrates", "Chile", "Valorant"]
response = r.get()

# Create an Answer Label.
answer_label = Label(q_frame, text="The answer is " + str(ans[0]), padx=5, pady=5)

user_answer = []

# Create a Function When RadioButton is Selected
def selected():
    global user_answer
    global response

    response = r.get()

    user_answer.append(response)
    print(user_answer)

    if r.get() is not NONE and len(user_answer) != 5:
        r1.configure(state=DISABLED)
        r2.configure(state=DISABLED)
        r3.configure(state=DISABLED)
        r4.configure(state=DISABLED)

        next_button.config(state=NORMAL)

# Create a Function to Start the Quiz.
def start():
    global my_label
    global q_label
    global r1, r2, r3, r4
    global next_button
    global close_button
    global start_button
    global my_label1, my_label2

    start_button.grid_forget()
    my_label1.grid_forget()
    my_label2.grid_forget()

    root.geometry("430x750")

    # Put the Question Image in the image_frame
    my_label = Label(image_frame, image=my_img1)
    my_label.grid(row=0, column=0, columnspan=3)

    # Create a Label For The Question
    q_label = Label(q_frame, text=question1)
    q_label.grid(row=0, column=0)

    # Create the Radio Button for The Choices
    r1 = Radiobutton(q_frame, text=q1_choice[0], variable=r, value=q1_choice[0], command=selected)
    r2 = Radiobutton(q_frame, text=q1_choice[1], variable=r, value=q1_choice[1], command=selected)
    r3 = Radiobutton(q_frame, text=q1_choice[2], variable=r, value=q1_choice[2], command=selected)
    r4 = Radiobutton(q_frame, text=q1_choice[3], variable=r, value=q1_choice[3], command=selected)

    r1.grid(row=1, column=0, sticky=W)
    r2.grid(row=2, column=0, sticky=W)
    r3.grid(row=3, column=0, sticky=W)
    r4.grid(row=4, column=0, sticky=W)

    # Create Button For Submit, Next and Close Window.
    next_button = Button(root, text="Next", state=DISABLED, command=lambda: next(2, 2, 2, 2))
    next_button.grid(row=2, column=2)

    close_button = Button(root, text="Close", command=close)
    close_button.grid(row=2, column=0)

# Create a Function for Next Button
def next(image_number, question_number, choice_number, answer_number):
    global my_label
    global next_button
    global q_label
    global r1, r2, r3, r4
    global answer_label
    global submit_button

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

    # Update the Radio Button
    r1 = Radiobutton(q_frame, text=choice_list[choice_number-1][0], variable=r, value=choice_list[choice_number-1][0], command=selected)
    r2 = Radiobutton(q_frame, text=choice_list[choice_number-1][1], variable=r, value=choice_list[choice_number-1][1], command=selected)
    r3 = Radiobutton(q_frame, text=choice_list[choice_number-1][2], variable=r, value=choice_list[choice_number-1][2], command=selected)
    r4 = Radiobutton(q_frame, text=choice_list[choice_number-1][3], variable=r, value=choice_list[choice_number-1][3], command=selected)

    if image_number == 5:
        next_button = Button(root, text="Next", state=DISABLED)

        #Create Button For Submit, Next and Close Window
        submit_button = Button(root, text="Submit Answer", command=answer)
        submit_button.grid(row=2, column=1)

    my_label.grid(row=0, column=0, columnspan=3)
    q_label.grid(row=0, column=0)
    next_button.grid(row=2, column=2)

    r1.grid(row=1, column=0, sticky=W)
    r2.grid(row=2, column=0, sticky=W)
    r3.grid(row=3, column=0, sticky=W)
    r4.grid(row=4, column=0, sticky=W)

# Create a Function to Calculate the Score.
def calc():
    global ans
    global user_answer

    return list(set(ans) - set(user_answer))

# Create a Function to reveal the Answer.
def reveal():
    global my_label3

    my_label3.grid_forget()

    # Create Label to Show the Answer
    ans_label = Label(root, text="The answer to Q1 is " + ans[0] + ". Your answer was " + user_answer[0] + ".")
    ans_label1 = Label(root, text="The answer to Q1 is " + ans[1] + ". Your answer was " + user_answer[1] + ".")
    ans_label2 = Label(root, text="The answer to Q1 is " + ans[2] + ". Your answer was " + user_answer[2] + ".")
    ans_label3 = Label(root, text="The answer to Q1 is " + ans[3] + ". Your answer was " + user_answer[3] + ".")
    ans_label4 = Label(root, text="The answer to Q1 is " + ans[4] + ". Your answer was " + user_answer[4] + ".")

    ans_label.grid(row=1, column=0, sticky=W)
    ans_label1.grid(row=2, column=0, sticky=W)
    ans_label2.grid(row=3, column=0, sticky=W)
    ans_label3.grid(row=4, column=0, sticky=W)
    ans_label4.grid(row=5, column=0, sticky=W)

# Create a Function to Show the Result at the End
def answer():
    global my_label, q_label
    global r1, r2, r3, r4
    global next_button
    global my_label3
    global image_frame, q_frame
    global submit_button

    my_label.grid_forget()
    q_label.grid_forget()
    image_frame.grid_forget()
    q_frame.grid_forget()
    r1.grid_forget()
    r2.grid_forget()
    r3.grid_forget()
    r4.grid_forget()
    next_button.grid_forget()

    root.geometry("390x400")

    calc()

    # Create a Label to Show the Result
    my_label3 = Label(root, text="You got " + str(5 - len(calc())) + "/5.")
    my_label3.grid(row=1, column=1, sticky=W+E)

    # Update the Submit Answer Button to Reveal Answers
    submit_button.configure(text="Reveal Answers", command=reveal)

# Create a Function to Close The Window
def close():
    root.destroy()

# Create a Start Button.
start_button = Button(root, text="START", command=start)
start_button.grid(row=12, column=1, padx=10, pady=10)

# Create a Label for the Message
my_label2 = Label(root,
                  font="times 10",
                  text="This is a quiz consisting of 5 questions.\nChoose your answer and press next.\nAt the end submit your answer and you will get your result.\nPress reveal answer to see the answers.")
my_label2.grid(row=14, column=1)

root.mainloop()