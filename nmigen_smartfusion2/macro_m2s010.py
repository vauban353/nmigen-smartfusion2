
def get_m2s010_macro():
       m2s010_silicon_macro = '`timescale 1 ns/100 ps\n\
// Version: \n\
\n\
\n\
module MSS_010(\n\
       CAN_RXBUS_MGPIO3A_H2F_A,\n\
       CAN_RXBUS_MGPIO3A_H2F_B,\n\
       CAN_TX_EBL_MGPIO4A_H2F_A,\n\
       CAN_TX_EBL_MGPIO4A_H2F_B,\n\
       CAN_TXBUS_MGPIO2A_H2F_A,\n\
       CAN_TXBUS_MGPIO2A_H2F_B,\n\
       CLK_CONFIG_APB,\n\
       COMMS_INT,\n\
       CONFIG_PRESET_N,\n\
       EDAC_ERROR,\n\
       F_FM0_RDATA,\n\
       F_FM0_READYOUT,\n\
       F_FM0_RESP,\n\
       F_HM0_ADDR,\n\
       F_HM0_ENABLE,\n\
       F_HM0_SEL,\n\
       F_HM0_SIZE,\n\
       F_HM0_TRANS1,\n\
       F_HM0_WDATA,\n\
       F_HM0_WRITE,\n\
       FAB_CHRGVBUS,\n\
       FAB_DISCHRGVBUS,\n\
       FAB_DMPULLDOWN,\n\
       FAB_DPPULLDOWN,\n\
       FAB_DRVVBUS,\n\
       FAB_IDPULLUP,\n\
       FAB_OPMODE,\n\
       FAB_SUSPENDM,\n\
       FAB_TERMSEL,\n\
       FAB_TXVALID,\n\
       FAB_VCONTROL,\n\
       FAB_VCONTROLLOADM,\n\
       FAB_XCVRSEL,\n\
       FAB_XDATAOUT,\n\
       FACC_GLMUX_SEL,\n\
       FIC32_0_MASTER,\n\
       FIC32_1_MASTER,\n\
       FPGA_RESET_N,\n\
       GTX_CLK,\n\
       H2F_INTERRUPT,\n\
       H2F_NMI,\n\
       H2FCALIB,\n\
       I2C0_SCL_MGPIO31B_H2F_A,\n\
       I2C0_SCL_MGPIO31B_H2F_B,\n\
       I2C0_SDA_MGPIO30B_H2F_A,\n\
       I2C0_SDA_MGPIO30B_H2F_B,\n\
       I2C1_SCL_MGPIO1A_H2F_A,\n\
       I2C1_SCL_MGPIO1A_H2F_B,\n\
       I2C1_SDA_MGPIO0A_H2F_A,\n\
       I2C1_SDA_MGPIO0A_H2F_B,\n\
       MDCF,\n\
       MDOENF,\n\
       MDOF,\n\
       MMUART0_CTS_MGPIO19B_H2F_A,\n\
       MMUART0_CTS_MGPIO19B_H2F_B,\n\
       MMUART0_DCD_MGPIO22B_H2F_A,\n\
       MMUART0_DCD_MGPIO22B_H2F_B,\n\
       MMUART0_DSR_MGPIO20B_H2F_A,\n\
       MMUART0_DSR_MGPIO20B_H2F_B,\n\
       MMUART0_DTR_MGPIO18B_H2F_A,\n\
       MMUART0_DTR_MGPIO18B_H2F_B,\n\
       MMUART0_RI_MGPIO21B_H2F_A,\n\
       MMUART0_RI_MGPIO21B_H2F_B,\n\
       MMUART0_RTS_MGPIO17B_H2F_A,\n\
       MMUART0_RTS_MGPIO17B_H2F_B,\n\
       MMUART0_RXD_MGPIO28B_H2F_A,\n\
       MMUART0_RXD_MGPIO28B_H2F_B,\n\
       MMUART0_SCK_MGPIO29B_H2F_A,\n\
       MMUART0_SCK_MGPIO29B_H2F_B,\n\
       MMUART0_TXD_MGPIO27B_H2F_A,\n\
       MMUART0_TXD_MGPIO27B_H2F_B,\n\
       MMUART1_DTR_MGPIO12B_H2F_A,\n\
       MMUART1_RTS_MGPIO11B_H2F_A,\n\
       MMUART1_RTS_MGPIO11B_H2F_B,\n\
       MMUART1_RXD_MGPIO26B_H2F_A,\n\
       MMUART1_RXD_MGPIO26B_H2F_B,\n\
       MMUART1_SCK_MGPIO25B_H2F_A,\n\
       MMUART1_SCK_MGPIO25B_H2F_B,\n\
       MMUART1_TXD_MGPIO24B_H2F_A,\n\
       MMUART1_TXD_MGPIO24B_H2F_B,\n\
       MPLL_LOCK,\n\
       PER2_FABRIC_PADDR,\n\
       PER2_FABRIC_PENABLE,\n\
       PER2_FABRIC_PSEL,\n\
       PER2_FABRIC_PWDATA,\n\
       PER2_FABRIC_PWRITE,\n\
       RTC_MATCH,\n\
       SLEEPDEEP,\n\
       SLEEPHOLDACK,\n\
       SLEEPING,\n\
       SMBALERT_NO0,\n\
       SMBALERT_NO1,\n\
       SMBSUS_NO0,\n\
       SMBSUS_NO1,\n\
       SPI0_CLK_OUT,\n\
       SPI0_SDI_MGPIO5A_H2F_A,\n\
       SPI0_SDI_MGPIO5A_H2F_B,\n\
       SPI0_SDO_MGPIO6A_H2F_A,\n\
       SPI0_SDO_MGPIO6A_H2F_B,\n\
       SPI0_SS0_MGPIO7A_H2F_A,\n\
       SPI0_SS0_MGPIO7A_H2F_B,\n\
       SPI0_SS1_MGPIO8A_H2F_A,\n\
       SPI0_SS1_MGPIO8A_H2F_B,\n\
       SPI0_SS2_MGPIO9A_H2F_A,\n\
       SPI0_SS2_MGPIO9A_H2F_B,\n\
       SPI0_SS3_MGPIO10A_H2F_A,\n\
       SPI0_SS3_MGPIO10A_H2F_B,\n\
       SPI0_SS4_MGPIO19A_H2F_A,\n\
       SPI0_SS5_MGPIO20A_H2F_A,\n\
       SPI0_SS6_MGPIO21A_H2F_A,\n\
       SPI0_SS7_MGPIO22A_H2F_A,\n\
       SPI1_CLK_OUT,\n\
       SPI1_SDI_MGPIO11A_H2F_A,\n\
       SPI1_SDI_MGPIO11A_H2F_B,\n\
       SPI1_SDO_MGPIO12A_H2F_A,\n\
       SPI1_SDO_MGPIO12A_H2F_B,\n\
       SPI1_SS0_MGPIO13A_H2F_A,\n\
       SPI1_SS0_MGPIO13A_H2F_B,\n\
       SPI1_SS1_MGPIO14A_H2F_A,\n\
       SPI1_SS1_MGPIO14A_H2F_B,\n\
       SPI1_SS2_MGPIO15A_H2F_A,\n\
       SPI1_SS2_MGPIO15A_H2F_B,\n\
       SPI1_SS3_MGPIO16A_H2F_A,\n\
       SPI1_SS3_MGPIO16A_H2F_B,\n\
       SPI1_SS4_MGPIO17A_H2F_A,\n\
       SPI1_SS5_MGPIO18A_H2F_A,\n\
       SPI1_SS6_MGPIO23A_H2F_A,\n\
       SPI1_SS7_MGPIO24A_H2F_A,\n\
       TCGF,\n\
       TRACECLK,\n\
       TRACEDATA,\n\
       TX_CLK,\n\
       TX_ENF,\n\
       TX_ERRF,\n\
       TXCTL_EN_RIF,\n\
       TXD_RIF,\n\
       TXDF,\n\
       TXEV,\n\
       WDOGTIMEOUT,\n\
       F_ARREADY_HREADYOUT1,\n\
       F_AWREADY_HREADYOUT0,\n\
       F_BID,\n\
       F_BRESP_HRESP0,\n\
       F_BVALID,\n\
       F_RDATA_HRDATA01,\n\
       F_RID,\n\
       F_RLAST,\n\
       F_RRESP_HRESP1,\n\
       F_RVALID,\n\
       F_WREADY,\n\
       MDDR_FABRIC_PRDATA,\n\
       MDDR_FABRIC_PREADY,\n\
       MDDR_FABRIC_PSLVERR,\n\
       CAN_RXBUS_F2H_SCP,\n\
       CAN_TX_EBL_F2H_SCP,\n\
       CAN_TXBUS_F2H_SCP,\n\
       COLF,\n\
       CRSF,\n\
       F2_DMAREADY,\n\
       F2H_INTERRUPT,\n\
       F2HCALIB,\n\
       F_DMAREADY,\n\
       F_FM0_ADDR,\n\
       F_FM0_ENABLE,\n\
       F_FM0_MASTLOCK,\n\
       F_FM0_READY,\n\
       F_FM0_SEL,\n\
       F_FM0_SIZE,\n\
       F_FM0_TRANS1,\n\
       F_FM0_WDATA,\n\
       F_FM0_WRITE,\n\
       F_HM0_RDATA,\n\
       F_HM0_READY,\n\
       F_HM0_RESP,\n\
       FAB_AVALID,\n\
       FAB_HOSTDISCON,\n\
       FAB_IDDIG,\n\
       FAB_LINESTATE,\n\
       FAB_M3_RESET_N,\n\
       FAB_PLL_LOCK,\n\
       FAB_RXACTIVE,\n\
       FAB_RXERROR,\n\
       FAB_RXVALID,\n\
       FAB_RXVALIDH,\n\
       FAB_SESSEND,\n\
       FAB_TXREADY,\n\
       FAB_VBUSVALID,\n\
       FAB_VSTATUS,\n\
       FAB_XDATAIN,\n\
       GTX_CLKPF,\n\
       I2C0_BCLK,\n\
       I2C0_SCL_F2H_SCP,\n\
       I2C0_SDA_F2H_SCP,\n\
       I2C1_BCLK,\n\
       I2C1_SCL_F2H_SCP,\n\
       I2C1_SDA_F2H_SCP,\n\
       MDIF,\n\
       MGPIO0A_F2H_GPIN,\n\
       MGPIO10A_F2H_GPIN,\n\
       MGPIO11A_F2H_GPIN,\n\
       MGPIO11B_F2H_GPIN,\n\
       MGPIO12A_F2H_GPIN,\n\
       MGPIO13A_F2H_GPIN,\n\
       MGPIO14A_F2H_GPIN,\n\
       MGPIO15A_F2H_GPIN,\n\
       MGPIO16A_F2H_GPIN,\n\
       MGPIO17B_F2H_GPIN,\n\
       MGPIO18B_F2H_GPIN,\n\
       MGPIO19B_F2H_GPIN,\n\
       MGPIO1A_F2H_GPIN,\n\
       MGPIO20B_F2H_GPIN,\n\
       MGPIO21B_F2H_GPIN,\n\
       MGPIO22B_F2H_GPIN,\n\
       MGPIO24B_F2H_GPIN,\n\
       MGPIO25B_F2H_GPIN,\n\
       MGPIO26B_F2H_GPIN,\n\
       MGPIO27B_F2H_GPIN,\n\
       MGPIO28B_F2H_GPIN,\n\
       MGPIO29B_F2H_GPIN,\n\
       MGPIO2A_F2H_GPIN,\n\
       MGPIO30B_F2H_GPIN,\n\
       MGPIO31B_F2H_GPIN,\n\
       MGPIO3A_F2H_GPIN,\n\
       MGPIO4A_F2H_GPIN,\n\
       MGPIO5A_F2H_GPIN,\n\
       MGPIO6A_F2H_GPIN,\n\
       MGPIO7A_F2H_GPIN,\n\
       MGPIO8A_F2H_GPIN,\n\
       MGPIO9A_F2H_GPIN,\n\
       MMUART0_CTS_F2H_SCP,\n\
       MMUART0_DCD_F2H_SCP,\n\
       MMUART0_DSR_F2H_SCP,\n\
       MMUART0_DTR_F2H_SCP,\n\
       MMUART0_RI_F2H_SCP,\n\
       MMUART0_RTS_F2H_SCP,\n\
       MMUART0_RXD_F2H_SCP,\n\
       MMUART0_SCK_F2H_SCP,\n\
       MMUART0_TXD_F2H_SCP,\n\
       MMUART1_CTS_F2H_SCP,\n\
       MMUART1_DCD_F2H_SCP,\n\
       MMUART1_DSR_F2H_SCP,\n\
       MMUART1_RI_F2H_SCP,\n\
       MMUART1_RTS_F2H_SCP,\n\
       MMUART1_RXD_F2H_SCP,\n\
       MMUART1_SCK_F2H_SCP,\n\
       MMUART1_TXD_F2H_SCP,\n\
       PER2_FABRIC_PRDATA,\n\
       PER2_FABRIC_PREADY,\n\
       PER2_FABRIC_PSLVERR,\n\
       RCGF,\n\
       RX_CLKPF,\n\
       RX_DVF,\n\
       RX_ERRF,\n\
       RX_EV,\n\
       RXDF,\n\
       SLEEPHOLDREQ,\n\
       SMBALERT_NI0,\n\
       SMBALERT_NI1,\n\
       SMBSUS_NI0,\n\
       SMBSUS_NI1,\n\
       SPI0_CLK_IN,\n\
       SPI0_SDI_F2H_SCP,\n\
       SPI0_SDO_F2H_SCP,\n\
       SPI0_SS0_F2H_SCP,\n\
       SPI0_SS1_F2H_SCP,\n\
       SPI0_SS2_F2H_SCP,\n\
       SPI0_SS3_F2H_SCP,\n\
       SPI1_CLK_IN,\n\
       SPI1_SDI_F2H_SCP,\n\
       SPI1_SDO_F2H_SCP,\n\
       SPI1_SS0_F2H_SCP,\n\
       SPI1_SS1_F2H_SCP,\n\
       SPI1_SS2_F2H_SCP,\n\
       SPI1_SS3_F2H_SCP,\n\
       TX_CLKPF,\n\
       USER_MSS_GPIO_RESET_N,\n\
       USER_MSS_RESET_N,\n\
       XCLK_FAB,\n\
       CLK_BASE,\n\
       CLK_MDDR_APB,\n\
       F_ARADDR_HADDR1,\n\
       F_ARBURST_HTRANS1,\n\
       F_ARID_HSEL1,\n\
       F_ARLEN_HBURST1,\n\
       F_ARLOCK_HMASTLOCK1,\n\
       F_ARSIZE_HSIZE1,\n\
       F_ARVALID_HWRITE1,\n\
       F_AWADDR_HADDR0,\n\
       F_AWBURST_HTRANS0,\n\
       F_AWID_HSEL0,\n\
       F_AWLEN_HBURST0,\n\
       F_AWLOCK_HMASTLOCK0,\n\
       F_AWSIZE_HSIZE0,\n\
       F_AWVALID_HWRITE0,\n\
       F_BREADY,\n\
       F_RMW_AXI,\n\
       F_RREADY,\n\
       F_WDATA_HWDATA01,\n\
       F_WID_HREADY01,\n\
       F_WLAST,\n\
       F_WSTRB,\n\
       F_WVALID,\n\
       FPGA_MDDR_ARESET_N,\n\
       MDDR_FABRIC_PADDR,\n\
       MDDR_FABRIC_PENABLE,\n\
       MDDR_FABRIC_PSEL,\n\
       MDDR_FABRIC_PWDATA,\n\
       MDDR_FABRIC_PWRITE,\n\
       PRESET_N,\n\
       CAN_RXBUS_USBA_DATA1_MGPIO3A_IN,\n\
       CAN_TX_EBL_USBA_DATA2_MGPIO4A_IN,\n\
       CAN_TXBUS_USBA_DATA0_MGPIO2A_IN,\n\
       DM_IN,\n\
       DRAM_DQ_IN,\n\
       DRAM_DQS_IN,\n\
       DRAM_FIFO_WE_IN,\n\
       I2C0_SCL_USBC_DATA1_MGPIO31B_IN,\n\
       I2C0_SDA_USBC_DATA0_MGPIO30B_IN,\n\
       I2C1_SCL_USBA_DATA4_MGPIO1A_IN,\n\
       I2C1_SDA_USBA_DATA3_MGPIO0A_IN,\n\
       MMUART0_CTS_USBC_DATA7_MGPIO19B_IN,\n\
       MMUART0_DCD_MGPIO22B_IN,\n\
       MMUART0_DSR_MGPIO20B_IN,\n\
       MMUART0_DTR_USBC_DATA6_MGPIO18B_IN,\n\
       MMUART0_RI_MGPIO21B_IN,\n\
       MMUART0_RTS_USBC_DATA5_MGPIO17B_IN,\n\
       MMUART0_RXD_USBC_STP_MGPIO28B_IN,\n\
       MMUART0_SCK_USBC_NXT_MGPIO29B_IN,\n\
       MMUART0_TXD_USBC_DIR_MGPIO27B_IN,\n\
       MMUART1_RXD_USBC_DATA3_MGPIO26B_IN,\n\
       MMUART1_SCK_USBC_DATA4_MGPIO25B_IN,\n\
       MMUART1_TXD_USBC_DATA2_MGPIO24B_IN,\n\
       RGMII_GTX_CLK_RMII_CLK_USBB_XCLK_IN,\n\
       RGMII_MDC_RMII_MDC_IN,\n\
       RGMII_MDIO_RMII_MDIO_USBB_DATA7_IN,\n\
       RGMII_RX_CLK_IN,\n\
       RGMII_RX_CTL_RMII_CRS_DV_USBB_DATA2_IN,\n\
       RGMII_RXD0_RMII_RXD0_USBB_DATA0_IN,\n\
       RGMII_RXD1_RMII_RXD1_USBB_DATA1_IN,\n\
       RGMII_RXD2_RMII_RX_ER_USBB_DATA3_IN,\n\
       RGMII_RXD3_USBB_DATA4_IN,\n\
       RGMII_TX_CLK_IN,\n\
       RGMII_TX_CTL_RMII_TX_EN_USBB_NXT_IN,\n\
       RGMII_TXD0_RMII_TXD0_USBB_DIR_IN,\n\
       RGMII_TXD1_RMII_TXD1_USBB_STP_IN,\n\
       RGMII_TXD2_USBB_DATA5_IN,\n\
       RGMII_TXD3_USBB_DATA6_IN,\n\
       SPI0_SCK_USBA_XCLK_IN,\n\
       SPI0_SDI_USBA_DIR_MGPIO5A_IN,\n\
       SPI0_SDO_USBA_STP_MGPIO6A_IN,\n\
       SPI0_SS0_USBA_NXT_MGPIO7A_IN,\n\
       SPI0_SS1_USBA_DATA5_MGPIO8A_IN,\n\
       SPI0_SS2_USBA_DATA6_MGPIO9A_IN,\n\
       SPI0_SS3_USBA_DATA7_MGPIO10A_IN,\n\
       SPI1_SCK_IN,\n\
       SPI1_SDI_MGPIO11A_IN,\n\
       SPI1_SDO_MGPIO12A_IN,\n\
       SPI1_SS0_MGPIO13A_IN,\n\
       SPI1_SS1_MGPIO14A_IN,\n\
       SPI1_SS2_MGPIO15A_IN,\n\
       SPI1_SS3_MGPIO16A_IN,\n\
       SPI1_SS4_MGPIO17A_IN,\n\
       SPI1_SS5_MGPIO18A_IN,\n\
       SPI1_SS6_MGPIO23A_IN,\n\
       SPI1_SS7_MGPIO24A_IN,\n\
       USBC_XCLK_IN,\n\
       CAN_RXBUS_USBA_DATA1_MGPIO3A_OUT,\n\
       CAN_TX_EBL_USBA_DATA2_MGPIO4A_OUT,\n\
       CAN_TXBUS_USBA_DATA0_MGPIO2A_OUT,\n\
       DRAM_ADDR,\n\
       DRAM_BA,\n\
       DRAM_CASN,\n\
       DRAM_CKE,\n\
       DRAM_CLK,\n\
       DRAM_CSN,\n\
       DRAM_DM_RDQS_OUT,\n\
       DRAM_DQ_OUT,\n\
       DRAM_DQS_OUT,\n\
       DRAM_FIFO_WE_OUT,\n\
       DRAM_ODT,\n\
       DRAM_RASN,\n\
       DRAM_RSTN,\n\
       DRAM_WEN,\n\
       I2C0_SCL_USBC_DATA1_MGPIO31B_OUT,\n\
       I2C0_SDA_USBC_DATA0_MGPIO30B_OUT,\n\
       I2C1_SCL_USBA_DATA4_MGPIO1A_OUT,\n\
       I2C1_SDA_USBA_DATA3_MGPIO0A_OUT,\n\
       MMUART0_CTS_USBC_DATA7_MGPIO19B_OUT,\n\
       MMUART0_DCD_MGPIO22B_OUT,\n\
       MMUART0_DSR_MGPIO20B_OUT,\n\
       MMUART0_DTR_USBC_DATA6_MGPIO18B_OUT,\n\
       MMUART0_RI_MGPIO21B_OUT,\n\
       MMUART0_RTS_USBC_DATA5_MGPIO17B_OUT,\n\
       MMUART0_RXD_USBC_STP_MGPIO28B_OUT,\n\
       MMUART0_SCK_USBC_NXT_MGPIO29B_OUT,\n\
       MMUART0_TXD_USBC_DIR_MGPIO27B_OUT,\n\
       MMUART1_RXD_USBC_DATA3_MGPIO26B_OUT,\n\
       MMUART1_SCK_USBC_DATA4_MGPIO25B_OUT,\n\
       MMUART1_TXD_USBC_DATA2_MGPIO24B_OUT,\n\
       RGMII_GTX_CLK_RMII_CLK_USBB_XCLK_OUT,\n\
       RGMII_MDC_RMII_MDC_OUT,\n\
       RGMII_MDIO_RMII_MDIO_USBB_DATA7_OUT,\n\
       RGMII_RX_CLK_OUT,\n\
       RGMII_RX_CTL_RMII_CRS_DV_USBB_DATA2_OUT,\n\
       RGMII_RXD0_RMII_RXD0_USBB_DATA0_OUT,\n\
       RGMII_RXD1_RMII_RXD1_USBB_DATA1_OUT,\n\
       RGMII_RXD2_RMII_RX_ER_USBB_DATA3_OUT,\n\
       RGMII_RXD3_USBB_DATA4_OUT,\n\
       RGMII_TX_CLK_OUT,\n\
       RGMII_TX_CTL_RMII_TX_EN_USBB_NXT_OUT,\n\
       RGMII_TXD0_RMII_TXD0_USBB_DIR_OUT,\n\
       RGMII_TXD1_RMII_TXD1_USBB_STP_OUT,\n\
       RGMII_TXD2_USBB_DATA5_OUT,\n\
       RGMII_TXD3_USBB_DATA6_OUT,\n\
       SPI0_SCK_USBA_XCLK_OUT,\n\
       SPI0_SDI_USBA_DIR_MGPIO5A_OUT,\n\
       SPI0_SDO_USBA_STP_MGPIO6A_OUT,\n\
       SPI0_SS0_USBA_NXT_MGPIO7A_OUT,\n\
       SPI0_SS1_USBA_DATA5_MGPIO8A_OUT,\n\
       SPI0_SS2_USBA_DATA6_MGPIO9A_OUT,\n\
       SPI0_SS3_USBA_DATA7_MGPIO10A_OUT,\n\
       SPI1_SCK_OUT,\n\
       SPI1_SDI_MGPIO11A_OUT,\n\
       SPI1_SDO_MGPIO12A_OUT,\n\
       SPI1_SS0_MGPIO13A_OUT,\n\
       SPI1_SS1_MGPIO14A_OUT,\n\
       SPI1_SS2_MGPIO15A_OUT,\n\
       SPI1_SS3_MGPIO16A_OUT,\n\
       SPI1_SS4_MGPIO17A_OUT,\n\
       SPI1_SS5_MGPIO18A_OUT,\n\
       SPI1_SS6_MGPIO23A_OUT,\n\
       SPI1_SS7_MGPIO24A_OUT,\n\
       USBC_XCLK_OUT,\n\
       CAN_RXBUS_USBA_DATA1_MGPIO3A_OE,\n\
       CAN_TX_EBL_USBA_DATA2_MGPIO4A_OE,\n\
       CAN_TXBUS_USBA_DATA0_MGPIO2A_OE,\n\
       DM_OE,\n\
       DRAM_DQ_OE,\n\
       DRAM_DQS_OE,\n\
       I2C0_SCL_USBC_DATA1_MGPIO31B_OE,\n\
       I2C0_SDA_USBC_DATA0_MGPIO30B_OE,\n\
       I2C1_SCL_USBA_DATA4_MGPIO1A_OE,\n\
       I2C1_SDA_USBA_DATA3_MGPIO0A_OE,\n\
       MMUART0_CTS_USBC_DATA7_MGPIO19B_OE,\n\
       MMUART0_DCD_MGPIO22B_OE,\n\
       MMUART0_DSR_MGPIO20B_OE,\n\
       MMUART0_DTR_USBC_DATA6_MGPIO18B_OE,\n\
       MMUART0_RI_MGPIO21B_OE,\n\
       MMUART0_RTS_USBC_DATA5_MGPIO17B_OE,\n\
       MMUART0_RXD_USBC_STP_MGPIO28B_OE,\n\
       MMUART0_SCK_USBC_NXT_MGPIO29B_OE,\n\
       MMUART0_TXD_USBC_DIR_MGPIO27B_OE,\n\
       MMUART1_RXD_USBC_DATA3_MGPIO26B_OE,\n\
       MMUART1_SCK_USBC_DATA4_MGPIO25B_OE,\n\
       MMUART1_TXD_USBC_DATA2_MGPIO24B_OE,\n\
       RGMII_GTX_CLK_RMII_CLK_USBB_XCLK_OE,\n\
       RGMII_MDC_RMII_MDC_OE,\n\
       RGMII_MDIO_RMII_MDIO_USBB_DATA7_OE,\n\
       RGMII_RX_CLK_OE,\n\
       RGMII_RX_CTL_RMII_CRS_DV_USBB_DATA2_OE,\n\
       RGMII_RXD0_RMII_RXD0_USBB_DATA0_OE,\n\
       RGMII_RXD1_RMII_RXD1_USBB_DATA1_OE,\n\
       RGMII_RXD2_RMII_RX_ER_USBB_DATA3_OE,\n\
       RGMII_RXD3_USBB_DATA4_OE,\n\
       RGMII_TX_CLK_OE,\n\
       RGMII_TX_CTL_RMII_TX_EN_USBB_NXT_OE,\n\
       RGMII_TXD0_RMII_TXD0_USBB_DIR_OE,\n\
       RGMII_TXD1_RMII_TXD1_USBB_STP_OE,\n\
       RGMII_TXD2_USBB_DATA5_OE,\n\
       RGMII_TXD3_USBB_DATA6_OE,\n\
       SPI0_SCK_USBA_XCLK_OE,\n\
       SPI0_SDI_USBA_DIR_MGPIO5A_OE,\n\
       SPI0_SDO_USBA_STP_MGPIO6A_OE,\n\
       SPI0_SS0_USBA_NXT_MGPIO7A_OE,\n\
       SPI0_SS1_USBA_DATA5_MGPIO8A_OE,\n\
       SPI0_SS2_USBA_DATA6_MGPIO9A_OE,\n\
       SPI0_SS3_USBA_DATA7_MGPIO10A_OE,\n\
       SPI1_SCK_OE,\n\
       SPI1_SDI_MGPIO11A_OE,\n\
       SPI1_SDO_MGPIO12A_OE,\n\
       SPI1_SS0_MGPIO13A_OE,\n\
       SPI1_SS1_MGPIO14A_OE,\n\
       SPI1_SS2_MGPIO15A_OE,\n\
       SPI1_SS3_MGPIO16A_OE,\n\
       SPI1_SS4_MGPIO17A_OE,\n\
       SPI1_SS5_MGPIO18A_OE,\n\
       SPI1_SS6_MGPIO23A_OE,\n\
       SPI1_SS7_MGPIO24A_OE,\n\
       USBC_XCLK_OE\n\
    ) ;\n\
/* synthesis syn_black_box\n\
\n\
syn_tsu0 = \" CAN_RXBUS_F2H_SCP->CLK_BASE = 1.047\"\n\
syn_tsu1 = \" F2HCALIB->CLK_BASE = 0.39\"\n\
syn_tsu2 = \" F2H_INTERRUPT[0]->CLK_BASE = 0.858\"\n\
syn_tsu3 = \" F2H_INTERRUPT[10]->CLK_BASE = 1.07\"\n\
syn_tsu4 = \" F2H_INTERRUPT[11]->CLK_BASE = 1.049\"\n\
syn_tsu5 = \" F2H_INTERRUPT[12]->CLK_BASE = 0.967\"\n\
syn_tsu6 = \" F2H_INTERRUPT[13]->CLK_BASE = 1.024\"\n\
syn_tsu7 = \" F2H_INTERRUPT[14]->CLK_BASE = 1.077\"\n\
syn_tsu8 = \" F2H_INTERRUPT[15]->CLK_BASE = 0.989\"\n\
syn_tsu9 = \" F2H_INTERRUPT[1]->CLK_BASE = 0.824\"\n\
syn_tsu10 = \" F2H_INTERRUPT[2]->CLK_BASE = 0.791\"\n\
syn_tsu11 = \" F2H_INTERRUPT[3]->CLK_BASE = 0.907\"\n\
syn_tsu12 = \" F2H_INTERRUPT[4]->CLK_BASE = 0.803\"\n\
syn_tsu13 = \" F2H_INTERRUPT[5]->CLK_BASE = 0.911\"\n\
syn_tsu14 = \" F2H_INTERRUPT[6]->CLK_BASE = 0.864\"\n\
syn_tsu15 = \" F2H_INTERRUPT[7]->CLK_BASE = 0.902\"\n\
syn_tsu16 = \" F2H_INTERRUPT[8]->CLK_BASE = 0.882\"\n\
syn_tsu17 = \" F2H_INTERRUPT[9]->CLK_BASE = 0.825\"\n\
syn_tsu18 = \" F_FM0_ADDR[0]->CLK_BASE = 0.915\"\n\
syn_tsu19 = \" F_FM0_ADDR[10]->CLK_BASE = 0.848\"\n\
syn_tsu20 = \" F_FM0_ADDR[11]->CLK_BASE = 0.957\"\n\
syn_tsu21 = \" F_FM0_ADDR[12]->CLK_BASE = 0.967\"\n\
syn_tsu22 = \" F_FM0_ADDR[13]->CLK_BASE = 1.194\"\n\
syn_tsu23 = \" F_FM0_ADDR[14]->CLK_BASE = 1.105\"\n\
syn_tsu24 = \" F_FM0_ADDR[15]->CLK_BASE = 1.093\"\n\
syn_tsu25 = \" F_FM0_ADDR[16]->CLK_BASE = 1.071\"\n\
syn_tsu26 = \" F_FM0_ADDR[17]->CLK_BASE = 1.001\"\n\
syn_tsu27 = \" F_FM0_ADDR[18]->CLK_BASE = 1.068\"\n\
syn_tsu28 = \" F_FM0_ADDR[19]->CLK_BASE = 0.571\"\n\
syn_tsu29 = \" F_FM0_ADDR[1]->CLK_BASE = 0.801\"\n\
syn_tsu30 = \" F_FM0_ADDR[20]->CLK_BASE = 0.879\"\n\
syn_tsu31 = \" F_FM0_ADDR[21]->CLK_BASE = 0.532\"\n\
syn_tsu32 = \" F_FM0_ADDR[22]->CLK_BASE = 0.878\"\n\
syn_tsu33 = \" F_FM0_ADDR[23]->CLK_BASE = 0.575\"\n\
syn_tsu34 = \" F_FM0_ADDR[24]->CLK_BASE = 0.596\"\n\
syn_tsu35 = \" F_FM0_ADDR[25]->CLK_BASE = 0.663\"\n\
syn_tsu36 = \" F_FM0_ADDR[26]->CLK_BASE = 0.712\"\n\
syn_tsu37 = \" F_FM0_ADDR[27]->CLK_BASE = 1.073\"\n\
syn_tsu38 = \" F_FM0_ADDR[28]->CLK_BASE = 0.696\"\n\
syn_tsu39 = \" F_FM0_ADDR[29]->CLK_BASE = 0.399\"\n\
syn_tsu40 = \" F_FM0_ADDR[2]->CLK_BASE = 0.331\"\n\
syn_tsu41 = \" F_FM0_ADDR[30]->CLK_BASE = 0.582\"\n\
syn_tsu42 = \" F_FM0_ADDR[31]->CLK_BASE = 0.479\"\n\
syn_tsu43 = \" F_FM0_ADDR[3]->CLK_BASE = 0.956\"\n\
syn_tsu44 = \" F_FM0_ADDR[4]->CLK_BASE = 1.273\"\n\
syn_tsu45 = \" F_FM0_ADDR[5]->CLK_BASE = 0.844\"\n\
syn_tsu46 = \" F_FM0_ADDR[6]->CLK_BASE = 1.139\"\n\
syn_tsu47 = \" F_FM0_ADDR[7]->CLK_BASE = 1.031\"\n\
syn_tsu48 = \" F_FM0_ADDR[8]->CLK_BASE = 1.018\"\n\
syn_tsu49 = \" F_FM0_ADDR[9]->CLK_BASE = 0.786\"\n\
syn_tsu50 = \" F_FM0_ENABLE->CLK_BASE = 1.163\"\n\
syn_tsu51 = \" F_FM0_SEL->CLK_BASE = 1.409\"\n\
syn_tsu52 = \" F_FM0_WDATA[0]->CLK_BASE = 0.131\"\n\
syn_tsu53 = \" F_FM0_WDATA[10]->CLK_BASE = 0.158\"\n\
syn_tsu54 = \" F_FM0_WDATA[11]->CLK_BASE = 0.086\"\n\
syn_tsu55 = \" F_FM0_WDATA[12]->CLK_BASE = 0.098\"\n\
syn_tsu56 = \" F_FM0_WDATA[13]->CLK_BASE = 0.093\"\n\
syn_tsu57 = \" F_FM0_WDATA[14]->CLK_BASE = 0.14\"\n\
syn_tsu58 = \" F_FM0_WDATA[15]->CLK_BASE = 0.126\"\n\
syn_tsu59 = \" F_FM0_WDATA[16]->CLK_BASE = 0.103\"\n\
syn_tsu60 = \" F_FM0_WDATA[17]->CLK_BASE = 0.107\"\n\
syn_tsu61 = \" F_FM0_WDATA[18]->CLK_BASE = 0.152\"\n\
syn_tsu62 = \" F_FM0_WDATA[19]->CLK_BASE = 0.13\"\n\
syn_tsu63 = \" F_FM0_WDATA[1]->CLK_BASE = 0.087\"\n\
syn_tsu64 = \" F_FM0_WDATA[20]->CLK_BASE = 0.108\"\n\
syn_tsu65 = \" F_FM0_WDATA[21]->CLK_BASE = 0.054\"\n\
syn_tsu66 = \" F_FM0_WDATA[22]->CLK_BASE = 0.052\"\n\
syn_tsu67 = \" F_FM0_WDATA[23]->CLK_BASE = 0.084\"\n\
syn_tsu68 = \" F_FM0_WDATA[24]->CLK_BASE = 0.094\"\n\
syn_tsu69 = \" F_FM0_WDATA[25]->CLK_BASE = 0.177\"\n\
syn_tsu70 = \" F_FM0_WDATA[26]->CLK_BASE = 0.117\"\n\
syn_tsu71 = \" F_FM0_WDATA[27]->CLK_BASE = 0.096\"\n\
syn_tsu72 = \" F_FM0_WDATA[28]->CLK_BASE = 0.157\"\n\
syn_tsu73 = \" F_FM0_WDATA[29]->CLK_BASE = 0.115\"\n\
syn_tsu74 = \" F_FM0_WDATA[2]->CLK_BASE = 0.059\"\n\
syn_tsu75 = \" F_FM0_WDATA[30]->CLK_BASE = 0.081\"\n\
syn_tsu76 = \" F_FM0_WDATA[31]->CLK_BASE = 0.126\"\n\
syn_tsu77 = \" F_FM0_WDATA[3]->CLK_BASE = 0.096\"\n\
syn_tsu78 = \" F_FM0_WDATA[4]->CLK_BASE = 0.055\"\n\
syn_tsu79 = \" F_FM0_WDATA[5]->CLK_BASE = 0.115\"\n\
syn_tsu80 = \" F_FM0_WDATA[6]->CLK_BASE = 0.082\"\n\
syn_tsu81 = \" F_FM0_WDATA[7]->CLK_BASE = 0.125\"\n\
syn_tsu82 = \" F_FM0_WDATA[8]->CLK_BASE = 0.121\"\n\
syn_tsu83 = \" F_FM0_WDATA[9]->CLK_BASE = 0.074\"\n\
syn_tsu84 = \" F_FM0_WRITE->CLK_BASE = 0.967\"\n\
syn_tsu85 = \" F_HM0_RDATA[0]->CLK_BASE = 0.367\"\n\
syn_tsu86 = \" F_HM0_RDATA[10]->CLK_BASE = 0.244\"\n\
syn_tsu87 = \" F_HM0_RDATA[11]->CLK_BASE = 0.329\"\n\
syn_tsu88 = \" F_HM0_RDATA[12]->CLK_BASE = 0.273\"\n\
syn_tsu89 = \" F_HM0_RDATA[13]->CLK_BASE = 0.341\"\n\
syn_tsu90 = \" F_HM0_RDATA[14]->CLK_BASE = 0.285\"\n\
syn_tsu91 = \" F_HM0_RDATA[15]->CLK_BASE = 0.276\"\n\
syn_tsu92 = \" F_HM0_RDATA[16]->CLK_BASE = 0.333\"\n\
syn_tsu93 = \" F_HM0_RDATA[17]->CLK_BASE = 0.3\"\n\
syn_tsu94 = \" F_HM0_RDATA[18]->CLK_BASE = 0.227\"\n\
syn_tsu95 = \" F_HM0_RDATA[19]->CLK_BASE = 0.284\"\n\
syn_tsu96 = \" F_HM0_RDATA[1]->CLK_BASE = 0.289\"\n\
syn_tsu97 = \" F_HM0_RDATA[20]->CLK_BASE = 0.297\"\n\
syn_tsu98 = \" F_HM0_RDATA[21]->CLK_BASE = 0.321\"\n\
syn_tsu99 = \" F_HM0_RDATA[22]->CLK_BASE = 0.327\"\n\
syn_tsu100 = \" F_HM0_RDATA[23]->CLK_BASE = 0.384\"\n\
syn_tsu101 = \" F_HM0_RDATA[24]->CLK_BASE = 0.296\"\n\
syn_tsu102 = \" F_HM0_RDATA[25]->CLK_BASE = 0.264\"\n\
syn_tsu103 = \" F_HM0_RDATA[26]->CLK_BASE = 0.22\"\n\
syn_tsu104 = \" F_HM0_RDATA[27]->CLK_BASE = 0.278\"\n\
syn_tsu105 = \" F_HM0_RDATA[28]->CLK_BASE = 0.285\"\n\
syn_tsu106 = \" F_HM0_RDATA[29]->CLK_BASE = 0.358\"\n\
syn_tsu107 = \" F_HM0_RDATA[2]->CLK_BASE = 0.263\"\n\
syn_tsu108 = \" F_HM0_RDATA[30]->CLK_BASE = 0.354\"\n\
syn_tsu109 = \" F_HM0_RDATA[31]->CLK_BASE = 0.252\"\n\
syn_tsu110 = \" F_HM0_RDATA[3]->CLK_BASE = 0.525\"\n\
syn_tsu111 = \" F_HM0_RDATA[4]->CLK_BASE = 0.459\"\n\
syn_tsu112 = \" F_HM0_RDATA[5]->CLK_BASE = 0.303\"\n\
syn_tsu113 = \" F_HM0_RDATA[6]->CLK_BASE = 0.328\"\n\
syn_tsu114 = \" F_HM0_RDATA[7]->CLK_BASE = 0.196\"\n\
syn_tsu115 = \" F_HM0_RDATA[8]->CLK_BASE = 0.308\"\n\
syn_tsu116 = \" F_HM0_RDATA[9]->CLK_BASE = 0.396\"\n\
syn_tsu117 = \" F_HM0_READY->CLK_BASE = 1.514\"\n\
syn_tsu118 = \" F_HM0_RESP->CLK_BASE = 0.921\"\n\
syn_tsu119 = \" I2C0_SDA_F2H_SCP->I2C0_SCL_F2H_SCP = 0.214\"\n\
syn_tsu120 = \" I2C1_SDA_F2H_SCP->I2C1_SCL_F2H_SCP = 0.23\"\n\
syn_tsu121 = \" MGPIO0A_F2H_GPIN->CLK_BASE = 0.881\"\n\
syn_tsu122 = \" MGPIO10A_F2H_GPIN->CLK_BASE = 1.068\"\n\
syn_tsu123 = \" MGPIO11A_F2H_GPIN->CLK_BASE = 0.325\"\n\
syn_tsu124 = \" MGPIO11B_F2H_GPIN->CLK_BASE = 0.381\"\n\
syn_tsu125 = \" MGPIO12A_F2H_GPIN->CLK_BASE = 0.385\"\n\
syn_tsu126 = \" MGPIO13A_F2H_GPIN->CLK_BASE = 0.463\"\n\
syn_tsu127 = \" MGPIO14A_F2H_GPIN->CLK_BASE = 0.379\"\n\
syn_tsu128 = \" MGPIO15A_F2H_GPIN->CLK_BASE = 0.414\"\n\
syn_tsu129 = \" MGPIO16A_F2H_GPIN->CLK_BASE = 0.358\"\n\
syn_tsu130 = \" MGPIO17B_F2H_GPIN->CLK_BASE = 0.477\"\n\
syn_tsu131 = \" MGPIO18B_F2H_GPIN->CLK_BASE = 0.5\"\n\
syn_tsu132 = \" MGPIO19B_F2H_GPIN->CLK_BASE = 0.521\"\n\
syn_tsu133 = \" MGPIO1A_F2H_GPIN->CLK_BASE = 0.435\"\n\
syn_tsu134 = \" MGPIO20B_F2H_GPIN->CLK_BASE = 0.468\"\n\
syn_tsu135 = \" MGPIO21B_F2H_GPIN->CLK_BASE = 0.507\"\n\
syn_tsu136 = \" MGPIO22B_F2H_GPIN->CLK_BASE = 0.473\"\n\
syn_tsu137 = \" MGPIO24B_F2H_GPIN->CLK_BASE = 0.381\"\n\
syn_tsu138 = \" MGPIO25B_F2H_GPIN->CLK_BASE = 0.787\"\n\
syn_tsu139 = \" MGPIO26B_F2H_GPIN->CLK_BASE = 0.727\"\n\
syn_tsu140 = \" MGPIO27B_F2H_GPIN->CLK_BASE = 1.08\"\n\
syn_tsu141 = \" MGPIO28B_F2H_GPIN->CLK_BASE = 1.311\"\n\
syn_tsu142 = \" MGPIO29B_F2H_GPIN->CLK_BASE = 1.047\"\n\
syn_tsu143 = \" MGPIO2A_F2H_GPIN->CLK_BASE = 0.746\"\n\
syn_tsu144 = \" MGPIO30B_F2H_GPIN->CLK_BASE = 0.888\"\n\
syn_tsu145 = \" MGPIO31B_F2H_GPIN->CLK_BASE = 0.895\"\n\
syn_tsu146 = \" MGPIO3A_F2H_GPIN->CLK_BASE = 1.046\"\n\
syn_tsu147 = \" MGPIO4A_F2H_GPIN->CLK_BASE = 0.886\"\n\
syn_tsu148 = \" MGPIO5A_F2H_GPIN->CLK_BASE = 0.654\"\n\
syn_tsu149 = \" MGPIO6A_F2H_GPIN->CLK_BASE = 0.704\"\n\
syn_tsu150 = \" MGPIO7A_F2H_GPIN->CLK_BASE = 0.759\"\n\
syn_tsu151 = \" MGPIO8A_F2H_GPIN->CLK_BASE = 0.769\"\n\
syn_tsu152 = \" MGPIO9A_F2H_GPIN->CLK_BASE = 0.68\"\n\
syn_tsu153 = \" MMUART0_CTS_F2H_SCP->CLK_BASE = 0.629\"\n\
syn_tsu154 = \" MMUART0_DCD_F2H_SCP->CLK_BASE = 0.655\"\n\
syn_tsu155 = \" MMUART0_DSR_F2H_SCP->CLK_BASE = 0.781\"\n\
syn_tsu156 = \" MMUART0_RI_F2H_SCP->CLK_BASE = 0.486\"\n\
syn_tsu157 = \" MMUART0_RXD_F2H_SCP->CLK_BASE = 0.559\"\n\
syn_tsu158 = \" MMUART0_SCK_F2H_SCP->CLK_BASE = 0.653\"\n\
syn_tsu159 = \" MMUART0_TXD_F2H_SCP->CLK_BASE = 0.608\"\n\
syn_tsu160 = \" MMUART1_CTS_F2H_SCP->CLK_BASE = 0.956\"\n\
syn_tsu161 = \" MMUART1_DCD_F2H_SCP->CLK_BASE = 1.076\"\n\
syn_tsu162 = \" MMUART1_DSR_F2H_SCP->CLK_BASE = 1.014\"\n\
syn_tsu163 = \" MMUART1_RI_F2H_SCP->CLK_BASE = 0.66\"\n\
syn_tsu164 = \" MMUART1_RXD_F2H_SCP->CLK_BASE = 0.661\"\n\
syn_tsu165 = \" MMUART1_SCK_F2H_SCP->CLK_BASE = 1.057\"\n\
syn_tsu166 = \" MMUART1_TXD_F2H_SCP->CLK_BASE = 0.649\"\n\
syn_tsu167 = \" SMBALERT_NI0->I2C0_SCL_F2H_SCP = 0\"\n\
syn_tsu168 = \" SMBALERT_NI1->I2C1_SCL_F2H_SCP = 0\"\n\
syn_tsu169 = \" SMBSUS_NI0->I2C0_SCL_F2H_SCP = 0\"\n\
syn_tsu170 = \" SMBSUS_NI1->I2C1_SCL_F2H_SCP = 0\"\n\
syn_tsu171 = \" SPI0_SDI_F2H_SCP->SPI0_CLK_IN = 1.304\"\n\
syn_tsu172 = \" SPI1_SDI_F2H_SCP->SPI1_CLK_IN = 1.418\"\n\
syn_tco0 = \" CLK_BASE->CAN_RXBUS_MGPIO3A_H2F_A = 3.276\"\n\
syn_tco1 = \" CLK_BASE->CAN_RXBUS_MGPIO3A_H2F_B = 3.202\"\n\
syn_tco2 = \" CLK_BASE->CAN_TXBUS_MGPIO2A_H2F_A = 3.179\"\n\
syn_tco3 = \" CLK_BASE->CAN_TXBUS_MGPIO2A_H2F_B = 3.083\"\n\
syn_tco4 = \" CLK_BASE->CAN_TXBUS_USBA_DATA0_MGPIO2A_OUT = 4.272\"\n\
syn_tco5 = \" CLK_BASE->CAN_TX_EBL_MGPIO4A_H2F_A = 3.308\"\n\
syn_tco6 = \" CLK_BASE->CAN_TX_EBL_MGPIO4A_H2F_B = 3.278\"\n\
syn_tco7 = \" CLK_BASE->CAN_TX_EBL_USBA_DATA2_MGPIO4A_OUT = 3.933\"\n\
syn_tco8 = \" CLK_BASE->F_FM0_RDATA[0] = 3.860\"\n\
syn_tco9 = \" CLK_BASE->F_FM0_RDATA[10] = 3.888\"\n\
syn_tco10 = \" CLK_BASE->F_FM0_RDATA[11] = 4.003\"\n\
syn_tco11 = \" CLK_BASE->F_FM0_RDATA[12] = 3.918\"\n\
syn_tco12 = \" CLK_BASE->F_FM0_RDATA[13] = 3.880\"\n\
syn_tco13 = \" CLK_BASE->F_FM0_RDATA[14] = 3.880\"\n\
syn_tco14 = \" CLK_BASE->F_FM0_RDATA[15] = 3.874\"\n\
syn_tco15 = \" CLK_BASE->F_FM0_RDATA[16] = 3.907\"\n\
syn_tco16 = \" CLK_BASE->F_FM0_RDATA[17] = 4.105\"\n\
syn_tco17 = \" CLK_BASE->F_FM0_RDATA[18] = 3.871\"\n\
syn_tco18 = \" CLK_BASE->F_FM0_RDATA[19] = 4.023\"\n\
syn_tco19 = \" CLK_BASE->F_FM0_RDATA[1] = 3.940\"\n\
syn_tco20 = \" CLK_BASE->F_FM0_RDATA[20] = 3.776\"\n\
syn_tco21 = \" CLK_BASE->F_FM0_RDATA[21] = 3.731\"\n\
syn_tco22 = \" CLK_BASE->F_FM0_RDATA[22] = 3.762\"\n\
syn_tco23 = \" CLK_BASE->F_FM0_RDATA[23] = 3.763\"\n\
syn_tco24 = \" CLK_BASE->F_FM0_RDATA[24] = 3.784\"\n\
syn_tco25 = \" CLK_BASE->F_FM0_RDATA[25] = 3.780\"\n\
syn_tco26 = \" CLK_BASE->F_FM0_RDATA[26] = 3.885\"\n\
syn_tco27 = \" CLK_BASE->F_FM0_RDATA[27] = 3.778\"\n\
syn_tco28 = \" CLK_BASE->F_FM0_RDATA[28] = 3.769\"\n\
syn_tco29 = \" CLK_BASE->F_FM0_RDATA[29] = 3.761\"\n\
syn_tco30 = \" CLK_BASE->F_FM0_RDATA[2] = 3.907\"\n\
syn_tco31 = \" CLK_BASE->F_FM0_RDATA[30] = 4.038\"\n\
syn_tco32 = \" CLK_BASE->F_FM0_RDATA[31] = 3.902\"\n\
syn_tco33 = \" CLK_BASE->F_FM0_RDATA[3] = 3.949\"\n\
syn_tco34 = \" CLK_BASE->F_FM0_RDATA[4] = 3.956\"\n\
syn_tco35 = \" CLK_BASE->F_FM0_RDATA[5] = 4.077\"\n\
syn_tco36 = \" CLK_BASE->F_FM0_RDATA[6] = 3.939\"\n\
syn_tco37 = \" CLK_BASE->F_FM0_RDATA[7] = 3.924\"\n\
syn_tco38 = \" CLK_BASE->F_FM0_RDATA[8] = 3.908\"\n\
syn_tco39 = \" CLK_BASE->F_FM0_RDATA[9] = 3.932\"\n\
syn_tco40 = \" CLK_BASE->F_FM0_READYOUT = 3.615\"\n\
syn_tco41 = \" CLK_BASE->F_FM0_RESP = 3.751\"\n\
syn_tco42 = \" CLK_BASE->F_HM0_ADDR[0] = 3.660\"\n\
syn_tco43 = \" CLK_BASE->F_HM0_ADDR[10] = 3.949\"\n\
syn_tco44 = \" CLK_BASE->F_HM0_ADDR[11] = 3.596\"\n\
syn_tco45 = \" CLK_BASE->F_HM0_ADDR[12] = 3.677\"\n\
syn_tco46 = \" CLK_BASE->F_HM0_ADDR[13] = 3.647\"\n\
syn_tco47 = \" CLK_BASE->F_HM0_ADDR[14] = 3.652\"\n\
syn_tco48 = \" CLK_BASE->F_HM0_ADDR[15] = 3.580\"\n\
syn_tco49 = \" CLK_BASE->F_HM0_ADDR[16] = 3.611\"\n\
syn_tco50 = \" CLK_BASE->F_HM0_ADDR[17] = 3.697\"\n\
syn_tco51 = \" CLK_BASE->F_HM0_ADDR[18] = 3.696\"\n\
syn_tco52 = \" CLK_BASE->F_HM0_ADDR[19] = 3.893\"\n\
syn_tco53 = \" CLK_BASE->F_HM0_ADDR[1] = 3.597\"\n\
syn_tco54 = \" CLK_BASE->F_HM0_ADDR[20] = 3.631\"\n\
syn_tco55 = \" CLK_BASE->F_HM0_ADDR[21] = 3.748\"\n\
syn_tco56 = \" CLK_BASE->F_HM0_ADDR[22] = 3.686\"\n\
syn_tco57 = \" CLK_BASE->F_HM0_ADDR[23] = 3.709\"\n\
syn_tco58 = \" CLK_BASE->F_HM0_ADDR[24] = 3.730\"\n\
syn_tco59 = \" CLK_BASE->F_HM0_ADDR[25] = 3.555\"\n\
syn_tco60 = \" CLK_BASE->F_HM0_ADDR[26] = 3.854\"\n\
syn_tco61 = \" CLK_BASE->F_HM0_ADDR[27] = 3.732\"\n\
syn_tco62 = \" CLK_BASE->F_HM0_ADDR[28] = 4.096\"\n\
syn_tco63 = \" CLK_BASE->F_HM0_ADDR[29] = 3.532\"\n\
syn_tco64 = \" CLK_BASE->F_HM0_ADDR[2] = 3.576\"\n\
syn_tco65 = \" CLK_BASE->F_HM0_ADDR[30] = 3.519\"\n\
syn_tco66 = \" CLK_BASE->F_HM0_ADDR[31] = 3.889\"\n\
syn_tco67 = \" CLK_BASE->F_HM0_ADDR[3] = 3.576\"\n\
syn_tco68 = \" CLK_BASE->F_HM0_ADDR[4] = 3.560\"\n\
syn_tco69 = \" CLK_BASE->F_HM0_ADDR[5] = 3.657\"\n\
syn_tco70 = \" CLK_BASE->F_HM0_ADDR[6] = 3.746\"\n\
syn_tco71 = \" CLK_BASE->F_HM0_ADDR[7] = 3.593\"\n\
syn_tco72 = \" CLK_BASE->F_HM0_ADDR[8] = 3.945\"\n\
syn_tco73 = \" CLK_BASE->F_HM0_ADDR[9] = 3.735\"\n\
syn_tco74 = \" CLK_BASE->F_HM0_ENABLE = 3.736\"\n\
syn_tco75 = \" CLK_BASE->F_HM0_SEL = 3.488\"\n\
syn_tco76 = \" CLK_BASE->F_HM0_WDATA[0] = 3.648\"\n\
syn_tco77 = \" CLK_BASE->F_HM0_WDATA[10] = 3.504\"\n\
syn_tco78 = \" CLK_BASE->F_HM0_WDATA[11] = 3.726\"\n\
syn_tco79 = \" CLK_BASE->F_HM0_WDATA[12] = 3.725\"\n\
syn_tco80 = \" CLK_BASE->F_HM0_WDATA[13] = 3.782\"\n\
syn_tco81 = \" CLK_BASE->F_HM0_WDATA[14] = 3.722\"\n\
syn_tco82 = \" CLK_BASE->F_HM0_WDATA[15] = 3.787\"\n\
syn_tco83 = \" CLK_BASE->F_HM0_WDATA[16] = 3.624\"\n\
syn_tco84 = \" CLK_BASE->F_HM0_WDATA[17] = 3.878\"\n\
syn_tco85 = \" CLK_BASE->F_HM0_WDATA[18] = 3.653\"\n\
syn_tco86 = \" CLK_BASE->F_HM0_WDATA[19] = 3.811\"\n\
syn_tco87 = \" CLK_BASE->F_HM0_WDATA[1] = 3.743\"\n\
syn_tco88 = \" CLK_BASE->F_HM0_WDATA[20] = 3.672\"\n\
syn_tco89 = \" CLK_BASE->F_HM0_WDATA[21] = 3.625\"\n\
syn_tco90 = \" CLK_BASE->F_HM0_WDATA[22] = 3.639\"\n\
syn_tco91 = \" CLK_BASE->F_HM0_WDATA[23] = 3.628\"\n\
syn_tco92 = \" CLK_BASE->F_HM0_WDATA[24] = 3.784\"\n\
syn_tco93 = \" CLK_BASE->F_HM0_WDATA[25] = 3.361\"\n\
syn_tco94 = \" CLK_BASE->F_HM0_WDATA[26] = 3.699\"\n\
syn_tco95 = \" CLK_BASE->F_HM0_WDATA[27] = 3.382\"\n\
syn_tco96 = \" CLK_BASE->F_HM0_WDATA[28] = 3.753\"\n\
syn_tco97 = \" CLK_BASE->F_HM0_WDATA[29] = 3.423\"\n\
syn_tco98 = \" CLK_BASE->F_HM0_WDATA[2] = 3.769\"\n\
syn_tco99 = \" CLK_BASE->F_HM0_WDATA[30] = 3.735\"\n\
syn_tco100 = \" CLK_BASE->F_HM0_WDATA[31] = 3.364\"\n\
syn_tco101 = \" CLK_BASE->F_HM0_WDATA[3] = 3.838\"\n\
syn_tco102 = \" CLK_BASE->F_HM0_WDATA[4] = 3.566\"\n\
syn_tco103 = \" CLK_BASE->F_HM0_WDATA[5] = 3.656\"\n\
syn_tco104 = \" CLK_BASE->F_HM0_WDATA[6] = 3.667\"\n\
syn_tco105 = \" CLK_BASE->F_HM0_WDATA[7] = 3.881\"\n\
syn_tco106 = \" CLK_BASE->F_HM0_WDATA[8] = 3.612\"\n\
syn_tco107 = \" CLK_BASE->F_HM0_WDATA[9] = 3.648\"\n\
syn_tco108 = \" CLK_BASE->F_HM0_WRITE = 3.682\"\n\
syn_tco109 = \" CLK_BASE->H2FCALIB = 3.640\"\n\
syn_tco110 = \" CLK_BASE->I2C0_SCL_MGPIO31B_H2F_B = 3.188\"\n\
syn_tco111 = \" CLK_BASE->I2C0_SCL_USBC_DATA1_MGPIO31B_OE = 3.985\"\n\
syn_tco112 = \" CLK_BASE->I2C0_SDA_MGPIO30B_H2F_A = 3.182\"\n\
syn_tco113 = \" CLK_BASE->I2C0_SDA_MGPIO30B_H2F_B = 3.192\"\n\
syn_tco114 = \" CLK_BASE->I2C0_SDA_USBC_DATA0_MGPIO30B_OE = 3.772\"\n\
syn_tco115 = \" CLK_BASE->I2C1_SCL_MGPIO1A_H2F_B = 3.346\"\n\
syn_tco116 = \" CLK_BASE->I2C1_SCL_USBA_DATA4_MGPIO1A_OE = 3.478\"\n\
syn_tco117 = \" CLK_BASE->I2C1_SDA_MGPIO0A_H2F_A = 3.284\"\n\
syn_tco118 = \" CLK_BASE->I2C1_SDA_MGPIO0A_H2F_B = 3.436\"\n\
syn_tco119 = \" CLK_BASE->I2C1_SDA_USBA_DATA3_MGPIO0A_OE = 3.212\"\n\
syn_tco120 = \" CLK_BASE->MMUART0_CTS_MGPIO19B_H2F_A = 3.383\"\n\
syn_tco121 = \" CLK_BASE->MMUART0_CTS_MGPIO19B_H2F_B = 3.249\"\n\
syn_tco122 = \" CLK_BASE->MMUART0_DCD_MGPIO22B_H2F_A = 3.254\"\n\
syn_tco123 = \" CLK_BASE->MMUART0_DCD_MGPIO22B_H2F_B = 3.219\"\n\
syn_tco124 = \" CLK_BASE->MMUART0_DSR_MGPIO20B_H2F_A = 3.239\"\n\
syn_tco125 = \" CLK_BASE->MMUART0_DSR_MGPIO20B_H2F_B = 3.270\"\n\
syn_tco126 = \" CLK_BASE->MMUART0_DTR_MGPIO18B_H2F_A = 3.307\"\n\
syn_tco127 = \" CLK_BASE->MMUART0_DTR_MGPIO18B_H2F_B = 3.259\"\n\
syn_tco128 = \" CLK_BASE->MMUART0_DTR_USBC_DATA6_MGPIO18B_OUT = 3.335\"\n\
syn_tco129 = \" CLK_BASE->MMUART0_RI_MGPIO21B_H2F_A = 3.320\"\n\
syn_tco130 = \" CLK_BASE->MMUART0_RI_MGPIO21B_H2F_B = 3.255\"\n\
syn_tco131 = \" CLK_BASE->MMUART0_RTS_MGPIO17B_H2F_A = 3.313\"\n\
syn_tco132 = \" CLK_BASE->MMUART0_RTS_MGPIO17B_H2F_B = 3.330\"\n\
syn_tco133 = \" CLK_BASE->MMUART0_RTS_USBC_DATA5_MGPIO17B_OUT = 3.332\"\n\
syn_tco134 = \" CLK_BASE->MMUART0_RXD_MGPIO28B_H2F_A = 3.253\"\n\
syn_tco135 = \" CLK_BASE->MMUART0_RXD_MGPIO28B_H2F_B = 3.152\"\n\
syn_tco136 = \" CLK_BASE->MMUART0_SCK_MGPIO29B_H2F_A = 3.246\"\n\
syn_tco137 = \" CLK_BASE->MMUART0_SCK_MGPIO29B_H2F_B = 3.213\"\n\
syn_tco138 = \" CLK_BASE->MMUART0_SCK_USBC_NXT_MGPIO29B_OE = 3.789\"\n\
syn_tco139 = \" CLK_BASE->MMUART0_SCK_USBC_NXT_MGPIO29B_OUT = 3.182\"\n\
syn_tco140 = \" CLK_BASE->MMUART0_TXD_MGPIO27B_H2F_A = 3.878\"\n\
syn_tco141 = \" CLK_BASE->MMUART0_TXD_MGPIO27B_H2F_B = 3.928\"\n\
syn_tco142 = \" CLK_BASE->MMUART0_TXD_USBC_DIR_MGPIO27B_OE = 3.813\"\n\
syn_tco143 = \" CLK_BASE->MMUART0_TXD_USBC_DIR_MGPIO27B_OUT = 3.494\"\n\
syn_tco144 = \" CLK_BASE->MMUART1_DTR_MGPIO12B_H2F_A = 3.262\"\n\
syn_tco145 = \" CLK_BASE->MMUART1_RTS_MGPIO11B_H2F_A = 3.252\"\n\
syn_tco146 = \" CLK_BASE->MMUART1_RTS_MGPIO11B_H2F_B = 3.279\"\n\
syn_tco147 = \" CLK_BASE->MMUART1_RXD_MGPIO26B_H2F_A = 3.206\"\n\
syn_tco148 = \" CLK_BASE->MMUART1_RXD_MGPIO26B_H2F_B = 3.113\"\n\
syn_tco149 = \" CLK_BASE->MMUART1_SCK_MGPIO25B_H2F_A = 3.342\"\n\
syn_tco150 = \" CLK_BASE->MMUART1_SCK_MGPIO25B_H2F_B = 3.278\"\n\
syn_tco151 = \" CLK_BASE->MMUART1_SCK_USBC_DATA4_MGPIO25B_OE = 3.543\"\n\
syn_tco152 = \" CLK_BASE->MMUART1_SCK_USBC_DATA4_MGPIO25B_OUT = 3.221\"\n\
syn_tco153 = \" CLK_BASE->MMUART1_TXD_MGPIO24B_H2F_A = 3.206\"\n\
syn_tco154 = \" CLK_BASE->MMUART1_TXD_MGPIO24B_H2F_B = 3.228\"\n\
syn_tco155 = \" CLK_BASE->MMUART1_TXD_USBC_DATA2_MGPIO24B_OE = 3.798\"\n\
syn_tco156 = \" CLK_BASE->MMUART1_TXD_USBC_DATA2_MGPIO24B_OUT = 3.509\"\n\
syn_tco157 = \" CLK_BASE->RGMII_MDIO_RMII_MDIO_USBB_DATA7_OE = 5.037\"\n\
syn_tco158 = \" CLK_BASE->RGMII_MDIO_RMII_MDIO_USBB_DATA7_OUT = 4.792\"\n\
syn_tco159 = \" CLK_BASE->SPI0_SDI_MGPIO5A_H2F_A = 3.181\"\n\
syn_tco160 = \" CLK_BASE->SPI0_SDI_MGPIO5A_H2F_B = 3.251\"\n\
syn_tco161 = \" CLK_BASE->SPI0_SDO_MGPIO6A_H2F_A = 3.287\"\n\
syn_tco162 = \" CLK_BASE->SPI0_SDO_MGPIO6A_H2F_B = 3.353\"\n\
syn_tco163 = \" CLK_BASE->SPI0_SDO_USBA_STP_MGPIO6A_OE = 5.073\"\n\
syn_tco164 = \" CLK_BASE->SPI0_SDO_USBA_STP_MGPIO6A_OUT = 5.638\"\n\
syn_tco165 = \" CLK_BASE->SPI0_SS0_MGPIO7A_H2F_A = 3.240\"\n\
syn_tco166 = \" CLK_BASE->SPI0_SS0_MGPIO7A_H2F_B = 3.270\"\n\
syn_tco167 = \" CLK_BASE->SPI0_SS1_MGPIO8A_H2F_A = 3.262\"\n\
syn_tco168 = \" CLK_BASE->SPI0_SS1_MGPIO8A_H2F_B = 3.303\"\n\
syn_tco169 = \" CLK_BASE->SPI0_SS2_MGPIO9A_H2F_A = 3.237\"\n\
syn_tco170 = \" CLK_BASE->SPI0_SS2_MGPIO9A_H2F_B = 3.267\"\n\
syn_tco171 = \" CLK_BASE->SPI0_SS3_MGPIO10A_H2F_A = 3.187\"\n\
syn_tco172 = \" CLK_BASE->SPI0_SS3_MGPIO10A_H2F_B = 3.112\"\n\
syn_tco173 = \" CLK_BASE->SPI0_SS4_MGPIO19A_H2F_A = 3.215\"\n\
syn_tco174 = \" CLK_BASE->SPI0_SS5_MGPIO20A_H2F_A = 3.345\"\n\
syn_tco175 = \" CLK_BASE->SPI0_SS6_MGPIO21A_H2F_A = 3.385\"\n\
syn_tco176 = \" CLK_BASE->SPI0_SS7_MGPIO22A_H2F_A = 3.320\"\n\
syn_tco177 = \" CLK_BASE->SPI1_SDI_MGPIO11A_H2F_A = 3.253\"\n\
syn_tco178 = \" CLK_BASE->SPI1_SDI_MGPIO11A_H2F_B = 3.201\"\n\
syn_tco179 = \" CLK_BASE->SPI1_SDO_MGPIO12A_H2F_A = 3.174\"\n\
syn_tco180 = \" CLK_BASE->SPI1_SDO_MGPIO12A_H2F_B = 3.251\"\n\
syn_tco181 = \" CLK_BASE->SPI1_SDO_MGPIO12A_OE = 5.581\"\n\
syn_tco182 = \" CLK_BASE->SPI1_SDO_MGPIO12A_OUT = 6.229\"\n\
syn_tco183 = \" CLK_BASE->SPI1_SS0_MGPIO13A_H2F_A = 3.204\"\n\
syn_tco184 = \" CLK_BASE->SPI1_SS0_MGPIO13A_H2F_B = 3.183\"\n\
syn_tco185 = \" CLK_BASE->SPI1_SS1_MGPIO14A_H2F_A = 3.223\"\n\
syn_tco186 = \" CLK_BASE->SPI1_SS1_MGPIO14A_H2F_B = 3.291\"\n\
syn_tco187 = \" CLK_BASE->SPI1_SS2_MGPIO15A_H2F_A = 3.345\"\n\
syn_tco188 = \" CLK_BASE->SPI1_SS2_MGPIO15A_H2F_B = 3.261\"\n\
syn_tco189 = \" CLK_BASE->SPI1_SS3_MGPIO16A_H2F_A = 3.270\"\n\
syn_tco190 = \" CLK_BASE->SPI1_SS3_MGPIO16A_H2F_B = 3.378\"\n\
syn_tco191 = \" CLK_BASE->SPI1_SS4_MGPIO17A_H2F_A = 3.245\"\n\
syn_tco192 = \" CLK_BASE->SPI1_SS5_MGPIO18A_H2F_A = 3.282\"\n\
syn_tco193 = \" CLK_BASE->SPI1_SS6_MGPIO23A_H2F_A = 3.253\"\n\
syn_tco194 = \" CLK_BASE->SPI1_SS7_MGPIO24A_H2F_A = 3.232\"\n\
*/\n\
/* synthesis black_box_pad_pin =\"\" */\n\
output CAN_RXBUS_MGPIO3A_H2F_A;\n\
output CAN_RXBUS_MGPIO3A_H2F_B;\n\
output CAN_TX_EBL_MGPIO4A_H2F_A;\n\
output CAN_TX_EBL_MGPIO4A_H2F_B;\n\
output CAN_TXBUS_MGPIO2A_H2F_A;\n\
output CAN_TXBUS_MGPIO2A_H2F_B;\n\
output CLK_CONFIG_APB;\n\
output COMMS_INT;\n\
output CONFIG_PRESET_N;\n\
output [7:0] EDAC_ERROR;\n\
output [31:0] F_FM0_RDATA;\n\
output F_FM0_READYOUT;\n\
output F_FM0_RESP;\n\
output [31:0] F_HM0_ADDR;\n\
output F_HM0_ENABLE;\n\
output F_HM0_SEL;\n\
output [1:0] F_HM0_SIZE;\n\
output F_HM0_TRANS1;\n\
output [31:0] F_HM0_WDATA;\n\
output F_HM0_WRITE;\n\
output FAB_CHRGVBUS;\n\
output FAB_DISCHRGVBUS;\n\
output FAB_DMPULLDOWN;\n\
output FAB_DPPULLDOWN;\n\
output FAB_DRVVBUS;\n\
output FAB_IDPULLUP;\n\
output [1:0] FAB_OPMODE;\n\
output FAB_SUSPENDM;\n\
output FAB_TERMSEL;\n\
output FAB_TXVALID;\n\
output [3:0] FAB_VCONTROL;\n\
output FAB_VCONTROLLOADM;\n\
output [1:0] FAB_XCVRSEL;\n\
output [7:0] FAB_XDATAOUT;\n\
output FACC_GLMUX_SEL;\n\
output [1:0] FIC32_0_MASTER;\n\
output [1:0] FIC32_1_MASTER;\n\
output FPGA_RESET_N;\n\
output GTX_CLK;\n\
output [15:0] H2F_INTERRUPT;\n\
output H2F_NMI;\n\
output H2FCALIB;\n\
output I2C0_SCL_MGPIO31B_H2F_A;\n\
output I2C0_SCL_MGPIO31B_H2F_B;\n\
output I2C0_SDA_MGPIO30B_H2F_A;\n\
output I2C0_SDA_MGPIO30B_H2F_B;\n\
output I2C1_SCL_MGPIO1A_H2F_A;\n\
output I2C1_SCL_MGPIO1A_H2F_B;\n\
output I2C1_SDA_MGPIO0A_H2F_A;\n\
output I2C1_SDA_MGPIO0A_H2F_B;\n\
output MDCF;\n\
output MDOENF;\n\
output MDOF;\n\
output MMUART0_CTS_MGPIO19B_H2F_A;\n\
output MMUART0_CTS_MGPIO19B_H2F_B;\n\
output MMUART0_DCD_MGPIO22B_H2F_A;\n\
output MMUART0_DCD_MGPIO22B_H2F_B;\n\
output MMUART0_DSR_MGPIO20B_H2F_A;\n\
output MMUART0_DSR_MGPIO20B_H2F_B;\n\
output MMUART0_DTR_MGPIO18B_H2F_A;\n\
output MMUART0_DTR_MGPIO18B_H2F_B;\n\
output MMUART0_RI_MGPIO21B_H2F_A;\n\
output MMUART0_RI_MGPIO21B_H2F_B;\n\
output MMUART0_RTS_MGPIO17B_H2F_A;\n\
output MMUART0_RTS_MGPIO17B_H2F_B;\n\
output MMUART0_RXD_MGPIO28B_H2F_A;\n\
output MMUART0_RXD_MGPIO28B_H2F_B;\n\
output MMUART0_SCK_MGPIO29B_H2F_A;\n\
output MMUART0_SCK_MGPIO29B_H2F_B;\n\
output MMUART0_TXD_MGPIO27B_H2F_A;\n\
output MMUART0_TXD_MGPIO27B_H2F_B;\n\
output MMUART1_DTR_MGPIO12B_H2F_A;\n\
output MMUART1_RTS_MGPIO11B_H2F_A;\n\
output MMUART1_RTS_MGPIO11B_H2F_B;\n\
output MMUART1_RXD_MGPIO26B_H2F_A;\n\
output MMUART1_RXD_MGPIO26B_H2F_B;\n\
output MMUART1_SCK_MGPIO25B_H2F_A;\n\
output MMUART1_SCK_MGPIO25B_H2F_B;\n\
output MMUART1_TXD_MGPIO24B_H2F_A;\n\
output MMUART1_TXD_MGPIO24B_H2F_B;\n\
output MPLL_LOCK;\n\
output [15:2] PER2_FABRIC_PADDR;\n\
output PER2_FABRIC_PENABLE;\n\
output PER2_FABRIC_PSEL;\n\
output [31:0] PER2_FABRIC_PWDATA;\n\
output PER2_FABRIC_PWRITE;\n\
output RTC_MATCH;\n\
output SLEEPDEEP;\n\
output SLEEPHOLDACK;\n\
output SLEEPING;\n\
output SMBALERT_NO0;\n\
output SMBALERT_NO1;\n\
output SMBSUS_NO0;\n\
output SMBSUS_NO1;\n\
output SPI0_CLK_OUT;\n\
output SPI0_SDI_MGPIO5A_H2F_A;\n\
output SPI0_SDI_MGPIO5A_H2F_B;\n\
output SPI0_SDO_MGPIO6A_H2F_A;\n\
output SPI0_SDO_MGPIO6A_H2F_B;\n\
output SPI0_SS0_MGPIO7A_H2F_A;\n\
output SPI0_SS0_MGPIO7A_H2F_B;\n\
output SPI0_SS1_MGPIO8A_H2F_A;\n\
output SPI0_SS1_MGPIO8A_H2F_B;\n\
output SPI0_SS2_MGPIO9A_H2F_A;\n\
output SPI0_SS2_MGPIO9A_H2F_B;\n\
output SPI0_SS3_MGPIO10A_H2F_A;\n\
output SPI0_SS3_MGPIO10A_H2F_B;\n\
output SPI0_SS4_MGPIO19A_H2F_A;\n\
output SPI0_SS5_MGPIO20A_H2F_A;\n\
output SPI0_SS6_MGPIO21A_H2F_A;\n\
output SPI0_SS7_MGPIO22A_H2F_A;\n\
output SPI1_CLK_OUT;\n\
output SPI1_SDI_MGPIO11A_H2F_A;\n\
output SPI1_SDI_MGPIO11A_H2F_B;\n\
output SPI1_SDO_MGPIO12A_H2F_A;\n\
output SPI1_SDO_MGPIO12A_H2F_B;\n\
output SPI1_SS0_MGPIO13A_H2F_A;\n\
output SPI1_SS0_MGPIO13A_H2F_B;\n\
output SPI1_SS1_MGPIO14A_H2F_A;\n\
output SPI1_SS1_MGPIO14A_H2F_B;\n\
output SPI1_SS2_MGPIO15A_H2F_A;\n\
output SPI1_SS2_MGPIO15A_H2F_B;\n\
output SPI1_SS3_MGPIO16A_H2F_A;\n\
output SPI1_SS3_MGPIO16A_H2F_B;\n\
output SPI1_SS4_MGPIO17A_H2F_A;\n\
output SPI1_SS5_MGPIO18A_H2F_A;\n\
output SPI1_SS6_MGPIO23A_H2F_A;\n\
output SPI1_SS7_MGPIO24A_H2F_A;\n\
output [9:0] TCGF;\n\
output TRACECLK;\n\
output [3:0] TRACEDATA;\n\
output TX_CLK;\n\
output TX_ENF;\n\
output TX_ERRF;\n\
output TXCTL_EN_RIF;\n\
output [3:0] TXD_RIF;\n\
output [7:0] TXDF;\n\
output TXEV;\n\
output WDOGTIMEOUT;\n\
output F_ARREADY_HREADYOUT1;\n\
output F_AWREADY_HREADYOUT0;\n\
output [3:0] F_BID;\n\
output [1:0] F_BRESP_HRESP0;\n\
output F_BVALID;\n\
output [63:0] F_RDATA_HRDATA01;\n\
output [3:0] F_RID;\n\
output F_RLAST;\n\
output [1:0] F_RRESP_HRESP1;\n\
output F_RVALID;\n\
output F_WREADY;\n\
output [15:0] MDDR_FABRIC_PRDATA;\n\
output MDDR_FABRIC_PREADY;\n\
output MDDR_FABRIC_PSLVERR;\n\
input  CAN_RXBUS_F2H_SCP;\n\
input  CAN_TX_EBL_F2H_SCP;\n\
input  CAN_TXBUS_F2H_SCP;\n\
input  COLF;\n\
input  CRSF;\n\
input  [1:0] F2_DMAREADY;\n\
input  [15:0] F2H_INTERRUPT;\n\
input  F2HCALIB;\n\
input  [1:0] F_DMAREADY;\n\
input  [31:0] F_FM0_ADDR;\n\
input  F_FM0_ENABLE;\n\
input  F_FM0_MASTLOCK;\n\
input  F_FM0_READY;\n\
input  F_FM0_SEL;\n\
input  [1:0] F_FM0_SIZE;\n\
input  F_FM0_TRANS1;\n\
input  [31:0] F_FM0_WDATA;\n\
input  F_FM0_WRITE;\n\
input  [31:0] F_HM0_RDATA;\n\
input  F_HM0_READY;\n\
input  F_HM0_RESP;\n\
input  FAB_AVALID;\n\
input  FAB_HOSTDISCON;\n\
input  FAB_IDDIG;\n\
input  [1:0] FAB_LINESTATE;\n\
input  FAB_M3_RESET_N;\n\
input  FAB_PLL_LOCK;\n\
input  FAB_RXACTIVE;\n\
input  FAB_RXERROR;\n\
input  FAB_RXVALID;\n\
input  FAB_RXVALIDH;\n\
input  FAB_SESSEND;\n\
input  FAB_TXREADY;\n\
input  FAB_VBUSVALID;\n\
input  [7:0] FAB_VSTATUS;\n\
input  [7:0] FAB_XDATAIN;\n\
input  GTX_CLKPF;\n\
input  I2C0_BCLK;\n\
input  I2C0_SCL_F2H_SCP;\n\
input  I2C0_SDA_F2H_SCP;\n\
input  I2C1_BCLK;\n\
input  I2C1_SCL_F2H_SCP;\n\
input  I2C1_SDA_F2H_SCP;\n\
input  MDIF;\n\
input  MGPIO0A_F2H_GPIN;\n\
input  MGPIO10A_F2H_GPIN;\n\
input  MGPIO11A_F2H_GPIN;\n\
input  MGPIO11B_F2H_GPIN;\n\
input  MGPIO12A_F2H_GPIN;\n\
input  MGPIO13A_F2H_GPIN;\n\
input  MGPIO14A_F2H_GPIN;\n\
input  MGPIO15A_F2H_GPIN;\n\
input  MGPIO16A_F2H_GPIN;\n\
input  MGPIO17B_F2H_GPIN;\n\
input  MGPIO18B_F2H_GPIN;\n\
input  MGPIO19B_F2H_GPIN;\n\
input  MGPIO1A_F2H_GPIN;\n\
input  MGPIO20B_F2H_GPIN;\n\
input  MGPIO21B_F2H_GPIN;\n\
input  MGPIO22B_F2H_GPIN;\n\
input  MGPIO24B_F2H_GPIN;\n\
input  MGPIO25B_F2H_GPIN;\n\
input  MGPIO26B_F2H_GPIN;\n\
input  MGPIO27B_F2H_GPIN;\n\
input  MGPIO28B_F2H_GPIN;\n\
input  MGPIO29B_F2H_GPIN;\n\
input  MGPIO2A_F2H_GPIN;\n\
input  MGPIO30B_F2H_GPIN;\n\
input  MGPIO31B_F2H_GPIN;\n\
input  MGPIO3A_F2H_GPIN;\n\
input  MGPIO4A_F2H_GPIN;\n\
input  MGPIO5A_F2H_GPIN;\n\
input  MGPIO6A_F2H_GPIN;\n\
input  MGPIO7A_F2H_GPIN;\n\
input  MGPIO8A_F2H_GPIN;\n\
input  MGPIO9A_F2H_GPIN;\n\
input  MMUART0_CTS_F2H_SCP;\n\
input  MMUART0_DCD_F2H_SCP;\n\
input  MMUART0_DSR_F2H_SCP;\n\
input  MMUART0_DTR_F2H_SCP;\n\
input  MMUART0_RI_F2H_SCP;\n\
input  MMUART0_RTS_F2H_SCP;\n\
input  MMUART0_RXD_F2H_SCP;\n\
input  MMUART0_SCK_F2H_SCP;\n\
input  MMUART0_TXD_F2H_SCP;\n\
input  MMUART1_CTS_F2H_SCP;\n\
input  MMUART1_DCD_F2H_SCP;\n\
input  MMUART1_DSR_F2H_SCP;\n\
input  MMUART1_RI_F2H_SCP;\n\
input  MMUART1_RTS_F2H_SCP;\n\
input  MMUART1_RXD_F2H_SCP;\n\
input  MMUART1_SCK_F2H_SCP;\n\
input  MMUART1_TXD_F2H_SCP;\n\
input  [31:0] PER2_FABRIC_PRDATA;\n\
input  PER2_FABRIC_PREADY;\n\
input  PER2_FABRIC_PSLVERR;\n\
input  [9:0] RCGF;\n\
input  RX_CLKPF;\n\
input  RX_DVF;\n\
input  RX_ERRF;\n\
input  RX_EV;\n\
input  [7:0] RXDF;\n\
input  SLEEPHOLDREQ;\n\
input  SMBALERT_NI0;\n\
input  SMBALERT_NI1;\n\
input  SMBSUS_NI0;\n\
input  SMBSUS_NI1;\n\
input  SPI0_CLK_IN;\n\
input  SPI0_SDI_F2H_SCP;\n\
input  SPI0_SDO_F2H_SCP;\n\
input  SPI0_SS0_F2H_SCP;\n\
input  SPI0_SS1_F2H_SCP;\n\
input  SPI0_SS2_F2H_SCP;\n\
input  SPI0_SS3_F2H_SCP;\n\
input  SPI1_CLK_IN;\n\
input  SPI1_SDI_F2H_SCP;\n\
input  SPI1_SDO_F2H_SCP;\n\
input  SPI1_SS0_F2H_SCP;\n\
input  SPI1_SS1_F2H_SCP;\n\
input  SPI1_SS2_F2H_SCP;\n\
input  SPI1_SS3_F2H_SCP;\n\
input  TX_CLKPF;\n\
input  USER_MSS_GPIO_RESET_N;\n\
input  USER_MSS_RESET_N;\n\
input  XCLK_FAB;\n\
input  CLK_BASE;\n\
input  CLK_MDDR_APB;\n\
input  [31:0] F_ARADDR_HADDR1;\n\
input  [1:0] F_ARBURST_HTRANS1;\n\
input  [3:0] F_ARID_HSEL1;\n\
input  [3:0] F_ARLEN_HBURST1;\n\
input  [1:0] F_ARLOCK_HMASTLOCK1;\n\
input  [1:0] F_ARSIZE_HSIZE1;\n\
input  F_ARVALID_HWRITE1;\n\
input  [31:0] F_AWADDR_HADDR0;\n\
input  [1:0] F_AWBURST_HTRANS0;\n\
input  [3:0] F_AWID_HSEL0;\n\
input  [3:0] F_AWLEN_HBURST0;\n\
input  [1:0] F_AWLOCK_HMASTLOCK0;\n\
input  [1:0] F_AWSIZE_HSIZE0;\n\
input  F_AWVALID_HWRITE0;\n\
input  F_BREADY;\n\
input  F_RMW_AXI;\n\
input  F_RREADY;\n\
input  [63:0] F_WDATA_HWDATA01;\n\
input  [3:0] F_WID_HREADY01;\n\
input  F_WLAST;\n\
input  [7:0] F_WSTRB;\n\
input  F_WVALID;\n\
input  FPGA_MDDR_ARESET_N;\n\
input  [10:2] MDDR_FABRIC_PADDR;\n\
input  MDDR_FABRIC_PENABLE;\n\
input  MDDR_FABRIC_PSEL;\n\
input  [15:0] MDDR_FABRIC_PWDATA;\n\
input  MDDR_FABRIC_PWRITE;\n\
input  PRESET_N;\n\
input  CAN_RXBUS_USBA_DATA1_MGPIO3A_IN;\n\
input  CAN_TX_EBL_USBA_DATA2_MGPIO4A_IN;\n\
input  CAN_TXBUS_USBA_DATA0_MGPIO2A_IN;\n\
input  [2:0] DM_IN;\n\
input  [17:0] DRAM_DQ_IN;\n\
input  [2:0] DRAM_DQS_IN;\n\
input  [1:0] DRAM_FIFO_WE_IN;\n\
input  I2C0_SCL_USBC_DATA1_MGPIO31B_IN;\n\
input  I2C0_SDA_USBC_DATA0_MGPIO30B_IN;\n\
input  I2C1_SCL_USBA_DATA4_MGPIO1A_IN;\n\
input  I2C1_SDA_USBA_DATA3_MGPIO0A_IN;\n\
input  MMUART0_CTS_USBC_DATA7_MGPIO19B_IN;\n\
input  MMUART0_DCD_MGPIO22B_IN;\n\
input  MMUART0_DSR_MGPIO20B_IN;\n\
input  MMUART0_DTR_USBC_DATA6_MGPIO18B_IN;\n\
input  MMUART0_RI_MGPIO21B_IN;\n\
input  MMUART0_RTS_USBC_DATA5_MGPIO17B_IN;\n\
input  MMUART0_RXD_USBC_STP_MGPIO28B_IN;\n\
input  MMUART0_SCK_USBC_NXT_MGPIO29B_IN;\n\
input  MMUART0_TXD_USBC_DIR_MGPIO27B_IN;\n\
input  MMUART1_RXD_USBC_DATA3_MGPIO26B_IN;\n\
input  MMUART1_SCK_USBC_DATA4_MGPIO25B_IN;\n\
input  MMUART1_TXD_USBC_DATA2_MGPIO24B_IN;\n\
input  RGMII_GTX_CLK_RMII_CLK_USBB_XCLK_IN;\n\
input  RGMII_MDC_RMII_MDC_IN;\n\
input  RGMII_MDIO_RMII_MDIO_USBB_DATA7_IN;\n\
input  RGMII_RX_CLK_IN;\n\
input  RGMII_RX_CTL_RMII_CRS_DV_USBB_DATA2_IN;\n\
input  RGMII_RXD0_RMII_RXD0_USBB_DATA0_IN;\n\
input  RGMII_RXD1_RMII_RXD1_USBB_DATA1_IN;\n\
input  RGMII_RXD2_RMII_RX_ER_USBB_DATA3_IN;\n\
input  RGMII_RXD3_USBB_DATA4_IN;\n\
input  RGMII_TX_CLK_IN;\n\
input  RGMII_TX_CTL_RMII_TX_EN_USBB_NXT_IN;\n\
input  RGMII_TXD0_RMII_TXD0_USBB_DIR_IN;\n\
input  RGMII_TXD1_RMII_TXD1_USBB_STP_IN;\n\
input  RGMII_TXD2_USBB_DATA5_IN;\n\
input  RGMII_TXD3_USBB_DATA6_IN;\n\
input  SPI0_SCK_USBA_XCLK_IN;\n\
input  SPI0_SDI_USBA_DIR_MGPIO5A_IN;\n\
input  SPI0_SDO_USBA_STP_MGPIO6A_IN;\n\
input  SPI0_SS0_USBA_NXT_MGPIO7A_IN;\n\
input  SPI0_SS1_USBA_DATA5_MGPIO8A_IN;\n\
input  SPI0_SS2_USBA_DATA6_MGPIO9A_IN;\n\
input  SPI0_SS3_USBA_DATA7_MGPIO10A_IN;\n\
input  SPI1_SCK_IN;\n\
input  SPI1_SDI_MGPIO11A_IN;\n\
input  SPI1_SDO_MGPIO12A_IN;\n\
input  SPI1_SS0_MGPIO13A_IN;\n\
input  SPI1_SS1_MGPIO14A_IN;\n\
input  SPI1_SS2_MGPIO15A_IN;\n\
input  SPI1_SS3_MGPIO16A_IN;\n\
input  SPI1_SS4_MGPIO17A_IN;\n\
input  SPI1_SS5_MGPIO18A_IN;\n\
input  SPI1_SS6_MGPIO23A_IN;\n\
input  SPI1_SS7_MGPIO24A_IN;\n\
input  USBC_XCLK_IN;\n\
output CAN_RXBUS_USBA_DATA1_MGPIO3A_OUT;\n\
output CAN_TX_EBL_USBA_DATA2_MGPIO4A_OUT;\n\
output CAN_TXBUS_USBA_DATA0_MGPIO2A_OUT;\n\
output [15:0] DRAM_ADDR;\n\
output [2:0] DRAM_BA;\n\
output DRAM_CASN;\n\
output DRAM_CKE;\n\
output DRAM_CLK;\n\
output DRAM_CSN;\n\
output [2:0] DRAM_DM_RDQS_OUT;\n\
output [17:0] DRAM_DQ_OUT;\n\
output [2:0] DRAM_DQS_OUT;\n\
output [1:0] DRAM_FIFO_WE_OUT;\n\
output DRAM_ODT;\n\
output DRAM_RASN;\n\
output DRAM_RSTN;\n\
output DRAM_WEN;\n\
output I2C0_SCL_USBC_DATA1_MGPIO31B_OUT;\n\
output I2C0_SDA_USBC_DATA0_MGPIO30B_OUT;\n\
output I2C1_SCL_USBA_DATA4_MGPIO1A_OUT;\n\
output I2C1_SDA_USBA_DATA3_MGPIO0A_OUT;\n\
output MMUART0_CTS_USBC_DATA7_MGPIO19B_OUT;\n\
output MMUART0_DCD_MGPIO22B_OUT;\n\
output MMUART0_DSR_MGPIO20B_OUT;\n\
output MMUART0_DTR_USBC_DATA6_MGPIO18B_OUT;\n\
output MMUART0_RI_MGPIO21B_OUT;\n\
output MMUART0_RTS_USBC_DATA5_MGPIO17B_OUT;\n\
output MMUART0_RXD_USBC_STP_MGPIO28B_OUT;\n\
output MMUART0_SCK_USBC_NXT_MGPIO29B_OUT;\n\
output MMUART0_TXD_USBC_DIR_MGPIO27B_OUT;\n\
output MMUART1_RXD_USBC_DATA3_MGPIO26B_OUT;\n\
output MMUART1_SCK_USBC_DATA4_MGPIO25B_OUT;\n\
output MMUART1_TXD_USBC_DATA2_MGPIO24B_OUT;\n\
output RGMII_GTX_CLK_RMII_CLK_USBB_XCLK_OUT;\n\
output RGMII_MDC_RMII_MDC_OUT;\n\
output RGMII_MDIO_RMII_MDIO_USBB_DATA7_OUT;\n\
output RGMII_RX_CLK_OUT;\n\
output RGMII_RX_CTL_RMII_CRS_DV_USBB_DATA2_OUT;\n\
output RGMII_RXD0_RMII_RXD0_USBB_DATA0_OUT;\n\
output RGMII_RXD1_RMII_RXD1_USBB_DATA1_OUT;\n\
output RGMII_RXD2_RMII_RX_ER_USBB_DATA3_OUT;\n\
output RGMII_RXD3_USBB_DATA4_OUT;\n\
output RGMII_TX_CLK_OUT;\n\
output RGMII_TX_CTL_RMII_TX_EN_USBB_NXT_OUT;\n\
output RGMII_TXD0_RMII_TXD0_USBB_DIR_OUT;\n\
output RGMII_TXD1_RMII_TXD1_USBB_STP_OUT;\n\
output RGMII_TXD2_USBB_DATA5_OUT;\n\
output RGMII_TXD3_USBB_DATA6_OUT;\n\
output SPI0_SCK_USBA_XCLK_OUT;\n\
output SPI0_SDI_USBA_DIR_MGPIO5A_OUT;\n\
output SPI0_SDO_USBA_STP_MGPIO6A_OUT;\n\
output SPI0_SS0_USBA_NXT_MGPIO7A_OUT;\n\
output SPI0_SS1_USBA_DATA5_MGPIO8A_OUT;\n\
output SPI0_SS2_USBA_DATA6_MGPIO9A_OUT;\n\
output SPI0_SS3_USBA_DATA7_MGPIO10A_OUT;\n\
output SPI1_SCK_OUT;\n\
output SPI1_SDI_MGPIO11A_OUT;\n\
output SPI1_SDO_MGPIO12A_OUT;\n\
output SPI1_SS0_MGPIO13A_OUT;\n\
output SPI1_SS1_MGPIO14A_OUT;\n\
output SPI1_SS2_MGPIO15A_OUT;\n\
output SPI1_SS3_MGPIO16A_OUT;\n\
output SPI1_SS4_MGPIO17A_OUT;\n\
output SPI1_SS5_MGPIO18A_OUT;\n\
output SPI1_SS6_MGPIO23A_OUT;\n\
output SPI1_SS7_MGPIO24A_OUT;\n\
output USBC_XCLK_OUT;\n\
output CAN_RXBUS_USBA_DATA1_MGPIO3A_OE;\n\
output CAN_TX_EBL_USBA_DATA2_MGPIO4A_OE;\n\
output CAN_TXBUS_USBA_DATA0_MGPIO2A_OE;\n\
output [2:0] DM_OE;\n\
output [17:0] DRAM_DQ_OE;\n\
output [2:0] DRAM_DQS_OE;\n\
output I2C0_SCL_USBC_DATA1_MGPIO31B_OE;\n\
output I2C0_SDA_USBC_DATA0_MGPIO30B_OE;\n\
output I2C1_SCL_USBA_DATA4_MGPIO1A_OE;\n\
output I2C1_SDA_USBA_DATA3_MGPIO0A_OE;\n\
output MMUART0_CTS_USBC_DATA7_MGPIO19B_OE;\n\
output MMUART0_DCD_MGPIO22B_OE;\n\
output MMUART0_DSR_MGPIO20B_OE;\n\
output MMUART0_DTR_USBC_DATA6_MGPIO18B_OE;\n\
output MMUART0_RI_MGPIO21B_OE;\n\
output MMUART0_RTS_USBC_DATA5_MGPIO17B_OE;\n\
output MMUART0_RXD_USBC_STP_MGPIO28B_OE;\n\
output MMUART0_SCK_USBC_NXT_MGPIO29B_OE;\n\
output MMUART0_TXD_USBC_DIR_MGPIO27B_OE;\n\
output MMUART1_RXD_USBC_DATA3_MGPIO26B_OE;\n\
output MMUART1_SCK_USBC_DATA4_MGPIO25B_OE;\n\
output MMUART1_TXD_USBC_DATA2_MGPIO24B_OE;\n\
output RGMII_GTX_CLK_RMII_CLK_USBB_XCLK_OE;\n\
output RGMII_MDC_RMII_MDC_OE;\n\
output RGMII_MDIO_RMII_MDIO_USBB_DATA7_OE;\n\
output RGMII_RX_CLK_OE;\n\
output RGMII_RX_CTL_RMII_CRS_DV_USBB_DATA2_OE;\n\
output RGMII_RXD0_RMII_RXD0_USBB_DATA0_OE;\n\
output RGMII_RXD1_RMII_RXD1_USBB_DATA1_OE;\n\
output RGMII_RXD2_RMII_RX_ER_USBB_DATA3_OE;\n\
output RGMII_RXD3_USBB_DATA4_OE;\n\
output RGMII_TX_CLK_OE;\n\
output RGMII_TX_CTL_RMII_TX_EN_USBB_NXT_OE;\n\
output RGMII_TXD0_RMII_TXD0_USBB_DIR_OE;\n\
output RGMII_TXD1_RMII_TXD1_USBB_STP_OE;\n\
output RGMII_TXD2_USBB_DATA5_OE;\n\
output RGMII_TXD3_USBB_DATA6_OE;\n\
output SPI0_SCK_USBA_XCLK_OE;\n\
output SPI0_SDI_USBA_DIR_MGPIO5A_OE;\n\
output SPI0_SDO_USBA_STP_MGPIO6A_OE;\n\
output SPI0_SS0_USBA_NXT_MGPIO7A_OE;\n\
output SPI0_SS1_USBA_DATA5_MGPIO8A_OE;\n\
output SPI0_SS2_USBA_DATA6_MGPIO9A_OE;\n\
output SPI0_SS3_USBA_DATA7_MGPIO10A_OE;\n\
output SPI1_SCK_OE;\n\
output SPI1_SDI_MGPIO11A_OE;\n\
output SPI1_SDO_MGPIO12A_OE;\n\
output SPI1_SS0_MGPIO13A_OE;\n\
output SPI1_SS1_MGPIO14A_OE;\n\
output SPI1_SS2_MGPIO15A_OE;\n\
output SPI1_SS3_MGPIO16A_OE;\n\
output SPI1_SS4_MGPIO17A_OE;\n\
output SPI1_SS5_MGPIO18A_OE;\n\
output SPI1_SS6_MGPIO23A_OE;\n\
output SPI1_SS7_MGPIO24A_OE;\n\
output USBC_XCLK_OE;\n\
parameter INIT = \'h0;\n\
parameter ACT_UBITS = \'h0;\n\
parameter MEMORYFILE = \"\";\n\
parameter RTC_MAIN_XTL_FREQ = 0.0;\n\
parameter RTC_MAIN_XTL_MODE = \"\";\n\
parameter DDR_CLK_FREQ = 0.0;\n\
\n\
endmodule\n'

       return m2s010_silicon_macro

