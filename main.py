import os
import platform
import psutil
import speedtest

def run_speed_test():
    # Run speed test
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping

    # Print results
    print(f'Download: {download_speed:.2f} Mbps')
    print(f'Upload: {upload_speed:.2f} Mbps')
    print(f'Ping: {ping} ms')

def get_system_info():
    # Get system information
    print('System Information:')
    print(f'  System: {platform.system()}')
    print(f'  Node Name: {platform.node()}')
    print(f'  Release: {platform.release()}')
    print(f'  Version: {platform.version()}')
    print(f'  Machine: {platform.machine()}')
    print(f'  Processor: {platform.processor()}')

def get_network_info():
    # Get network information
    print('\nNetwork Information:')
    for interface, addrs in psutil.net_if_addrs().items():
        print(f'  {interface}:')
        for addr in addrs:
            print(f'    {addr.address}')

def main():
    get_network_info()
    get_system_info()
    run_speed_test()

if __name__ == '__main__':
    main()
