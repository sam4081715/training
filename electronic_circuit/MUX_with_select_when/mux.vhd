LIBRARY ieee;
USE ieee.std_logic_1164.all;
-------------------------------------------
ENTITY mux IS
   PORT ( a, b, c, d: IN STD_LOGIC;
                 sel: IN STD_LOGIC_VECTOR(1 DOWNTO 0);
                   y: OUT STD_LOGIC);
END mux;
-------------------------------------------
ARCHITECTURE mux2 OF mux IS
BEGIN
   WITH sel SELECT
      y <= a WHEN "00", 	-- notice "," instead of ";"
           b WHEN "01",
           c WHEN "10",
           d WHEN OTHERS; 	-- cannot be "d WHEN "11" "
END mux2;
