02/21/2024
- The Data was taken from: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- First downloaded the data (around 300,000 entries)
- dropped any rows with missing values (around 227,000 entries)
- Used Lucid Charts for Data Modelling, creating fact tables and dimension tables.
- Followed the Data Model created to create fact table and dimension table using pandas

02/22/2024
- Created a New public Bucket for storing dataset in Google Cloud Storage using Google Cloud Services (GCS)
- Created a Virtual Machine (VM) instance using Compute Engine using Google Cloud Services (GCS)
    * Ran sudo apt-get update -y
    * Ran sudo apt-get install python-distutils
    * Ran sudo apt-get install python-apt
    * Ran sudo apt-get upgrade python-apt

- To install Python packages system-wide, try apt install python3-xyz, where xyz is the package you are trying to install.
- Encountered some problems when installing mage-ai, had to install venv and then created a virtual environment to be able to pipx and then installed mage-ai
- 


