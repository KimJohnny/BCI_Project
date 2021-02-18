#!/usr/bin/env python
# coding: utf-8

# In[141]:


from tkinter import *


# In[142]:




# In[144]:


#defining the Boring number generator
import random


def boring_algorithm_generator():
    first_number = random.randint(100,109)
    Difference = 110 - first_number
    second_number = random.randint(1,Difference)
    summation_string = str(first_number) +" + " +str(second_number)
    return first_number, second_number, summation_string


# In[145]:


#checking if the answer and what is provided by the Boring algorithm is correct
def check(number_one, number_two, answer):
    result = True
    if (number_one + number_two)==int(answer):
        result = True 
    else:
        result = False
        
    return result


# In[ ]:





# In[146]:


import random
def level_up(level):
    last_digit = 0;
    temporary = 0;
    if level%2 == 0:
        last_digit = random.randint(10,99)
    if (level)%2 ==1:
        
        last_digit = random.randint(1,9)
    
    number_of_terms = 1
    for x in range(0,level):
        if x%2==1:
            number_of_terms = number_of_terms + 1
        
        
    
    my_list_of_numbers = []
    
    if level%2==1:
        for x in range(0, number_of_terms):
            my_list_of_numbers.append(random.randint(1,99))
        my_list_of_numbers.append(last_digit)
    if level%2==0:
        for x in range(0, number_of_terms-1):
            my_list_of_numbers.append(random.randint(1,99))
        my_list_of_numbers.append(last_digit)
    
    my_sum = 0;
    for x in my_list_of_numbers:
        my_sum = my_sum + x
    
    return my_list_of_numbers, my_sum


# In[ ]:





# In[ ]:





# In[ ]:


root = Tk()
root.title("Boring Calculator")


e = Entry(root, width = 40, borderwidth = 0)
e.grid(row = 1, column = 0, columnspan=3, padx=10, pady=10)

i = Entry(root, width = 40, borderwidth = 0)
i.grid(row = 0, column = 0, columnspan=3, padx=10, pady=10)
number_one, number_two, sum_string = boring_algorithm_generator()





#e.insert(0, "Enter your name: ")



answers_for_flow = []
answers_correct = [True, True]

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return

attempt = 0

def button_clear():
    global level
    global my_array
    global my_sum
    global my_string
    
    global answers_for_flow
    global attempt
    global difficulty
    global number_one
    global number_two
    global sum_string
    global file_name_holder
    attempt = attempt + 1
    value = file_name_holder
    if difficulty=="Difficulty: BORING":
        
        current = e.get()
        result = check(number_one, number_two, current)


        
        f= open(value,"a+")
        f.write("ATTEMPT "+str(attempt)+": "+str(number_one)+" + "+str(number_two)+" = "+str(number_one+number_two)+"\n")
        f.write("Participant answer: "+current+"\n"+"Which is " + str(result))
        f.write("\n")
        f.write("\n")
        f.close()

        number_one, number_two, sum_string = boring_algorithm_generator()

        i.delete(0, END)
        i.insert(0, sum_string)
        e.delete(0, END)
    if difficulty=="Difficulty: FLOW":
        
        
        

        if int(e.get())==my_sum:
            answer_counter.append(True)
        else:
            answer_counter.append(False)
        f = open(value,"a+")
        f.write("ATTEMPT "+str(attempt)+" "+display(my_array)+"\n")
        f.write("Participant answer: "+str(e.get())+"\n"+"Which is " + str(answer_counter[-1]))
        f.write("\n")
        f.write("\n")
        f.close()

        if answer_counter[-2]==True and answer_counter[-1]==True:
            level = level + 1
            my_array, my_sum = level_up(level)
        else:
            if level!=1:
                level = level - 1
                my_array, my_sum = level_up(level)
            else:
                my_array, my_sum = level_up(level)
        
        i.delete(0, END)
        i.insert(0, str(display(my_array)))
        e.delete(0, END)
        



def display(my_array):
    my_string = str(my_array[0])
    for x in my_array[1:]:
        my_string = my_string + " + " + str(x)
    return my_string
        
    
        
        

def button_delete_last():
    current_number = e.get()
    e.delete(0, END)
    current_number = current_number[:-1]
    e.insert(0, current_number)
    
#Defining the buttons
button_1 = Button(root, text="1",padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2",padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3",padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4",padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5",padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6",padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7",padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8",padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9",padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0",padx=40, pady=20, command=lambda: button_click(0))
button_D = Button(root,text="D",bg='red', fg='white', padx=40,pady=20, command=lambda: button_delete_last())
button_E = Button(root,text="E",bg='green', fg='white', padx=40,pady=20, command=lambda: button_clear())

#Put the buttons on the screen with the grid

button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)

