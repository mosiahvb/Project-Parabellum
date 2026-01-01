import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option('-i', '--interface', dest='interface', help='Interface to change MAC adddress')
parser.add_option('-m', '--mac', dest='new_mac', help='new MAC adress')

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print(f'[+] changing MAC address for {interface} to {new_mac}')

# option 1: not secure allows shell injection(the user can enter malicious commands)
subprocess.call(f'ifconfig {interface} down', shell=True)
subprocess.call(f'ifconfig {interface} hw ether {new_mac}', shell=True)
subprocess.call(f'ifconfig {interface} up', shell=True)

# option 2: secure way to avoid shell injection
subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])

