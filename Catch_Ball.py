from tkinter import *
import random

root = Tk()
root.title("Catch the Ball Game")
root.geometry("800x600")
root.config(bg="black")

canvas = Canvas(root, width=800, height=600, bg="black", highlightthickness=0)
canvas.pack()

score = 0
lives = 5
game_over = False

score_text = canvas.create_text(100, 30, text=f"Score: {score}", font=("Arial", 20, "bold"), fill="white")
lives_text = canvas.create_text(700, 30, text=f"Lives: {lives}", font=("Arial", 20, "bold"), fill="red")

paddle = canvas.create_rectangle(350, 550, 450, 570, fill="cyan", outline="cyan")
ball = canvas.create_oval(0, 0, 30, 30, fill="yellow", outline="yellow")
canvas.move(ball, random.randint(100, 700), 0)

paddle_speed = 40
ball_speed = 10

def move_left(event):
    if not game_over:
        x1, y1, x2, y2 = canvas.coords(paddle)
        if x1 > 0:
            canvas.move(paddle, -paddle_speed, 0)

def move_right(event):
    if not game_over:
        x1, y1, x2, y2 = canvas.coords(paddle)
        if x2 < 800:
            canvas.move(paddle, paddle_speed, 0)

def update_ball():
    global score, lives, game_over
    if game_over:
        return
    canvas.move(ball, 0, ball_speed)
    bx1, by1, bx2, by2 = canvas.coords(ball)
    px1, py1, px2, py2 = canvas.coords(paddle)

    if by2 >= py1 and px1 < (bx1 + bx2)/2 < px2:
        score += 1
        canvas.itemconfig(score_text, text=f"Score: {score}")
        reset_ball()
    elif by2 >= 600:
        lives -= 1
        canvas.itemconfig(lives_text, text=f"Lives: {lives}")
        if lives == 0:
            end_game()
        else:
            reset_ball()

    root.after(50, update_ball)

def reset_ball():
    canvas.coords(ball, random.randint(100, 700), 0, random.randint(100, 700) + 30, 30)

def end_game():
    global game_over
    game_over = True
    canvas.create_text(400, 300, text="GAME OVER", font=("Arial", 50, "bold"), fill="red")
    canvas.create_text(400, 370, text=f"Final Score: {score}", font=("Arial", 30, "bold"), fill="white")

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

update_ball()
root.mainloop()
