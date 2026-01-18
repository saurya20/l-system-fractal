import turtle
import tkinter as tk



def expand_lsystem(axiom, rules, iterations):
    #expanding the string
    current_string = axiom

    for _ in range(iterations):
        new_string = ""

        for char in current_string:
            if char in rules:
                new_string += rules[char]
            else:
                #doesnt change other symbols
                new_string += char

        current_string = new_string

    return current_string


def drawlsystem(t, instruction, angle, step):
    stack = []
    for char in instruction:
        if char == "F":
            t.forward(step)

        elif char == "+":
            t.right(angle)

        elif char == "-":
            t.left(angle)

        elif char == "[":
            position = t.position()
            heading = t.heading()
            stack.append((position, heading))
            depth = len(stack)
            green=min(1,0.2+depth*0.2)
            t.pencolor(0.3, green, 0)

        elif char == "]":
            position, heading = stack.pop()
            t.penup()
            t.goto(position)
            t.setheading(heading)
            t.pendown()
            depth = len(stack)
            green = min(1, 0.2 + depth * 0.2)
            t.pencolor(0.3, green, 0)


def parse_rules(rules_text):
    rules = {}
    parts = rules_text.split(",")

    for part in parts:
        symbol, replacement = part.split(":")
        rules[symbol.strip()] = replacement.strip()

    return rules


if __name__ == "__main__":
    root = tk.Tk()
    root.title("L-System Fractal Generator")

    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack(side=tk.RIGHT)

    t = turtle.RawTurtle(canvas)
    t.speed(0)
    turtle.colormode(1)

    # --- controls --
    control_frame = tk.Frame(root)
    control_frame.pack(side=tk.LEFT, padx=10)

    tk.Label(control_frame, text="Axiom").pack()
    axiom_entry = tk.Entry(control_frame)
    axiom_entry.pack()
    axiom_entry.insert(0, "F")

    tk.Label(control_frame, text="Rules (F:F+F-F)").pack()
    rules_entry = tk.Entry(control_frame)
    rules_entry.pack()
    rules_entry.insert(0, "F:F[+F]F[-F]F")

    tk.Label(control_frame, text="Angle").pack()
    angle_entry = tk.Entry(control_frame)
    angle_entry.pack()
    angle_entry.insert(0, "25")

    tk.Label(control_frame, text="Iterations").pack()
    iterations_entry = tk.Entry(control_frame)
    iterations_entry.pack()
    iterations_entry.insert(0, "4")

    def generate():
        t.clear()
        t.penup()
        t.home()
        t.goto(-canvas.winfo_width() // 2 + 20, 0)
        t.setheading(0)
        t.pendown()
        axiom = axiom_entry.get()
        rules_text = rules_entry.get()
        angle = int(angle_entry.get())
        iterations = int(iterations_entry.get())

        step = 18 - iterations*2
        if step < 4:
            step = 4

        rules = parse_rules(rules_text)
        instructions = expand_lsystem(axiom, rules, iterations)

        turtle.tracer(0, 0)
        drawlsystem(t, instructions, angle, step)
        turtle.update()

    generate_button = tk.Button(control_frame, text="Generate", command=generate)
    generate_button.pack(pady=10)

    root.mainloop()
