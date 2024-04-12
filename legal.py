import psycopg2
from faker import Faker

# Create an instance of the Faker class
fake = Faker()


# Function to generate random data for the legal_info_table
def generate_legal_data():
    # Generate random data for each column
    case_number = fake.random_number(digits=8)
    offence = fake.sentence(nb_words=3)
    arrest_date = fake.date_this_decade()
    court_date = fake.date_between(start_date=arrest_date, end_date='+1y')
    verdict = fake.random_element(elements=("Guilty", "Not Guilty", "Dismissed"))
    sentence = fake.sentence(nb_words=6)

    # Return data as tuple
    return (case_number, offence, arrest_date, court_date, verdict, sentence)


# Function to insert data into the legal_info_table
def insert_legal_data():
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

        # Generate random data and insert into the legal_info_table
        data = generate_legal_data()
        insert_query = """
            INSERT INTO legal_info_table (case_number, offence, arrest_date, court_date, verdict, sentence)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, data)

        # Commit the transaction
        connection.commit()

        # Print a success message
        print("Data inserted into the legal_info_table successfully.")

        # Close the cursor and connection
        cursor.close()
        connection.close()
    except Exception as e:
        # Print an error message if connection fails
        print(f"Error connecting to the database: {e}")


insert_legal_data()
