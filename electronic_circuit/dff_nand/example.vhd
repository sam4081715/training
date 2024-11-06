ENTITY example IS   
	PORT ( a, b, clk: IN BIT;
						q: OUT BIT);
END example;

ARCHITECTURE example OF example IS
SIGNAL temp : BIT;
BEGIN
	temp <= a NAND b;
	PROCESS (clk)
	BEGIN
		IF (clk'EVENT AND clk='1') THEN q <= temp;
			END IF;
	END PROCESS;
END example;