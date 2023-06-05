# Librobot
Robot que interactua amb una persona per buscar un llibre a les prestatgeries donant un títol per veu i que el succiona depositant-lo a un suport per poder-lo agafar.
<br> </br>


<img src="images/librobot.PNG" alt="">

## Taula de continguts
1. [En què consiteix?](#en-que-consiteix)
2. [Requisits](#requisits)
3. [Com funciona?](#com-funciona)
4. [Components](#components)
5. [Esquema de *hardware*](#esquema-de-hardware)
6. [Peces 3D](#peces-3d)
7. [Arquitectura de *software*](#arquitectura-de-software)
8. [Vídeo](#video)
9. [Llicència](#llicencia)
10. [Autors](#autors)
11. [Bibliografia](#bibliografia)

<h2 id="en-que-consiteix">En què consiteix?</h2>
Aquest robot és un sistema que inclou components físics i electrònics amb la capacitat de realitzar quatre moviments (graus de llibertat) diferents, cadascun dels quals implica una base mòbil davant d'un prestatge amb una barra vertical que mou un braç per agafar un llibre. El sistema utilitza una càmara, un micròfon per sol·licitar un llibre, una ventosa al final del braç i algorismes per identificar i localitzar llibres específics a la prestatgeria, i el braç està dissenyat per estendre's i arronsar-se, succionant els llibres i deixant-los a sobre d'un suport metàl·lic. Amb aquest punt de partida inicial establit, es faran servir una sèrie de components electrònics que permetràn posar en funcionament el robot ajustant-se a les restriccions de moviment anteriors.

<h2 id="requisits">Requisits</h2>
Per fer funcionar el robot fem servir els següents entorns:
<ul>
 <li>C++ (variant de l'Arduino)</li>
 <li>Python (Raspberry Pi)</li>
</ul>
A més d'incloure les següents llibreries:
<ul>
 <li>Math (C++)</li>
 <li>OpenCV (Pyhton)</li>
 <li>NumPy (Python)</li>
 <li>TensorFlow (Python)</li>
</ul>

<h2 id="com-funciona">Com funciona?</h2>
1. Clona aquest repositori:

   ```terminal
   git clone https://github.com/RubenRS040398/librobot.git
   ```

2. Instal·la les llibreries necessàries:

- Si es fa servir conda:

  ```terminal
  conda install -c menpo opencv3
  ```
 
- Si es fa servir pip:

  ```terminal
  pip install opencv-python
  ```

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
<img src="images/librobot_bb.jpg" alt="" width="640">

<h2 id="peces-3d">Peces 3D</h2>
¿?

<h2 id="arquitectura-de-software">Arquitectura de <i>software</i></h2>
<img src="images/arquitecturasoftware.PNG" alt="" width="480">
La implementació del robot es divideix en els següents mòduls operatius:
<ul>
 <li>Mòdul Central: Interconecta tots els mòduls.</li>
 <li>Mòdul Càmera: Conté l’algorisme de Visió per computador per reconèixer els títols dels llibres.</li>
 <li>Mòdul Veu: Conté l’algorisme de reconeixement de veu.</li>
 <li>Mòdul de moviment: Conté l’algorisme per controlar els moviments del robot. Tant del braç com de les rodes</li>
</ul>

<h2 id="video">Vídeo</h2>
¿?

<h2 id="llicencia">Llicència</h2>
MIT

<h2 id="autors">Autors</h2>
Daniel García Castro<br>
Maria Jordana Marín<br>
Rubén Ramos Segarra<br>
Ferran Antón Serrano<br>
Oscar Pocurull Rodríguez

<h2 id="bibliografia">Bibliografia</h2>
1. https://rlpengineeringsschooluab2022.wordpress.com/2022/06/01/nonabot/<br>
2. https://rlpengineeringsschooluab2022.wordpress.com/2022/06/01/98/
