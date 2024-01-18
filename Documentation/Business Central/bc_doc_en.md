# Business Central Management System Documentation

## Table of Contents
1. [Overview](#overview)
2. [Power Apps Entry Table](#power-apps-entry-table)
3. [Error Handling](#error-handling)
4. [Daily Data Processing](#daily-data-processing)
5. [Data Integrity and Checks](#data-integrity-and-checks)
6. [Data Generation Script](#data-generation-script)

## Overview
This documentation provides an overview of the key functionalities of the custom Business Central management system, which integrates with a PowerApps application.

## Power Apps Entry Table
The system features a table named 'Power Apps Entry' that receives data from the PowerApps application via API.

### Entry Types
- **Quantity**: Entries made when an order is sent.
- **Error**: A state that an entry takes when the program encounters an issue and cannot proceed.

## Error Handling
The management system is designed to handle errors efficiently, ensuring that execution is not halted by unexpected issues.

## Daily Data Processing
Routine data processing involves several key steps carried out every working day:

1. **Data Retrieval**: Data is pulled from the 'Power Apps Entry' table.
2. **Data Movement**: Data is then moved to the 'Item Journal Line'.
3. **Historical Recording**: Finally, data is recorded in historical logs, namely 'Item Ledger Entry' and 'Capacity Ledger Entry'.

## Data Integrity and Checks
The system includes numerous checks to maintain data integrity and ensure accurate processing.

## Data Generation Script
- A custom script has been developed to generate over a thousand mock data entries.
- This data is used for testing and ends up in historical records.

