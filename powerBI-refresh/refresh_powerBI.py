import logging
import requests as re
import pandas as pd
import azure.functions as func

    
    


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    
    
    
    
    

    
    
    
    
    client_id='4f1e48d0-9cad-45c7-866d-82c09202b062'
    tenant_id='86c49f02-90c7-4fbf-8380-51efd55e7a17'
    secret_vale='AqD7Q~zJOCNptLeSPHFXB1pXT2X0Ue1tvMmMj'
    client_secret='5863cbdb-1549-48c7-a062-fd24e4342376'
    authority_url = 'https://login.microsoftonline.com/dataracy.onmicrosoft.com'
    scope = ['https://analysis.windows.net/powerbi/api/.default']
    url_groups = 'https://api.powerbi.com/v1.0/myorg/groups'
    url_datasets = 'https://api.powerbi.com/v1.0/myorg/datasets'
    username='pbhavsar@dataracy.com'
    password='Pbhavsa123!'
    

    
    url = 'https://login.microsoftonline.com/common/oauth2/token'
    data = { 'grant_type': 'password', 'resource': 'https://analysis.windows.net/powerbi/api', "scope" : 'https://api.powerbi.com',
    'client_id': "150f6718-2032-492e-be67-23c5cb9d6015", "client_secret" : "zSG3zs7IFOaz81Fl/a6wjzJdBKVMW4YyjgFYLTqvn8k=",
    "redirect_uri": "https://localhost/redirect", "username" : "pbhavsar@dataracy.com", "password" : "Pbhavsa123!"}
    r = re.get(url, data=data)
    access_token = r.json().get('access_token')
    
    
    refresh_url = 'https://api.powerbi.com/v1.0/myorg/datasets/540ae23f-a1a7-47d6-b8ee-324d121f517d/refreshes'
    header = {"Authorization": f'Bearer {access_token}'}
    r2 = re.post(url=refresh_url, headers=header)
    print(r2)
    logging.info('done with refresh')
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
        
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
