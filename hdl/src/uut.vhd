library ieee;
use ieee.std_logic_1164.all;


entity uut is
    port (
        iClk: in std_logic;

        iValid: in std_logic;
        iData: in std_logic_vector (7 downto 0);
        oAck: out std_logic;

        oValid: out std_logic;
        oData: out std_logic_vector (7 downto 0);
        iAck: in std_logic
    );
end entity;

architecture v1 of uut is
begin

    oAck <= iAck;
    oValid <= iValid;
    oData <= iData;

end v1;

