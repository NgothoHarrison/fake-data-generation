import tkinter as tk
from tkinter import scrolledtext
from faker import Faker


# Function to generate random data
def generate_data():
    fake = Faker()
    data = ""
    # Generate random data for 10 records
    for _ in range(30):
        name = fake.name()
        email = fake.email()
        address = fake.address()
        phone_number = fake.phone_number()
        dob = fake.date_of_birth(minimum_age=18, maximum_age=90)
        # Append the data to the string
        data += f"Name: {name}, Email: {email}, Address: {address}, Phone Number: {phone_number}, Date of Birth: {dob}\n"
    # Update the text area with generated data
    text_area.delete(1.0, tk.END)  # Clear previous data
    text_area.insert(tk.END, data)


# Create a Tkinter window
window = tk.Tk()
window.title("Random Data Generator")


# Create a button to generate data
generate_button = tk.Button(window, text="Generate Data", command=generate_data)
generate_button.pack(pady=10)

# Create a scrolled text area to display generated data
text_area = scrolledtext.ScrolledText(window, width=160, height=20)
text_area.pack(padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
