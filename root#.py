import tkinter as tk

def update_labels(event):
    selected_option = selected_option_var.get()
    
    if selected_option == "Hello":
        label.config(text="You selected 'Hello'.")
    elif selected_option == "World":
        label.config(text="You selected 'World'.")
    else:
        label.config(text="Please select 'Hello' or 'World'.")

root = tk.Tk()
root.title("Update Label Text on OptionMenu Selection")

options = ["Hello", "World"]

selected_option_var = tk.StringVar()
selected_option_var.set(options[0])

# Create an OptionMenu widget with the options and set the command to update_label_text
option_menu = tk.OptionMenu(root, selected_option_var, *options, command=update_labels)
option_menu.pack()

# Create a label with initial text
label = tk.Label(root, text="Select an option from the menu.")
label.pack()

root.mainloop()
