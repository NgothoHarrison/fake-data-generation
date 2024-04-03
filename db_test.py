import psycopg2


def test_db_connection():
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

        # Print a success message
        print("Connected to the database successfully.")

        # Close the cursor and connection
        cursor.close()
        connection.close()
    except Exception as e:
        # Print an error message if connection fails
        print(f"Error connecting to the database: {e}")


test_db_connection()
