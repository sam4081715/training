LIBRARY ieee;
USE ieee.std_logic_1164.all;
-------------------------------------------
ENTITY mux IS
   PORT ( a, b, c, d: IN STD_LOGIC;
                 sel: IN STD_LOGIC_VECTOR(1 DOWNTO 0);
                   y: OUT STD_LOGIC);
END mux;
-------------------------------------------
ARCHITECTURE mux1 OF mux IS
BEGIN
   y <= a WHEN sel="00" ELSE
        b WHEN sel="01" ELSE
        c WHEN sel="10" ELSE
        d;
END mux1;
