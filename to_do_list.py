import tkinter as tk
from tkinter import messagebox
import random

# Function to add a new task with a color animation
def add_task():
    task = task_entry.get()
    if task:
        color = random.choice(colors)  # Randomly select a color
        task_listbox.insert(tk.END, task)
        task_listbox.itemconfig(tk.END, {'bg': color})  # Set background color
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to update a selected task with a color animation
def update_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        updated_task = task_entry.get()
        if updated_task:
            color = random.choice(colors)  # Randomly select a color
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task[0], updated_task)
            task_listbox.itemconfig(selected_task[0], {'bg': color})  # Set background color
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        messagebox.showwarning("Warning", "Please select a task to update!")

# Function to delete a selected task
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Create the main application window
root = tk.Tk()
root.title("To-Do List Application")

# Define a list of colors for task items
colors = ['#FFC0CB', '#FFA07A', '#FFD700', '#90EE90', '#ADD8E6', '#FFB6C1']

# Create an input field for task entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, bg='white')
task_listbox.pack()

# Create buttons for adding, updating, and deleting tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
update_button = tk.Button(root, text="Update Task", command=update_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)

add_button.pack(pady=5)
update_button.pack(pady=5)
delete_button.pack(pady=5)

# Run the application
root.mainloop()