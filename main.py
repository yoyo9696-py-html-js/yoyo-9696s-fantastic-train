
from ai_character_sdk import Character
import pyttsx3 as engine
import tkinter as tk
import tkinter as tk

def draw_yoyo9696():
    root = tk.Tk()
    root.title("yoyo9696")
    
    canvas = tk.Canvas(root, width=400, height=400, bg='black')
    canvas.pack()
    
    # Left eye (large light grey oval)
    canvas.create_oval(100, 120, 160, 200, fill='light grey', outline='black', width=2)
    
    # Right eye (large light grey oval)
    canvas.create_oval(240, 120, 300, 200, fill='light grey', outline='black', width=2)
    
    # Left pupil (vertical light blue oval)
    canvas.create_oval(120, 140, 140, 180, fill='light blue', outline='black', width=2)
    
    # Right pupil (vertical light blue oval)
    canvas.create_oval(260, 140, 280, 180, fill='light blue', outline='black', width=2)
    
    # Large inverted yellow triangle above center of eyes
    canvas.create_polygon(200, 50, 160, 110, 240, 110, fill='yellow', outline='black', width=2)
    
    # Small yellow triangle below left eye
    canvas.create_polygon(130, 210, 115, 230, 145, 230, fill='yellow', outline='black', width=2)
    
    # Small yellow triangle below right eye
    canvas.create_polygon(270, 210, 255, 230, 285, 230, fill='yellow', outline='black', width=2)
    
    # Small red rectangle between eyes (slightly below center)
    canvas.create_rectangle(185, 195, 215, 210, fill='red', outline='black', width=2)
    
    # Light pink rectangle (below red rectangle)
    canvas.create_rectangle(175, 215, 195, 230, fill='light pink', outline='black', width=2)
    
    # Light purple rectangle (below red rectangle)
    canvas.create_rectangle(205, 215, 225, 230, fill='light purple', outline='black', width=2)
    
    root.mainloop()


 
# Create a character
hero = Character(
    name="YOYO9696.EXE",
    character_class="VIRTUAL PET",
    personality={"bravery": 90.0, "kindness": 100.0}
)

# Use the character
response = hero.think("I see a VIRUS  approaching")
engine.say(response.content)

# Remember experiences
hero.remember("The VIRUS was actually an ANTIVIRUS", importance=100.0)

# Learn from outcomes
hero.learn(outcome="you just created me in 29/02/2024(leap day)", success=True, reward=100.0)
hero.learn(outcome="Made a new ally", success=True, reward=100.0)
hero.learn(outcome="Made a PYTHON CODE WITH TURTLE ", success=True, reward=100.0)

if __name__ == "__main__" 
draw_yoyo9696()
hero.remember()
hero.learn()
hero.remember()
hero.learn()
hero.remember()
hero.learn()
hero.remember()
