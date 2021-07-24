import time
from roboclaw import Roboclaw
from roboclaw_3 import Roboclaw

recyclingPosition = 0
landfillPosition = 2125
compostPosition = 4250

positions = {
    "Recycling": recyclingPosition,
    "Landfill": landfillPosition,
    "Compost": compostPosition
}

address = 0x80
roboclaw = Roboclaw("/dev/ttyACM0", 460800)
roboclaw.Open()
roboclaw.SetEncM1(address, 0) #starts at recycling

def moveToBin(bin):
    pos = positions[bin]
    roboclaw.SpeedAccelDeccelPositionM1(address, 10000, 5000, 10000, pos, 0)

def resetPos():
    roboclaw.SpeedAccelDeccelPositionM1(address, 10000, 5000, 10000, 0, 0)

