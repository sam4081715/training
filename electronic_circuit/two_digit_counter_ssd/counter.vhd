--------------------------------------------------
LIBRARY ieee;
USE ieee.std_logic_1164.all;
--------------------------------------------------
ENTITY counter IS
   PORT (clk, reset : IN STD_LOGIC;
     digit1, digit2 : OUT STD_LOGIC_VECTOR (0 TO 6));
END counter;
--------------------------------------------------
ARCHITECTURE counter OF counter IS
BEGIN
   PROCESS(clk, reset)
      VARIABLE temp1: INTEGER RANGE 0 TO 10;
      VARIABLE temp2: INTEGER RANGE 0 TO 10;
   BEGIN
      ---- counter: ----------------------
      IF (reset='0') THEN
         temp1 := 0;
         temp2 := 0;
      ELSIF (clk'EVENT AND clk='1') THEN
         temp1 := temp1 + 1;
         IF (temp1=10) THEN
            temp1 := 0;
            temp2 := temp2 + 1;
            IF (temp2=10) THEN
               temp2 := 0;              
            END IF;                             
         END IF;                             
      END IF;                             
		---- BCD to SSD conversion: --------
      CASE temp1 IS                       
         WHEN 0 => digit1 <= "0000001"; 
         WHEN 1 => digit1 <= "1001111";  
         WHEN 2 => digit1 <= "0010010";  
         WHEN 3 => digit1 <= "0000110";  
         WHEN 4 => digit1 <= "1001100";  
         WHEN 5 => digit1 <= "0100100";  
         WHEN 6 => digit1 <= "1100000";  
         WHEN 7 => digit1 <= "0001111";  
         WHEN 8 => digit1 <= "0000000";  
         WHEN 9 => digit1 <= "0001100";  
         WHEN OTHERS => NULL;                
      END CASE;                           
      CASE temp2 IS                       
         WHEN 0 => digit2 <= "0000001";  
         WHEN 1 => digit2 <= "1001111";  
         WHEN 2 => digit2 <= "0010010";  
         WHEN 3 => digit2 <= "0000110";  
         WHEN 4 => digit2 <= "1001100";  
         WHEN 5 => digit2 <= "0100100";  
         WHEN 6 => digit2 <= "1100000";  
         WHEN 7 => digit2 <= "0001111";  
         WHEN 8 => digit2 <= "0000000";  
         WHEN 9 => digit2 <= "0001100";  
         WHEN OTHERS => NULL;                
      END CASE;                           
   END PROCESS;                        
END counter;                        
--------------------------------------------------
