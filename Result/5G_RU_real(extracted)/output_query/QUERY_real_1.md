Ports are not radiatting with PS alarm

# RAG answer
## Information (RAG)
- Datetime (RAG): 2024-12-08 08:13:55.040796
- Processing time [s] (RAG): 3.5855894088745117
- input_token (RAG): 4092
- output_token (RAG): 331
## Response (RAG)
### response 1 (RAG)
- ref 1 (RAG): [sentence0_17](#sentence0_17)
- response 1 (RAG): MOP 18: Antenna ports are not radiating. To resolve it, the issue is related to the ADI component, and Plan B DB solves this problem. 
### response 2 (RAG)
- ref 2 (RAG): [sentence0_82](#sentence0_82)
- response 2 (RAG): MOP 83: Power issue on Antenna ports. To resolve it, the issue is related to the ADI component, and Plan B DB solves this problem. 
### response 3 (RAG)
- ref 3 (RAG): [sentence0_104](#sentence0_104)
- response 3 (RAG): MOP 105: Internal PS Alarm on TB and DB Radios. To resolve it, the issue is related to the ADI component, and Plan B DB solves this problem. 
### response 4 (RAG)
- ref 4 (RAG): [sentence0_14](#sentence0_14)
- response 4 (RAG): MOP 15: [FCC-DB : non-recoverable] TX GAIN and PS alarm issue. To resolve it, the issue is related to the ADI component, and Plan B DB solves this problem. 
### response 5 (RAG)
- ref 5 (RAG): [sentence0_88](#sentence0_88)
- response 5 (RAG): MOP 89: No TX Power for Antenna ports A&C /PS Alarm. To resolve it, it is related to the ADI issue, and Plane B HW resolves this issue. 
### response 6 (RAG)
- ref 6 (RAG): [sentence0_11](#sentence0_11)
- response 6 (RAG): MOP 12: "RF-B 50V PS Alarm ON" Issue. To resolve it, this issue is related to the ADI component, and the Plan B DB should solve this problem. 


# KG1 answer
## Information (KG1)
- Datetime (KG1): 2024-12-08 08:13:56.484458
- Processing time [s] (KG1): 1.4121968746185303
- input_token (KG1): 174
- output_token (KG1): 16
## Response (KG1)
### summary of root cause candidates (KG1)
- *bios misconfiguration in SD cluster* [response 1] (KG1)
- *incorrect BIOS configuration* [response 2] (KG1)
- *power supply issue* [response 3] (KG1)
- *ADI component issue* [response 3] (KG1)
- *Missing CLI command execution* [response 4] (KG1)
- *RF hardware failure* [response 5] (KG1)
- *defective ADI power device regulator (N 29, port_B)* [response 6] (KG1)
- *software version v0212 with RF-B OBP issue* [response 7] (KG1)
- *software version before v3112* [response 8] (KG1)
- *software version v3111* [response 9] (KG1)
- *ADI known issue with switching regulator* [response 10] (KG1)
- *outdated software version* [response 11] (KG1)
- *carrier configuration push* [response 12] (KG1)

### response 1 (KG1): 
We identified incidents similar to yours:
- *internal PS alarm not observed*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *bios misconfiguration in SD cluster*. &nbsp; (See {'TSG': ['[sentence1_32](#sentence1_32)']} for details.)

This root cause(s) may happen if

- 
- 

This root cause(s) could result in your incident through

- *RU reboots*.
- *DU does not send watchdog reset timer*.
- *supervision timeout at the radio*.

### response 2 (KG1): 
We identified incidents similar to yours:
- *internal PS alarm not observed*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *incorrect BIOS configuration*. &nbsp; (See {'TSG': ['[sentence1_32](#sentence1_32)']} for details.)

This root cause(s) may happen if

- 

 and/or 

- *log shows netconf close session*.
- *log shows Netconf session close*.
- *log shows netconf close session is sent*.
- *log shows RU_TIMING_UNLOCKED transition*.
- *log shows RU_TERMINATE_CONNECTION transition*.

This root cause(s) could result in your incident through

- *RU reboots*.
- *Netconf session instability*.
- *Netconf session close*.

### response 3 (KG1): 
We identified incidents similar to yours:
- *internal PS alarm not observed*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *power supply issue*. &nbsp; (See {'TSG': ['[sentence1_12](#sentence1_12)', '[sentence1_14](#sentence1_14)']} for details.)
2. *ADI component issue*. &nbsp; (See {'TSG': ['[sentence1_82](#sentence1_82)', '[sentence1_17](#sentence1_17)', '[sentence1_104](#sentence1_104)', '[sentence1_14](#sentence1_14)']} for details.)

This root cause(s) may happen if

- *transmission gain issue*.

 and/or 

- *log shows POWER ON RESET*.

This root cause(s) could result in your incident through

- *RU reboots*.
- *POWER ON RESET*.

### response 4 (KG1): 
We identified incidents similar to yours:
- *Antenna port D not radiating*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *Missing CLI command execution*. &nbsp; (See {'TSG': ['[sentence1_39](#sentence1_39)']} for details.)

This root cause(s) may happen if

- *Antenna port B not radiating*.
- *internal PS alarm*.

 and/or 

- *log shows PS alarm*.
- *log shows PS ALM*.
- *log shows PS ALM 500 seconds after boot*.
- *log shows PS ALM 1300 seconds after boot*.

This root cause(s) could result in your incident through

- *carrier configuration issue*.

### response 5 (KG1): 
We identified incidents similar to yours:
- *Antenna port D not radiating*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *RF hardware failure*. &nbsp; (See {'TSG': ['[sentence1_39](#sentence1_39)']} for details.)

This root cause(s) may happen if

- *Antenna port B not radiating*.
- *internal PS alarm*.

 and/or 

- *log shows PS alarm*.
- *log shows PS ALM*.
- *log shows PS ALM 500 seconds after boot*.
- *log shows PS ALM 1300 seconds after boot*.
- *log shows hardware failure on RF part*.

This root cause(s) could result in your incident through

- *carrier configuration issue*.

### response 6 (KG1): 
We identified incidents similar to yours:
- *Antenna port D not radiating*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *defective ADI power device regulator (N 29, port_B)*. &nbsp; (See {'TSG': ['[sentence1_104](#sentence1_104)']} for details.)

This root cause(s) may happen if

- *Antenna port B not radiating*.
- *internal PS alarm*.

 and/or 

- *log shows PS alarm*.
- *log shows PS ALM*.
- *log shows PS ALM 500 seconds after boot*.
- *log shows PS ALM 1300 seconds after boot*.

This root cause(s) could result in your incident through

- *carrier configuration issue*.
- *RU malfunction*.

### response 7 (KG1): 
We identified incidents similar to yours:
- *Antenna port D not radiating*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *software version v0212 with RF-B OBP issue*. &nbsp; (See {'TSG': ['[sentence1_95](#sentence1_95)']} for details.)

This root cause(s) may happen if

- *Antenna port B not radiating*.
- *internal PS alarm*.

 and/or 

- *log shows PS alarm*.
- *log shows PS ALM*.
- *log shows PS ALM 500 seconds after boot*.
- *log shows PS ALM 1300 seconds after boot*.

This root cause(s) could result in your incident through

- *carrier configuration issue*.

### response 8 (KG1): 
We identified incidents similar to yours:
- *Antenna port D not radiating*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *software version before v3112*. &nbsp; (See {'TSG': ['[sentence1_94](#sentence1_94)']} for details.)

This root cause(s) may happen if

- *Antenna port B not radiating*.
- *internal PS alarm*.

 and/or 

- *log shows PS alarm*.
- *log shows PS ALM*.
- *log shows PS ALM 500 seconds after boot*.
- *log shows PS ALM 1300 seconds after boot*.

This root cause(s) could result in your incident through

- *carrier configuration issue*.
- *software malfunction*.
- *power supply failure*.

### response 9 (KG1): 
We identified incidents similar to yours:
- *Antenna port D not radiating*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *software version v3111*. &nbsp; (See {'TSG': ['[sentence1_94](#sentence1_94)', '[sentence1_107](#sentence1_107)']} for details.)

This root cause(s) may happen if

- *Antenna port B not radiating*.
- *internal PS alarm*.

 and/or 

- *log shows PS alarm*.
- *log shows PS ALM*.
- *log shows PS ALM 500 seconds after boot*.
- *log shows PS ALM 1300 seconds after boot*.

This root cause(s) could result in your incident through

- *carrier configuration issue*.
- *low power mode transient condition*.

### response 10 (KG1): 
We identified incidents similar to yours:
- *Antenna port D not radiating*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *ADI known issue with switching regulator*. &nbsp; (See {'TSG': ['[sentence1_94](#sentence1_94)']} for details.)

This root cause(s) may happen if

- *Antenna port B not radiating*.
- *internal PS alarm*.

 and/or 

- *log shows PS alarm*.
- *log shows PS ALM*.
- *log shows PS ALM 500 seconds after boot*.
- *log shows PS ALM 1300 seconds after boot*.

This root cause(s) could result in your incident through

- *carrier configuration issue*.
- *non-functional switching regulator for n29 port C*.

### response 11 (KG1): 
We identified incidents similar to yours:
- *Antenna port D not radiating*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *outdated software version*. &nbsp; (See {'TSG': ['[sentence1_101](#sentence1_101)']} for details.)

This root cause(s) may happen if

- *Antenna port B not radiating*.
- *internal PS alarm*.

 and/or 

- *log shows PS alarm*.
- *log shows PS ALM*.
- *log shows PS ALM 500 seconds after boot*.
- *log shows PS ALM 1300 seconds after boot*.

This root cause(s) could result in your incident through

- *carrier configuration issue*.
- *software malfunction*.

### response 12 (KG1): 
We identified incidents similar to yours:
- *Antenna port D not radiating*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *carrier configuration push*. &nbsp; (See {'TSG': ['[sentence1_17](#sentence1_17)']} for details.)

This root cause(s) may happen if

- *Antenna port B not radiating*.
- *internal PS alarm*.

 and/or 

- *log shows PS alarm*.
- *log shows PS ALM*.
- *log shows PS ALM 500 seconds after boot*.
- *log shows PS ALM 1300 seconds after boot*.

This root cause(s) could result in your incident through

- *carrier configuration issue*.




# KG2 answer
## Information (KG2)
- Datetime (KG2): 2024-12-08 08:14:03.588005
- Processing time [s] (KG2): 7.0834760665893555
- input_token (KG2): 174
- output_token (KG2): 16
## Response (KG2)
### summary of root cause candidates (KG2)
- *power supply failure* [response 1] (KG2)
- *Firmware version 8303* [response 1] (KG2)
- *ClockClass set to 135* [response 2] (KG2)
- *software bug in version prior to v3009* [response 3] (KG2)
- *default non-forwardable MAC address setting* [response 4] (KG2)
- *switch port PTP profile defaulted to non-forwardable MAC address* [response 5] (KG2)
- *M-Plane not run in EB1* [response 5] (KG2)
- *physical connection problem between switch to RU* [response 6] (KG2)
- *EB2 SFP compatibility issue* [response 6] (KG2)
- *SW-Version, HW-Version & HW-Serial Number issues* [response 7] (KG2)
- *VLAN scan range set to 201-210 in build 0209* [response 8] (KG2)
- *manifest.xml path definition supports absolute path only* [response 9] (KG2)
- *2nd scan range setting 418-428* [response 10] (KG2)
- *VLAN scan logic error in pre-v3009 version* [response 11] (KG2)
- *Incorrect BIOS configuration on the SD cluster* [response 12] (KG2)
- *Radio reboots* [response 13] (KG2)
- *duplicated lines in DHCP message from DU software* [response 14] (KG2)

### response 1 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue, power supply failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *power supply failure*. &nbsp; (See {'TSG': ['[[sentence2_6](#sentence2_6)1](#[sentence2_6](#sentence2_6)1)', '[sentence2_94](#sentence2_94)', '[sentence2_12](#sentence2_12)', '[sentence2_3](#sentence2_3)', '[sentence2_7](#sentence2_7)']} for details.)
2. *Firmware version 8303*. &nbsp; (See {'TSG': ['[sentence2_41](#sentence2_41)', '[sentence2_49](#sentence2_49)', '[sentence2_6](#sentence2_6)']} for details.)

This root cause(s) may happen if

- *intermittent unlocking*.

 and/or 

- *log shows PTP status*.
- *log shows POWER ON RESET*.
- *log shows PTP is unlocked intermittently*.
- *log shows PS alarm*.

This root cause(s) could result in your incident through

- *inability to handle FH delay*.
- *PTP unlock*.
- *POWER ON RESET*.
- *RU reboots*.
- *sensitivity to FH delay*.

### response 2 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue, power supply failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

2. *ClockClass set to 135*. &nbsp; (See {'TSG': ['[sentence2_3](#sentence2_3)']} for details.)

This root cause(s) may happen if

- *intermittent unlocking*.

 and/or 

- *log shows PTP status*.
- *log shows POWER ON RESET*.
- *log shows PTP is unlocked intermittently*.
- *log shows change in ClockClass to 135*.
- *log shows PS alarm*.

This root cause(s) could result in your incident through

- *PTP unlock*.
- *POWER ON RESET*.
- *RU reboots*.

### response 3 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue, power supply failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

2. *software bug in version prior to v3009*. &nbsp; (See {'TSG': ['[sentence2_94](#sentence2_94)', '[sentence2_101](#sentence2_101)', '[sentence2_60](#sentence2_60)']} for details.)

This root cause(s) may happen if

- 

 and/or 

- *log shows POWER ON RESET*.
- *log shows PS alarm*.

This root cause(s) could result in your incident through

- *POWER ON RESET*.
- *RU reboots*.

### response 4 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue, power supply failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

2. *default non-forwardable MAC address setting*. &nbsp; (See {'TSG': ['[sentence2_9](#sentence2_9)']} for details.)

This root cause(s) may happen if

- 

 and/or 

- *log shows POWER ON RESET*.
- *log shows PTP packets not received*.
- *log shows Toolong*.
- *log shows PS alarm*.

This root cause(s) could result in your incident through

- *POWER ON RESET*.
- *RU reboots*.
- *PTP packets not forwarded to RU*.

### response 5 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue, power supply failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

2. *switch port PTP profile defaulted to non-forwardable MAC address*. &nbsp; (See {'TSG': ['[sentence2_4](#sentence2_4)', '[sentence2_9](#sentence2_9)', '[sentence2_7](#sentence2_7)']} for details.)
3. *M-Plane not run in EB1*. &nbsp; (See {'TSG': ['[sentence2_18](#sentence2_18)', '[[sentence2_4](#sentence2_4)0](#[sentence2_4](#sentence2_4)0)', '[sentence2_7](#sentence2_7)']} for details.)

This root cause(s) may happen if

- 

 and/or 

- *log shows POWER ON RESET*.
- *log shows PTP packets not received*.
- *log shows MAC address not learned*.
- *log shows Toolong*.
- *log shows PS alarm*.
- *log shows M-plane disable*.

This root cause(s) could result in your incident through

- *POWER ON RESET*.
- *RU reboots*.
- *PTP packets not forwarded to RU*.
- *RU stays waiting for PTP MAC*.
- *PTP packets not forwarded*.
- *syncE not getting locked*.

### response 6 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue, power supply failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

2. *physical connection problem between switch to RU*. &nbsp; (See {'TSG': ['[sentence2_83](#sentence2_83)', '[sentence2_0](#sentence2_0)', '[sentence2_71](#sentence2_71)']} for details.)
3. *EB2 SFP compatibility issue*. &nbsp; (See {'TSG': ['[sentence2_0](#sentence2_0)']} for details.)

This root cause(s) may happen if

- *SyncE not getting locked*.

 and/or 

- *log shows POWER ON RESET*.
- *log shows L1 down*.
- *log shows PTP packets not received*.
- *log shows Toolong*.
- *log shows PS alarm*.
- *log shows PTP is not locked*.

This root cause(s) could result in your incident through

- *POWER ON RESET*.
- *RU reboots*.
- *L1 was down*.
- *PTP not getting locked*.
- *PTP packets not forwarded to RU*.

### response 7 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue, power supply failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

3. *SW-Version, HW-Version & HW-Serial Number issues*. &nbsp; (See {'TSG': ['[sentence2_83](#sentence2_83)']} for details.)

This root cause(s) may happen if

- *SyncE not getting locked*.

 and/or 

- *log shows POWER ON RESET*.
- *log shows L1 down*.
- *log shows PTP packets not received*.
- *log shows Toolong*.
- *log shows PS alarm*.
- *log shows PTP is not locked*.

This root cause(s) could result in your incident through

- *POWER ON RESET*.
- *RU reboots*.
- *L1 was down*.
- *PTP not getting locked*.
- *PTP packets not forwarded to RU*.

### response 8 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue, power supply failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

2. *VLAN scan range set to 201-210 in build 0209*. &nbsp; (See {'TSG': ['[sentence2_66](#sentence2_66)']} for details.)

This root cause(s) may happen if

- *IP assignment is not stable*.

 and/or 

- *log shows POWER ON RESET*.
- *log shows PTP packets not received*.
- *log shows Toolong*.
- *log shows PS alarm*.
- *log shows failure to obtain IP via DHCP on M-Plane*.
- *log shows not stable*.
- *log shows CU-IP is not configured on RU*.
- *log shows PTP is not locked*.

This root cause(s) could result in your incident through

- *POWER ON RESET*.
- *RU reboots*.
- *PTP not getting locked*.
- *PTP packets not forwarded to RU*.
- *RU not accepting VLAN ID 452*.
- *RU fails to obtain IP*.

### response 9 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue, power supply failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

2. *manifest.xml path definition supports absolute path only*. &nbsp; (See {'TSG': ['[sentence2_65](#sentence2_65)']} for details.)

This root cause(s) may happen if

- *incorrect edit-config setting*.
- *IP assignment is not stable*.

 and/or 

- *log shows POWER ON RESET*.
- *log shows PTP packets not received*.
- *log shows Toolong*.
- *log shows PS alarm*.
- *log shows failure to obtain IP via DHCP on M-Plane*.
- *log shows incorrect path*.
- *log shows download failure*.
- *log shows not stable*.
- *log shows CU-IP is not configured on RU*.
- *log shows PTP is not locked*.

This root cause(s) could result in your incident through

- *POWER ON RESET*.
- *RU reboots*.
- *PTP not getting locked*.
- *PTP packets not forwarded to RU*.
- *relative path treated as absolute path*.
- *invalid path in manifest.xml*.
- *RU not accepting VLAN ID 452*.
- *RU fails to obtain IP*.
- *unsuccessful download process*.

### response 10 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue, power supply failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

2. *2nd scan range setting 418-428*. &nbsp; (See {'TSG': ['[sentence2_69](#sentence2_69)']} for details.)

This root cause(s) may happen if

- *IP assignment is not stable*.

 and/or 

- *log shows POWER ON RESET*.
- *log shows PTP packets not received*.
- *log shows Toolong*.
- *log shows PS alarm*.
- *log shows failure to obtain IP via DHCP on M-Plane*.
- *log shows download failure*.
- *log shows DHCP scan settings*.
- *log shows not stable*.
- *log shows CU-IP is not configured on RU*.
- *log shows PTP is not locked*.

This root cause(s) could result in your incident through

- *POWER ON RESET*.
- *RU reboots*.
- *PTP not getting locked*.
- *PTP packets not forwarded to RU*.
- *RU not accepting VLAN ID 452*.
- *RU fails to obtain IP*.
- *unsuccessful download process*.

### response 11 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue, power supply failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

2. *VLAN scan logic error in pre-v3009 version*. &nbsp; (See {'TSG': ['[sentence2_84](#sentence2_84)', '[sentence2_27](#sentence2_27)']} for details.)

This root cause(s) may happen if

- *IP assignment is not stable*.

 and/or 

- *log shows POWER ON RESET*.
- *log shows PTP packets not received*.
- *log shows Toolong*.
- *log shows PS alarm*.
- *log shows failure to obtain IP via DHCP on M-Plane*.
- *log shows not stable*.
- *log shows CU-IP is not configured on RU*.
- *log shows PTP is not locked*.

This root cause(s) could result in your incident through

- *POWER ON RESET*.
- *RU reboots*.
- *PTP not getting locked*.
- *PTP packets not forwarded to RU*.
- *RU fails to obtain IP*.

### response 12 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue, power supply failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

2. *Incorrect BIOS configuration on the SD cluster*. &nbsp; (See {'TSG': ['[sentence2_32](#sentence2_32)']} for details.)

This root cause(s) may happen if

- *IP assignment is not stable*.

 and/or 

- *log shows POWER ON RESET*.
- *log shows PTP packets not received*.
- *log shows Toolong*.
- *log shows PS alarm*.
- *log shows failure to obtain IP via DHCP on M-Plane*.
- *log shows supervision timeout*.
- *log shows not stable*.
- *log shows CU-IP is not configured on RU*.
- *log shows PTP is not locked*.

This root cause(s) could result in your incident through

- *POWER ON RESET*.
- *RU reboots*.
- *PTP not getting locked*.
- *PTP packets not forwarded to RU*.
- *watchdog reset timer not sent by DU*.
- *supervision timeout at the radio*.
- *RU fails to obtain IP*.
- *multiple auto reboots*.

### response 13 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *Radio reboots*. &nbsp; (See {'TSG': ['[sentence2_50](#sentence2_50)']} for details.)

This root cause(s) may happen if

- 

 and/or 

- *log shows netconf session not stable*.
- *log shows call home IP gets updated*.
- *log shows pcap*.
- *log shows logs at Management server*.

This root cause(s) could result in your incident through

- *RU reboots*.
- *Netconf session instability*.
- *call home IP update*.

### response 14 (KG2): 
We identified incidents similar to yours:
- *PS alarm issue*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *duplicated lines in DHCP message from DU software*. &nbsp; (See {'TSG': ['[sentence2_73](#sentence2_73)']} for details.)

This root cause(s) may happen if

- 

 and/or 

- *log shows netconf session not stable*.
- *log shows call home IP gets updated*.
- *log shows DHCP IP address not assigned*.
- *log shows pcap*.
- *log shows logs at Management server*.

This root cause(s) could result in your incident through

- *RU reboots*.
- *Netconf session instability*.
- *call home IP update*.
- *incorrect DHCP message processing*.




# References
## sentence0_88
(Deleted)

## sentence0_11
(Deleted)

## sentence0_104
(Deleted)

## sentence0_82
(Deleted)

## sentence0_14
(Deleted)

## sentence0_17
MOP 18: Antenna ports are not radiating

1.Description
On FCC-DB Antenna Ports B and D are not transmitting and an internal PS Alarm seen.
: SW-Version, HW-Version & HW-Serial Number: V2001, 00018.
Lab setup
E2E system
2. Observation
a) After reboot ,PS alarm was not observed. But when the carrier configuration is pushed from M-Plane to the RU, observed port B is not 
transmitting and Internal PS alarm was seen.
b) In previous issues related to PS alarm, After RU reboot Internal PS alarm used to be present, but this particular RU not showing any alarm after 
RU reboot.

3. Procedure/Step Involved
a) When sector is configured for 4x4 configuration(gain:46dBm/antenna), ports B and D were not transmitting. When sector is configured for 2x2 
configuration (gain:46dBm/antenna), Port B was not transmitting.
b) Observed low throughput, when RU diagnosed for above two configurations, ports B and D are faulty.
c) Logs provided for before and after carrier configuration push .
d) Checked the SW version previous and present version V2001.
e) According to the cmd_alllog, there are PS ALM 500~1300 seconds after boot. This issue is recoverable after a reboot, so it is not a HW issue. if 
Hardware issue, This ALM will happen immediately after boot.

