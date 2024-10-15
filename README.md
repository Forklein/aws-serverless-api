# Serverless Framework Python HTTP API on AWS

## Requirements
1. **Amazon AWS**
   - https://signin.aws.amazon.com/signup?request_type=register

2. **NodeJS**
   - Versione 18.20 o superiore

3. **Serverless Framework**
   - Installazione: [Serverless Framework](https://www.serverless.com/)
   
   ```
   npm install -g serverless
   ```
4. **File requirements.txt**
   - Librerie utilizzate: **boto3** SDK di aws + librerie standard di python
   
   ```
   pip install -r requirements.txt
   ```

## Start
1. **Inizializzazione di serverless**
  -Recarsi nella directory interessata, aprire il terminale come amministratore e digitare
   ```
   serverless
   ```
2. **Configurazioni**<br>
  -Selezionare il template: la mia scelta è stata HTTP API on AWS utilizzando Python<br>
  -Seguire le istruzioni a schermo: verrà creata un app su https://app.serverless.com/ dove si potranno monitorare le funzioni Lambda, visualizzare log e metriche, e gestire gli eventi mentre su aws verrà creato uno "stack".<br>
  -Configurare correttamente il file serverless.yml [Reference qui](https://www.serverless.com/framework/docs/providers/aws/guide/serverless.yml): In questo file nel corrente progetto è stato configurato **DYNAMOBDB** (la tabella si chiama Users), database NO-SQL dove vengono appunto salvati gli user(ID,nome,cognome,email) definendo soltanto la chiave primaria(ID), le **Lambda Functions**, ovvero createUser, getUserById e getAllUsers che si occupano appunto di creare un utente, leggere il singolo utente e vedere tutti gli utenti(in questo esempio vengono retrivati tutti gli id degli user) e infine molto importante **iamRoleStatements**, ovvero i permessi per scrivere e leggere.<br>
   -Nel file handler.py ho settato anche dei logger: questi sono visualizzabili da CloudWatch direttamente su aws

## Usage
  ```
  serverless deploy
  ```
  -Tramite questo comando verrà deployato il progetto direttamente su AWS utilizzando serverless.<br>
  -E' possibile anche definire l'ambiente per il deploy(ad esempio stage)

### Curl
```
curl https://xxxxxxx.execute-api.us-east-1.amazonaws.com/
```
Per poter testare gli endPoint dopo il deploy, serverless mostrerà a schermo l'endpoint dove xxxxxxx corrisponde all'ID dell'API Gateway. Questo ID viene generato automaticamente da AWS quando si crea una nuova API tramite API Gateway.Ho utilizzato personalmente postman per testare gli endpoint.

### Endpoint
**METHOD: GET**<br>
**https://xxxxxxx.execute-api.us-east-1.amazonaws.com/users**<br>
Questo endpoint serve per retrivare tutti gli users<br>
**METHOD: GET**<br>
**https://xxxxxxx.execute-api.us-east-1.amazonaws.com/users/{id}**<br>
Questo endpoint serve per retrivare le informazioni dettagliate di un singolo user<br>
**METHOD: POST**<br>
**https://xxxxxxx.execute-api.us-east-1.amazonaws.com/users**<br>
Questo endpoint serve per creare uno user

## Alcuni screen
<img src="https://i.ibb.co/nBV0CF6/Schermata-del-2024-10-15-14-26-56.png" />
<img src="https://i.ibb.co/nk3KrqB/Schermata-del-2024-10-15-14-29-20.png" />
<img src="https://i.ibb.co/SVqmsfZ/Schermata-del-2024-10-15-14-31-15.png" />
