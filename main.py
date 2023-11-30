# Importazione delle librerie necessarie
import requests
import mysql.connector

# Effettua una richiesta GET all'API designata
response = requests.get('https://jsonplaceholder.typicode.com/posts/17')

# Check per vedere se la richiesta ha avuto successo (restituisce il codice di risposta HTTP 200)
if response.status_code == 200:
    # Estrae i dati JSON dalla risposta
    data = response.json()

    # Connessione al database MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='prova'
    )
    cursor = conn.cursor()

    # Inserimento dei dati nel database
    cursor.execute('INSERT INTO posts (postId, userId, title, body) VALUES (%s, %s, %s, %s)',
                   (data['id'], data['userId'], data['title'], data['body']))

    # Conferma e chiude la connessione con il db
    conn.commit()
    conn.close()

# Check per vedere se i dati sono stati inseriti con successo nel db, in caso contrario restituisce un errore
    print("Dati inseriti nel database con successo.")
else:
    print(f"Errore nella richiesta API: {response.status_code}")
