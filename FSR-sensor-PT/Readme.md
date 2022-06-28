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


Após fazer isso, temos que saber a condutância elétrica:

Ao comparar as fórmulas, é fácil de perceber que a contutãncia elétrica é o oposto da resistência elétrica.

![Img. 3](https://user-images.githubusercontent.com/89589831/175951223-72508f11-a1ae-453a-a457-4676292dfc39.jpeg)


## Circuito
O sensor possui dois pinos, o direito e o esquerdo.

**1. PINO ESQUERDO:**
- Iremos conectar o esquerdo apenas com o VCC (5V) -- cabo vermelho 


**2. PINO DIREITO:**
- Primeiro, iremos pegar um resistor de 10Kohm e colocar um dos seus pinos alinhados com o pino direito do sensor, e o outro iremos colocar em um espaço vazio na nossa protoboard.


**3. CONECÇÕES COM O RESISTOR:**
- Acima do resistor, nós vamos conectar na entrada analógica no Arduíno -- cabo azul
- Abaixo do resistor, vamos conectar com o GND -- cabo preto


![Circuit](https://user-images.githubusercontent.com/89589831/175819253-d190b07d-48bd-44ff-b732-99d5664948bd.jpeg)


### Referência
https://www.caplinq.com/blog/force-sensitive-resistor-fsr-sensor_1638/#:~:text=A%20force%20sensitive%20resistor%20(FSR,physical%20pressure%2C%20squeezing%20and%20weight.

https://www.elprocus.com/force-sensing-resistor-technology/

