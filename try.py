import streamlit as st
import math
from PIL import Image
st.markdown("PHYSICS")
#st.header("***Not only is the Universe stranger than we think, it is stranger than we can think...***")
tab1,tab2,tab3,tab4= st.tabs(['RESISTOR COLOR CODE CALCULATOR','NUMBER CONVERSION','OHMS LAW','CONSTANTS'])
with tab1:
 st.title("RESISTOR COLOR CODE CALCULATOR")
#color_digit = {'black': '0','brown': '1','red': '2','orange': '3','yellow': '4','green' : '5','blue' : '6','violet' : '7','grey' : '8','white': '9'}
#multiplier = {'black': '1','brown': '10','red': '100','orange': '1k','yellow': '10k','green' : '100k','blue' : '1M','violet' : '10M','grey' : '100M','white': '1G'}
#tolerance = {'brown': '+/- 1 %','red' : '+/- 2 %','green': "+/- 0.5 %",'blue': '+/- 0.25 %','violet' : '+/- 0.1 %','gold': '+/- 5 %','silver' : '+/- 10 %','none': '+/-20 %'}
 img=Image.open("resistor-color-chart.png")
 st.image(img) 
 first=st.selectbox("1st Band of Color",('Black','Brown','Red','Orange','Yellow','Green','Blue','Grey','White'))
 if first=='Black':
  first=0
 if first=='Brown':
  first=1
 if first=='Red':
  first=2
 if first=='Orange':
  first=3
 if first=='Yellow':
  first=4
 if first=='Green':
  first=5
 if first=='Blue':
  first=6 
 if first=='Violet':
  first=7
 if first=='Grey':
  first=8 
 if first=='White':
  first=9
 second=st.selectbox("2nd Band of Color",('Black','Brown','Red','Orange','Yellow','Green','Blue','Grey','White'))
 if second=='Black':
  second=0
 if second=='Brown':
  second=1
 if second=='Red':
  second=2
 if second=='Orange':
  second=3
 if second=='Yellow':
  second=4
 if second=='Green':
  second=5
 if second=='Blue':
  second=6
 if second=='Violet':
  second=7
 if second=='Grey':
  second=8
 if second=='White':
  second=9
 third=st.selectbox("3rd Band of Color",('Black','Brown','Red','Orange','Yellow','Green','Blue','Grey','White'))
 if third=='Black':
  third=1
 if third=='Brown':
  third=10
 if third=='Red':
  third=100
 if third=='Orange':
  third=1000
 if third=='Yellow':
  third=10000
 if third=='Green':
  third=100000
 if third=='Blue':
  third=1000000
 if third=='Violet':
  third=10000000
 if third=='Grey':
  third=100000000
 if third=='White':
  third=1000000000
 fourth=st.selectbox("4th Band of Color",('Brown','Red','Green','Blue','Violet','Gold','Silver'))
 if fourth=='Brown':
  fourth= 1 
 if fourth=='Red':
  fourth= 2
 if fourth=='Green':
  fourth= 0.5
 if fourth=='Blue':
  fourth= 0.25
 if fourth=='Violet':
  fourth= 0.1
 if fourth=='Gold':
  fourth= 5
 if fourth=='Silver':
  fourth= 10 
 if fourth=='None':
  fourth= 20
 vi = (third)
 st.write("Resistance Value ",first,second*vi ,"±",fourth ,"%","ohms")  
with tab2:
 img=Image.open("Number-Systems.jpg")
 st.image(img)
#st.info("Number Conversion Explained :\n The decimal numbering system is what we use on a daily basis. In the decimal numbering system the position of the digits represent a power of 10 (base 10). This means that as you move left from the least significant bit, you will increment to the next position after you reach 9. A value of 9 represents 9 “ones”, while 10 represents 1 “ten”.\n Binary is a base 2 system in which only 1’s and 0’s are used. Each position represents a step of 1. A binary number of 1 is followed sequentially with 10 (1 in the “2’s” place and “0” in the ones). Next would be 11 (1 in the 2’s, +1 in the ones). 100 would be Decimal 4 (1 in the fours, 0 in the 2, 0 in the ones). The biggest advantage of a binary numbering system when it comes to programming is that it’s very easy for circuits to represent the two states. In electronics, the 1’s and 0’s can be used as off or on states. This makes Binary the base for all programming. Binary’s downfalls come from the fact that binary numbers end up being very long if the number is large.\nThe Octal system is base 8 which means the positional indication of the numbers (from LSB) go 1’s, 8’s, 64’s, etc. For example – in the octal numbering system 135 breaks down as 1x64 + 3x8 + 5x1 for a total of 93. The octal system is less popular today and has largely been replaced by the base 16 Hexadecimal system.\nThe Hexadecimal system is based on a base of 16 and uses the numbers 0-9 and the letters A~F. In this system the “ones” position increments 0-9 but “10” is represented by the letter A, 11 by B, etc. The biggest advantage of the hex system is that it is an easier way to represent very large numbers. A hex value of 4B6 breaks down to 4 (binary 0100) B (binary 1011) 6 (binary 0110). In this way it can take a very long binary string and condense it into an easier to read format.")
#sys=st.selectbox("Select the Number System to be Converted",('Binary','Octadecimal','Decimal'))
 def decimal_into_binary(decimal_1): 
  decimal = int(decimal_1)   
  st.write("The given decimal number", decimal, "in Binary number is: ", bin(decimal))  
 def decimal_into_octal(decimal_1):  
  decimal = int(decimal_1)  
  st.write("The given decimal number", decimal, "in Octal number is: ", oct(decimal))    
 def decimal_into_hexadecimal(decimal_1):
  decimal = int(decimal_1)     
  st.write("The given decimal number", decimal, " in Hexadecimal number is: ", hex(decimal))   
 decimal_1 = st.number_input(" Enter the Decimal Number: ")
 st.write(decimal_into_binary(decimal_1))  
 st.write(decimal_into_octal(decimal_1))  
 st.write(decimal_into_hexadecimal(decimal_1))  

with tab3:
  col1, col2= st.columns(2)

with col1:
 img=Image.open("ohms-law-chart.png")
 st.image(img) 
with col2:
  st.title("OHM'S LAW CALCULATOR")
  st.write("1. Calculate Voltage")
  st.write("2. Calculate Resistance")
  st.write("3. Calculate Current")
  ask = st.text_input("Enter the quantity to be calculated by Ohms Law: ")
  if (ask == "1"):
        
        st.write("-- Calculating Voltage --")
        i = st.number_input("Current: ")
        r = st.number_input("Resistance: ")
        v = i*r
        st.write("Voltage = ", format(v, ".2f"),"volts")

  if(ask == "2"):
        st.write("-- Calculating Resistance --")
        v =st.number_input("Voltage: ")
        i =st.number_input("Current: ")
        r = v/i
        st.write("Resistance = ", format(r, ".2f"),"ohms")

  if(ask == "3"):
        st.write("-- Calculating Current --")
        v = st.number_input("Voltage: ")
        r = st.number_input("Resistance: ")
        i = v/r
        st.write("Current = ", format(i, ".2f"),"amperes")
with tab4:
 img=Image.open("constants.jpg")
 st.image(img)

 

