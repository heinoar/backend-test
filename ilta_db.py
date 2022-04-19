
import os
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime



def connect():
 #Seuraavassa luetaan ympäristömuuttujista tietokannan tiedot
  HOST = os.environ.get('COSMOS_HOST')
  MASTER_KEY = os.environ.get('MYSQLCONNSTR_MASTER_KEY')
  DATABASE_ID = os.environ.get('COSMOS_DATABASE_ID')
  CONTAINER_ID = os.environ.get('COSMOS_RAW_CONTAINER_ID')

  #Luodaan instanssi, jolla kantaa voi käsitellä
  client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPython", user_agent_overwrite=True)
  try:
    db = client.get_database_client(DATABASE_ID)
    print('Database with id \'{0}\' was found'.format(DATABASE_ID))
  except:
    print('Database not found')
  try:
    container = db.get_container_client(CONTAINER_ID)
    print('Container with id \'{0}\' was found'.format(CONTAINER_ID))
    return container
  except:
      print('Container not found')

  
#Kirjoitetaan kantaan. Item on json-typpinen tieto
def create_item(container,item):
    print('\nCreating Items\n'+str(item))
    print(container)
    container.create_item(body=item)


#Luetaan containerin itemit
def read_items(container):
    print('\nReading all items in a container\n')
    item_list = list(container.read_all_items(max_item_count=10))

    print('Found {0} items'.format(item_list.__len__()))

    for doc in item_list:
        print('Item Id: {0}'.format(doc.get('id')))
    return str(item_list)


