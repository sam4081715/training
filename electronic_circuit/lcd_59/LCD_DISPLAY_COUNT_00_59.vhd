--**********************************************
--*  Counter From 00 To 59 And Display In LCD  *
--*   Filename : LCD_DISPLAY_COUNT_00_59.VHD   *
--**********************************************

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity LCD_DISPLAY_COUNT_00_59 is
    Port ( CLK      : in std_logic;
           RESET    : in std_logic;
  		 LCM_RW   : out std_logic;
           LCM_EN   : out std_logic;
           LCM_RS   : out std_logic;
           LCM_DATA : out std_logic_vector(7 downto 0));
end LCD_DISPLAY_COUNT_00_59;

architecture Behavioral of LCD_DISPLAY_COUNT_00_59 is
  signal INIT_CLK  : std_logic;
  signal COUNT_CLK : std_logic;
  signal TIME_BCD  : std_logic_vector(7 downto 0);
  signal LCM_COUNT : std_logic_vector(5 downto 0);
  signal DIVIDER   : std_logic_vector(25 downto 1); 
begin

--*******************************
--*     Time Base Generation    *
--*******************************

  process (CLK,RESET)
    begin
	if RESET    = '0' then 
	   DIVIDER <= "0000000000000000000000000";
	elsif CLK'event and CLK = '1' then 
	   DIVIDER <= DIVIDER + 1;
	end if;
  end process;
  INIT_CLK  <= DIVIDER(15);
  COUNT_CLK <= DIVIDER(25);
  LCM_EN    <= INIT_CLK;

--*************************************************
--*  Generate LCD Write Counter And Display Data  *
--*************************************************

process (RESET,INIT_CLK)

     begin
       if RESET      = '0' then
	     LCM_COUNT <= "000000";
	     LCM_RS    <= '0';
          LCM_RW    <= '0';
	     LCM_DATA  <= "00000001";
	  elsif INIT_CLK'event and INIT_CLK = '1' then
	    if LCM_COUNT < "100110" then
            LCM_COUNT <= LCM_COUNT + 1;
         else
	       LCM_COUNT <= "000101";
	    end if;
         case LCM_COUNT is
	      when "000000"   =>
	           LCM_RS    <= '0';
		      LCM_RW    <= '0';
		      LCM_DATA  <= "00111100";  -- 8 BIT, 2 Lines, 5 * 7 Dot
		 when "000001"	  =>
			 LCM_DATA  <= "00111100";  -- 8 BIT, 2 Lines, 5 * 7 Dot
           when "000010"   => 
	            LCM_DATA <= "00000001";  -- Clear LCD Display 
	       when "000011"  => 				
                 LCM_DATA <= "00000110";  -- Cursor Shift Right ,AC + 1
	       when "000100"  => 
                 LCM_DATA <= "00001100";  -- Display on, Cursor off
            when "000101"  =>
		       LCM_RS   <= '0';
                 LCM_DATA <= "10000000";  -- Set Cursor
	       when "000110"  =>
		       LCM_RS   <= '1';
		       LCM_DATA <= "01001100";  -- L
	       when "000111"  => 
		       LCM_DATA <= "01000011";  -- C
	       when "001000"  => 
		       LCM_DATA <= "01000100";  -- D
	       when "001001"  => 
	            LCM_DATA <= "00100000";  --  
	       when "001010"  =>
	         	  LCM_DATA <= "01000100";  -- D
		  when "001011"  =>
	            LCM_DATA <= "01001001";  -- I
	       when "001100"  => 
	            LCM_DATA <= "01010011";  -- S
	       when "001101"  => 			
                 LCM_DATA <= "01010000";  -- P
	       when "001110"  => 			 
                 LCM_DATA <= "01001100";  -- L
            when "001111"  =>
                 LCM_DATA <= "01000001";  -- A
		  when "010000"  => 
	            LCM_DATA <= "01011001";  -- Y
	       when "010001"  => 				
                 LCM_DATA <= "00100000";  --  
	       when "010010"  => 
                 LCM_DATA <= "01010100";  -- T
            when "010011"  =>
                 LCM_DATA <= "01000101";  -- E
	      when  "010100"  => 
                 LCM_DATA <= "01010011";  -- S
            when "010101"  =>
                 LCM_DATA <= "01010100";  -- T
            when "010110"  =>
                 LCM_RS   <= '0';
                 LCM_DATA <= "11000000";  -- Set Cursor
            when "010111" =>
                 LCM_RS   <= '1';
		       LCM_DATA <= "01000011";  -- C
	       when "011000"  => 
		       LCM_DATA <= "01001111";  -- O
		  when "011001"  => 
		       LCM_DATA <= "01010101";  -- U
	       when "011010"  => 
	            LCM_DATA <= "01001110";  -- N
	       when "011011"  =>
	       	  LCM_DATA <= "01010100";  -- T
     	  when "011100"  =>
	            LCM_DATA <= "00100000";  --  
	       when "011101"  => 
	            LCM_DATA <= "01010110";  -- V
	       when "011110"  => 			
                 LCM_DATA <= "01000001";  -- A
	       when "011111"  => 			 
                 LCM_DATA <= "01001100";  -- L
            when "100000"  =>
                 LCM_DATA <= "01010101";  -- U
		  when "100001"  => 
	            LCM_DATA <= "01000101";  -- E
	       when "100010"  => 				
                 LCM_DATA <= "00100000";  --  
	       when "100011"  => 
                 LCM_DATA <= "00111010";  -- :
            when "100100"  =>
                 LCM_DATA <= "00100000";  --  
	       when "100101"  =>
                 LCM_DATA <= "0011" & TIME_BCD(7 downto 4);
            when others    =>
                 LCM_DATA <= "0011" & TIME_BCD(3 downto 0);
         end case;
	  end if;
   end process;

--**************************************
--*  Up Counter range  From 00 To 59   *
--**************************************

  process (COUNT_CLK,RESET)

    begin
      if RESET = '0' then 
	    TIME_BCD(7 downto 0) <= "00000000";
	 elsif COUNT_CLK'event and COUNT_CLK = '1' then
	    if TIME_BCD(3 downto 0)  = "1001" then
	       TIME_BCD(3 downto 0) <= "0000";
            TIME_BCD(7 downto 4) <= TIME_BCD(7 downto 4) + 1;
	     else
	       TIME_BCD(3 downto 0) <= TIME_BCD(3 downto 0) + 1;
	     end if;
          if TIME_BCD(7 downto 0)   = "01011001" then
             TIME_BCD(7 downto 0) <= "00000000";
	   end if;
	 end if;
  end process;

end Behavioral;
	   