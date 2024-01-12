# LaboratorioIntegrato

##  Ruoli:
DB: Gabriele Inglese. Si occupa di definire i seguenti punti:
1) Schema Entità Relazione
2) Definire lo script di creazione del database e il relativo script di creazione e mantenimento delle tabelle
3) Documentazione

# ETL: Alberto Puggioni
 Ruolo che si occupa di:
1) Recepire e consumare le API's prodotte dal team di ERP
2) Analisi ed eventuale modifica delle colonne per contenere i dati provenienti dalle API's
3) Sviluppare lo script di Extraction Transformation Load dei dati dalle API's al database di appoggio
4) Documentazione

# Metabase: Francesco Messana
 Ruolo che si occupa di.
1) Capire quali indicatori mostrare nelle dashboards
2) Profilazione delle dashboards (dashboards diverse in base al ruolo)
3) Questions
4) Documentazione 

# Il processo di sviluppo:
Abbiamo approcciato il problema costruendo, in primo luogo, il database nel quale verranno inseriti i dati provenienti da Business Central per mezzo delle API. <br>
<br> Allo stesso tempo, ci siamo occupati di sviluppare un ETL custom basato sul linguaggio Python, il cui lavoro consiste nel recepire i dati esposti -in formato JSON- per mezzo delle API ed inserirle nel nostro database di appoggio. In aggiunta l'ETL è stato sviluppato in maniera tale da aggiornare i dati al suo interno costantemente (dato un determinato giorno ed orario). </br>
<br> In ultima battuta, avendo a disposizione una connessione con il db contenente i dati abbiamo effettuato tutte le analisi necessarie utilizzando Metabase come strumento di BI. </br>
