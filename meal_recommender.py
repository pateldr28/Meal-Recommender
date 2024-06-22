"""
Author: Dristi Patel
Description:
This is an app that suggests a user a random meal to eat for the user's chosen 
meal type which are breakfast, lunch, or dinner. The user can input meal ideas
for a certain meal type that they would like to add the meal to. This is a great
app for people that areindecisive when it come to what to eat for breakfast,
lunch, and/ or dinner."""

#Imported modules tkinter and random
from tkinter import *
import random

#Lists of breakfast, lunch, and dinner foods
breakfast=["Eggs", "Pancakes", "Oatmeal", "Smoothie", "Toast", "Fruit", "Cereal"]
lunch=["Salad", "Sandwhich", "Soup", "Veggie Wrap", "Noodles", "Hummus and Pita Bread"]
dinner=["Lasagna", "Burrito", "Burger", "Rice and Curry", "Steak", "Hot Dog"]

#Initialize the root window 
root=Tk()

#Size of the window, title of the window and sets the color of the window
root.geometry("500x400")
root.title("What should you eat today?")

#Title of the app displayed as "What should you eat today?"
label= Label(root, text="What should you eat today?", font=('Arial', 18))
label.pack()


#Header of the textbox  and the textbox for user to input food they want 
#to add to a certain meal of the day
label_food=Label(root, text="Enter food", font="Arial 12", width=30, bg="#FFCCCB")
label_food.pack()   
text_box_food=Entry(root, width=30, font="Arial 12", fg="grey")
text_box_food.pack()

#Header of the textbox and textbox for the user to input the meal of the day 
#they want to add a food item to
label_time=Label(root, text="For what meal?", font="Arial 12", width=30, bg="#FFCCCB")
label_time.pack()
text_box_time=Entry(root, width=30, font="Arial 12", fg="grey")
text_box_time.pack()


#The function text_get retrieves that food item and meal of the day the user
# wants to add the food item to 
#For example, if the user input yogurt as their food item and want to put it in
#their list of food for breakfast, the item will be
#added to the breakfast list.
#The text in the textboxes is then cleared so the user know they can now input
#another item
def text_get():
    meal=text_box_food.get()
    time=text_box_time.get()

    if time.lower()=="breakfast":
        breakfast.append(meal)
    elif time.lower()=="lunch":
        lunch.append(meal)
    elif time.lower()=="dinner":
        dinner.append(meal)
    
    text_box_food.delete(0,END)
    text_box_time.delete(0,END)

#This function is gets a random breakfast food from the breakfast list and 
#displays it on the window 
def breakfast_click():
    randommeal=random.choice(breakfast)
    label_display.configure(text=randommeal)
    label_mealtype.configure(text="Breakfast")

#This function is gets a random lunch food from the lunch list and displays it
#on the window 
def lunch_click():
    randommeal=random.choice(lunch)
    label_display.configure(text=randommeal)
    label_mealtype.configure(text="Lunch")

#This function is gets a random dinner food from the dinner list and displays
#it on the window 
def dinner_click():
    randommeal=random.choice(dinner)
    label_display.configure(text=randommeal)
    label_mealtype.configure(text="Dinner")

#Displays the meal type the user chose to get a random food item from on the window
label_mealtype=Label(root,width=27, height=2, text="", bg="#734f96", font=("Arial", 12, "bold"))
label_mealtype.pack()

#Displays how the app works on the window and provides the user with instructions 
label_display=Label(root, width=30, height=9)
label_display.configure(
    anchor="center",
    text="Add food items you would like for breakfast, lunch, or dinner by filling out the textboxes above and then clicking the add button!\n\nClick on which meal of the day you want a food idea for to get a random food idea!", 
    font="Arial 12", 
    justify="center", 
    wraplength=200,
    bg="#D8BFD8")
label_display.pack()

#Displays a button that says "Add" on the window 
add_button=Button(root, text="Add", font=('Arial', 16), command=text_get, bg="light green")
add_button.place(x=420, y=65)

#Displays a button that say "Breakfast" on the window
button_b=Button(root, text="Breakfast", font=('Arial', 16), command=breakfast_click)
button_b.pack(padx=0, pady=100)
button_b.place(x=75, y=350)
button_b.configure(bg="#63b7b7")

##Displays a button that say "Lunch" on the window
button_l=Button(root, text="Lunch", font=('Arial', 16), command=lunch_click)
button_l.pack(padx=0, pady=100)
button_l.place(x=215, y=350)
button_l.configure(bg="#63b7b7")

#Displays a button that say "Dinner" on the window
button_d=Button(root, text="Dinner", font=('Arial', 16), command=dinner_click)
button_d.pack(padx=0, pady=100)
button_d.place(x=325, y=350)
button_d.configure(bg="#63b7b7")

#A main window method that allows the app to run until the user exits the window
root.mainloop()
