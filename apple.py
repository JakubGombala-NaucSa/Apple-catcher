import tkinter as tk
import random

root = tk.Tk()
root.title("Apple catcher")

canvas = tk.Canvas(root, width=400, height=600, bg="lightblue")
canvas.pack()

basket = canvas.create_rectangle(175, 550, 225, 570, fill="brown")

def move_left(event):
    if canvas.coords(basket)[0] > 0:
        canvas.move(basket, -30, 0)

def move_right(event):
    if canvas.coords(basket)[2] < 400:
        canvas.move(basket, 30, 0)
    
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

apples = []

def create_apple():
    x = random.randint(20, 380)
    apple = canvas.create_oval(x-10, 30, x + 10, 50, fill="red")
    apples.append(apple)
    canvas.after(random.randint(1000,2000), create_apple)

def update_all():
    global basket
    basket_coords = canvas.coords(basket)
    for apple in apples:
        canvas.move(apple, 0, 10)
        apple_coords = canvas.coords(apple)
        if (apple_coords[1] >= basket_coords[1] and
        apple_coords[2] >= basket_coords[0] and
        apple_coords[0] <= basket_coords[2]):
            apples.remove(apple)
            canvas.delete(apple)

    canvas.after(50, update_all)
        

create_apple()
update_all()

