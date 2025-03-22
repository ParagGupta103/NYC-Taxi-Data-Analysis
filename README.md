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
 
02/24/2024

- Got the Solution to the problem encountered - https://stackoverflow.com/questions/76576650/receiving-bash-mage-command-not-found-when-trying-to-start-a-new-mage-ai-pro
- started a mage instance using mage start nyc_cab_project
- Accessed the VM to add a firewall rul to allow external sources to access port 6789 using external IP link
- Succefully accessed thr Mage-ai project instance just created, located at: 34.138.251.170:6789
- Created a new project, chose the name, then chose the data loader option within which we chose Python and then API
- The above generated a code for us, then we pasted the public access url from the GCS cloud storage bucket of our dataset in the code
-  Encountered a Problem where the server being used for mage, has randomly become not accessible


