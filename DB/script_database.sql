/* SQL script to create two tables in our support database that mirror the corresponding tables in Business Central.

   Tables:
        - capacity_ledger
        - item_ledger

   Database type: MySQL (RDBMS)
   Reference site: www.mysql.com
 */

CREATE TABLE IF NOT EXISTS capacity_ledger (
    entry_no INT PRIMARY KEY,
    posting_date DATE,
    item_no VARCHAR(255),
    type VARCHAR(255),
    no VARCHAR(255),
    document_no VARCHAR(255),
    description VARCHAR(255),
    routing_no VARCHAR(255),
    routing_reference_no INT,
    operation_no VARCHAR(255),
    output_quantity INT,
    unit_of_measure_code VARCHAR(10),
    scrap_quantity INT,
    setup_time INT,
    run_time INT,
    stop_time INT,
    cap_unit_of_measure_code VARCHAR(255),
    starting_time TIME,
    ending_time TIME,
    order_type VARCHAR(255),
    order_no VARCHAR(255),
    order_line_no INT
);

CREATE TABLE IF NOT EXISTS item_ledger (
    entry_no INT PRIMARY KEY,
    item_no VARCHAR(255),
    posting_date DATE,
    entry_type VARCHAR(255),
    source_no VARCHAR(255),
    document_no VARCHAR(255),
    description VARCHAR(255),
    location_code VARCHAR(255),
    quantity DECIMAL(10, 2),
    unit_of_measure_code VARCHAR(255),
    item_category_code VARCHAR(255),
    document_type VARCHAR(255),
    document_line_no INT,
    order_type VARCHAR(255),
    order_no VARCHAR(255),
    order_line_no INT
);
