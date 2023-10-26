import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def submit():
    username = entry1.get()
    mobile_number = entry2.get()
    email = entry3.get()
    password = entry4.get()

    # Add your validation logic here
    if not (username and mobile_number and email and password):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Check if username is unique
    connection = sqlite3.connect("user_accounts.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()
    connection.close()

    if existing_user:
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        return

    # If username is unique, proceed with insertion
    connection = sqlite3.connect("user_accounts.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, mobile_number, email, password) VALUES (?, ?, ?, ?)",
                   (username, mobile_number, email, password))
    connection.commit()
    connection.close()

    messagebox.showinfo("Success", "Account created successfully!")
    window.destroy()  # Close the create account window

def createAcc():
    window.withdraw()  # Hide the login window
    page2 = tk.Toplevel()  # Create a new window for account creation
    page2.title("Create account page")
    page2.geometry('1000x600')
    page2.configure(bg="sky blue")  # Set the background color to sky blue

    label1 = tk.Label(page2, text="Create a new account!!", font=("Helvetica", 18), bg="sky blue", fg="white", anchor='center')
    label1.grid(row=0, column=1)

    label2 = tk.Label(page2, text="Username ", fg="black", bg="azure2", anchor='center', justify='center')
    label2.grid(row=1, column=0)
    global entry1
    entry1 = tk.Entry(page2, width=50, borderwidth=10, justify='center')
    entry1.grid(row=1, column=1)

    label3 = tk.Label(page2, text="Mobile number ", fg="black", bg="azure2", anchor='center', justify='center')
    label3.grid(row=2, column=0)
    global entry2
    entry2 = tk.Entry(page2, width=50, borderwidth=10, justify='center')
    entry2.grid(row=2, column=1)

    label4 = tk.Label(page2, text="Email id ", fg="black", bg="azure2", anchor='center', justify='center')
    label4.grid(row=3, column=0)
    global entry3
    entry3 = tk.Entry(page2, width=50, borderwidth=10, justify='center')
    entry3.grid(row=3, column=1)

    label5 = tk.Label(page2, text="Password ", fg="black", bg="azure2", anchor='center', justify='center')
    label5.grid(row=4, column=0)
    global entry4
    entry4 = tk.Entry(page2, width=50, borderwidth=10, justify='center', show='*')
    entry4.grid(row=4, column=1)

    submit_button = tk.Button(page2, command=submit, text="Create Account", bg="red", fg="white")
    submit_button.grid(row=6, column=1)
class TravelAgencyApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Travel Agency")
   
            # Configure the background color to pink
            self.root.configure(bg="pink")
   
            # Configure text font size
            text_font = ("Helvetica", 25)
            self.city_distances = {
    'Mumbai': {'Pune': 150, 'Chattrapati Sambhajinagar': 200, 'Nagpur': 800, 'Nashik': 170, 'Nanded': 600, 'jalna': 400, 'hingoli': 300, 'parbhani': 250, 'delhi': 200, 'jalgaon': 300, 'thane': 200, 'beed': 250, 'amravati': 400, 'solapur': 350, 'mahabaleshwar': 300, 'lonavla': 250, 'shirdi': 300},
    'Pune': {'Mumbai': 150, 'Chattrapati Sambhajinagar': 100, 'Nagpur': 900, 'Nashik': 200, 'Nanded': 500, 'jalna': 350, 'hingoli': 300, 'parbhani': 300, 'delhi': 350, 'jalgaon': 250, 'thane': 200, 'beed': 300, 'amravati': 450, 'solapur': 400, 'mahabaleshwar': 350, 'lonavla': 300, 'shirdi': 350},
    'Chattrapati Sambhajinagar': {'Mumbai': 200, 'Pune': 100, 'Nagpur': 1000, 'Nashik': 180, 'Nanded': 400, 'jalna': 300, 'hingoli': 250, 'parbhani': 350, 'delhi': 350, 'jalgaon': 250, 'thane': 200, 'beed': 350, 'amravati': 450, 'solapur': 400, 'mahabaleshwar': 350, 'lonavla': 300, 'shirdi': 350},
    'Nagpur': {'Mumbai': 800, 'Pune': 900, 'Chattrapati Sambhajinagar': 1000, 'Nashik': 700, 'Nanded': 100, 'jalna': 500, 'hingoli': 400, 'parbhani': 200, 'delhi': 200, 'jalgaon': 200, 'thane': 200, 'beed': 200, 'amravati': 250, 'solapur': 200, 'mahabaleshwar': 250, 'lonavla': 300, 'shirdi': 400},
    'Nashik': {'Mumbai': 170, 'Pune': 200, 'Chattrapati Sambhajinagar': 180, 'Nagpur': 700, 'Nanded': 350, 'jalna': 250, 'hingoli': 200, 'parbhani': 300, 'delhi': 300, 'jalgaon': 300, 'thane': 300, 'beed': 300, 'amravati': 350, 'solapur': 300, 'mahabaleshwar': 350, 'lonavla': 300, 'shirdi': 400},
    'Nanded': {'Mumbai': 600, 'Pune': 500, 'Chattrapati Sambhajinagar': 400, 'Nagpur': 100, 'Nashik': 350, 'jalna': 300, 'hingoli': 250, 'parbhani': 350, 'delhi': 350, 'jalgaon': 250, 'thane': 200, 'beed': 350, 'amravati': 450, 'solapur': 400, 'mahabaleshwar': 350, 'lonavla': 300, 'shirdi': 350},
    'jalna': {'Mumbai': 400, 'Pune': 350, 'Chattrapati Sambhajinagar': 300, 'Nagpur': 500, 'Nashik': 250, 'Nanded': 300, 'hingoli': 100, 'parbhani': 150, 'delhi': 300, 'jalgaon': 150, 'thane': 150, 'beed': 250, 'amravati': 250, 'solapur': 200, 'mahabaleshwar': 200, 'lonavla': 200, 'shirdi': 300},
    'hingoli': {'Mumbai': 300, 'Pune': 300, 'Chattrapati Sambhajinagar': 250, 'Nagpur': 400, 'Nashik': 200, 'Nanded': 250, 'jalna': 100, 'parbhani': 180, 'delhi': 250, 'jalgaon': 180, 'thane': 150, 'beed': 200, 'amravati': 250, 'solapur': 200, 'mahabaleshwar': 250, 'lonavla': 250, 'shirdi': 350},
    'parbhani': {'Mumbai': 250, 'Pune': 300, 'Chattrapati Sambhajinagar': 350, 'Nagpur': 200, 'Nashik': 300, 'Nanded': 350, 'jalna': 150, 'hingoli': 180, 'delhi': 300, 'jalgaon': 150, 'thane': 150, 'beed': 250, 'amravati': 250, 'solapur': 200, 'mahabaleshwar': 200, 'lonavla': 200, 'shirdi': 300},
    'delhi': {'Mumbai': 250, 'Pune': 300, 'Chattrapati Sambhajinagar': 350, 'Nagpur': 200, 'Nashik': 300, 'Nanded': 350, 'jalna': 150, 'hingoli': 180, 'parbhani': 300, 'jalgaon': 150, 'thane': 150, 'beed': 250, 'amravati': 250, 'solapur': 200, 'mahabaleshwar': 200, 'lonavla': 200, 'shirdi': 300},
    'jalgaon': {'Mumbai': 250, 'Pune': 300, 'Chattrapati Sambhajinagar': 350, 'Nagpur': 200, 'Nashik': 300, 'Nanded': 350, 'jalna': 150, 'hingoli': 180, 'parbhani': 150, 'delhi': 150, 'thane': 150, 'beed': 250, 'amravati': 250, 'solapur': 200, 'mahabaleshwar': 200, 'lonavla': 200, 'shirdi': 300},
    'thane': {'Mumbai': 250, 'Pune': 300, 'Chattrapati Sambhajinagar': 350, 'Nagpur': 200, 'Nashik': 300, 'Nanded': 350, 'jalna': 150, 'hingoli': 180, 'parbhani': 150, 'delhi': 150, 'jalgaon': 150, 'beed': 250, 'amravati': 250, 'solapur': 200, 'mahabaleshwar': 200, 'lonavla': 200, 'shirdi': 300},
    'beed': {'Mumbai': 250, 'Pune': 300, 'Chattrapati Sambhajinagar': 350, 'Nagpur': 200, 'Nashik': 300, 'Nanded': 350, 'jalna': 150, 'hingoli': 180, 'parbhani': 250, 'delhi': 250, 'jalgaon': 250, 'thane': 250, 'amravati': 250, 'solapur': 200, 'mahabaleshwar': 200, 'lonavla': 200, 'shirdi': 300},
    'amravati': {'Mumbai': 400, 'Pune': 450, 'Chattrapati Sambhajinagar': 450, 'Nagpur': 250, 'Nashik': 350, 'Nanded': 450, 'jalna': 250, 'hingoli': 250, 'parbhani': 450, 'delhi': 450, 'jalgaon': 250, 'thane': 250, 'beed': 250, 'solapur': 150, 'mahabaleshwar': 300, 'lonavla': 250, 'shirdi': 350},
    'solapur': {'Mumbai': 350, 'Pune': 400, 'Chattrapati Sambhajinagar': 400, 'Nagpur': 200, 'Nashik': 300, 'Nanded': 400, 'jalna': 200, 'hingoli': 200, 'parbhani': 400, 'delhi': 400, 'jalgaon': 200, 'thane': 200, 'beed': 200, 'amravati': 150, 'mahabaleshwar': 200, 'lonavla': 150, 'shirdi': 250},
    'mahabaleshwar': {'Mumbai': 300, 'Pune': 350, 'Chattrapati Sambhajinagar': 350, 'Nagpur': 250, 'Nashik': 350, 'Nanded': 350, 'jalna': 200, 'hingoli': 250, 'parbhani': 350, 'delhi': 350, 'jalgaon': 200, 'thane': 200, 'beed': 250, 'amravati': 300, 'solapur': 200, 'lonavla': 150, 'shirdi': 250},
    'lonavla': {'Mumbai': 250, 'Pune': 300, 'Chattrapati Sambhajinagar': 300, 'Nagpur': 300, 'Nashik': 300, 'Nanded': 300, 'jalna': 200, 'hingoli': 250, 'parbhani': 200, 'delhi': 200, 'jalgaon': 200, 'thane': 200, 'beed': 200, 'amravati': 250, 'solapur': 150, 'mahabaleshwar': 150, 'shirdi': 250},
    'shirdi': {'Mumbai': 300, 'Pune': 350, 'Chattrapati Sambhajinagar': 350, 'Nagpur': 400, 'Nashik': 400, 'Nanded': 350, 'jalna': 300, 'hingoli': 350, 'parbhani': 300, 'delhi': 300, 'jalgaon': 300, 'thane': 300, 'beed': 300, 'amravati': 350, 'solapur': 250, 'mahabaleshwar': 250, 'lonavla': 250},
}
            self.hotel_data = {
    'Mumbai': {'QOURA': 2000, 'TAAJ': 1500, '5star': 5000, '3star': 1800, 'HAPPY': 1200, 'SAYLI': 1800, 'click': 1000, 'athithi': 1300, 'taaj': 1000, 'bhoj': 1000, 'Hotel7': 900, 'Hotel8': 1100},
    'Pune': {'HAPPY': 1200, 'SAYLI': 1800, 'l': 1000, 'peace': 1000, 'click': 1000, 'athithi': 1300, 'taaj': 1000, 'bhoj': 1000, 'QOURA': 2000, 'TAAJ': 1500, '5star': 5000, '3star': 1800, 'Hotel7': 900, 'Hotel8': 1100},
    'Chattrapati Sambhajinagar': {'click': 1000, 'athithi': 1300, 'taaj': 1000, 'bhoj': 1000, 'QOURA': 2000, 'TAAJ': 1500, '3star': 1800, 'HAPPY': 1200, 'SAYLI': 1800, 'l': 1000, 'peace': 1000, 'Hotel7': 900, 'Hotel8': 1100},
    'Nagpur': {'Hotel7': 900, 'Hotel8': 1100, 'HAPPY': 1200, 'SAYLI': 1800, 'l': 1000, 'peace': 1000, 'QOURA': 2000, 'TAAJ': 1500, '5star': 5000, '3star': 1800, 'Hotel7': 900, 'Hotel8': 1100},
    'Nashik': {'Hotel9': 800, 'Hotel10': 1200, 'QOURA': 2000, 'TAAJ': 1500, '5star': 5000, '3star': 1800, 'HAPPY': 1200, 'SAYLI': 1800, 'l': 1000, 'peace': 1000, 'click': 1000, 'athithi': 1300, 'taaj': 1000, 'bhoj': 1000},
    'Nanded': {'QOURA': 2200, 'TAAJ': 1600, '5star': 5200, '3star': 1900, 'HAPPY': 1300, 'SAYLI': 1900, 'click': 1100, 'athithi': 1400, 'taaj': 1100, 'bhoj': 1100, 'Hotel7': 950, 'Hotel8': 1150},
    'jalna': {'QOURA': 1800, 'TAAJ': 1400, '5star': 4800, '3star': 1700, 'HAPPY': 1100, 'SAYLI': 1700, 'click': 900, 'athithi': 1200, 'taaj': 900, 'bhoj': 900, 'Hotel7': 800, 'Hotel8': 1000},
    'hingoli': {'QOURA': 1700, 'TAAJ': 1300, '5star': 4700, '3star': 1600, 'HAPPY': 1000, 'SAYLI': 1600, 'click': 800, 'athithi': 1100, 'taaj': 800, 'bhoj': 800, 'Hotel7': 700, 'Hotel8': 900},
    'parbhani': {'QOURA': 1600, 'TAAJ': 1200, '5star': 4600, '3star': 1500, 'HAPPY': 900, 'SAYLI': 1500, 'click': 700, 'athithi': 1000, 'taaj': 700, 'bhoj': 700, 'Hotel7': 600, 'Hotel8': 800},
    'delhi': {'QOURA': 2200, 'TAAJ': 1600, '5star': 5200, '3star': 1900, 'HAPPY': 1300, 'SAYLI': 1900, 'click': 1100, 'athithi': 1400, 'taaj': 1100, 'bhoj': 1100, 'Hotel7': 950, 'Hotel8': 1150},
    'jalgaon': {'QOURA': 2100, 'TAAJ': 1500, '5star': 5100, '3star': 1800, 'HAPPY': 1250, 'SAYLI': 1850, 'click': 1050, 'athithi': 1350, 'taaj': 1050, 'bhoj': 1050, 'Hotel7': 950, 'Hotel8': 1100},
    'thane': {'QOURA': 2100, 'TAAJ': 1550, '5star': 5050, '3star': 1850, 'HAPPY': 1250, 'SAYLI': 1850, 'click': 1050, 'athithi': 1350, 'taaj': 1050, 'bhoj': 1050, 'Hotel7': 950, 'Hotel8': 1150},
    'beed': {'QOURA': 1700, 'TAAJ': 1350, '5star': 4750, '3star': 1650, 'HAPPY': 1150, 'SAYLI': 1650, 'click': 850, 'athithi': 1150, 'taaj': 850, 'bhoj': 850, 'Hotel7': 750, 'Hotel8': 950},
    'amravati': {'QOURA': 2000, 'TAAJ': 1500, '5star': 5000, '3star': 1800, 'HAPPY': 1200, 'SAYLI': 1800, 'click': 1000, 'athithi': 1300, 'taaj': 1000, 'bhoj': 1000, 'Hotel7': 900, 'Hotel8': 1100},
    'solapur': {'QOURA': 1800, 'TAAJ': 1400, '5star': 4800, '3star': 1700, 'HAPPY': 1100, 'SAYLI': 1700, 'click': 900, 'athithi': 1200, 'taaj': 900, 'bhoj': 900, 'Hotel7': 800, 'Hotel8': 1000},
    'mahabaleshwar': {'QOURA': 2200, 'TAAJ': 1600, '5star': 5200, '3star': 1900, 'HAPPY': 1300, 'SAYLI': 1900, 'click': 1100, 'athithi': 1400, 'taaj': 1100, 'bhoj': 1100, 'Hotel7': 950, 'Hotel8': 1150},
    'lonavla': {'QOURA': 2000, 'TAAJ': 1500, '5star': 5000, '3star': 1800, 'HAPPY': 1200, 'SAYLI': 1800, 'click': 1000, 'athithi': 1300, 'taaj': 1000, 'bhoj': 1000, 'Hotel7': 900, 'Hotel8': 1100},
    'shirdi': {'QOURA': 2200, 'TAAJ': 1600, '5star': 5200, '3star': 1900, 'HAPPY': 1300, 'SAYLI': 1900, 'click': 1100, 'athithi': 1400, 'taaj': 1100, 'bhoj': 1100, 'Hotel7': 950, 'Hotel8': 1150},
}

            self.location_label = tk.Label(root, text="Select Current Location:", font=text_font, bg="pink")
            self.location_label.pack()
            self.current_location = ttk.Combobox(root, values=list(self.city_distances.keys()))
            self.current_location.pack()
   
            self.destination_label = tk.Label(root, text="Select Destination:", font=text_font, bg="pink")
            self.destination_label.pack()
            self.destination = ttk.Combobox(root, values=list(self.city_distances.keys()))
            self.destination.pack()
   
            self.transport_mode = tk.StringVar()
            self.mode_label = tk.Label(root, text="Select Mode of Transport:", font=text_font, bg="pink")
            self.mode_label.pack()
            self.car_radio = tk.Radiobutton(root, text="Car", variable=self.transport_mode, value="car")
            self.bus_radio = tk.Radiobutton(root, text="Bus", variable=self.transport_mode, value="bus")
            self.train_radio = tk.Radiobutton(root, text="Train", variable=self.transport_mode, value="train")
            self.car_radio.pack()
            self.bus_radio.pack()
            self.train_radio.pack()
   
            self.destination.bind("<<ComboboxSelected>>", self.update_hotel_dropdown)
   
            self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_travel, font=text_font, bg="pink")
            self.calculate_button.pack()
   
            self.stay_label = tk.Label(root, text="Number of Days in Hotel:", font=text_font, bg="pink")
            self.stay_label.pack()
            self.stay_entry = ttk.Entry(root)
            self.stay_entry.pack()
   
            self.hotel_label = tk.Label(root, text="Select Hotel:", font=text_font, bg="pink")
            self.hotel_label.pack()
            self.hotel = ttk.Combobox(root, values=[])
            self.hotel.pack()
   
            self.total_button = tk.Button(root, text="Calculate travelling total", command=self.total_travel, font=text_font, bg="pink")
            self.total_button.pack()
   
            # Configure the text label to center align
            self.output_text = tk.Label(root, text="", font=text_font, bg="pink")
            self.output_text.pack(expand=True, fill="both")
   
        def update_hotel_dropdown(self, event):
            destination = self.destination.get()
            if destination in self.hotel_data:
                hotels = list(self.hotel_data[destination].keys())
                self.hotel['values'] = hotels
            else:
                self.hotel.set("")  # Clear the hotel selection
                self.hotel['values'] = []
   
        def calculate_travel(self):
            current_location = self.current_location.get()
            destination = self.destination.get()
            mode_of_transport = self.transport_mode.get()
            stay_days = self.stay_entry.get()
   
            if not mode_of_transport:
                self.show_error("Error", "Please enter a valid mode of transport.")
                return
   
            if current_location in self.city_distances and destination in self.city_distances[current_location]:
                distance = self.city_distances[current_location][destination]
                hotel_cost = self.hotel_data[destination] if destination in self.hotel_data else None
                if hotel_cost:
                    result = f"Distance from {current_location} to {destination}: {distance} km\n"
                    result += "Hotel options and cost per day:\n"
                    travel_cost = self.calculate_travel_cost(distance, mode_of_transport)
                    for hotel, cost in hotel_cost.items():
                        result += "{}: ₹{} per day\n".format(hotel, cost)  # Using ₹ for Rupees
                    travel_cost = self.calculate_travel_cost(distance, mode_of_transport)
                    self.show_result("Travel Details", result)
                else:
                    self.show_error("Error", "Hotel information not available for the destination.")
            else:
                self.show_error("Error", "Invalid city names or route not found.")
   
        def total_travel(self):
            current_location = self.current_location.get()
            destination = self.destination.get()
            mode_of_transport = self.transport_mode.get()
            stay_days = self.stay_entry.get()
   
            if not stay_days.isdigit():
                self.show_error("Error", "Please enter a valid number of days for the hotel stay.")
                return
   
            stay_days = int(stay_days)
   
            if current_location in self.city_distances and destination in self.city_distances[current_location]:
                distance = self.city_distances[current_location][destination]
                hotel_cost = self.hotel_data[destination] if destination in self.hotel_data else None
                if hotel_cost:
                    result = f"Distance from {current_location} to {destination}: {distance} km\n"
                    result += "Selected Hotel: {}\n".format(self.hotel.get())
                    travel_cost = self.calculate_travel_cost(distance, mode_of_transport)
                    total_cost = (travel_cost + hotel_cost.get(self.hotel.get(), 0)) * stay_days
                    result += "Total travel cost: ₹{:.2f} per day\n".format(travel_cost)  # Using ₹ for Rupees
                    result += "Total cost including hotel stay for {} days: ₹{:.2f}\n".format(stay_days, total_cost)  # Using ₹ for Rupees
                    self.show_result("Total Travel Cost", result)
                else:
                    self.show_error("Error", "Hotel information not available for the destination.")
            else:
                self.show_error("Error", "Invalid city names or route not found.")
   
        def calculate_travel_cost(self, distance, mode):
            if mode == 'bus':
                return distance * 30  # Sample cost per kilometer for bus
            elif mode == 'car':
                return distance * 50  # Sample cost per kilometer for car
            elif mode == 'train':
                return distance * 65
            else:
                return 0
   
        def show_result(self, title, message):
            result_window = tk.Toplevel(self.root)
            result_window.title(title)
            result_label = tk.Label(result_window, text=message)
            result_label.pack()
   
        def show_error(self, title, message):
            messagebox.showerror(title, message)
