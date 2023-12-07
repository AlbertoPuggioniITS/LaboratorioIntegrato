import requests
import mysql.connector
import schedule
import time

# Funzione di request per le API's
def get_api_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

# Fetch per controllare i record presenti sul db
def fetch_data_from_database(cursor, post_id):
    cursor.execute('SELECT postId, userId, title, body FROM posts WHERE postId = %s', (post_id,))
    return cursor.fetchone()

# Funzione che inserisce / aggiorna i record sul db
def update_or_insert_data_in_database(data, cursor):
    try:
        cursor.execute('INSERT INTO posts (postId, userId, title, body) VALUES (%s, %s, %s, %s) '
                       'ON DUPLICATE KEY UPDATE userId = VALUES(userId), title = VALUES(title), body = VALUES(body)',
                       (data['id'], data['userId'], data['title'], data['body']))
        print("Dati inseriti o aggiornati nel database con successo.")
    except mysql.connector.Error as err:
        print(f"Errore durante l'operazione nel database: {err}")
        raise

# Funzione che prende le API's da una route predefinita + impostazioni di connessione con il db
def main():
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'prova'
    }

    # Effettua una connessione al database
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Prende i dati dalle API
        api_data_list = get_api_data(api_url)

        for api_data in api_data_list:
            # Inserisce o aggiorna dati nel database
            update_or_insert_data_in_database(api_data, cursor)

        # Commit delle modifiche
        conn.commit()

    except Exception as e:
        print(f"Errore durante l'esecuzione dello script: {e}")

    finally:
        # Chiude la connessione con il db
        cursor.close()
        conn.close()


# Schedule dell'esecuzione dello script ogni sabato alle 01:00
schedule.every().saturday.at("01:00").do(main)

# Loop per eseguire continuamente il programma
while True:
    schedule.run_pending()
    time.sleep(1)