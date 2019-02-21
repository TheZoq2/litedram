from litedram.modules import MT41J256M16
from litedram.phy import K7DDRPHY

core_config = {
    # General ------------------------------------------------------------------
    "cpu":        "vexriscv", # Type of CPU used for init/calib (vexriscv, lm32)
    "speedgrade": -2,         # FPGA speedgrade

    # PHY ----------------------------------------------------------------------
    "cmd_delay":       0,           # Command additional delay (in taps)
    "cmd_latency":     0,           # Command additional latency
    "sdram_module":    MT41J256M16, # SDRAM modules of the board or SO-DIMM
    "sdram_module_nb": 4,           # Number of byte groups
    "sdram_rank_nb":   1,           # Number of ranks
    "sdram_phy":       K7DDRPHY,    # Type of FPGA PHY

    # Electrical ---------------------------------------------------------------
    "rtt_nom": "60ohm", # Nominal termination
    "rtt_wr":  "60ohm", # Write termination
    "ron":     "34ohm", # Output driver impedance

    # Frequency ----------------------------------------------------------------
    "input_clk_freq":   200e6, # Input clock frequency
    "sys_clk_freq":     100e6, # System clock frequency (DDR_clk = 4 x sys_clk)
    "iodelay_clk_freq": 200e6, # IODELAYs reference clock frequency

    # Core ---------------------------------------------------------------------
    "cmd_buffer_depth": 16,    # Depth of the command buffer

    # User Ports ---------------------------------------------------------------
    "user_ports_nb":       2,     # Number of user ports
    "user_ports_type":     "axi", # Type of ports (axi, native)
    "user_ports_id_width": 32,    # AXI identifier width
}
