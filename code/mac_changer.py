import subprocess

interface = input('please enter the interface name(wlan0, ):')
new_mac = input('please enter the new MAC address(00:11:22:33:44:55): ')

# option 1: not secure allows shell injection(the user can enter malicious commands)
subprocess.call(f'ifconfig {interface} down', shell=True)
subprocess.call(f'ifconfig {interface} hw ether {new_mac}', shell=True)
subprocess.call(f'ifconfig {interface} up', shell=True)

# option 2: secure way to avoid shell injection
subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])

