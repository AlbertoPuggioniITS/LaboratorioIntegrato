# Documentazione Laboratorio Integrato (ERP - FinTech)

## Scopo del Programma

Questo script ETL (Extract, Transform, Load) è stato sviluppato per automatizzare l'estrazione di dati da Business Central attraverso le API JSON. I dati estratti vengono successProgram Purpose
This Extract, Transform, Load (ETL) script is developed to automate data extraction from Business Central through JSON APIs. The extracted data is subsequently loaded into a dedicated database. The capacity_ledger and item_ledger scripts run in parallel.ivamente caricati in un database dedicato. Gli script `capacity_ledger` e `item_ledger` vengono eseguiti in parallelo.

## Struttura del Progetto

Il progetto è organizzato nei seguenti moduli:

- `main.py`: Punto di ingresso principale per l'esecuzione dello script ETL.
- `capacity_ledger.py`: Modulo per l'estrazione e la gestione dei dati relativi al capacity ledger.
- `item_ledger.py`: Modulo per l'estrazione e la gestione dei dati relativi all'item ledger.

## Installazione

Per installare le dipendenze necessarie, eseguire il seguente comando:

```bash
pip install -r requirements.txt
```

## Configurazione

Di seguito è riportato il template (presente nello script) da modificare con le proprie credenziali di Business Central e con URL delle proprie API.

``` bash 
business_central:
  bc_username: 'username'
  bc_password: 'password'
  bc_domain: 'dominio'
  capacity_ledger_api_url: 'http://localhost:7048/BC210/api/its/gamma/v1.0/companies(7841464b-e73a-ed11-bbaf-6045bd8e5a17)/capacityentries'
  item_ledger_api_url: 'http://localhost:7048/BC210/api/its/gamma/v1.0/companies(7841464b-e73a-ed11-bbaf-6045bd8e5a17)/ledgerentries'
```
Qui sotto è riportato un esempio della connessione con il proprio database (in questo caso MySQL). Anche in questo caso, è da modificare come opportuno.

``` bash
database:
  host: 'localhost'
  port: 3306
  user: 'root'
  password: ''
  name: 'nome_tabella'
```
## Utilizzo

Per come è stato progettato lo script, è solo necessario far partire il main.py

``` bash
'/path/della/directory' python main.py
``` 
Lo script continuerà a girare in background e ogni sabato alle ore 01:00 (giorno ed ora sono comunque personalizzabili) i record verranno aggiornati ed inseriti nel database.
## Contribuire

Per contribuire, aprire una nuova issue o inviare una pull request. Siamo aperti a miglioramenti e ad accogliere eventuali correzioni o bug reports.