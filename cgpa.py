from tkinter import *
import tkinter.messagebox

root=Tk()

root.title("CGPA Calculator")

labelframe = LabelFrame(root,text="Sem 1")
labelframe.pack(fill="both")

def grade(grd):
    dic={"O":10, "A+":9, "A":8, "B+":7, "B":6, "C":5, "D":4, "E":3, "F":0}
    return dic[grd]

label_1 = Label(labelframe, text="Grade", relief=GROOVE, width="17", pady=8, padx=100)
label_1.grid(row=1,column=1)

label_2 = Label(labelframe, text="Credit", relief=GROOVE, width="17", pady=8, padx=100)
label_2.grid(row=1,column=2)

label_3 = Label(labelframe,text="Subject 1", pady=8, padx=100)
label_3.grid(row=2,column=0)

entry_1 = Spinbox(labelframe, values=("O", "A+", "A", "B+", "B", "C", "D", "E", "F"))
entry_1.grid(row=2,column=1)

entry_2 = Spinbox(labelframe, values=(0,1,2,3,4,5,6))
entry_2.grid(row=2,column=2)

label_4 = Label(labelframe,text="Subject 2", pady=8, padx=100)
label_4.grid(row=3,column=0)

entry_3 = Spinbox(labelframe, values=("O", "A+", "A", "B+", "B", "C", "D", "E", "F"))
entry_3.grid(row=3,column=1)

entry_4 = Spinbox(labelframe, values=(0,1,2,3,4,5,6))
entry_4.grid(row=3,column=2)

label_5 = Label(labelframe,text="Subject 3", pady=8, padx=100)
label_5.grid(row=4,column=0)

entry_5 = Spinbox(labelframe, values=("O", "A+", "A", "B+", "B", "C", "D", "E", "F"))
entry_5.grid(row=4,column=1)

entry_6 = Spinbox(labelframe, values=(0,1,2,3,4,5,6))
entry_6.grid(row=4,column=2)

label_6 = Label(labelframe,text="Subject 4", pady=8, padx=100)
label_6.grid(row=5,column=0)

entry_7 = Spinbox(labelframe, values=("O", "A+", "A", "B+", "B", "C", "D", "E", "F"))
entry_7.grid(row=5,column=1)

entry_8 = Spinbox(labelframe, values=(0,1,2,3,4,5,6))
entry_8.grid(row=5,column=2)

label_7 = Label(labelframe,text="Subject 5", pady=8, padx=100)
label_7.grid(row=6,column=0)

entry_9 = Spinbox(labelframe, values=("O", "A+", "A", "B+", "B", "C", "D", "E", "F"))
entry_9.grid(row=6,column=1)

entry_10 = Spinbox(labelframe, values=(0,1,2,3,4,5,6))
entry_10.grid(row=6,column=2)

label_8 = Label(labelframe,text="Subject 6", pady=8, padx=100)
label_8.grid(row=7,column=0)

entry_11 = Spinbox(labelframe, values=("O", "A+", "A", "B+", "B", "C", "D", "E", "F"))
entry_11.grid(row=7,column=1)

entry_12 = Spinbox(labelframe, values=(0,1,2,3,4,5,6))
entry_12.grid(row=7,column=2)

label_9 = Label(labelframe, text="TGPA", pady=8, padx=100)
label_9.grid(row=4, column=3)

int_value_1 = IntVar()

entry_13 = Entry(labelframe, textvariable = int_value_1)
entry_13.grid(row=4, column=4)

def add_courses_1():
    grades_list_1=[]
    credits_list_1=[]

    grades_list_1.append(grade(entry_1.get()))
    credits_list_1.append(entry_2.get())
    grades_list_1.append(grade(entry_3.get()))
    credits_list_1.append(entry_4.get())
    grades_list_1.append(grade(entry_5.get()))
    credits_list_1.append(entry_6.get())
    grades_list_1.append(grade(entry_7.get()))
    credits_list_1.append(entry_8.get())
    grades_list_1.append(grade(entry_9.get()))
    credits_list_1.append(entry_10.get())
    grades_list_1.append(grade(entry_11.get()))
    credits_list_1.append(entry_12.get())

    credit_point_1=0
    total_credits_1=0
    for i in range(0,6):
        credit_point_1 = credit_point_1 + ((grades_list_1[i])*int(credits_list_1[i]))
        total_credits_1 = total_credits_1 + int(credits_list_1[i])

    global tgpa_1
    tgpa_1 = float(credit_point_1/total_credits_1)
    print(credit_point_1)
    print(total_credits_1)
    print(tgpa_1)

    int_value_1.set(tgpa_1)
    return tgpa_1

btn_1 = Button(root,text="Calculate", command = add_courses_1)
btn_1.pack(pady=2)


labelframe_1 = LabelFrame(root,text="Sem 2")
labelframe_1.pack(fill="both")

label_10 = Label(labelframe_1, text="Grade", relief=GROOVE, width="17", pady=8, padx=100)
label_10.grid(row=10,column=1)

label_11 = Label(labelframe_1, text="Credit", relief=GROOVE, width="17", pady=8, padx=100)
label_11.grid(row=10,column=2)

