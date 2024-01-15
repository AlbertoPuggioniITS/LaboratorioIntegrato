# Documentazione di Installazione di Metabase

## Panoramica

Metabase è uno strumento open source per l'intelligence aziendale e l'analisi dei dati. Questa documentazione fornisce istruzioni passo-passo per configurare Metabase per la tua organizzazione.

## Prerequisiti

Prima di iniziare il processo di installazione, assicurati di avere quanto segue:

- Un server o piattaforma cloud per ospitare Metabase.
- Un database supportato (es. MySQL, PostgreSQL, SQLite) a cui Metabase si collegherà.
- Java Runtime Environment (JRE) installato sul tuo server.

## Passaggi di Installazione

### Step 1: Scarica Metabase

Visita il sito ufficiale di Metabase [https://www.metabase.com/start/](https://www.metabase.com/start/) e scarica l'ultima versione di Metabase.

### Step 2: Estrai Metabase

Estrai l'archivio Metabase scaricato in una directory sul tuo server.

### Step 3: Configura la Connessione al Database

Modifica il file `application.properties` nella directory di Metabase per configurare la connessione al database. Specifica il tipo di database, host, porta, nome, utente e password.

Esempio (`application.properties`):

```plaintext
# Configurazione della connessione al database
#
# Esempio per MySQL:
# database.driver=com.mysql.cj.jdbc.Driver
# database.url=jdbc:mysql://localhost:3306/metabase
# database.user=tuo_username
# database.password=tua_password
#
# Esempio per PostgreSQL:
# database.driver=org.postgresql.Driver
# database.url=jdbc:postgresql://localhost:5432/metabase
# database.user=tuo_username
# database.password=tua_password
```

### Step 4: Avvia Metabase
Vai alla directory di Metabase ed esegui il seguente comando per avviare Metabase:
```bash
java -jar metabase.jar
```
### Step 5: Accedi a  Metabase
Apri un browser web e vai a http://localhost:3000 (sostituisci localhost con l'IP o il dominio del tuo server). Segui le istruzioni visualizzate per completare il processo di installazione, inclusa la creazione di un account amministratore.

### Step 6: Connetti il tuo database
Dopo aver effettuato l'accesso, Metabase ti chiederà di connetterti a un database. Fornisci i dettagli necessari in base alla connessione al database configurata al Passo 3.

### Step 7: Esplora Metabase
Una volta connesso, esplora l'interfaccia utente di Metabase per creare dashboard, interrogazioni e visualizzazioni. Consulta la documentazione di Metabase per istruzioni dettagliate sull'uso.

## Risorse Aggiuntive

- [Documentazion Ufficiale Metabase](https://www.metabase.com/docs/latest/)
- [Metabase GitHub Repository](https://github.com/metabase/metabase)

## Supporto e Communita'

Per supporto o discussioni nella comunità, visita [il forum di discussione di Metabase](https://discourse.metabase.com/).