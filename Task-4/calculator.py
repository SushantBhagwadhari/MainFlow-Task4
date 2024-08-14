import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Arithmetic Calculator")
        self.window.configure(bg="grey")  # Set the background color of the calculator to grey
        self.window.geometry("240x325")  # Set the size of the calculator window to 250x250 pixels
        self.window.resizable(False, False)  # Make the window non-resizable

        self.entry_field = tk.Entry(self.window, width=25, borderwidth=5, bg="black", fg="white", font=("Arial", 12))  # Set the background color of the entry field to black and the text color to white
        self.entry_field.grid(row=0, column=0, columnspan=4, pady=5)  # Add some padding to the top of the entry field

        self.create_buttons()

        self.window.bind("<Return>", self.equals_button)  # Bind the Enter key to the equals button

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button in ['+', '-', '*', '/']:  # Color the operation buttons lime
                tk.Button(self.window, text=button, width=5, height=2, command=lambda button=button: self.click_button(button), bg="lime", font=("Arial", 12)).grid(row=row_val, column=col_val, pady=2)  # Add some padding to the top and bottom of the buttons
            elif button == '=':  # Color the equals button white
                tk.Button(self.window, text=button, width=5, height=2, command=lambda button=button: self.click_button(button), bg="white", font=("Arial", 12)).grid(row=row_val, column=col_val, pady=2)
            else:  # Color the numeric buttons cyan
                tk.Button(self.window, text=button, width=5, height=2, command=lambda button=button: self.click_button(button), bg="cyan", font=("Arial", 12)).grid(row=row_val, column=col_val, pady=2)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.window, text="<-", width=5, height=2, command=self.back_button, bg="lime", font=("Arial", 12)).grid(row=row_val, column=0, columnspan=1, pady=2)  # Add some padding to the top and bottom of the back button
        tk.Button(self.window, text="C", width=10, height=2, command=self.clear_entry, bg="red", font=("Arial", 12)).grid(row=row_val, column=1, columnspan=3, pady=2)  # Add some padding to the top and bottom of the clear button

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry_field.get())
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, str(result))
            except Exception as e:
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, "Error")
        else:
            if button in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', '*', '/']:
                self.entry_field.insert(tk.END, button)

    def equals_button(self, event):
        try:
            result = eval(self.entry_field.get())
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, str(result))
        except Exception as e:
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, "Error")

    def clear_entry(self):
        self.entry_field.delete(0, tk.END)

    def back_button(self):
        current_text = self.entry_field.get()
        self.entry_field.delete(0, tk.END)
        self.entry_field.insert(tk.END, current_text[:-1])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()