label_12 = Label(labelframe_1,text="Subject 1", pady=8, padx=100)
label_12.grid(row=11,column=0)

entry_14 = Spinbox(labelframe_1, values=("O", "A+", "A", "B+", "B", "C", "D", "E", "F"))
entry_14.grid(row=11,column=1)

entry_15 = Spinbox(labelframe_1, values=(0,1,2,3,4,5,6))
entry_15.grid(row=11,column=2)

label_13 = Label(labelframe_1,text="Subject 2", pady=8, padx=100)
label_13.grid(row=12,column=0)

entry_16 = Spinbox(labelframe_1, values=("O", "A+", "A", "B+", "B", "C", "D", "E", "F"))
entry_16.grid(row=12,column=1)

entry_17 = Spinbox(labelframe_1, values=(0,1,2,3,4,5,6))
entry_17.grid(row=12,column=2)

label_14 = Label(labelframe_1,text="Subject 3", pady=8, padx=100)
label_14.grid(row=13,column=0)

entry_18 = Spinbox(labelframe_1, values=("O", "A+", "A", "B+", "B", "C", "D", "E", "F"))
entry_18.grid(row=13,column=1)

entry_19 = Spinbox(labelframe_1, values=(0,1,2,3,4,5,6))
entry_19.grid(row=13,column=2)

label_15 = Label(labelframe_1,text="Subject 4", pady=8, padx=100)
label_15.grid(row=14,column=0)

entry_20 = Spinbox(labelframe_1, values=("O", "A+", "A", "B+", "B", "C", "D", "E", "F"))
entry_20.grid(row=14,column=1)

entry_21 = Spinbox(labelframe_1, values=(0,1,2,3,4,5,6))
entry_21.grid(row=14,column=2)

label_16 = Label(labelframe_1,text="Subject 5", pady=8, padx=100)
label_16.grid(row=15,column=0)

entry_22 = Spinbox(labelframe_1, values=("O", "A+", "A", "B+", "B", "C", "D", "E", "F"))
entry_22.grid(row=15,column=1)

entry_23 = Spinbox(labelframe_1, values=(0,1,2,3,4,5,6))
entry_23.grid(row=15,column=2)

label_17 = Label(labelframe_1,text="Subject 6", pady=8, padx=100)
label_17.grid(row=16,column=0)

entry_24 = Spinbox(labelframe_1, values=("O", "A+", "A", "B+", "B", "C", "D", "E", "F"))
entry_24.grid(row=16,column=1)

entry_25 = Spinbox(labelframe_1, values=(0,1,2,3,4,5,6))
entry_25.grid(row=16,column=2)

label_18 = Label(labelframe_1, text="TGPA", pady=8, padx=100)
label_18.grid(row=13, column=3)

int_value_2 = IntVar()

entry_26 = Entry(labelframe_1, textvariable = int_value_2)
entry_26.grid(row=13, column=4)

def add_courses_2():
    grades_list_2=[]
    credits_list_2=[]

    grades_list_2.append(grade(entry_14.get()))
    credits_list_2.append(entry_15.get())
    grades_list_2.append(grade(entry_16.get()))
    credits_list_2.append(entry_17.get())
    grades_list_2.append(grade(entry_18.get()))
    credits_list_2.append(entry_19.get())
    grades_list_2.append(grade(entry_20.get()))
    credits_list_2.append(entry_21.get())
    grades_list_2.append(grade(entry_22.get()))
    credits_list_2.append(entry_23.get())
    grades_list_2.append(grade(entry_24.get()))
    credits_list_2.append(entry_25.get())

    credit_point_2=0
    total_credits_2=0
    for i in range(0,6):
        credit_point_2 = credit_point_2 + ((grades_list_2[i])*int(credits_list_2[i]))
        total_credits_2 = total_credits_2 + int(credits_list_2[i])

    global tgpa_2
    tgpa_2= float(credit_point_2/total_credits_2)
    print(credit_point_2)
    print(total_credits_2)
    print(tgpa_2)

    int_value_2.set(tgpa_2)
    return tgpa_2

btn_2 = Button(root,text="Calculate", command = add_courses_2)
btn_2.pack(pady=2)


labelframe_2 = LabelFrame(root)
labelframe_2.pack(fill="both")

label_19 = Label(labelframe_2, text="CGPA", pady=8, width=100)
label_19.grid(row=18, column=1)

int_value_3 = IntVar()

entry_27 = Entry(labelframe_2, textvariable = int_value_3)
entry_27.grid(row=18, column=2)

label_20 = Label(labelframe_2, text="Remarks", pady=8, width=100)
label_20.grid(row=19, column=1)

entry_28 = Entry(labelframe_2)
entry_28.grid(row=19, column=2)

def final_grade():
    cgpa = (tgpa_1+tgpa_2)/2
    print(cgpa)

    int_value_3.set(cgpa)

btn_3 = Button(root,text="Calculate CGPA", command = final_grade)
btn_3.pack(pady=2)

frame_3 = Frame(root)
frame_3.pack()
