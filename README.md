# sunsaver_mppt_modbus
**sunsaver_log.py** - download the 32 days logged data from Morningstar MPPT Sunsaver charge controller thru TCP/IP Modbus protocol

Command syntax:  python sunsaver_log.py “ip address” >> "xxxx_powerhealth_ddmmyy.log"
"xxxx" any 4 character name, "ddmmyy" date format (usually current date)

Sample output:
hourmeter, alarm_daily, Vb_min_daily, Vb_max_daily, Ahc_daily, Ahl_daily, Array_Fault, Load_Fault, Va_max_daily, absortion_time(hr), eq(hr), float(hr)
9227,RTS OPEN,13.226318359375,14.24560546875,15.3,13.600000000000001,Battery HVD (High Voltage Disconnect),no faults,36.8438720703125,0.6333333333333333,0.0,0.0
9251,RTS OPEN,13.2354736328125,14.2425537109375,14.8,13.600000000000001,Battery HVD (High Voltage Disconnect),no faults,37.921142578125,0.31666666666666665,0.0,0.0
9274,RTS OPEN,13.2354736328125,14.2425537109375,13.9,13.700000000000001,Battery HVD (High Voltage Disconnect),no faults,37.3809814453125,0.23333333333333334,0.0,0.0


**add_timestamp.py** - add time stamp to the downloaded logged data and save to a csv file

Sample output:

Time,hourmeter, alarm_daily, Vb_min_daily, Vb_max_daily,Ahc_daily, Ahl_daily, Array_Fault, Load_Fault, Va_max_daily, absortion_time(hr), eq(hr), float(hr)
2023-08-14,23281,RTS OPEN,13.2537841796875,14.0045166015625,8.4,1.5,Battery HVD (High Voltage Disconnect),no faults,34.9853515625,0.65,0.0,0.0
2023-08-15,23305,RTS OPEN,13.2568359375,14.0228271484375,8.0,1.6,Battery HVD (High Voltage Disconnect),no faults,34.796142578125,1.0,0.0,0.0
2023-08-16,23329,RTS OPEN,13.2537841796875,13.983154296875,7.4,1.2000000000000002,Battery HVD (High Voltage Disconnect),no faults,34.8846435546875,0.8,0.0,0.0








