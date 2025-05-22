
<h1> ETL Automation Project 1 </h1>


<h2>Description</h2>
This project automates an ETL (Extract, Transform, Load) pipeline that consolidates data from three sources:

- **Google Sheets**
- **Local hard disk (CSV/Excel files)**
- **PostgreSQL database**


The data is extracted, cleaned, and standardized before being loaded into a PostgreSQL database under the `clean_data` schema. A local copy of the cleaned data is also saved to the `output/` folder for reference or downstream processing.

<h2> Key Features </h2>

- **Extract** from:
  - Google Sheets using API credentials
  - Local files stored in the `data/` directory
  - An existing PostgreSQL database
- **Transform**:
  - Drop duplicates
  - Drop null values
  - Standardize date formats
- **Load**:
  - PostgreSQL database under `clean_data` schema
  - Local machine (`output/` folder)

<h2> Requirements </h2>

- Python 3.8+
- PostgreSQL
- Google API credentials (for Sheets access)

<h2>Python Libaries Used</h2>

- <b>see requirements.text</b>

<h2> Recommended Tools</h2>

- VS Code (with Python and Jupyter extensions)

- DBeaver or pgAdmin for interacting with PostgreSQL

- Git for version control

<h2>ETL_Automation Folder</h2>

<img src="https://i.imgur.com/ExQlYW0.png" alt=" ETL_Automation Folder" width="600"/>


<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
