import os
import re
import threading

received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")

def ping_ip(ip):
    ping_out = os.popen("ping -q -c2 " + ip, "r")
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])

def main():
    threads = []

    for suffix in range(20, 30):
        ip = "192.168.178." + str(suffix)
        thread = threading.Thread(target=ping_ip, args=(ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()