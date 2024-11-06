---------------------------------------------
LIBRARY ieee;
USE ieee.std_logic_1164.all;
use IEEE.STD_LOGIC_ARITH.all;
use IEEE.STD_LOGIC_UNSIGNED.all;
---------------------------------------------
ENTITY counter4 IS
   PORT (KEY  : IN STD_LOGIC_VECTOR(0 to 1);
       LEDG : OUT STD_LOGIC_VECTOR(3 downto 0));
END counter4;
---------------------------------------------
ARCHITECTURE counter OF counter4 IS
 signal rst,clk: std_logic;
 signal pre_Q: std_logic_vector(3 downto 0);
BEGIN
   rst <= KEY(1); clk <= KEY(0);
   count: PROCESS(rst,clk)
   BEGIN
      IF (rst= '0' )THEN
	 pre_Q <= "0000";
      ELSIF(clk'EVENT AND clk='1') THEN
	  IF (pre_Q = "1111") THEN pre_Q <= "0000"; 
	  ELSE pre_Q <= pre_Q+1;
          END IF;
      END IF;
      LEDG <= pre_Q;
   END PROCESS count;
END counter;
