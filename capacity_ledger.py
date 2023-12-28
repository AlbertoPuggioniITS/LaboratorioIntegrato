import requests
import mysql.connector
from requests_ntlm import HttpNtlmAuth


# Funzione di request per le API's
## Aggiunto username, password e domain per collegarsi a Business Central
def get_api_data(api_url, username, password, domain):
    try:
        response = requests.get(api_url, auth=HttpNtlmAuth(f'{domain}\\{username}', password))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

# Funzione che inserisce / aggiorna i record sul db
def update_or_insert_data_in_database(data, cursor):
    try:
        # Esclude le colonne "@odata.etag e SystemId dalle API per l'importazione delle API nel db
        excluded_columns = ["@odata.etag", "SystemId"]
        data = {key: value for key, value in data.items() if key not in excluded_columns}
        cursor.execute('INSERT INTO capacity_ledger (entry_no, posting_date, item_no, type, no, document_no, description, routing_no, routing_reference_no, operation_no, output_quantity, unit_of_measure_code, scrap_quantity, setup_time, run_time, stop_time, cap_unit_of_measure_code, starting_time, ending_time, order_type, order_no, order_line_no) '
                       'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, '
                       '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE posting_date = VALUES(posting_date), '
                       'item_no = VALUES(item_no), type = VALUES(type), no = VALUES(no), document_no = VALUES(document_no), description = VALUES(description), routing_no = VALUES(routing_no), routing_reference_no = VALUES(routing_reference_no), '
                       'operation_no = VALUES(operation_no), output_quantity = VALUES(output_quantity), unit_of_measure_code = VALUES(unit_of_measure_code), scrap_quantity = VALUES(scrap_quantity), setup_time = VALUES(setup_time), run_time = VALUES(run_time), stop_time = VALUES(stop_time), '
                       'cap_unit_of_measure_code = VALUES(cap_unit_of_measure_code), starting_time = VALUES(starting_time), ending_time = VALUES(ending_time), order_type = VALUES(order_type), order_no = VALUES(order_no), order_line_no = VALUES(order_line_no)',

                       (data['entry_no'], data['posting_date'], data['item_no'], data['type'], data['no'],
                        data['document_no'], data['description'], data['routing_no'], data['routing_reference_no'], data['operation_no'], data['output_quantity'], data['unit_of_measure_code'], data['scrap_quantity'], data['setup_time'], data['run_time'], data['stop_time'], data['cap_unit_of_measure_code'], data['starting_time'], data['ending_time'], data['order_type'],
                        data['order_no'], data['order_line_no']))
        print("Dati inseriti o aggiornati nel database con successo.")
    except mysql.connector.Error as err:
        print(f"Errore durante l'operazione nel database: {err}")
        raise

# Funzione che prende le API's da una route predefinita + impostazioni di connessione con il db
def main():
    #api_url = "http://localhost:7048/BC210/api/its/gamma/v1.0/$metadata#companies(7841464b-e73a-ed11-bbaf-6045bd8e5a17)/capacityentries"
    api_url = 'https://mocki.io/v1/f9e1d377-9b43-41a5-a7b0-6f7e8ae28cf5'
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'laboratorio'
    }

    # Credenziali NTLM per Business Central
    bc_username = 'username_di_business_central'
    bc_password = 'password_di_business_central'
    bc_domain = 'domain_di_business_central'

    # Effettua una connessione al database
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Prende i dati dalle API
        api_data_list = get_api_data(api_url, bc_username, bc_password, bc_domain)

        for api_data in api_data_list['value']:
            # Inserisce o aggiorna dati nel database
            update_or_insert_data_in_database(api_data, cursor)

        # Commit delle modifiche
        conn.commit()

    except mysql.connector.Error as err:
        print(f"Errore durante la connessione al database: {err}")

    except Exception as e:
        print(f"Si è verificato un errore: {e}")

    finally:
        # Chiude la connessione con il db
        cursor.close()
        conn.close()
