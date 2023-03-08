# WebScrapperService
This is a repository intended for completing a task provided by ManushTech

# Setup Guide:
Requirements:
- Python 3.9 or higher
- In order to use the API, you will need to have Chrome browser installed on the machine where the code will run. 
Chrome installation guide: 
    - https://linuxconfig.org/how-to-install-google-chrome-browser-on-linux (Linux), 
    - https://www.google.com/chrome/ (Windows)
- pip version 21.1.2

Guide:
1. Go to the directory where you cloned the project and create a virtual environment. 
    - Command: python -m venv venv
2. Activate the virtual environment.
    - Command for windows: venv\Scripts\activate 
    - Command for linux: source venv/bin/activate
3. Install the requirements from the requirements.txt file:
    - Command: pip install -r requirements.txt
4. Once the installation is complete, run the project by the command: 
    - python manage.py runserver server_ip:port

# Requesting the API:
To request the api from Postman - 
  - Method: POST,
  - URL: http://{server_ip:port}/pandamart/pandamart_scrappy/,
  - Body: { "keyword": "Dettol" }
