import json
#sdk aws
import boto3
from botocore.exceptions import ClientError
#id utente
import uuid
#log
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

#POST
def create_user(event, context):
    logger.info("Evento ricevuto: %s", event)
    
    body = json.loads(event['body'])

    # check semplice dei dati
    if 'name' not in body or 'surname' not in body or 'email' not in body:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'errore'})
        }
    
    #32 caratteri
    user_id = str(uuid.uuid4())
    name = body['name']
    surname = body['surname']
    email = body['email']
    
    Item = {
        'id': user_id,
        'name': name,
        'surname': surname,
        'email': email
    }

    try:
        table.put_item(Item=Item)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Utente creato correttamente!', 'id': Item['id']})
        }
    except ClientError as e:
        logger.error("Errore nella creazione dello user: %s", str(e))
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
#GET     
def get_all_users(event, context):
    logger.info("Evento ricevuto: %s", event)
    try:
        response = table.scan()
        users = response.get('Items', [])
        user_ids = []
        for user in users:
            user_ids.append(user['id'])
        #Ritorno gli ids
        return {
            'statusCode': 200,
            'body': json.dumps(user_ids)
        }
    except ClientError as e:
        logger.error("Errore nel recuperare gli utenti: %s", str(e))
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
#GET
def get_user_by_id(event, context):
    user_id = event['pathParameters']['id']
    logger.info("Evento per cercare un utente: %s", user_id)
    
    try:
        response = table.get_item(Key={'id': user_id})
        user = response.get('Item')
        if user:
            return {
                'statusCode': 200,
                'body': json.dumps(user)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Utente non trovato'})
            }
    except ClientError as e:
        logger.error("Errore nel recuperare un utente: %s", str(e))
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }