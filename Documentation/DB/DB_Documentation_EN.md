# Documentation Database

## Purpose

This SQL script is designed to create two tables in our support database, reflecting the corresponding tables in Business Central.

## Tables

- `capacity_ledger`
- `item_ledger`

## Database Type

MySQL

## Reference Site

[MySQL Official Website](https://www.mysql.com)

## Table Definitions

### Table: capacity_ledger

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

### Table: item_ledger

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
- `order_line_no`: Integer
