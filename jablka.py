import tkinter as tk
import random

# Inicializácia okna
root = tk.Tk()
root.title("Chytanie jabĺk")

# Plátno pre hru
canvas = tk.Canvas(root, width=400, height=600, bg="lightblue")
canvas.pack()

# Hráč (košík)
basket = canvas.create_rectangle(175, 550, 225, 570, fill="brown")

# Premenné
apples = []
obstacles = []
score = 0
lives = 3

# Texty pre skóre a životy
score_text = canvas.create_text(50, 20, text="Skóre: " + str(score))
lives_text = canvas.create_text(350, 20, text="Životy: " + str(lives))

# Pohyb košíka
def move_left(event):
    if canvas.coords(basket)[0] > 0:
        canvas.move(basket, -20, 0)

def move_right(event):
    if canvas.coords(basket)[2] < 400:
        canvas.move(basket, 20, 0)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Generovanie padajúcich objektov
a = tk.PhotoImage(file="Apple.png")
s = tk.PhotoImage(file="Spike.png")

def create_apple():
    global lives, a
    if lives == 0:
        return
    x = random.randint(20, 380)
    # apple = canvas.create_oval(x-10, 0, x+10, 20, fill="red")
    apple = canvas.create_image(x-10, 30, image=a)
    apples.append(apple)
    root.after(random.randint(1000, 2000), create_apple)

def create_obstacle():
    global lives, s
    if lives == 0:
        return
    x = random.randint(20, 380)
    # obstacle = canvas.create_rectangle(x-10, 0, x+10, 20, fill="black")
    obstacle = canvas.create_image(x-10, 30, image=s)
    obstacles.append(obstacle)
    root.after(random.randint(2000, 3000), create_obstacle)

# Aktualizácia hry
def update_game():
    global score, lives
    basket_coords = canvas.coords(basket)
    # Pohyb jabĺk
    for apple in apples:
        canvas.move(apple, 0, 5)
        apple_coords = canvas.coords(apple)
        if canvas.coords(apple)[1]+32 >= 600:  # Jablko spadlo mimo
            apples.remove(apple)
            canvas.delete(apple)
        elif apple_coords[1]+32 >= basket_coords[1] and apple_coords[0]+32 >= basket_coords[0] and apple_coords[0] <= basket_coords[2]:
            score += 1
            apples.remove(apple)
            canvas.delete(apple)
            canvas.itemconfig(score_text, text="Skóre: "+ str(score))

    # Pohyb prekážok
    for obstacle in obstacles:
        canvas.move(obstacle, 0, 5)
        obstacle_coords = canvas.coords(obstacle)
        if canvas.coords(obstacle)[1]+32 >= 600:  # Prekážka spadla mimo
            obstacles.remove(obstacle)
            canvas.delete(obstacle)
        elif obstacle_coords[1]+32 >= basket_coords[1] and obstacle_coords[0]+32 >= basket_coords[0] and obstacle_coords[0] <= basket_coords[2]:
            lives -= 1
            obstacles.remove(obstacle)
            canvas.delete(obstacle)
            canvas.itemconfig(lives_text, text=f"Životy: {lives}")
            if lives == 0:
                canvas.create_text(200, 300, text="Koniec hry!", font=("Arial", 30), fill="red")
                return

    root.after(50, update_game)

# Spustenie hry
create_apple()
create_obstacle()
update_game()

root.mainloop()
