# Documentation 

## Program Purpose

This Extract, Transform, Load (ETL) script is developed to automate data extraction from Business Central through JSON APIs. The extracted data is subsequently loaded into a dedicated database. The `capacity_ledger` and `item_ledger` scripts run in parallel.

## Project Structure

The project is organized into the following modules:

- `main.py`: Main entry point for executing the ETL script.
- `capacity_ledger.py`: Module for extracting and managing data related to the capacity ledger.
- `item_ledger.py`: Module for extracting and managing data related to the item ledger.

## Installation

To install the necessary dependencies, execute the following command:

```bash
pip install -r requirements.txt
```

## Configuration

As follows there's a template that has to be modified with your Business Central authorization credentials and with the API's URL ready to be consumed.

``` bash 
business_central:
  bc_username: 'username'
  bc_password: 'password'
  bc_domain: 'domain'
  capacity_ledger_api_url: 'http://localhost:7048/BC210/api/its/gamma/v1.0/companies(7841464b-e73a-ed11-bbaf-6045bd8e5a17)/capacityentries'
  item_ledger_api_url: 'http://localhost:7048/BC210/api/its/gamma/v1.0/companies(7841464b-e73a-ed11-bbaf-6045bd8e5a17)/ledgerentries'
```
That's a part of the script designed to make a connection with a chosen support database. Also in this case, it has to be modified with your own parameters.


``` bash
database:
  host: 'localhost'
  port: 3306
  user: 'root'
  password: ''
  name: 'table_name'
```
## How to use it

Just need to run the main.py from command line

``` bash
'/dicrectory/path/' python main.py
``` 
The script will continue to run in the background, and every Saturday at 01:00 (day and time are customizable), records will be updated and inserted into the chosen support database.
## Contribute

To contribute, open a new issue or submit a pull request. We welcome improvements and appreciate any corrections or bug reports.
