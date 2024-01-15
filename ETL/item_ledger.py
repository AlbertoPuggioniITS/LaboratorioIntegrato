# Import necessary libraries
import requests
import mysql.connector
from requests_ntlm import HttpNtlmAuth

# Function to retrieve data from APIs
## Added username, password, and domain for connection with Business Central
def get_api_data(api_url, bc_username, bc_password, bc_domain):
    try:
        # Added auth=HttpNtlmAuth to the response
        response = requests.get(api_url, auth=HttpNtlmAuth(bc_username, bc_password, bc_domain))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

# Function to insert/update records in the database
def update_or_insert_data_in_database(data, cursor):
    try:
        # Remove unwanted columns from the data dictionary
        excluded_columns = ["@odata.etag", "SystemId"]
        data = {key: value for key, value in data.items() if key not in excluded_columns}

        cursor.execute("""
            INSERT INTO item_ledger 
            (entry_no, item_no, posting_date, entry_type, source_no, document_no, description, location_code, 
            quantity, unit_of_measure_code, item_category_code, document_type, document_line_no, order_type, 
            order_no, order_line_no) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
            ON DUPLICATE KEY UPDATE 
            item_no = VALUES(item_no), posting_date = VALUES(posting_date), entry_type = VALUES(entry_type), 
            source_no = VALUES(source_no), document_no = VALUES(document_no), description = VALUES(description), 
            location_code = VALUES(location_code), quantity = VALUES(quantity), unit_of_measure_code = VALUES(unit_of_measure_code), 
            item_category_code = VALUES(item_category_code), document_type = VALUES(document_type), 
            document_line_no = VALUES(document_line_no), order_type = VALUES(order_type), 
            order_no = VALUES(order_no), order_line_no = VALUES(order_line_no)
        """,
        (data['entry_no'], data['item_no'], data['posting_date'], data['entry_type'], data['source_no'],
         data['document_no'], data['description'], data['location_code'], data['quantity'],
         data['unit_of_measure_code'], data['item_category_code'], data['document_type'],
         data['document_line_no'], data['order_type'], data['order_no'], data['order_line_no']))
        print("Data inserted or updated in the database successfully.")
    except mysql.connector.Error as err:
        print(f"Error during database operation: {err}")
        raise

# Function that fetches APIs from a predefined route + database connection settings
def main():
    api_url = "http://localhost:7048/BC210/api/its/gamma/v1.0/companies(7841464b-e73a-ed11-bbaf-6045bd8e5a17)/ledgerentries"
    #api_url = 'https://mocki.io/v1/3147771d-a04c-442b-b857-6f068c7c29e5'
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'laboratorio'
    }

    # Business Central credentials for authentication
    bc_username = 'ICTS22-24.438'
    bc_password = '********'
    bc_domain = '\studenti'

    # Establish a connection to the database
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Get data from APIs
        api_data_list = get_api_data(api_url, bc_username, bc_password, bc_domain)

        # Insert or update data in the database
        for api_data in api_data_list['value']:
            update_or_insert_data_in_database(api_data, cursor)

        # Commit changes
        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the database connection
        cursor.close()
        conn.close()
