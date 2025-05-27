
<h1>🔄 ETL Automation Project 1 </h1>


<h2>📌 Project Overview</h2>
This project automates an ETL (Extract, Transform, Load) pipeline that consolidates data from three sources:

- **Google Sheets**
- **Local hard disk (CSV/Excel files)**
- **PostgreSQL database**

<b>The ETL pipeline completes the following:</b>

- Data is extracted, cleaned, and standardized
- Cleaned data loaded into a PostgreSQL database under the `clean_data` schema.
- Copy of the cleaned data is also saved to the `output/` folder for reference.
- A success email is sent after the process has been completed.

<h2> ⚙️ Key Features </h2>

- 🗂️ **Extract** from:
  - Google Sheets using API credentials
  - Local files stored in the `data/` directory
  - An existing PostgreSQL database
- 🧹**Transform**:
  - Drop duplicates
  - Drop null values
  - Standardize date formats
- 🗃️ **Load**:
  - PostgreSQL database under `clean_data` schema
  - Local machine (`output/` folder)

<h2>🧰 Requirements </h2>

- Python 3.8+
- PostgreSQL
- Google API credentials (for Sheets access)

<h2>📚 Python Libaries Used</h2>

- <b>[see requirements.text](https://github.com/SimonMuriu-pro/Etl-Automation-Project-1/blob/main/Requirements.txt)</b>

<h2>🛠️ Recommended Tools</h2>

- VS Code (with Python and Jupyter extensions)

- DBeaver or pgAdmin for interacting with PostgreSQL

- Git for version control

<h2> 📁 ETL_Automation Folder Structure</h2>

<img src="https://i.imgur.com/ExQlYW0.png" alt=" ETL_Automation Folder" width="600"/>

<h2> 👤 Author / Contact </h2>

<b>Simon Muriu</b> 
<b>Data Analyst</b>  
[LinkedIn](https://www.linkedin.com/in/simon-muriu-0a1310251/) | 
[Email](mailto:smuriu06@gmail.com)


<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
