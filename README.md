# WebScrapperService
This is a repository intended for completing a task provided by Manush Tech.

The project is an API that will take a "keyword" from the request and search for it in the given urls of Pandamart (Gulshan: [https://www.foodpanda.com.bd/darkstore/w2lx/pandamart-gulshan-w2lx](https://www.foodpanda.com.bd/darkstore/w2lx/pandamart-gulshan-w2lx),
Mirpur : [https://www.foodpanda.com.bd/darkstore/h9jp/pandamart-mirpur](https://www.foodpanda.com.bd/darkstore/h9jp/pandamart-mirpur)). After searching it will respond with the data in the format of  

{    
		"darkStore" : "location",    
		"title" : "product name",    
		"url" : "product url",    
		"price" : "product price",    
		"priceAfterDiscount" : "product discounted price",    
		"stockStatus" : "product availability"  IN STOCK / OUT OF STOCK    
}    

in a list.

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
