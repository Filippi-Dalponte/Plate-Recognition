#Riconoscimento targhe
![alt tag](https://cloud.githubusercontent.com/assets/13135708/8456190/0b7d348c-200a-11e5-92ec-68970b237f75.png)
#Introduzione
Il Lavoro ideato ha il fine di automatizzare un sistema di accesso mediante il riconoscimento delle autovetture. Consiste nella lettura automatica delle targhe, con il dato digitalizzato è quindi possibile lo sviluppo di un software adattato alle proprie esigenze;  nel nostro caso i dati acquisiti vengono confrontati con un database e, se la targa è consentita, si esegue  l’apertura di una barriera automatica per l’ingresso ad un’area ad accesso limitato.  
Il progetto è multidisciplinare e richiede conoscenze di:  
•	**automazione** dato che uno dei nostri obiettivi è quello di far effettuare operazioni ripetitive al sistema riducendo il  contributo umano necessario;  
•	 **elettronica** a cui è assegnata la gestione del funzionamento tradizionale del cancello;  
•	 **elettrotecnica** che si occupa del trasformatore necessario ad alimentare il motore asincrono monofase a condensatore fisso;  
•	**informatica** che si occupa dell' elaborazione, dell' interfaccia con l' utente e della gestione dell' impianto  
Il progetto offre molteplici possibili sviluppi applicativi nell' ambito del riconoscimento oggetti, gestione remota di automazioni industriali, centralizzazione e trasmissione dati. L' intero sistema è stato volutamente realizzato con piattaforme software e hardware Open-Source non dipende quindi da licenze di costosi software e sistemi operativi proprietari. Il progetto propone una soluzione ai tradizionali sistemi adottati come la chiave elettronica a contatto oppure il codice di accesso e si adatta molto bene a luoghi come parcheggi scolastici, uffici aziende o campeggi.
#Struttura del progetto
![alt tag](https://cloud.githubusercontent.com/assets/13135708/8456352/2c8185ec-200b-11e5-9a68-e979e7b6566d.jpg)
Il Sistema realizzato è suddiviso in cinque blocchi fondamentali:  
•	**telecamera** acquisisce e comprime il flusso video  
•	**Banana pi** (computer) data la sua compattezza nelle dimensioni, nel costo e vista la sua sufficiente potenza di calcolo si presta più che bene nel sistema del riconoscimento targhe;  
•	**Arduino** (microcontrollore) grazie alla sua stabilità e continuità di utilizzo ha il compito di comandare il funzionamento dell'hardware del cancello garantendone sempre il funzionamento tradizionale con chiavi e telecomando;  
•	**computer remoto** che può visualizzare e modificare il database contenente le targhe a cui è permesso l' accesso. Questa    parte ha un fine solo di gestione o sorveglianza, non è necessaria per il funzionamento ordinario  
•	**scheda cancello** necessaria per l' interfaccia del microcontrollore alle parti di potenza come il motore e per l'        accoppiamento della sensoristica  

#Mappa concettuale
![alt tag](https://cloud.githubusercontent.com/assets/13135708/8456373/3fd55fec-200b-11e5-81de-0101d4076ec8.jpg)