button_D.grid(row=5,column=0)
button_0.grid(row=5, column=1)
button_E.grid(row=5,column=2)






top = Toplevel()
root.title("Mental calculation")
top.title("For the researchers")
#lbl = Label(top, text = "Please input session information").pack()

info = Entry(top, width = 40, borderwidth = 0)
info.grid(row = 0, column = 0, columnspan=3, padx=10, pady=10)

button_lofi = Button(top, text="Lo-Fi",bg='blue', fg='white',padx=40, pady=20, command=lambda: pass_genre("Lo-Fi"))
button_classical = Button(top, text="Classical",bg='blue', fg='white',padx=40, pady=20, command=lambda: pass_genre("Classical"))
button_pop = Button(top, text="Pop",bg='blue', fg='white',padx=40, pady=20, command=lambda: pass_genre("Pop"))
button_ID1 = Button(top, text="P1",padx=40, pady=20, command=lambda: pass_ID("1"))
button_ID2 = Button(top, text="P2",padx=40, pady=20, command=lambda: pass_ID("2"))
button_ID3 = Button(top, text="P3",padx=40, pady=20, command=lambda: pass_ID("3"))
button_ID4 = Button(top, text="P4",padx=40, pady=20, command=lambda: pass_ID("4"))
button_ID5 = Button(top, text="P5",padx=40, pady=20, command=lambda: pass_ID("5"))
button_difficulty_change = Button(top, text="FLOW/BORING",bg='orange', fg='white', padx=40,pady=20, command=lambda: change_difficulty_level())
button_enter = Button(top,text="E", bg='green', fg='white', padx=40, pady=20, command=lambda: enter())

button_lofi.grid(row=1, column=0)
button_classical.grid(row=1, column=1)
button_pop.grid(row=1, column=2)

button_ID1.grid(row=2, column=0)
button_ID2.grid(row=2, column=1)
button_ID3.grid(row=2, column=2)

button_ID4.grid(row=3, column=0)
button_ID5.grid(row=3, column=1)
button_enter.grid(row=3, column=2)
button_ID4.grid_columnconfigure(0,weight=1)

button_difficulty_change.grid(row = 4, column = 0, columnspan=3, padx=10, pady=10)

genre = "Genre: "
participant = "Participant: "
difficulty = "Difficulty: "
total_info = genre+" "+participant

def pass_genre(number):
    global genre
    global participant
    global difficulty
    current = info.get()
    info.delete(0, END)
    genre = "Genre: "+number
    total_info = genre+" "+participant+" "+difficulty
    info.insert(0, total_info)
    return


file_name_holder = ""
def file_name_holder(jok):
    global file_name_holder
    file_name_holder = jok
    return
    
def pass_ID(number):
    global genre
    global participant
    global difficulty
    current = info.get()
    
    
    info.delete(0, END)
    participant = "Participant: "+number
    total_info = genre+" "+participant+" "+difficulty
    info.insert(0, total_info)
    return

difficulty_counter = 0;
def change_difficulty_level():
    global difficulty_counter
    difficulty_counter = difficulty_counter+ 1
    global genre
    global participant
    global difficulty
    
    if difficulty_counter%2 == 1:
        difficulty = "Difficulty:"+" FLOW"
    if difficulty_counter%2 == 0:
        difficulty = "Difficulty:"+" BORING"
    
    current = info.get()
    info.delete(0, END)

    total_info = genre+" "+participant+" "+difficulty
    info.insert(0, total_info)
    return
my_array = []
my_sum = 0
level = 0
answer_counter = []
def enter():
    global my_array
    global my_sum
    global level
    global answer_counter
    value = info.get()+".txt"
    holder = value
    value = "".join(x for x in value if x.isalnum())
    f= open(value,"w+")
    f.write(holder+"\n")
    f.write("\n")
    file_name_holder(value)
    f.close()
    on_closing_top()
    if (difficulty=='Difficulty: BORING'):
        i.insert(0, sum_string)
    
    if (difficulty=="Difficulty: FLOW"):
        level = 1
        my_array, my_sum = level_up(level)
        i.insert(0, display(my_array))

        answer_counter = [True, True]

        
    top.destroy()


# In[143]:


#defining the close window event

from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        
        root.destroy()

def on_closing_top():
    global genre
    global participant
    global difficulty
    if genre == "Genre: ":
        if messagebox.askokcancel("Quit", "You forgot to indicate genre. You want to quit altogether?"):
            top.destroy()
            root.destroy()
    if participant == "Participant: ":
        if messagebox.askokcancel("Quit", "You forgot to indicate participant ID. You want to quit altogether?"):
            top.destroy()
            root.destroy()
    if difficulty=="Difficulty: ":
        if messagebox.askokcancel("Quit", "You forgot to indicate Difficulty level. You want to quit altogether?"):
            top.destroy()
            root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()


