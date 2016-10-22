import re
import time
import serial
from serial.tools import list_ports
import psutil


START_MARKER = 'Clujlusjarr7'
RETRY_INTERVAL = 5


def displayToHardware(s, line1, line2=""):
    line1_str = "%s".ljust(16, ' ') % line1
    line2_str = "%s".ljust(16, ' ') % line2

    s.write(START_MARKER)
    s.write(line1_str + '\n')
    s.write(line2_str + '\n')


def run():
    serial_port = None
    ports = list_ports.comports()
    r = re.compile(r'^Arduino*')

    # Guess serial port
    for port in ports:
        if r.match(port.description) is not None:
            print "\nDevice found (%s)! %s" % (port.description, port.device)
            serial_port = port.device

    if serial_port is None:
        raise "Cannot find a device"
    else:
        loop(serial_port)


def loop(serial_port):
    print "Connecting to %s..." % serial_port
    s = serial.Serial(serial_port)

    while(True):
        # CPU Percentage
        cpu_pct = psutil.cpu_percent(interval=1, percpu=False)

        # Memory Percentage
        mem = psutil.virtual_memory()
        mem_pct = mem.percent

        displayToHardware(s, "CPU: %s%%" % cpu_pct, "MEM: %s%%" % mem_pct)
        time.sleep(2)


if __name__ == '__main__':
    while True:
        try:
            run()
        except:
            print "Connection failed! Retry in %s seconds..." % RETRY_INTERVAL
            time.sleep(RETRY_INTERVAL)
