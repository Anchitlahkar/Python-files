from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.geometry("430x400")
window.configure(bg="lightgreen")


# calulating BMI
def calculate_bmi():
    weight = int(weight_entry.get())
    height = int(height_entry.get())/100

    bmi = weight/(height*height)
    bmi = round(bmi, 1)

    name = user_name.get()

    result_label.destroy()

    msg = ""

    if bmi <= 18.5:
        msg = "You are Under Weight"

    elif bmi > 18.5 and bmi <= 24.9:
        msg = "Your Weight is in normal range"

    elif bmi > 25 and bmi <= 29.9:
        msg = "You are overweight"

    elif bmi > 30:
        msg = "You are obesc"

    else:
        msg = "Something went wrong"

    # displaying output
    output_msg = Label(result_frame, text=name +
                       ", your BMI is " + str(bmi)+" and "+msg, bg="lightgreen", font=("Calibri", 12), width=50)
    output_msg.place(x=20, y=40)
    output_msg.pack()


app_label = Label(window, text="BMI Calculator", fg="black",
                  bg="lightgreen", font=("Calibri", 20), bd=5)

app_label.place(x=50, y=20)


# user name
name_label = Label(window, text="Your Name: ", fg="black",
                   bg="lightgreen", font=("Calibri", 12), bd=1)

name_label.place(x=20, y=90)

user_name = Entry(window, text="", bd=2, width=22)
user_name.place(x=150, y=92)


# Height
height_label = Label(window, text="Enter Height (cm): ", fg="black",
                     bg="lightgreen", font=("Calibri", 12))

height_label.place(x=20, y=140)

height_entry = Entry(window, text="", bd=2, width=15)
height_entry.place(x=150, y=142)


# weight
weight_label = Label(window, text="Enter Weight (kg): ", fg="black",
                     bg="lightgreen", font=("Calibri", 12))

weight_label.place(x=20, y=185)

weight_entry = Entry(window, text="", bd=2, width=15)
weight_entry.place(x=150, y=187)


# calculate Button
calculate_button = Button(window, text="Calculate",
                          fg="black", bg="green", bd=4, command=calculate_bmi)

calculate_button.place(x=20, y=250)


# Result
result_frame = LabelFrame(window, text="Result",
                          bg="lightgreen", font=("Calibri", 12))
result_frame.pack()
result_frame.place(x=20, y=300)


result_label = Label(result_frame, text="",
                     bg="lightgreen", font=("Calibri", 12), width=33)
result_label.place(x=20, y=20)
result_label.pack()


window.mainloop()
