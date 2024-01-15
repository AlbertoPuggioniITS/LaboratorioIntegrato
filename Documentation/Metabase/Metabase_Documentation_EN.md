# Metabase Setup Documentation

## Overview

Metabase is an open-source business intelligence and analytics tool. This documentation provides step-by-step instructions to set up Metabase for your organization.

## Prerequisites

Before you begin the setup process, ensure that you have the following:

- A server or cloud platform to host Metabase.
- A supported database (e.g., MySQL, PostgreSQL, SQLite) for Metabase to connect to.
- Java Runtime Environment (JRE) installed on your server.

## Installation Steps

### Step 1: Download Metabase

Visit the official Metabase website [https://www.metabase.com/start/](https://www.metabase.com/start/) and download the latest version of Metabase.

### Step 2: Extract Metabase

Extract the downloaded Metabase archive to a directory on your server.

### Step 3: Configure Database Connection

Edit the `application.properties` file in the Metabase directory to configure the database connection. Specify the database type, host, port, name, username, and password.

Example (`application.properties`):

```plaintext
# Database connection configuration

#
# Example for MySQL:
# database.driver=com.mysql.cj.jdbc.Driver
# database.url=jdbc:mysql://localhost:3306/metabase
# database.user=your_username
# database.password=your_password
#
# Example for PostgreSQL:
# database.driver=org.postgresql.Driver
# database.url=jdbc:postgresql://localhost:5432/metabase
# database.user=your_username
# database.password=your_password


```

### Step 4: Start Metabase
Navigate to the Metabase directory and run the following command to start Metabase:
```bash
java -jar metabase.jar
```
### Step 5: Access Metabase
Open a web browser and navigate to http://localhost:3000 (replace localhost with your server's IP or domain). Follow the on-screen instructions to complete the setup process, including creating an admin account.

### Step 6: Connect to your Database
After logging in, Metabase will prompt you to connect to a database. Provide the necessary details based on your configured database connection in Step 3.

### Step 7: Explore Metabase
Once connected, explore Metabase's user interface to create dashboards, queries, and visualizations. Refer to the Metabase documentation for detailed usage instructions.

## Additional Resources

- [Metabase Documentation](https://www.metabase.com/docs/latest/)
- [Metabase GitHub Repository](https://github.com/metabase/metabase)

## Support and Community

For support or community discussions, visit the [Metabase discussion forum](https://discourse.metabase.com/).

