import requests
import mysql.connector

def get_api_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def fetch_data_from_database(cursor, post_id):
    cursor.execute('SELECT postId, userId, title, body FROM posts WHERE postId = %s', (post_id,))
    return cursor.fetchone()

def update_or_insert_data_in_database(data, cursor):
    try:
        cursor.execute('INSERT INTO posts (postId, userId, title, body) VALUES (%s, %s, %s, %s) '
                       'ON DUPLICATE KEY UPDATE userId = VALUES(userId), title = VALUES(title), body = VALUES(body)',
                       (data['id'], data['userId'], data['title'], data['body']))
        print("Dati inseriti o aggiornati nel database con successo.")
    except mysql.connector.Error as err:
        print(f"Errore durante l'operazione nel database: {err}")
        raise

def main():
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'prova'
    }

    # Connessione al database MySQL
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Ottieni dati dall'API
        api_data_list = get_api_data(api_url)

        for api_data in api_data_list:
            # Inserisci o aggiorna dati nel database
            update_or_insert_data_in_database(api_data, cursor)

        # Conferma e chiude la connessione con il database
        conn.commit()

    except Exception as e:
        print(f"Errore durante l'esecuzione dello script: {e}")

    finally:
        # Chiude la connessione con il database
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
