from pymodbus.client import ModbusTcpClient

PLC_IP = "10.10.1.10"
PORT = 5020

client = ModbusTcpClient(PLC_IP, port=PORT)

# Attempt connection to the PLC
if not client.connect():
    print(f"Failed to connect to {PLC_IP}:{PORT}")
    exit(1)

# Read 5 holding registers starting at address 0
rr = client.read_holding_registers(address=0, count=5, slave=1)

if rr.isError():
    print("Read failed:", rr)
else:
    print("Before Write:", rr.registers)

# Write value 123 to holding register 0
wr = client.write_register(address=0, value=123, slave=1)

if wr.isError():
    print("Write failed:", wr)

# Read the registers again to verify the write
rr = client.read_holding_registers(address=0, count=5, slave=1)

if rr.isError():
    print("Read failed:", rr)
else:
    print("After Write:", rr.registers)

client.close()
