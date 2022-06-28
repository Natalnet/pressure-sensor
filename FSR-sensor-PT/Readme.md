# FSR-sensor (Português)
Sensor de Força Resistiva, ele detecta pressão física e muda a resistência quando a força ou pressão for aplicada. Quanto maior for a pressão, mais material condutivo irá entrar em contato com os cabos e diminuir a resistência. 

![Img. 1](https://user-images.githubusercontent.com/89589831/175841407-2f120a7c-c3ec-4b06-8f27-fa62ea024843.png)


## Informações do FSR

- FSR 402
- **Parte ativa:** 12,7mm
- **Sensibilidade:** 0.1N a 10.0²N

## Aplicação

Devemos ver, no monitor serial, informações em Newton e em Pascal. Normalmente, o valor retornado é em milivolts, porém essa unidade de mendida não nos ajuda na análise dos dados.

Essa é a fórmula que vamos usar pra calcular a resistência:
 - Rfsr = resistência do sensor
 - Vcc = tensão de saída do Arduíno (estamos usando 5V)
 - U = tensão medida
 - R1 = resistência do pull-down 


![Img. 2](https://user-images.githubusercontent.com/89589831/175950357-a65712df-8a8a-41fb-a32a-d6d6ac32dbab.png)


After doing it, we will need to know the electrical conductance :

It’s easy to see that the electrical conductance is the opposite of the electrical resistance.

![Img. 3](https://user-images.githubusercontent.com/89589831/175951223-72508f11-a1ae-453a-a457-4676292dfc39.jpeg)


## Circuit
The sensor has two pins, the right and the left one.

**1. LEFT PIN:**
- We're going to connect only to the VCC (5V) -- red cable 


**2. RIGHT PIN:**
- First, we're going to get a 10kohm resistor and put one of its pin here and the other on a free spot inside the breadboard


**3. CONNECTIONS WITH THE RESISTOR:**
- Above the resistor, we're going to connect on the analog input on the Arduino -- blue cable
- Under the resistor, we're goin to connect to the GND (ground) -- black cable



![Circuit](https://user-images.githubusercontent.com/89589831/175819253-d190b07d-48bd-44ff-b732-99d5664948bd.jpeg)


### References
https://www.caplinq.com/blog/force-sensitive-resistor-fsr-sensor_1638/#:~:text=A%20force%20sensitive%20resistor%20(FSR,physical%20pressure%2C%20squeezing%20and%20weight.

https://www.elprocus.com/force-sensing-resistor-technology/

