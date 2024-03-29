# Documentazione del Database

## Scopo
Il seguente script SQL e' stato pensato per replicare le tabelle presenti su Business Central su un nostro database di appoggio sul quale inserire i dati provenienti dalle API

## Tabelle

- `capacity_ledger`
- `item_ledger`

## Database scelto

MySQL

## Sito di Riferimento per il database

[MySQL Official Website](https://www.mysql.com)

## Definizione delle tabelle

### Tabella: capacity_ledger

- `entry_no`: Integer, Primary Key
- `posting_date`: Date[..](..)
- `item_no`: VARCHAR(255)
- `type`: VARCHAR(255)
- `no`: VARCHAR(255)
- `document_no`: VARCHAR(255)
- `description`: VARCHAR(255)
- `routing_no`: VARCHAR(255)
- `routing_reference_no`: Integer
- `operation_no`: VARCHAR(255)
- `output_quantity`: Integer
- `unit_of_measure_code`: VARCHAR(10)
- `scrap_quantity`: Integer
- `setup_time`: Integer
- `run_time`: Integer
- `stop_time`: Integer
- `cap_unit_of_measure_code`: VARCHAR(255)
- `starting_time`: TIME
- `ending_time`: TIME
- `order_type`: VARCHAR(255)
- `order_no`: VARCHAR(255)
- `order_line_no`: Integer

### Tabella: item_ledger

- `entry_no`: Integer, Primary Key
- `item_no`: VARCHAR(255)
- `posting_date`: Date
- `entry_type`: VARCHAR(255)
- `source_no`: VARCHAR(255)
- `document_no`: VARCHAR(255)
- `description`: VARCHAR(255)
- `location_code`: VARCHAR(255)
- `quantity`: Decimal(10, 2)
- `unit_of_measure_code`: VARCHAR(255)
- `item_category_code`: VARCHAR(255)
- `document_type`: VARCHAR(255)
- `document_line_no`: Integer
- `order_type`: VARCHAR(255)
- `order_no`: VARCHAR(255)
-  `order_line_no`: Integer
