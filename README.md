# Hello and welcome to the 'Cat facts restful API'

## Summary  
This simple RESTful API connects to 2 external APIS:  
  - Cat Fact API (https://cat-fact.herokuapp.com/facts),  
  - Google Cloud Translation API (https://cloud.google.com/translate).  
  
It allows users to learn interesting facts about cats (in English) or then to translate them to any language 
that is supported by Google Cloud Translation API. 
  

## Running the app
To use the code, you need to create a service account at Google Cloud API and download a service_account.json file
containing your credentials from there (see: service_account.json.example to see the example).  
Next, install all the dependencies (see: requirements.txt).  
Finally, you can run the app from the console by using: 'python app.py' command.

To test the app, you can use a platform for API development, e.g. Postman. 
I provide a Postman collection in a file cat_facts_rest_api.postman_collection.json.  
  
  
## API's available endpoints
The API has the following endpoints: 
  
/facts (GET) - you need to add parameters in there: animal and amount (of facts you want to learn about an animal),  
  e.g. /facts?animal=cat&amount=4  
  
/translate (POST)  
    

You can check how the endpoints work using the postman collection documentation cat_facts_rest_api.postman_collection.json.  


## API collection
As mentioned above, the Postman collection is saved in the file at_facts_rest_api.postman_collection.json. Feel free to download it to check the API endpoints easily.
