// programma per il funzionamento logico del cancello

/////////// seriale  //////////
int serial = 0;
/////////// input  //////////
int chiaveA = A1;
int chiaveC = 2;
int fcA = 3;
int fcC = 4;
int bmA = 5;
int bmC = 6;
int foto = 7;
int stopE = 8;
int plateRecognition = 9;
////////// output  //////////
int mA = 12;
int mC = 11;
int luce = 10;

int ma[5] = {0,0,0,0};
int mc[5] = {0,0,0,0};
int lum[5] = {0,0,0,0,0};
//timer inversione marcia cw/ccw
long tim00=0;
long tim01=0;
int stopTime = 500;
//timer autochiusura
long tim02=0;
int autoCloseTime = 2000;
//blocco d'emergenza
boolean stopEm =1;

void setup() {
Serial.begin(9600);

/////////// input  //////////
pinMode(chiaveA,INPUT_PULLUP);
pinMode(chiaveC,INPUT_PULLUP);
pinMode(fcA,INPUT_PULLUP);
pinMode(fcC,INPUT_PULLUP);
pinMode(bmA,INPUT_PULLUP);
pinMode(bmC,INPUT_PULLUP);
pinMode(foto,INPUT_PULLUP);
pinMode(stopE,INPUT_PULLUP);
pinMode(plateRecognition,INPUT_PULLUP);
////////// output  //////////
pinMode(mA,OUTPUT);
pinMode(mC,OUTPUT);
pinMode(luce,OUTPUT);
pinMode(13,OUTPUT);

delay(1000);
}

void loop() {
///////////  SERIALE  //////////
serial = Serial.read();
if(serial==49){
  Serial.flush();
  digitalWrite(13,HIGH);
  ma[0] = 1;
  mc[0] = 0;
}

if (digitalRead(plateRecognition)==0){  //comando apertura con riconoscimento targhe
  ma[0] = 1;
  mc[0] = 0;
}

if (digitalRead(chiaveA) == 0){ //comando apertura con chiavi
  ma[0] =1;
  mc[0] = 0;
}

if (digitalRead(chiaveC) == 0){ //comando chiusura con chiavi
  mc[0] = 1;
  ma[0] = 0;
}
if(digitalRead(foto)==1 && mc[0]==1){ //fotocellula solo sulla chiusura
 ma[0] = 1;
 mc[0] = 0;
}

if(digitalRead(bmC) == 1 && mc[0]==1){  //barriera mobile sulla chiusura
 mc[0]=0;
 ma[0]=1;
}

if(digitalRead(bmA) == 1 && ma[0]==1){  //barriera mobile sull'apertura
 ma[0]=0;
 mc[0]=1;
}

if(digitalRead(fcA) == 0){  //fotocellula fine apertura che avvia timer autochiusura
if(ma[0]==1){
  tim02 = millis();
  }
   ma[0] =0;
}

if((millis()-tim02)>autoCloseTime && (millis()-tim02)<(autoCloseTime+100) && millis()>(autoCloseTime+100)){  //autochiusura dopo tot millisecondi
  tim02 = tim02 - 1000;  //tolgo tempo per evitare che Arduino rientri più volte
  mc[0] = 1;
}
  
if(digitalRead(fcC) == 0){  //fotocellula fine chiusura
  mc[0] =0;
}

if(digitalRead(stopE)==1){  //pulsante d'emergenza
  mc[0] = 0;
  ma[0] = 0;
  lum[0] = 0;
}

if(ma[2]==1 || mc[2]==1 ){  
  lum[0]=1;  //accendiamo la luce lampeggiante insieme ai motori
  stopEm = 1;  //se un motore è viene acceso dopo lo stop di emergenza riabilitiamo il sistema
}else{
  lum[0]=0;
}
////////// RIAPRE  ///////////
if (ma[0] > ma[1] && mc[0] < mc[2]){ //è stato invertito il senso di marcia dopo tot tempo riAPRE
tim00 = millis();
//delay(1);
}
if((millis()-tim00)<stopTime){  //prima di invertire la marcia spegni tutto per un tot di tempo
if(digitalRead(stopE)==1){ //rimani pronto se fosse premuto il pulsante di stop d'emergenza
stopEm =0;
}
ma[0] = 0;
mc[0] = 0;
lum[0] = 1;
}else if ((millis()-tim00)<(stopTime+100) && (millis()-tim00)>stopTime && stopEm ==1){  //fai riaprire la stanga
ma[0] = 1;
tim00 = tim00 - 101;
}
////////// RICHIUDE  ///////////
if (mc[0] > mc[1] && ma[0] < ma[2]){ //è stato invertito il senso di marcia dopo tot tempo richiude
tim01 = millis();
//delay(1);
}
if((millis()-tim01)<stopTime){
if(digitalRead(stopE)==1){
stopEm =0;
}
ma[0] = 0;
mc[0] = 0;
lum[0] = 1;
}else if ((millis()-tim01)<(stopTime+100) && (millis()-tim01)>stopTime && stopEm ==1){
mc[0] = 1;
tim01 = tim01 - 101;
}

////////// SHIFT  //////////
for(int i=0; i<4; i++){
  ma[(4-i)] = ma[(3-i)];
  mc[(4-i)] = mc[(3-i)];
  lum[(4-i)] = lum[(3-i)];
  }

//////////  SCRITTURA USCITE  /////////
if (ma[0] == mc[0]) { //evitiamo corti piuttosto spegniamo tutto
  ma[0] =0;
  mc[0] =0;
}

if (ma[0] == ma[4]){ //per qualche ciclo le variabili possono essere oscillanti se per 5 cicli rimangono costanti allora possiamo accendere il relè!
digitalWrite(mA,ma[0]);
}
if (mc[0] == mc[4]){
digitalWrite(mC,mc[0]);
}
if (lum[0] == lum[4]){
digitalWrite(luce,lum[0]);
}
}
