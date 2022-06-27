# FSR-sensor
Force Sensor Resistor, it detects physical pressure which changes its resistance when a force or pressure is applied. The higher the pressure, more conductive material will contact to the wires

![Img. 1](https://user-images.githubusercontent.com/89589831/175841407-2f120a7c-c3ec-4b06-8f27-fa62ea024843.png)


## FSR information

- FSR 402
-** Active part:** 12,7mm
- **Sensitivity:** 0.1N a 10.0²N


## Circuit
The sensor has two pins, the right and the left one.

**1. LEFT PIN:**
- We're going to connect only to the CVV (5V) -- red cable 


**2. RIGHT PIN:**
- First, we're going to get a 10kohm resistor and put one of its pin here and the other on a free spot inside the breadboard


**3. CONNECTIONS WITH THE RESISTOR:**
- Above the resistor, we're going to connect on the analog input on the Arduino -- blue cable
- Under the resistor, we're goin to connect to the GND (ground) -- black cable



![Circuit](https://user-images.githubusercontent.com/89589831/175819253-d190b07d-48bd-44ff-b732-99d5664948bd.jpeg)


### References
https://www.caplinq.com/blog/force-sensitive-resistor-fsr-sensor_1638/#:~:text=A%20force%20sensitive%20resistor%20(FSR,physical%20pressure%2C%20squeezing%20and%20weight.

https://www.elprocus.com/force-sensing-resistor-technology/
