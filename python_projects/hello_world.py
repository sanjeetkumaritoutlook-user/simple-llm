import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x200")  # width x height

# Add a label widget
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=20)

# Add a button
def on_click():
    label.config(text="You clicked the button!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

# Run the app
root.mainloop()