4. Resolution
Issue is related to the ADI component. Plan B DB solves this problem.

## sentence1_82
(Deleted)

## sentence1_14
(Deleted)

## sentence1_107
(Deleted)

## sentence1_32
(Deleted)

## sentence1_39
(Deleted)

## sentence1_95
(Deleted)

## sentence1_12
(Deleted)

## sentence1_94
(Deleted)

## sentence1_17
MOP 18: Antenna ports are not radiating

1.Description
On FCC-DB Antenna Ports B and D are not transmitting and an internal PS Alarm seen.
: SW-Version, HW-Version & HW-Serial Number: V2001, 00018.
Lab setup
E2E system
2. Observation
a) After reboot ,PS alarm was not observed. But when the carrier configuration is pushed from M-Plane to the RU, observed port B is not 
transmitting and Internal PS alarm was seen.
b) In previous issues related to PS alarm, After RU reboot Internal PS alarm used to be present, but this particular RU not showing any alarm after 
RU reboot.

3. Procedure/Step Involved
a) When sector is configured for 4x4 configuration(gain:46dBm/antenna), ports B and D were not transmitting. When sector is configured for 2x2 
configuration (gain:46dBm/antenna), Port B was not transmitting.
b) Observed low throughput, when RU diagnosed for above two configurations, ports B and D are faulty.
c) Logs provided for before and after carrier configuration push .
d) Checked the SW version previous and present version V2001.
e) According to the cmd_alllog, there are PS ALM 500~1300 seconds after boot. This issue is recoverable after a reboot, so it is not a HW issue. if 
Hardware issue, This ALM will happen immediately after boot.

4. Resolution
Issue is related to the ADI component. Plan B DB solves this problem.

## sentence1_104
(Deleted)

## sentence1_101
(Deleted)

## sentence2_60
(Deleted)

## sentence2_49
(Deleted)

## sentence2_61
(Deleted)

## sentence2_4
(Deleted)

## sentence2_27
(Deleted)

## sentence2_73
(Deleted)

## sentence2_65
(Deleted)

## sentence2_101
(Deleted)

## sentence2_9
(Deleted)

## sentence2_6
(Deleted)

## sentence2_69
(Deleted)

## sentence2_7
(Deleted)

## sentence2_32
(Deleted)

## sentence2_41
(Deleted)

## sentence2_12
(Deleted)

## sentence2_18
(Deleted)

## sentence2_3
(Deleted)

## sentence2_84
(Deleted)

## sentence2_83
(Deleted)

## sentence2_50
(Deleted)

## sentence2_0
(Deleted)

## sentence2_40
(Deleted)

## sentence2_94
(Deleted)

## sentence2_66
(Deleted)
