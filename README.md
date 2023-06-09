# Librobot
Robot que interactua amb una persona per buscar un llibre a les prestatgeries donant un títol per veu i que el succiona per poder-lo agafar.
<br> </br>

<img src="images/librobot_final.jpg" alt="">

## Taula de continguts
1. [En què consiteix?](#en-que-consiteix)
2. [Requisits](#requisits)
3. [Com funciona?](#com-funciona)
4. [Contribucions Espectaculars](#amazing-contributions)
5. [Components](#components)
6. [Esquema de *hardware*](#esquema-de-hardware)
7. [Peces 3D](#peces-3d)
8. [Arquitectura de *software*](#arquitectura-de-software)
9. [Vídeo](#video)
10. [Contribucions](#contribucions)
11. [Citacions](#Citacions)
12. [Llicència](#llicencia)
13. [Autors](#autors)
14. [Bibliografia](#bibliografia)

<h2 id="en-que-consiteix">En què consiteix?</h2>
Aquest robot és un sistema que inclou components físics i electrònics amb la capacitat de realitzar quatre moviments (graus de llibertat) diferents, cadascun dels quals implica una base mòbil davant d'un prestatge amb una barra vertical que mou un braç per agafar un llibre. El sistema utilitza una càmera, un micròfon per sol·licitar un llibre, una ventosa al final del braç i algorismes per identificar i localitzar llibres específics a la prestatgeria, i agafar-los succionant amb la ventosa els llibres i deixant-los a sobre d'un suport metàl·lic.

<img src="images/librobot.PNG" alt=""><br/>
<i>Il·lustració inicial del robot (Rubén R.S.)</i>

<h2 id="com-funciona">Com funciona?</h2>

1. Clona aquest repositori:

  ```terminal
  git clone https://github.com/RubenRS040398/librobot.git
  ```

2. Instal·la les llibreries necessàries:

  ```terminal
  cd librobot
  ```

  ```terminal
  pip install -r requirements.txt
  ```

Python terminal

  ```terminal
  import nltk
  nltk.download()
  ```

<h2 id=amazing-contributions> Contribucions Espectaculars </h2>
El nostre robot està pensat per facilitar la feina a llibreters, personal de biblioteca i fins i tot en l'àmbit industrial per magatzems. Òbviament, el nostre robot és una versió petita i prototipada, feta a petita escala però escalable i portable a altres entorns o dimensions. Com que fa automàticament la tasca de buscar un nom d'un llibre, reconèixer-lo i agafar-lo, fa més senzilla la tasca de buscar a prestatgeries i agafar un llibre. Això pot prevenir certs accidents laborals o riscos que poden patir les persones i/o treballadors en dur a terme aquestes tasques. També pot ajudar a reduir l'estrès sobre el cos humà en estar dempeus molt de temps, carregar amb molt de pes (pot prevenir el mal d'esquena a la gent que fa un esforç per poder estirar-se, pujar a una escala per agafar un llibre...) i a més, com és interactiu al demanar el llibre per detecció de veu, és més divertit i accessible per més persones. 
Per acabar, cal destacar, com s'ha exposat abans, que el robot és escalable a altres entorns o funcionalitats. Pot fer-se servir per agafar o detectar llibres, però si es volgués, podria modificar-se per agafar algun altre tipus d'objecte. També es podria augmentar l'escala del robot; fer-lo més gran; amb una ventosa més potent o un sistema de recol·lecció d'objectes més ferm per poder agafar objectes més pesats; canviar el sistema de detecció d'objectes per en comptes de detectar llibres detectar algun altre tipus d'objecte... 
En resum, aquest robot contribueix a facilitar una tasca que pot ser feixuga per a certs tipus de persones i es pot escalar i portar a altres entorns i funcionalitats, tenint un potencial atractiu per poder modificar, canviar i implementar en altres necessitats.
<h2 id="components">Components</h2>
<table>
<thead>
  <tr>
    <th class="tg-c3ow"><span style="font-weight:bold">Nom</span></th>
    <th class="tg-c3ow"><span style="font-weight:bold">Quantitat</span></th>
    <th class="tg-c3ow"><span style="font-weight:bold">Imatge</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">Arduino Nano</td>
    <td class="tg-c3ow">2</td>
    <td class="tg-c3ow"><img src="https://roboticafacil.es/wp-content/uploads/2017/04/Arduino-Nano-V3-2-e1492726589312.jpg" alt="" width="240"></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Raspberry Pi 4b</td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Raspberry_Pi_4_Model_B_-_Side.jpg/640px-Raspberry_Pi_4_Model_B_-_Side.jpg" alt="" width="240"></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Bateries 7,2V</td>
    <td class="tg-c3ow">2</td>
    <td class="tg-c3ow"><img src="https://www.ninco.com/images/product/1/large/pl_1_1_8411.jpg" alt="" width="240"></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Raspberry Pi Cam</td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow"><img src="https://diotronic.com/22112-large_default/camara-5mp-ov5647-rpi.jpg" alt="" width="240"></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Micròfon USB</td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow"><img src="https://m.media-amazon.com/images/I/61aLrDHYj+L._AC_SL1300_.jpg" alt="" width="240"></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Protoboard</td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow"><img src="https://www.electrio.es/WebRoot/StoreES3/Shops/80295836/5E75/0236/E7D3/0030/608F/0A0C/6D10/89ED/Protoboad_400_1.jpg" alt="" width="240"></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Relé</td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow"><img src="https://createc3d.com/1244-large_default/comprar-modulo-rele-5v-compatible-con-arduino-1-canal-precio-oferta.webp" alt="" width="240"></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Controladores</td>
    <td class="tg-c3ow">3</td>
    <td class="tg-c3ow"><img src="https://www.electrio.es/WebRoot/StoreES3/Shops/80295836/5FFD/F7AD/ADB1/BDCA/56DA/0A0C/6D12/501D/L298_Puente_H_3.jpg" alt="" width="240"></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Motors</td>
    <td class="tg-c3ow">6</td>
    <td class="tg-c3ow"><img src="https://www.bds-tech.com.hk/image/cache/catalog/VEX%20EDR/EDR%20Accessories%20-%20Motion/276-2177%202-Wire%20Motor%20393-800x800.jpg" alt="" width="240"></td>
  </tr>
  <tr>
    <td class="tg-c3ow">Succionador</td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow"><img src="https://cdn.shopify.com/s/files/1/0058/3145/8904/products/5194Y48vx0L._SL1100.jpg?v=1597440457" alt="" width="240"></td>
  </tr>
</tbody>
</table>

<h2 id="esquema-de-hardware">Esquema de <i>hardware</i></h2>
<img src="images/librobot_bb.jpg" alt="">
La Raspberry Pi 4 controla els 2 Arduino Nano (connectats per USB), el micròfon USB i la Raspberry Pi Cam, està connectada a una bateria portàtil. 
La base té 5 motors controlats per 3 controladores i un Arduino, els dos motors d'un costat connectats a una controladora, els de l'altre costat a una altra i el de la roda del centre connectat a una altra. En aquesta última controladora també està connectat el motor que puja i baixa. Els motors estan connectats directament a les contrladores, les controladores estan conectades al Arduino Nano i les 3 reben alimentació d'una bateria de 7,2 Volts.
L'altre Arduino controla el succionador mitjançant un relé connectat a una altra bateria de 7,2 Volts.

<h2 id="arquitectura-de-software">Arquitectura de <i>software</i></h2>
En la següent imatge es mostra l'esquema software que fa servir el nostre robot:
<img src="images/arquitecturasoftware.PNG" alt="" width="480">
La implementació del robot es divideix en els següents mòduls operatius:
<ul>
 <li>Mòdul Central: Interconecta tots els mòduls.</li>
 <li>Mòdul Càmera: Conté l’algorisme de Visió per computador per reconèixer els títols dels llibres.</li>
 <li>Mòdul Veu: Conté l’algorisme de reconeixement de veu.</li>
 <li>Mòdul de moviment: Conté l’algorisme per controlar els moviments del robot. Tant del braç com de les rodes.</li>
</ul>
El primer que es fa és activar el mòdul de detecció de veu (s'escolta el llibre que es vol recollir). Seguidament, activem el mòdul de la càmera per veure si en la posició inicial es troba el llibre en la visió de la càmera. Tant si es troba com si no, activem el mòdul de moviment per poder moure el robot i encaixar-lo en una posició on tingui el llibre centrat amb el braç per poder-lo agafar.

<h2 id="video">Vídeo</h2>
<a href="https://youtu.be/lkXDEsOFu7Q"><img src="http://i3.ytimg.com/vi/lkXDEsOFu7Q/maxresdefault.jpg" style="height: 50%; width:50%;"/></a>

<h2 id=contribucions>Contribucions</h2>
Tothom és lliure de contribuir amb qualsevol cosa que pugui potencialment millorar el projecte, sigui en temes de disseny, arquitectura del software, codi, components hardware... Qualsevol cosa és benvinguda, i apreciem les contribucions. Si et sents capaç, contacta amb el propietari d'aquest GitHub sense cap tipus de problema i contestarem el més aviat possible.

<h2 id=Citacions> Citacions </h2>
Si fas servir aquest projecte com a model acadèmic de treball o industrial, si us plau, cita'ns. Fes servir aquest format: "Librobot, robot que interactua amb una persona per buscar un llibre a les prestatgeries donant un títol per veu i que el succiona per poder-lo agafar", 2023, nom dels autors (els nostres noms) i un enllaç a aquest GitHub.

<h2 id="llicencia">Llicència</h2>
MIT

<h2 id="autors">Autors</h2>
Daniel García Castro<br>
Maria Jordana Marín<br>
Rubén Ramos Segarra<br>
Ferran Antón Serrano<br>
Oscar Pocurull Rodríguez

<h2 id="bibliografia">Bibliografia</h2>
Aquest projecte ha sigut inspirat pels següents projectes d'Internet: <br>
1. https://rlpengineeringsschooluab2022.wordpress.com/2022/06/01/nonabot/<br>
2. https://rlpengineeringsschooluab2022.wordpress.com/2022/06/01/98/

