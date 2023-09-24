import tkinter


window = tkinter.Tk()
window.title("BMI CALCULATOR")
window.minsize(width=250,height=250)

def bmi_calculator():
    weight = bmi_entry2.get()
    height = bmi_entry1.get()

    if weight == "" or height == "":
        result_label.config(text="fill in the blanks above")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_bmi(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="enter a valid number")



bmi_label1 = tkinter.Label(text="Enter Your Height (cm)")
bmi_label1.pack(side="top")

bmi_entry1 = tkinter.Entry()
bmi_entry1.pack(side="top")

bmi_label2 = tkinter.Label(text="Enter Your Weight (kg)")
bmi_label2.pack(side="top")

bmi_entry2 = tkinter.Entry()
bmi_entry2.pack(side="top")

bmi_button = tkinter.Button(text="calculate" , command= bmi_calculator)
bmi_button.pack(side="top")

result_label = tkinter.Label()
result_label.pack(side="top")


def write_bmi(bmi):
    bmi_string =  bmi_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        bmi_string += "severely thin!"
    elif 16 < bmi <= 17:
        bmi_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        bmi_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        bmi_string += "normal weight"
    elif 25 < bmi <= 30:
        bmi_string += "overweight"
    elif 30 < bmi <= 35:
        bmi_string += "obese class 1"
    elif 35 < bmi <= 40:
        bmi_string += "obese class 2"
    else:
        bmi_string += "obese class 3"
    return bmi_string

window.mainloop()