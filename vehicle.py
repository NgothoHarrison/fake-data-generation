import psycopg2
from faker import Faker

fake = Faker()
def generate_vehicle_data():

    # vehicles = []

    # for _ in range(30):
    # person_id = fake.random_number(digits=8)
    registration_number = fake.random_int(min=10000, max=99999)
    make = fake.company()
    model = fake.word().capitalize()
    year = fake.random_int(min=1980, max=2023)
    color = fake.color_name()

    return (registration_number, make, model, year, color)




def insert_vehicle_data():
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

        # Generate vehicle data
        vehicles_data = generate_vehicle_data()

        # Insert data into the vehicle_info_table
        insert_query = """
            INSERT INTO vehicle_info_table (person_id, registration_number, make, model, year, color)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.executemany(insert_query, vehicles_data)

        # Commit the transaction
        connection.commit()

        # Print a success message
        print("Data inserted into the vehicle_info_table successfully.")

        # Close the cursor and connection
        cursor.close()
        connection.close()
    except Exception as e:
        # Print an error message if connection fails
        print(f"Error connecting to the database: {e}")


insert_vehicle_data()
