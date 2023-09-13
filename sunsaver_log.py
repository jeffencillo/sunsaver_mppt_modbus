#!/usr/bin/python3
from pyModbusTCP.client import ModbusClient
import time
import numpy as np
import struct
import sys


from ast import literal_eval 

def main():
	ip = sys.argv[1]


SERVER_HOST = sys.argv[1]
SERVER_PORT = 502

c = ModbusClient()

c.host(SERVER_HOST)
c.port(SERVER_PORT)

while True:
# open or reconnect TCP to server
	if not c.is_open():
		if not c.open():
			print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

    # if open() is ok, read register (modbus function 0x03)
	if c.is_open():
		print ("hourmeter, alarm_daily, Vb_min_daily, Vb_max_daily, Ahc_daily, Ahl_daily, Array_Fault, Load_Fault, Va_max_daily, absortion_time(hr), eq(hr), float(hr)")
		varhex = "0x8000"
		for i in range(0,31):
			i = int(varhex, 16)
			regs = c.read_input_registers(i,17)
#			print (regs)
			#print ("POWER HEALTH INFORMATION")
			#print (hex(i))
			hourmeter = regs[0] + ((regs[1] & 0x00FF) << 16)
			print (hourmeter, end=",")
			
			#print ("Today's self-diagnostic alarm:", end="")
			alarm = (regs[2] << 8) + (regs[1] >> 8)
			if alarm == 0:
				print ("No alarms", end=",")
			elif (alarm & 1):
				print ("RTS OPEN", end=",")
			elif ((alarm & (1 << 1)) >> 1):
				print("RTS shorted", end=",") 
			elif ((alarm & (1 << 2)) >> 2):
				print("RTS Disconnected", end=",")
			elif ((alarm & (1 << 3)) >> 3):
				print("Ths (heatsink temp sensor) Open", end=",")
			elif ((alarm & (1 << 4)) >> 4):
				print("Ths (heatsink temp sensor)Sorted", end=",")
			elif ((alarm & (1 << 5)) >> 5):
				print("Heatsink Hot (active temp limiting)", end=",")
			elif ((alarm & (1 << 6)) >> 6):
				print("Tind (inductor temp sensor) Open", end=",")
			elif ((alarm & (1 << 7)) >> 7):
				print("Tind (inductor temp sensor) Short", end=",")
			elif ((alarm & (1 << 8)) >> 8):
				print("Tind Hot (active temp limiting)", end=",")
			elif ((alarm & (1 << 9)) >> 9):
				print("Current Limit", end=",")
			elif ((alarm & (1 << 10)) >> 10):
				print("I Offset", end=",")
			elif ((alarm & (1 << 11)) >> 11):
				print("Battery Sense Out of Range", end=",")
			elif ((alarm & (1 << 12)) >> 12):
				print("Battery Sense Disconnected", end=",")
			elif ((alarm & (1 << 13)) >> 13):
				print("Uncalibrated", end=",")
			elif ((alarm & (1 << 14)) >> 14):
				print("TB 5V", end=",")
			elif ((alarm & (1 << 15)) >> 15):
				print("FP10 Supply Out of Range", end=",")
			elif ((alarm & (1 << 16)) >> 16):
				print("[unused]", end=",")
			elif ((alarm & (1 << 17)) >> 17):
				print("FET Open", end=",")
			elif ((alarm & (1 << 18)) >> 18):
				print("IA Offset", end=",")
			elif ((alarm & (1 << 19)) >> 19):
				print("IL Offset", end=",")
			elif ((alarm & (1 << 20)) >> 20):
				print("3V Supply Out of Range", end=",")
			elif ((alarm & (1 << 21)) >> 21):
				print("12V Supply Out of Range", end=",")
			elif ((alarm & (1 << 22)) >> 22):
				print("VA High (current limit due to high Voc)", end=",")
			elif ((alarm & (1 << 23)) >> 23):
				print("Reset", end=",")
			elif ((alarm & (1 << 24)) >> 24):
				print("LVD", end=",")
			elif ((alarm & (1 << 25)) >> 25):
				print("Log Timeout", end=",")
			elif ((alarm & (1 << 26)) >> 26):
				print("EEPROM Access Failure", end=",")
			



			
			
			print (regs[3]*100/32768, end=",")

			print (regs[4]*100/32768, end=",")

			print(regs[5]*0.1, end=",")
			print (regs[6]*0.1, end=",")

			array_fault = regs[7] 


			if array_fault == 0:
				print ("no faults", end=",")
			elif (array_fault & 1):
				print ("Overcurrent Phase 1", end=",")
			elif ((array_fault & (1 << 1)) >> 1):
				print("FET(s) Shorted", end=",")
			elif ((array_fault & (1 << 2)) >> 2):
				print("Software Bug", end=",")
			elif ((array_fault & (1 << 3)) >> 3):
				print("Battery HVD (High Voltage Disconnect)", end=",")
			elif ((array_fault & (1 << 4)) >> 4):
				print("Array HVD (High Voltage Disconnect)", end=",")
			elif ((array_fault & (1 << 5)) >> 5):
				print("EEPROM Setting Edit (reset required)", end=",")
			elif ((array_fault & (1 << 6)) >> 6):
				print("RTS Shorted", end=",")
			elif ((array_fault & (1 << 7)) >> 7):
				print("RTS was valid, now disconnected", end=",")
			elif ((array_fault & (1 << 8)) >> 8):
				print("Local temp. sensor failed", end=",")
			elif ((array_fault & (1 << 9)) >> 9):
				print("Battery LVD (Low Voltage Disconnect)", end=",")
			elif ((array_fault & (1 << 10)) >> 10):
				print("Slave Control Timeout", end=",")
			elif ((array_fault & (1 << 11)) >> 11):
				print("DIP Switch Changed (excl. DIP 8)", end=",")
	
			load_fault = regs[8]

			if load_fault == 0:
				print ("no faults", end=",")
			elif (load_fault & 1):
				print ("External Short Circuit", end=",")
			elif ((load_fault & (1 << 1)) >> 1):
				print("Overcurrent", end=",")
			elif ((load_fault & (1 << 2)) >> 2):
				print("FET(s) Shorted", end=",")
			elif ((load_fault & (1 << 3)) >> 3):
				print("Software Bug", end=",")
			elif ((load_fault & (1 << 4)) >> 4):
				print("High Voltage Disconnect", end=",")
			elif ((load_fault & (1 << 5)) >> 5):
				print("Heatsink Over-Temperature", end=",")
			elif ((load_fault & (1 << 6)) >> 6):
				print("DIP Switch Changed (excl. DIP 8)", end=",")
			elif ((load_fault & (1 << 7)) >> 7):
				print("EEPROM Setting Edit (reset required)", end=",")

				
			
			
			print(regs[9]*100/32768.0, end=",")

			print(regs[10]/60, end=",")
			print(regs[11]/60, end=",")
			print(regs[12]/60)			

			i += 0x0010
			varhex = hex(i)
	exit()
