# Documentazione del Sistema di Gestione Business Central

## Indice
1. [Panoramica](#panoramica)
2. [Tabella Power Apps Entry](#tabella-power-apps-entry)
3. [Gestione degli Errori](#gestione-degli-errori)
4. [Elaborazione Giornaliera dei Dati](#elaborazione-giornaliera-dei-dati)
5. [Integrità dei Dati e Controlli](#integrità-dei-dati-e-controlli)
6. [Script di Generazione Dati](#script-di-generazione-dati)

## Panoramica
Questa documentazione fornisce una panoramica delle principali funzionalità del sistema di gestione personalizzato in Business Central, che si integra con un'applicazione PowerApps.

## Tabella Power Apps Entry
Il sistema dispone di una tabella chiamata 'Power Apps Entry' che riceve i dati dall'applicazione PowerApps tramite API.

### Tipi di Entry
- **Quantity**: Entry effettuate quando viene inviato un ordine.
- **Error**: Uno stato che un'entry assume quando il programma incontra un problema e non può procedere.

## Gestione degli Errori
Il sistema di gestione è progettato per gestire gli errori in modo efficiente, assicurando che l'esecuzione non sia interrotta da problemi imprevisti.

## Elaborazione Giornaliera dei Dati
L'elaborazione dei dati avviene quotidianamente attraverso diversi passaggi chiave:

1. **Recupero Dati**: I dati vengono estratti dalla tabella 'Power Apps Entry'.
2. **Movimentazione Dati**: Successivamente, i dati vengono spostati nella 'Item Journal Line'.
3. **Registrazione Storica**: Infine, i dati vengono registrati nei registri storici, ovvero 'Item Ledger Entry' e 'Capacity Ledger Entry'.

## Integrità dei Dati e Controlli
Il sistema include numerosi controlli per mantenere l'integrità dei dati e garantire un'elaborazione accurata.

## Script di Generazione Dati
- È stato sviluppato uno script personalizzato per generare oltre mille voci di dati fittizi.
- Questi dati vengono utilizzati per test e finiscono nei registri storici.

