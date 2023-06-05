// Rueda Central
#define in1 12  
#define in2 11

// Rueda 1
#define in3 10
#define in4 9

// Rueda 2
#define in5 8
#define in6 7

// Rueda 3
#define in7 6
#define in8 5

// Rueda 4
#define in9 4
#define in10 3

// Ascensor
#define in11 13
#define in12 2


int tiempo = 0;
int pos = 0;
int metodo = 0;
String metodoStr = "";
String tiempoStr = "";

void setup() {
  Serial.begin(9600);
  while(!Serial){}

  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  
  pinMode(in5, OUTPUT);
  pinMode(in6, OUTPUT);
  
  pinMode(in7, OUTPUT);
  pinMode(in8, OUTPUT);

  pinMode(in9, OUTPUT);
  pinMode(in10, OUTPUT);

  pinMode(in11, OUTPUT);
  pinMode(in12, OUTPUT);
}

void loop() {
  tiempo = 2000;

  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    
    if (data != NULL){
      pos = data.indexOf(',');
      metodoStr = data.substring(0, pos);
      metodo = metodoStr.toInt();
      tiempoStr = data.substring(pos+1, data.length());
      tiempo = tiempoStr.toInt();
      
      Serial.println(metodo, tiempo);

      switch (metodo){
        case 1:
          avanzar(tiempo);
          parar();
          delay(1000);
          break;
        case 2:
          retroceder(tiempo);
          parar();
          delay(1000);
          break;
        case 3:
          girar90();
          parar();
          delay(1000);
          break;
        case 4:
          acercarse(tiempo);
          pararCentral();
          delay(1000);
          break;
        case 5:
          alejarse(tiempo);
          pararCentral();
          delay(1000);
          break;
        case 6:
          subir(tiempo);
          pararAscensor();
          delay(1000);
          break;
        case 7:
          bajar(tiempo);
          pararAscensor();
          delay(1000);
          break;
        default:
          parar();
          pararCentral();
          pararAscensor();
          delay(1000);
      }
    }
  }
}   


// Funciones

void avanzar(int tiempo) {
  // Rueda 1
  digitalWrite(in3, 10); 
  digitalWrite(in4, 0);
  
  // Rueda 2
  digitalWrite(in5, 10); 
  digitalWrite(in6, 0);
 
  // Rueda 3
  digitalWrite(in7, 10);
  digitalWrite(in8, 0);
  
  // Rueda 4
  digitalWrite(in9, 10);
  digitalWrite(in10, 0);

  delay(tiempo);
}

void retroceder(int tiempo){
  // Rueda 1
  digitalWrite(in3, 0);
  digitalWrite(in4, 10);
  
  // Rueda 2
  digitalWrite(in5, 0);
  digitalWrite(in6, 10);

  // Rueda 3
  digitalWrite(in7, 0);
  digitalWrite(in8, 10);
  
  // Rueda 4
  digitalWrite(in9, 0);
  digitalWrite(in10, 10);
  
  delay(2000);
}

void parar(){
  // Rueda 1
  digitalWrite(in3, 0); 
  digitalWrite(in4, LOW);

  // Rueda 2
  digitalWrite(in5, 0); 
  digitalWrite(in6, LOW);

  // Rueda 3
  digitalWrite(in7, 0);
  digitalWrite(in8, LOW);

  // Rueda 4
  digitalWrite(in9, 0);
  digitalWrite(in10, LOW);
}

void girar90(){
  // Rueda 1
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  
  // Rueda 2
  digitalWrite(in5, LOW);
  digitalWrite(in6, HIGH);

  // Rueda 3
  digitalWrite(in7, HIGH);
  digitalWrite(in8, LOW);

  // Rueda 4
  digitalWrite(in9, HIGH);
  digitalWrite(in10, LOW);

  delay(750);
}

void acercarse(int tiempo){
  // Rueda central
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  delay(tiempo);
}

void alejarse(int tiempo){
  // Rueda central
  digitalWrite(in1, HIGH); 
  digitalWrite(in2, LOW);
  delay(tiempo);
}

void pararCentral(){
  // Rueda Central
  digitalWrite(in1, LOW);
  digitalWrite(in2, 0);
}

void subir(int tiempo){
  // Ascensor
  digitalWrite(in11, LOW);
  digitalWrite(in12, HIGH);
  delay(tiempo);
}

void bajar(int tiempo){
  digitalWrite(in11, HIGH);
  digitalWrite(in12, LOW);
  delay(tiempo);
}

void pararAscensor(){
  digitalWrite(in11, LOW);
  digitalWrite(in12, 0);
}