LIBRARY ieee;
USE ieee.std_logic_1164.all;

ENTITY decoder_ssd IS
	PORT ( SW: IN STD_LOGIC_VECTOR (3 DOWNTO 0);
			 HEX0: OUT STD_LOGIC_VECTOR (0 TO 6));
END decoder_ssd;
	
ARCHITECTURE decoder1 OF decoder_ssd IS
BEGIN
	HEX0 <= "1001000" WHEN SW="0000" ELSE
			"0110000" WHEN SW ="0001" ELSE
			"1110001" WHEN SW ="0011" ELSE
			"1110001" WHEN SW ="0111" ELSE
			"0000001" WHEN SW ="1111" ELSE
			"1111111";
END decoder1;
