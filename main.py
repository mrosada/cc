import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Create the entry widget for displaying calculations
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.display = tk.Entry(root, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        # Define button texts and layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # Create and place buttons in the grid
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda btn=button: self.on_button_click(btn)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button_text):
        if button_text == 'C':
            self.result_var.set("0")
        elif button_text == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            if current_text == "0":
                self.result_var.set(button_text)
            else:
                self.result_var.set(current_text + button_text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
