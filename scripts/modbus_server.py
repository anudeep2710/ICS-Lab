from pymodbus.server import StartTcpServer
from pymodbus.datastore import (
    ModbusSlaveContext,
    ModbusServerContext,
    ModbusSequentialDataBlock
)

# -------------------------------------------------------------------
# Create the Modbus data store
#
# Each block contains 100 values initialized to 0.
#
# di = Discrete Inputs       (read-only bits, function code 2)
# co = Coils                 (read/write bits, function codes 1 and 5/15)
# hr = Holding Registers     (read/write 16-bit registers, function codes 3 and 6/16)
# ir = Input Registers       (read-only 16-bit registers, function code 4)
# -------------------------------------------------------------------

store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0] * 100),
    co=ModbusSequentialDataBlock(0, [0] * 100),
    hr=ModbusSequentialDataBlock(0, [0] * 100),
    ir=ModbusSequentialDataBlock(0, [0] * 100),
)

context = ModbusServerContext(slaves=store, single=True)

print("Starting Modbus TCP Server on 0.0.0.0:5020 with device_id=1")

StartTcpServer(context=context, address=("0.0.0.0", 5020))
