# ERP_login
a script that is used to login into erp.
It has an option to let you log into ERP in local office network or when you are in external network(i.e via internet)
This is the first 'easy' step to automate the whole ERP platform.
The script is written in python and uses Selenium for automating the web requests.
This script doesn't include environment variables for storing credentials because the user of the window has no admin previlages.
Instead a dictionary that is called 'Pass' must be created on the same directory with this script to store the credentials.