def login():
    username = entry1.get()
    password = entry2.get()

    if not (username and password):
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    connection = sqlite3.connect("user_accounts.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    connection.close()

    if user:
        messagebox.showinfo("Success", "Login successful!")
        # Add code to proceed after successful login
        window.destroy()
        if __name__ == "__main__":
            root = tk.Tk()
            app = TravelAgencyApp(root)
       
            # Center the window on the screen
            window_width = 1000
            window_height = 800
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            root.geometry(f'{window_width}x{window_height}+{x}+{y}')
       
            root.mainloop()
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Create a table for user accounts (if not already exists)
connection = sqlite3.connect("user_accounts.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        mobile_number TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
""")
connection.commit()
connection.close()

window = tk.Tk()
window.title("Front page")
window.geometry('320x240')
window.configure(bg="sky blue")  # Set the background color to sky blue

label1 = tk.Label(window, text="Welcome to Login", font=("Helvetica", 18), bg="sky blue", fg="white", anchor='center')
label1.grid(row=0, column=1)

label2 = tk.Label(window, text="Username", fg="black", bg="azure2", anchor='center', justify='center')
label2.grid(row=1, column=0)
entry1 = tk.Entry(window, width=50, borderwidth=10, justify='center')
entry1.grid(row=1, column=1)

label3 = tk.Label(window, text="Password", fg="black", bg="azure2", anchor='center', justify='center')
label3.grid(row=2, column=0)
entry2 = tk.Entry(window, width=50, borderwidth=10, show='*')
entry2.grid(row=2, column=1)

create_acc_button = tk.Button(window, command=createAcc, text="Create a new account?", fg="blue", bg="azure2")
create_acc_button.grid(row=3, column=0)
submit_button = tk.Button(window, command=login, text="Login", bg="red", fg="white")
submit_button.grid(row=3, column=1)

window.mainloop()
