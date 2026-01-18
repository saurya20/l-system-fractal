L-System Fractal Generator
This project implements a simple L-system (Lindenmayer system) visualizer using Python, Tkinter, and Turtle graphics.
 The program expands an initial axiom using production rules defined by the user and renders the resulting structure using turtle graphics.
Features
Parallel L-system string expansion


Turtle graphics interpretation (F, +, -, [, ])


Branching using a stack ([ and ])


Interactive Tkinter GUI for user input


Step-size scaling to keep drawings visible


Depth-based color variation for better visualization


How to Run
Make sure Python is installed.


Run the file:


python system_turtle.py
3. Enter the axiom, rules, angle, and iterations.


4. Click Generate to draw the L-system.


Example Input
Axiom: F
Rules: F:F[+F]F[-F]F
Angle: 25
Iterations: 4

Notes
The project uses only built-in Python libraries.


Turtle graphics are embedded inside a Tkinter window using RawTurtle.

