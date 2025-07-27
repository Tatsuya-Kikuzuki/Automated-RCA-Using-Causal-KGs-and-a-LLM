CRC (Cyclic Redundancy Check) fails.

# RAG answer
## Information (RAG)
- Datetime (RAG): 2025-07-27 21:39:30.953567
- Processing time [s] (RAG): 81.48153948783875
- input_token (RAG): 1426
- output_token (RAG): 464
## Response (RAG)
### response 1 (RAG)
- ref 1 (RAG): [sentence0_8](#sentence0_8)
- response 1 (RAG): CRC (Cyclic Redundancy Check) has failed during 256 QAM test. It was caused by the RF power fluctuation and Constellation fluctuation inside RU. RF power seems fluctuating and is unstable with all bandwidths and modulations. RF power fluctuation Issue is not seen after replacing this RU. Observed issue with the old RU. Environment and carrier configuration including cable connections and attenuators is exactly the same for both old RU and new RU. Observed that this is a HW issue and the amplifier is damaged on this unit. To resolve it, replace the RU as the amplifier is damaged. 
### response 2 (RAG)
- ref 2 (RAG): [sentence0_7](#sentence0_7)
- response 2 (RAG): Interference from neighbouring cells was greater than expected. We observed RF power fluctuating with the RU. We ran Downlink test case 64QAM where we are able to see good constellation, But after some time when we retest again, we started observing poor constellation and RF power fluctuating. We asked Vendor C and their investigation found that it was not calibrated yet with new power supply used in the field. They recalibrated it and Interference power mitigated as usual. To resolve it, recalibrate the RU with the new power supply used in the field. 
### response 3 (RAG)
- ref 3 (RAG): [sentence0_9](#sentence0_9)
- response 3 (RAG): UE attach failed after configuring the radio. After Post successful PDU (Protocol Data Unit) establishment, Downlink data stops within seconds and UE doesn't see the cell any more when the carrier is brought up via M-Plane. Log analysis: User plane packet is not coming after UE attached. RU receives U-plane packet but it is unstable. When using command rrh-power, when the UE can not see the cell, the RF power is fluctuating. We confirmed that RF power fluctuation has occurred inside the RU because DPD (digital predistortion) is turned on. For now, the DPD setting was switched off and the problem was solved as UE does not fail to see the cell. The performance of the DPD needs to be re-examined. To resolve it, switch off the DPD setting and re-examine its performance. 


# KG answer
## Information (KG)
- Datetime (KG): 2025-07-27 21:40:33.721214
- Processing time [s] (KG): 62.765130281448364
- input_token (KG): 176
- output_token (KG): 19
## Response (KG)
### summary of root cause candidates (KG)
- *old RU causing RF power fluctuation* [response 1] (KG)
- *damaged amplifier in new RU* [response 1] (KG)
- *DPD activation* [response 2] (KG)
- *lack of calibration with new power supply* [response 3] (KG)
- *v356 software version* [response 4] (KG)
- *v1 SFP module* [response 4] (KG)
- *v356 software conflict between FQDN and DHCP* [response 4] (KG)
- *absence of exclusive control of PTP control* [response 5] (KG)
- *increase in throughput* [response 6] (KG)
- *increase in UE connections* [response 7] (KG)
- *PTP threshold set to 80ns in v201 software* [response 8] (KG)
- *compatibility issue* [response 9] (KG)

### response 1 (KG): 
We identified incidents similar to yours:
- *CRC failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *old RU causing RF power fluctuation*. &nbsp; (See {'TSG': ['[sentence1_8](#sentence1_8)']} for details.)
2. *damaged amplifier in new RU*. &nbsp; (See {'TSG': ['[sentence1_8](#sentence1_8)']} for details.)

This root cause(s) may happen if

- *RF power fluctuation*.
- *Constellation fluctuation*.

 and/or 

- *log shows power fluctuation*.
- *log shows power instability*.
- *log shows RF power fluctuation*.
- *log shows RF power fluctuating*.

This root cause(s) could result in your incident through

- *unstable RF power*.

### response 2 (KG): 
We identified incidents similar to yours:
- *CRC failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *DPD activation*. &nbsp; (See {'TSG': ['[sentence1_9](#sentence1_9)']} for details.)

This root cause(s) may happen if

- *RF power fluctuation*.
- *Constellation fluctuation*.

 and/or 

- *log shows power fluctuation*.
- *log shows power instability*.
- *log shows RF power fluctuation*.
- *log shows RF power fluctuating*.

This root cause(s) could result in your incident through

- *unstable RF power*.

### response 3 (KG): 
We identified incidents similar to yours:
- *CRC failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *lack of calibration with new power supply*. &nbsp; (See {'TSG': ['[sentence1_7](#sentence1_7)']} for details.)

This root cause(s) may happen if

- *RF power fluctuation*.
- *Constellation fluctuation*.

 and/or 

- *log shows power fluctuation*.
- *log shows power instability*.
- *log shows RF power fluctuation*.
- *log shows RF power fluctuating*.

This root cause(s) could result in your incident through

- *unstable RF power*.

### response 4 (KG): 
We identified incidents similar to yours:
- *software failure, DU failure to transmit data*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *v356 software version*. &nbsp; (See {'TSG': ['[sentence1_3](#sentence1_3)']} for details.)
2. *v1 SFP module*. &nbsp; (See {'TSG': ['[sentence1_4](#sentence1_4)']} for details.)
3. *v356 software conflict between FQDN and DHCP*. &nbsp; (See {'TSG': ['[sentence1_3](#sentence1_3)']} for details.)

This root cause(s) may happen if

- *PTP unlocked*.
- *SyncE unlocked*.
- *CU-IP not assigned*.
- *partial FQDN functionality development*.

 and/or 

- *log shows L1 was down*.
- *log shows 5gdulls logs*.
- *log shows PTP unlocked*.
- *log shows unlocked PTP*.
- *log shows Software-Failure*.
- *log shows unlocked state*.

This root cause(s) could result in your incident through

- *L1 down*.
- *RU could not catch the DHCP IP address correctly*.

### response 5 (KG): 
We identified incidents similar to yours:
- *software failure, DU failure to transmit data*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *absence of exclusive control of PTP control*. &nbsp; (See {'TSG': ['[sentence1_6](#sentence1_6)']} for details.)

This root cause(s) may happen if

- *PTP unlocked*.
- *SyncE unlocked*.
- *CU-IP not assigned*.
- *partial FQDN functionality development*.

 and/or 

- *log shows L1 was down*.
- *log shows 5gdulls logs*.
- *log shows PTP unlocked*.
- *log shows unlocked PTP*.
- *log shows Software-Failure*.
- *log shows unlocked state*.

This root cause(s) could result in your incident through

- *L1 down*.
- *memory overload*.
- *PTP control program error state*.
- *RU could not catch the DHCP IP address correctly*.

### response 6 (KG): 
We identified incidents similar to yours:
- *software failure, DU failure to transmit data*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *increase in throughput*. &nbsp; (See {'TSG': ['[sentence1_6](#sentence1_6)']} for details.)

This root cause(s) may happen if

- *PTP unlocked*.
- *SyncE unlocked*.
- *CU-IP not assigned*.
- *partial FQDN functionality development*.

 and/or 

- *log shows L1 was down*.
- *log shows 5gdulls logs*.
- *log shows PTP unlocked*.
- *log shows unlocked PTP*.
- *log shows Software-Failure*.
- *log shows unlocked state*.

This root cause(s) could result in your incident through

- *L1 down*.
- *memory overload*.
- *PTP control program error state*.
- *RU could not catch the DHCP IP address correctly*.

### response 7 (KG): 
We identified incidents similar to yours:
- *software failure, DU failure to transmit data*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *increase in UE connections*. &nbsp; (See {'TSG': ['[sentence1_6](#sentence1_6)']} for details.)

This root cause(s) may happen if

- *PTP unlocked*.
- *SyncE unlocked*.
- *CU-IP not assigned*.
- *partial FQDN functionality development*.

 and/or 

- *log shows L1 was down*.
- *log shows 5gdulls logs*.
- *log shows PTP unlocked*.
- *log shows unlocked PTP*.
- *log shows Software-Failure*.
- *log shows unlocked state*.

This root cause(s) could result in your incident through

- *L1 down*.
- *memory overload*.
- *PTP control program error state*.
- *RU could not catch the DHCP IP address correctly*.

### response 8 (KG): 
We identified incidents similar to yours:
- *software failure, DU failure to transmit data*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *PTP threshold set to 80ns in v201 software*. &nbsp; (See {'TSG': ['[sentence1_5](#sentence1_5)']} for details.)

This root cause(s) may happen if

- *PTP unlocked*.
- *SyncE unlocked*.
- *CU-IP not assigned*.
- *partial FQDN functionality development*.

 and/or 

- *log shows L1 was down*.
- *log shows 5gdulls logs*.
- *log shows PTP unlocked*.
- *log shows unlocked PTP*.
- *log shows Software-Failure*.
- *log shows unlocked state*.

This root cause(s) could result in your incident through

- *L1 down*.
- *RU could not catch the DHCP IP address correctly*.
- *PTP accuracy below threshold*.

### response 9 (KG): 
We identified incidents similar to yours:
- *software failure, DU failure to transmit data*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *compatibility issue*. &nbsp; (See {'TSG': ['[sentence1_4](#sentence1_4)']} for details.)

This root cause(s) may happen if

- *PTP unlocked*.
- *SyncE unlocked*.
- *CU-IP not assigned*.
- *partial FQDN functionality development*.

 and/or 

- *log shows L1 was down*.
- *log shows 5gdulls logs*.
- *log shows PTP unlocked*.
- *log shows unlocked PTP*.
- *log shows Software-Failure*.
- *log shows unlocked state*.

This root cause(s) could result in your incident through

- *L1 down*.
- *RU could not catch the DHCP IP address correctly*.




# References
## sentence0_7
Interference from neighbouring cells was greater than expected.

We observed RF power fluctuating with the RU.
We ran Downlink test case 64QAM where we are able to see good constellation, But after some time when we retest again, we started observing poor constellation and RF power fluctuating.

We asked Vendor C and their investigation found that it was not calibrated yet with new power supply used in the field.
They recalibrated it and Interference power mitigated as usual.
## sentence0_9
UE attach failed after configuring the radio.

After Post successful PDU (Protocol Data Unit) establishment, Downlink data stops within seconds and UE doesn't see the cell any more when the carrier is brought up via M-Plane.

Log analysis: User plane packet is not coming after UE attached.RU receives U-plane packet but it is unstable.
When using command rrh-power, when the UE can not see the cell, the RF power is fluctuating.

We confirmed that RF power fluctuation has occurred inside the RU because DPD (digital predistortion) is turned on.

For now, the DPD setting was switched off and the problem was solved as UE does not fail to see the cell. The performance of the DPD needs to be re-examined.
## sentence0_8
CRC (Cyclic Redundancy Check) has failed during 256 QAM test.
It was caused by the RF power fluctuation and Constellation fluctuation inside RU.

RF power seems fluctuating and is unstable with all bandwidths and modulations.

RF power fluctuation Issue is not seen after replacing this RU. Observed issue with the old RU.
Environment and carrier configuration including cable connections and attenuators is exactly the same for both old RU and new RU. Observed that this is a HW issue and the amplifier is damaged on this unit.
## sentence1_4
No Data was transmitted from DU.
It was observed that PTP and SyncE getting unlocked and those caused the incident.

According to 5gdulls logs, L1 was down. Need to check connection from DU to RU.

After replacing the v1 SFP with v2 SFP, PTP and SyncE got locked state successfully.
Here problem was not SFP itself, but it should be compatibility issue.
## sentence1_9
UE attach failed after configuring the radio.

After Post successful PDU (Protocol Data Unit) establishment, Downlink data stops within seconds and UE doesn't see the cell any more when the carrier is brought up via M-Plane.

Log analysis: User plane packet is not coming after UE attached.RU receives U-plane packet but it is unstable.
When using command rrh-power, when the UE can not see the cell, the RF power is fluctuating.

We confirmed that RF power fluctuation has occurred inside the RU because DPD (digital predistortion) is turned on.

For now, the DPD setting was switched off and the problem was solved as UE does not fail to see the cell. The performance of the DPD needs to be re-examined.
## sentence1_6
During the connection test, the DU stopped sending packets.
It was found that the PTP got unlocked.

When the number of UE connections or throughput increased, the process to handle those caused a memory overload and the PTP control program was in an error state. This caused issues.

The problem was addressed by implementing exlusive control of PTP control and data processing.
## sentence1_8
CRC (Cyclic Redundancy Check) has failed during 256 QAM test.
It was caused by the RF power fluctuation and Constellation fluctuation inside RU.

RF power seems fluctuating and is unstable with all bandwidths and modulations.

RF power fluctuation Issue is not seen after replacing this RU. Observed issue with the old RU.
Environment and carrier configuration including cable connections and attenuators is exactly the same for both old RU and new RU. Observed that this is a HW issue and the amplifier is damaged on this unit.
## sentence1_3
CU-IP was not getting assigned in RU with v356 software.
We observed PTP too was getting unlocked with v356 build.

5gdulls log shows "Software-Failure", which incicates the fact that RU could not catch the DHCP IP address correctly by the stacking of the software. In the v356 software, functionality of FQDN is developed partially and it conflicts with the DHCP function. It affects the PTP unlocked issue as well.

Issue has been fixed with software v359, Now CU-IP getting configured on RU and PTP unlocked issue cleared.

## sentence1_7
Interference from neighbouring cells was greater than expected.

We observed RF power fluctuating with the RU.
We ran Downlink test case 64QAM where we are able to see good constellation, But after some time when we retest again, we started observing poor constellation and RF power fluctuating.

We asked Vendor C and their investigation found that it was not calibrated yet with new power supply used in the field.
They recalibrated it and Interference power mitigated as usual.
## sentence1_5
The DU failed to transmit data because PTP got unlocked.

We tried rebooting RU. Once RU is up, PTP gets locked and in 4 to 5 minutes goes unlocked state again, then no data is obserbed from DU.

Checked PTP accuracy and found that the PTP threshold for v201 software (±80 nsec) was too low, resulting in an unlocked state.
The issue was no longer observed after threshold of PTP accuracy was changed from 80ns to 1420ns in v206.

CRC (Cyclic Redundancy Check) fails.

# RAG answer
## Information (RAG)
- Datetime (RAG): 2025-07-27 22:04:38.736672
- Processing time [s] (RAG): 80.70869207382202
- input_token (RAG): 1426
- output_token (RAG): 186
## Response (RAG)
### response 1 (RAG)
- ref 1 (RAG): [sentence0_8](#sentence0_8)
- response 1 (RAG): CRC (Cyclic Redundancy Check) has failed during 256 QAM test. It was caused by the RF power fluctuation and Constellation fluctuation inside RU. To resolve it, replacing the RU resolved the issue as the amplifier was damaged on the old unit. 
### response 2 (RAG)
- ref 2 (RAG): [sentence0_7](#sentence0_7)
- response 2 (RAG): Interference from neighbouring cells was greater than expected, and RF power fluctuating was observed. To resolve it, recalibration with the new power supply mitigated the interference power. 
### response 3 (RAG)
- ref 3 (RAG): [sentence0_9](#sentence0_9)
- response 3 (RAG): UE attach failed after configuring the radio, and RF power fluctuation occurred inside the RU because DPD (digital predistortion) is turned on. To resolve it, switching off the DPD setting solved the problem. 


# KG answer
## Information (KG)
- Datetime (KG): 2025-07-27 22:05:44.207860
- Processing time [s] (KG): 65.46818232536316
- input_token (KG): 176
- output_token (KG): 19
## Response (KG)
### summary of root cause candidates (KG)
- *old RU causing RF power fluctuation* [response 1] (KG)
- *damaged amplifier in new RU* [response 1] (KG)
- *DPD activation* [response 2] (KG)
- *lack of calibration with new power supply* [response 3] (KG)
- *v356 software version* [response 4] (KG)
- *v1 SFP module* [response 4] (KG)
- *v356 software conflict between FQDN and DHCP* [response 4] (KG)
- *absence of exclusive control of PTP control* [response 5] (KG)
- *increase in throughput* [response 6] (KG)
- *increase in UE connections* [response 7] (KG)
- *PTP threshold set to 80ns in v201 software* [response 8] (KG)
- *compatibility issue* [response 9] (KG)

### response 1 (KG): 
We identified incidents similar to yours:
- *CRC failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *old RU causing RF power fluctuation*. &nbsp; (See {'TSG': ['[sentence1_8](#sentence1_8)']} for details.)
2. *damaged amplifier in new RU*. &nbsp; (See {'TSG': ['[sentence1_8](#sentence1_8)']} for details.)

This root cause(s) may happen if

- *RF power fluctuation*.
- *Constellation fluctuation*.

 and/or 

- *log shows power fluctuation*.
- *log shows power instability*.
- *log shows RF power fluctuation*.
- *log shows RF power fluctuating*.

This root cause(s) could result in your incident through

- *unstable RF power*.

### response 2 (KG): 
We identified incidents similar to yours:
- *CRC failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *DPD activation*. &nbsp; (See {'TSG': ['[sentence1_9](#sentence1_9)']} for details.)

This root cause(s) may happen if

- *RF power fluctuation*.
- *Constellation fluctuation*.

 and/or 

- *log shows power fluctuation*.
- *log shows power instability*.
- *log shows RF power fluctuation*.
- *log shows RF power fluctuating*.

This root cause(s) could result in your incident through

- *unstable RF power*.

### response 3 (KG): 
We identified incidents similar to yours:
- *CRC failure*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *lack of calibration with new power supply*. &nbsp; (See {'TSG': ['[sentence1_7](#sentence1_7)']} for details.)

This root cause(s) may happen if

- *RF power fluctuation*.
- *Constellation fluctuation*.

 and/or 

- *log shows power fluctuation*.
- *log shows power instability*.
- *log shows RF power fluctuation*.
- *log shows RF power fluctuating*.

This root cause(s) could result in your incident through

- *unstable RF power*.

### response 4 (KG): 
We identified incidents similar to yours:
- *software failure, DU failure to transmit data*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *v356 software version*. &nbsp; (See {'TSG': ['[sentence1_3](#sentence1_3)']} for details.)
2. *v1 SFP module*. &nbsp; (See {'TSG': ['[sentence1_4](#sentence1_4)']} for details.)
3. *v356 software conflict between FQDN and DHCP*. &nbsp; (See {'TSG': ['[sentence1_3](#sentence1_3)']} for details.)

This root cause(s) may happen if

- *PTP unlocked*.
- *SyncE unlocked*.
- *CU-IP not assigned*.
- *partial FQDN functionality development*.

 and/or 

- *log shows L1 was down*.
- *log shows 5gdulls logs*.
- *log shows PTP unlocked*.
- *log shows unlocked PTP*.
- *log shows Software-Failure*.
- *log shows unlocked state*.

This root cause(s) could result in your incident through

- *L1 down*.
- *RU could not catch the DHCP IP address correctly*.

### response 5 (KG): 
We identified incidents similar to yours:
- *software failure, DU failure to transmit data*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *absence of exclusive control of PTP control*. &nbsp; (See {'TSG': ['[sentence1_6](#sentence1_6)']} for details.)

This root cause(s) may happen if

- *PTP unlocked*.
- *SyncE unlocked*.
- *CU-IP not assigned*.
- *partial FQDN functionality development*.

 and/or 

- *log shows L1 was down*.
- *log shows 5gdulls logs*.
- *log shows PTP unlocked*.
- *log shows unlocked PTP*.
- *log shows Software-Failure*.
- *log shows unlocked state*.

This root cause(s) could result in your incident through

- *L1 down*.
- *memory overload*.
- *PTP control program error state*.
- *RU could not catch the DHCP IP address correctly*.

### response 6 (KG): 
We identified incidents similar to yours:
- *software failure, DU failure to transmit data*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *increase in throughput*. &nbsp; (See {'TSG': ['[sentence1_6](#sentence1_6)']} for details.)

This root cause(s) may happen if

- *PTP unlocked*.
- *SyncE unlocked*.
- *CU-IP not assigned*.
- *partial FQDN functionality development*.

 and/or 

- *log shows L1 was down*.
- *log shows 5gdulls logs*.
- *log shows PTP unlocked*.
- *log shows unlocked PTP*.
- *log shows Software-Failure*.
- *log shows unlocked state*.

This root cause(s) could result in your incident through

- *L1 down*.
- *memory overload*.
- *PTP control program error state*.
- *RU could not catch the DHCP IP address correctly*.

### response 7 (KG): 
We identified incidents similar to yours:
- *software failure, DU failure to transmit data*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *increase in UE connections*. &nbsp; (See {'TSG': ['[sentence1_6](#sentence1_6)']} for details.)

This root cause(s) may happen if

- *PTP unlocked*.
- *SyncE unlocked*.
- *CU-IP not assigned*.
- *partial FQDN functionality development*.

 and/or 

- *log shows L1 was down*.
- *log shows 5gdulls logs*.
- *log shows PTP unlocked*.
- *log shows unlocked PTP*.
- *log shows Software-Failure*.
- *log shows unlocked state*.

This root cause(s) could result in your incident through

- *L1 down*.
- *memory overload*.
- *PTP control program error state*.
- *RU could not catch the DHCP IP address correctly*.

### response 8 (KG): 
We identified incidents similar to yours:
- *software failure, DU failure to transmit data*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *PTP threshold set to 80ns in v201 software*. &nbsp; (See {'TSG': ['[sentence1_5](#sentence1_5)']} for details.)

This root cause(s) may happen if

- *PTP unlocked*.
- *SyncE unlocked*.
- *CU-IP not assigned*.
- *partial FQDN functionality development*.

 and/or 

- *log shows L1 was down*.
- *log shows 5gdulls logs*.
- *log shows PTP unlocked*.
- *log shows unlocked PTP*.
- *log shows Software-Failure*.
- *log shows unlocked state*.

This root cause(s) could result in your incident through

- *L1 down*.
- *RU could not catch the DHCP IP address correctly*.
- *PTP accuracy below threshold*.

### response 9 (KG): 
We identified incidents similar to yours:
- *software failure, DU failure to transmit data*

Based on the root cause analysis from this incident, we have the following findings:


Root cause(s):

1. *compatibility issue*. &nbsp; (See {'TSG': ['[sentence1_4](#sentence1_4)']} for details.)

This root cause(s) may happen if

- *PTP unlocked*.
- *SyncE unlocked*.
- *CU-IP not assigned*.
- *partial FQDN functionality development*.

 and/or 

- *log shows L1 was down*.
- *log shows 5gdulls logs*.
- *log shows PTP unlocked*.
- *log shows unlocked PTP*.
- *log shows Software-Failure*.
- *log shows unlocked state*.

This root cause(s) could result in your incident through

- *L1 down*.
- *RU could not catch the DHCP IP address correctly*.




# References
## sentence0_7
Interference from neighbouring cells was greater than expected.

We observed RF power fluctuating with the RU.
We ran Downlink test case 64QAM where we are able to see good constellation, But after some time when we retest again, we started observing poor constellation and RF power fluctuating.

We asked Vendor C and their investigation found that it was not calibrated yet with new power supply used in the field.
They recalibrated it and Interference power mitigated as usual.
## sentence0_9
UE attach failed after configuring the radio.

After Post successful PDU (Protocol Data Unit) establishment, Downlink data stops within seconds and UE doesn't see the cell any more when the carrier is brought up via M-Plane.

Log analysis: User plane packet is not coming after UE attached.RU receives U-plane packet but it is unstable.
When using command rrh-power, when the UE can not see the cell, the RF power is fluctuating.

We confirmed that RF power fluctuation has occurred inside the RU because DPD (digital predistortion) is turned on.

For now, the DPD setting was switched off and the problem was solved as UE does not fail to see the cell. The performance of the DPD needs to be re-examined.
## sentence0_8
CRC (Cyclic Redundancy Check) has failed during 256 QAM test.
It was caused by the RF power fluctuation and Constellation fluctuation inside RU.

RF power seems fluctuating and is unstable with all bandwidths and modulations.

RF power fluctuation Issue is not seen after replacing this RU. Observed issue with the old RU.
Environment and carrier configuration including cable connections and attenuators is exactly the same for both old RU and new RU. Observed that this is a HW issue and the amplifier is damaged on this unit.
## sentence1_4
No Data was transmitted from DU.
It was observed that PTP and SyncE getting unlocked and those caused the incident.

According to 5gdulls logs, L1 was down. Need to check connection from DU to RU.

After replacing the v1 SFP with v2 SFP, PTP and SyncE got locked state successfully.
Here problem was not SFP itself, but it should be compatibility issue.
## sentence1_9
UE attach failed after configuring the radio.

After Post successful PDU (Protocol Data Unit) establishment, Downlink data stops within seconds and UE doesn't see the cell any more when the carrier is brought up via M-Plane.

Log analysis: User plane packet is not coming after UE attached.RU receives U-plane packet but it is unstable.
When using command rrh-power, when the UE can not see the cell, the RF power is fluctuating.

We confirmed that RF power fluctuation has occurred inside the RU because DPD (digital predistortion) is turned on.

For now, the DPD setting was switched off and the problem was solved as UE does not fail to see the cell. The performance of the DPD needs to be re-examined.
## sentence1_6
During the connection test, the DU stopped sending packets.
It was found that the PTP got unlocked.

When the number of UE connections or throughput increased, the process to handle those caused a memory overload and the PTP control program was in an error state. This caused issues.

The problem was addressed by implementing exlusive control of PTP control and data processing.
## sentence1_8
CRC (Cyclic Redundancy Check) has failed during 256 QAM test.
It was caused by the RF power fluctuation and Constellation fluctuation inside RU.

RF power seems fluctuating and is unstable with all bandwidths and modulations.

RF power fluctuation Issue is not seen after replacing this RU. Observed issue with the old RU.
Environment and carrier configuration including cable connections and attenuators is exactly the same for both old RU and new RU. Observed that this is a HW issue and the amplifier is damaged on this unit.
## sentence1_3
CU-IP was not getting assigned in RU with v356 software.
We observed PTP too was getting unlocked with v356 build.

5gdulls log shows "Software-Failure", which incicates the fact that RU could not catch the DHCP IP address correctly by the stacking of the software. In the v356 software, functionality of FQDN is developed partially and it conflicts with the DHCP function. It affects the PTP unlocked issue as well.

Issue has been fixed with software v359, Now CU-IP getting configured on RU and PTP unlocked issue cleared.

## sentence1_7
Interference from neighbouring cells was greater than expected.

We observed RF power fluctuating with the RU.
We ran Downlink test case 64QAM where we are able to see good constellation, But after some time when we retest again, we started observing poor constellation and RF power fluctuating.

We asked Vendor C and their investigation found that it was not calibrated yet with new power supply used in the field.
They recalibrated it and Interference power mitigated as usual.
## sentence1_5
The DU failed to transmit data because PTP got unlocked.

We tried rebooting RU. Once RU is up, PTP gets locked and in 4 to 5 minutes goes unlocked state again, then no data is obserbed from DU.

Checked PTP accuracy and found that the PTP threshold for v201 software (±80 nsec) was too low, resulting in an unlocked state.
The issue was no longer observed after threshold of PTP accuracy was changed from 80ns to 1420ns in v206.

