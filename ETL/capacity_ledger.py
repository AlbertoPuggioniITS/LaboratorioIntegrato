# Import necessary libraries
import requests
import mysql.connector
from requests_ntlm import HttpNtlmAuth

# Function for API requests
## Added username, password, and domain for connecting to Business Central
def get_api_data(api_url, bc_username, bc_password, bc_domain):
    try:
        response = requests.get(api_url, auth=HttpNtlmAuth(bc_username, bc_password, bc_domain))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

# Function that inserts/updates records in the database
def update_or_insert_data_in_database(data, cursor):
    try:
        # Exclude columns "@odata.etag" and "SystemId" from the API for import into the database
        excluded_columns = ["@odata.etag", "SystemId"]
        data = {key: value for key, value in data.items() if key not in excluded_columns}

        # Added condition to exclude records with 'starting_time' or 'ending_time' set to '0000-00-00 00:00:00' from being imported into the database
        if str(data['starting_time']).startswith('00:00') or str(data['ending_time']).startswith('00:00'):
            print("The record will not be inserted as starting_time or ending_time is '00:00'.")
            return

        cursor.execute('INSERT INTO capacity_ledger (entry_no, posting_date, item_no, type, no, document_no, description, routing_no, routing_reference_no, operation_no, output_quantity, unit_of_measure_code, scrap_quantity, setup_time, run_time, stop_time, cap_unit_of_measure_code, starting_time, ending_time, order_type, order_no, order_line_no) '
                       'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '
                       '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE posting_date = VALUES(posting_date), '
                       'item_no = VALUES(item_no), type = VALUES(type), no = VALUES(no), document_no = VALUES(document_no), description = VALUES(description), routing_no = VALUES(routing_no), routing_reference_no = VALUES(routing_reference_no), '
                       'operation_no = VALUES(operation_no), output_quantity = VALUES(output_quantity), unit_of_measure_code = VALUES(unit_of_measure_code), scrap_quantity = VALUES(scrap_quantity), setup_time = VALUES(setup_time), run_time = VALUES(run_time), stop_time = VALUES(stop_time), '
                       'cap_unit_of_measure_code = VALUES(cap_unit_of_measure_code), starting_time = VALUES(starting_time), ending_time = VALUES(ending_time), order_type = VALUES(order_type), order_no = VALUES(order_no), order_line_no = VALUES(order_line_no)',

                       (data['entry_no'], data['posting_date'], data['item_no'], data['type'], data['no'],
                        data['document_no'], data['description'], data['routing_no'], data['routing_reference_no'], data['operation_no'], data['output_quantity'], data['unit_of_measure_code'], data['scrap_quantity'], data['setup_time'], data['run_time'], data['stop_time'], data['cap_unit_of_measure_code'], data['starting_time'], data['ending_time'], data['order_type'],
                        data['order_no'], data['order_line_no']))
        print("Data inserted or updated in the database successfully.")
    except mysql.connector.Error as err:
        print(f"Error during database operation: {err}")
        raise

# Function that fetches APIs from a predefined route + database connection settings
def main():
    api_url = "http://localhost:7048/BC210/api/its/gamma/v1.0/companies(7841464b-e73a-ed11-bbaf-6045bd8e5a17)/capacityentries"
    #api_url = 'https://mocki.io/v1/f9e1d377-9b43-41a5-a7b0-6f7e8ae28cf5'
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

        for api_data in api_data_list['value']:
            # Insert or update data in the database
            update_or_insert_data_in_database(api_data, cursor)

        # Commit changes
        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection with the database
        cursor.close()
        conn.close()
