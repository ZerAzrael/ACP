import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Factify")
        self.root.geometry("800x600")

        # Database simulation (in-memory dictionary)
        self.user_db = {}
        self.fact_db = []  # Placeholder for the fact database
        self.ratings = []  # Placeholder for storing ratings

        # Dark mode state
        self.is_dark_mode = True

        # Initialize UI
        self.create_toggle_button()
        self.create_login_screen()
        self.apply_theme()

    def create_toggle_button(self):
        self.toggle_button = tk.Button(
            self.root, text="🌙", font=("Arial", 12), width=3, command=self.toggle_theme
        )
        self.toggle_button.place(x=10, y=10)

    def create_login_screen(self):
        self.clear_screen()

        self.title_label = tk.Label(self.root, text="Factify", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        self.username_label = tk.Label(self.root, text="Username:", font=("Arial", 12))
        self.username_label.pack(pady=5)

        self.username_entry = tk.Entry(self.root, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Password:", font=("Arial", 12))
        self.password_label.pack(pady=5)

        self.password_entry = tk.Entry(self.root, font=("Arial", 12), show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Login", font=("Arial", 12), command=self.login)
        self.login_button.pack(pady=15)

        self.register_button = tk.Button(self.root, text="Register", font=("Arial", 12), command=self.create_register_screen)
        self.register_button.pack(pady=15)

        self.forgot_button = tk.Button(self.root, text="Forgot Password", font=("Arial", 12), command=self.create_forgot_password_screen)
        self.forgot_button.pack(pady=15)

        self.delete_button = tk.Button(self.root, text="Delete Account", font=("Arial", 12), command=self.create_delete_account_screen)
        self.delete_button.pack(pady=15)

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()

    def apply_theme(self):
        if self.is_dark_mode:
            self.root.configure(bg="black")
            text_color = "white"
            button_color = "purple"
            entry_bg = "black"
            entry_fg = "white"
            self.toggle_button.configure(text="☀️", bg="black", fg="white")
        else:
            self.root.configure(bg="white")
            text_color = "black"
            button_color = "lime green"
            entry_bg = "white"
            entry_fg = "black"
            self.toggle_button.configure(text="🌙", bg="white", fg="black")

        # Update widget colors
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg=self.root["bg"], fg=text_color)
            elif isinstance(widget, tk.Button):
                widget.configure(bg=button_color, fg=text_color)
            elif isinstance(widget, tk.Entry):
                widget.configure(bg=entry_bg, fg=entry_fg)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_toggle_button()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.user_db and self.user_db[username]["password"] == password:
            messagebox.showinfo("Login Success", "Welcome back!")
            self.create_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def create_register_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Register", font=("Arial", 24, "bold")).pack(pady=20)
        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=5)
        username_entry = tk.Entry(self.root, font=("Arial", 12))
        username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", font=("Arial", 12)).pack(pady=5)
        password_entry = tk.Entry(self.root, font=("Arial", 12), show="*")
        password_entry.pack(pady=5)

        def submit():
            username = username_entry.get()
            password = password_entry.get()
            if username in self.user_db:
                messagebox.showerror("Error", "Username already exists.")
            else:
                code = f"{random.randint(100, 999)}"
                self.user_db[username] = {"password": password, "code": code}
                messagebox.showinfo("Success", f"Registration successful! Your code is {code}")
                self.create_login_screen()

        tk.Button(self.root, text="Submit", font=("Arial", 12), command=submit).pack(pady=15)
        tk.Button(self.root, text="Back", font=("Arial", 12), command=self.create_login_screen).pack(pady=15)

    def create_forgot_password_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Forgot Password", font=("Arial", 24, "bold")).pack(pady=20)
        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=5)
        username_entry = tk.Entry(self.root, font=("Arial", 12))
        username_entry.pack(pady=5)

        tk.Label(self.root, text="Three-Digit Code:", font=("Arial", 12)).pack(pady=5)
        code_entry = tk.Entry(self.root, font=("Arial", 12))
        code_entry.pack(pady=5)

        tk.Label(self.root, text="New Password:", font=("Arial", 12)).pack(pady=5)
        new_password_entry = tk.Entry(self.root, font=("Arial", 12), show="*")
        new_password_entry.pack(pady=5)

        def submit():
            username = username_entry.get()
            code = code_entry.get()
            new_password = new_password_entry.get()
            if username not in self.user_db:
                messagebox.showerror("Error", "Username not found.")
            elif self.user_db[username]["code"] != code:
                messagebox.showerror("Error", "Incorrect code.")
            else:
                self.user_db[username]["password"] = new_password
                messagebox.showinfo("Success", "Password updated successfully!")
                self.create_login_screen()

        tk.Button(self.root, text="Submit", font=("Arial", 12), command=submit).pack(pady=15)
        tk.Button(self.root, text="Back", font=("Arial", 12), command=self.create_login_screen).pack(pady=15)

    def create_delete_account_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Delete Account", font=("Arial", 24, "bold")).pack(pady=20)
        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=5)
        username_entry = tk.Entry(self.root, font=("Arial", 12))
        username_entry.pack(pady=5)

        tk.Label(self.root, text="Three-Digit Code:", font=("Arial", 12)).pack(pady=5)
        code_entry = tk.Entry(self.root, font=("Arial", 12))
        code_entry.pack(pady=5)

        def submit():
            username = username_entry.get()
            code = code_entry.get()
            if username not in self.user_db:
                messagebox.showerror("Error", "Username not found.")
            elif self.user_db[username]["code"] != code:
                messagebox.showerror("Error", "Incorrect code.")
            else:
                del self.user_db[username]
                messagebox.showinfo("Success", "Account deleted successfully!")
                self.create_login_screen()

        tk.Button(self.root, text="Submit", font=("Arial", 12), command=submit).pack(pady=15)
        tk.Button(self.root, text="Back", font=("Arial", 12), command=self.create_login_screen).pack(pady=15)

    def create_dashboard(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to Factify!", font=("Arial", 30, "bold"), bg=self.root["bg"], fg=self.get_text_color()).pack(pady=20)

        # Add a Fact button
        def add_fact():
            fact_input = simpledialog.askstring("Add a Fact", "Enter a new fact:")
            if fact_input:
                self.fact_db.append(fact_input)
                messagebox.showinfo("Success", "Fact added successfully!")

        add_fact_button = tk.Button(self.root, text="Add a Fact", font=("Arial", 30), command=add_fact)
        add_fact_button.pack(pady=20)

        # Generate button
        def generate_fact():
            if self.fact_db:
                fact = random.choice(self.fact_db)
                messagebox.showinfo("Generated Fact", fact)
            else:
                messagebox.showwarning("No Facts", "No facts available in the database.")

        generate_button = tk.Button(self.root, text="Generate", font=("Arial", 30), command=generate_fact)
        generate_button.pack(pady=20)

        # Rate button
        def rate_fact():
            rate = simpledialog.askinteger("Rate Fact", "Rate this fact from 1 to 5:", minvalue=1, maxvalue=5)
            if rate:
                self.ratings.append(rate)
                messagebox.showinfo("Rating Submitted", f"Your rating of {rate} has been submitted.")

        rate_button = tk.Button(self.root, text="Rate", font=("Arial", 30), command=rate_fact)
        rate_button.pack(pady=20)

    def get_text_color(self):
        return "white" if self.is_dark_mode else "black"


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
