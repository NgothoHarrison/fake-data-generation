import psycopg2
from faker import Faker
import random


# Function to generate random data
def generate_data():
    fake = Faker()
    full_name = fake.name()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=90)
    gender = random.choice(['Male', 'Female'])
    id_no = fake.random_number(digits=10)
    district_of_birth = fake.city()
    division = fake.state()
    location = fake.street_name()
    sublocation = fake.street_address()
    active_warranty = fake.boolean(chance_of_getting_true=50)  # 50% chance of being True
    photo = psycopg2.Binary(fake.binary(length=random.randint(1000, 5000)))  # Random binary data
    license_number = fake.random_number(digits=10)
    return (full_name, dob, gender, id_no, district_of_birth, division, location, sublocation, active_warranty, photo,
            license_number)


# Function to insert data into the database
def insert_data():
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

        # Generate random data and insert into the info_table
        data = generate_data()
        insert_query = """
            INSERT INTO info_table (full_name, dob, gender, id_no, district_of_birth, division, location, sublocation, active_warranty, photo, license_number)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, data)

        # Commit the transaction
        connection.commit()

        # Print a success message
        print("Data inserted into the info_table successfully.")

        # Close the cursor and connection
        cursor.close()
        connection.close()
    except Exception as e:
        # Print an error message if connection fails
        print(f"Error connecting to the database: {e}")


insert_data()
