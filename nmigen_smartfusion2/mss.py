from nmigen import *
from nmigen_boards.m2s010_mkr_kit import *

from mss_port_list import *


class SmartFusion2MSS(Elaboratable):
    def __init__(self):
#        self.mss_test_input_signal = Signal(3)
#        self.mss_test_output_signal = Signal(1)
        self._connection_list = self._build_connection_list

    @property
    def _build_connection_list(self):
        port_list = get_mss_port_list()
        conn_list = []
        for port in port_list:
            port_name, port_width, port_direction, default_value = port
            print(port)
            s = Signal(port_width)
            s.name = port_name.lower()
            if port_direction == "in":
                s.reset = default_value
            setattr(self, port_name.lower(), s)
            conn_list.append((port_name, port_direction, s))
        return conn_list

    def _get_macro_ports(self):
        ports = {}
        for port_name, direction, signal in self._connection_list:
            if direction == 'in':
                prefix = 'i_'
            else:
                prefix = 'o_'
            ports[prefix + port_name] = signal
        return ports

    def elaborate(self, platform):
        m = Module()
        m.submodules.MSS_ADLIB_INST = Instance("MSS_010",
            p_ACT_UBITS=0xFFFFFFFFFFFFFF,
            p_DDR_CLK_FREQ=100.0,
            p_INIT=0x00000000000000300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000F00000000F000000000000000000000000000000007FFFFFFFB000001007C33F00001000E092C0F00003FFFFE400000000000010000000000E01C000001FF5FC4010842108421000001FE34001FF8000000400000000020091007FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF,
            p_MEMORYFILE="ENVM_init.mem",
            p_RTC_MAIN_XTL_FREQ=0.0,
            p_RTC_MAIN_XTL_MODE=" ",
#            i_mss_test_signal = self.mss_test_input_signal,
#            o_mss_test_output_signal = self.mss_test_output_signal,
            **self._get_macro_ports(),
        )
        return m


if __name__ == "__main__":
    platform = DigiKeySmartFusion2MakerKitPlatform()
    platform.build(SmartFusion2MSS(), do_program=False)
