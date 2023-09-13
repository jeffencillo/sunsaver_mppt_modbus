# sunsaver_mppt_modbus

This is a python script that download the 32 days logged data from Morningstar MPPT Sunsaver charge controller thru TCP/IP Modbus protocol.

Command syntax:  python sunsaver_log.py “ip address”

Sample output:

hourmeter, alarm_daily, Vb_min_daily, Vb_max_daily, Ahc_daily, Ahl_daily, Array_Fault, Load_Fault, Va_max_daily, absortion_time(hr), eq(hr), float(hr)
9227,RTS OPEN,13.226318359375,14.24560546875,15.3,13.600000000000001,Battery HVD (High Voltage Disconnect),no faults,36.8438720703125,0.6333333333333333,0.0,0.0
9251,RTS OPEN,13.2354736328125,14.2425537109375,14.8,13.600000000000001,Battery HVD (High Voltage Disconnect),no faults,37.921142578125,0.31666666666666665,0.0,0.0
9274,RTS OPEN,13.2354736328125,14.2425537109375,13.9,13.700000000000001,Battery HVD (High Voltage Disconnect),no faults,37.3809814453125,0.23333333333333334,0.0,0.0
9298,RTS OPEN,13.232421875,14.215087890625,16.0,13.600000000000001,Battery HVD (High Voltage Disconnect),no faults,35.8734130859375,0.0,0.0,0.0
9322,RTS OPEN,13.2354736328125,14.22119140625,14.8,13.4,Battery HVD (High Voltage Disconnect),no faults,36.1724853515625,0.0,0.0,0.0
9346,RTS OPEN,13.2354736328125,14.2425537109375,14.700000000000001,13.600000000000001,Battery HVD (High Voltage Disconnect),no faults,37.615966796875,0.3,0.0,0.0
9370,RTS OPEN,13.2354736328125,14.208984375,14.8,13.700000000000001,Battery HVD (High Voltage Disconnect),no faults,36.3250732421875,0.0,0.0,0.0
9394,RTS OPEN,13.232421875,14.24560546875,14.5,13.600000000000001,Battery HVD (High Voltage Disconnect),no faults,36.627197265625,0.7,0.0,0.0
9418,RTS OPEN,13.238525390625,14.24560546875,14.4,13.600000000000001,Battery HVD (High Voltage Disconnect),no faults,37.445068359375,0.7333333333333333,0.0,0.0
9442,RTS OPEN,13.24462890625,14.24560546875,14.700000000000001,13.600000000000001,Battery HVD (High Voltage Disconnect),no faults,37.274169921875,0.5,0.0,0.0
