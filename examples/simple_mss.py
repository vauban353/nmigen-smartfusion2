from nmigen import *
from nmigen_boards.m2s010_mkr_kit import *
from nmigen_smartfusion2.mss import *

from nmigen.build.dsl import *
from nmigen.build.res import *
from nmigen.build import Platform
from nmigen.lib.cdc import ResetSynchronizer

from nmigen_smartfusion2.macro_ccc import *
from nmigen_smartfusion2.macro_rcosc import *

class FabricOscillator(Elaboratable):
    def __init__(self):
        self.rcosc_50mhz_clkout = Signal(1)

    def elaborate(self, platform: Platform) -> Module:
        platform.add_file("./osc_comps.v", get_rcosc_macro())
        m = Module()
        rcosc_out = Signal(1)
        m.submodules.I_RCOSC_25_50MHZ = Instance("RCOSC_25_50MHZ", p_FREQUENCY=50.0, o_CLKOUT=rcosc_out)
        rcoscfab_out = Signal(1)
        m.submodules.rcosc50mhz_fab = Instance("RCOSC_25_50MHZ_FAB", i_A=rcosc_out, o_CLKOUT=rcoscfab_out)
        m.submodules.rcosc50mhz_clkint = Instance("CLKINT", i_A=rcoscfab_out, o_Y=self.rcosc_50mhz_clkout)
        return m


class ClockConditioningCircuit(Elaboratable):
    def __init__(self):
        self.clkin_50mhz = Signal()
        self.clkout_100mhz = Signal()
        self.pll_lock = Signal()

    def elaborate(self, platform: Platform) -> Module:
        platform.add_file("./CCC_50mhz_rcosc_in_100mhz_out.v", get_ccc_macro())
        m = Module()
        m.submodules.ccc_instance = Instance("CCC_50MHZ_RCOSC_IN_100MHZ_OUT",
                                         i_RCOSC_25_50MHZ=self.clkin_50mhz,
                                         o_LOCK=self.pll_lock,
                                         o_GL0=self.clkout_100mhz)
        return m


class MSSTestDesign(Elaboratable):

    def elaborate(self, platform):
        led = platform.request("led", 0)
        timer = Signal(24)

        uart = platform.request("uart")
        print(uart)

        m = Module()
        m.d.sync += timer.eq(timer + 1)
        m.d.comb += led.o.eq(timer[-1])

        can_tx_bus = platform.request("led", 1)
        mss = SmartFusion2MSS()
        m.d.comb += can_tx_bus.o.eq(mss.can_tx_ebl_mgpio4a_h2f_a)
        m.d.comb += can_tx_bus.o.eq(mss.can_tx_ebl_mgpio4a_h2f_a)

        #
        # Clocks
        #
        my_rc_osc = FabricOscillator()
        m.submodules.rc_oscillator = my_rc_osc
        m.submodules.pll = ClockConditioningCircuit()
        m.d.comb += m.submodules.pll.clkin_50mhz.eq(m.submodules.rc_oscillator.rcosc_50mhz_clkout)
        m.d.comb += mss.clk_base.eq(m.submodules.pll.clkout_100mhz)

        #
        # Reset
        #
        devrst_n = platform.request("DEVRST_N", 0)
        rst_i = ~devrst_n
        m.submodules.reset_sync = ResetSynchronizer(rst_i, domain="sync")

        #
        # Clock domain
        #
        m.domains.sync = ClockDomain()
        m.d.comb += ClockSignal().eq(m.submodules.rc_oscillator.rcosc_50mhz_clkout)

        #
        # Connect MSS MUART0 to FTDI serial to USB chip
        #
        m.d.comb += uart.tx.eq(mss.mmuart0_txd_mgpio27b_h2f_a)
        m.d.comb += mss.mmuart0_rxd_f2h_scp.eq(uart.rx)

        #
        # Connect debug signals to "mod1" connector
        #
        platform.add_resources([Resource("debug_pin", 0, Pins("1", dir="o", conn=("mod1", 0))),
                                Resource("debug_pin", 1, Pins("2", dir="o", conn=("mod1", 0))),
                                Resource("debug_pin", 2, Pins("3", dir="o", conn=("mod1", 0))),
                                Resource("debug_pin", 3, Pins("4", dir="o", conn=("mod1", 0))),
                                Resource("debug_pin", 4, Pins("5", dir="o", conn=("mod1", 0))),
                                Resource("debug_pin", 5, Pins("6", dir="o", conn=("mod1", 0))),
                                         ])

        debug0 = platform.request("debug_pin", 0)
        print(debug0)
        m.d.comb += debug0.o.eq(mss.mmuart0_txd_mgpio27b_h2f_a)

        clock = ClockSignal("sync")
        debug_clk = platform.request("debug_pin", 1)
        m.d.comb += debug_clk.o.eq(clock.bit_select(0,1))

        debug_rst = platform.request("debug_pin", 3)
        m.d.comb += debug_rst.o.eq(ResetSignal("sync"))

        debug_led = platform.request("debug_pin", 5)
        m.d.comb += debug_led.o.eq(timer[-1])

        #
        # Add Microcontroller subsystem to the design
        #
        m.submodules.mss = mss

        return m


if __name__ == "__main__":
    platform = DigiKeySmartFusion2MakerKitPlatform()
    platform.build(MSSTestDesign(), do_program=False)