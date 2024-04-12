import tkinter as tk
import psycopg2

def fetch_data():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            dbname='project',
            user='admin',
            password='mypassword',
            host='localhost',
            port='5432'
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Fetch all data from the database
        cursor.execute("SELECT * FROM info_table")
        rows = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Display the data in a Tkinter window
        root = tk.Tk()
        root.title("Data from PostgreSQL Database")

        # Create a text box to display the fetched data
        text_box = tk.Text(root, height=100, width=150)
        text_box.pack()

        # Insert the fetched data into the text box
        for row in rows:
            text_box.insert(tk.END, row)
            text_box.insert(tk.END, '\n')

        # Function to execute when the button is clicked
        def execute_command():
            fetch_data()

        # Create a button to execute the command
        fetch_button = tk.Button(root, text="Fetch Data", command=execute_command)
        fetch_button.pack()

        root.mainloop()

    except Exception as e:
        # Print an error message if connection fails
        print(f"Error connecting to the database: {e}")

fetch_data()
