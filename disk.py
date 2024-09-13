import psutil
import shutil
import os
from colorama import Fore, Back, Style, init
from datetime import datetime, timedelta

# Initialize colorama
init()

# Define global variables
logo_text = "0xYumeko"
logo_color = Fore.CYAN
logo_style = Style.BRIGHT
section_color = Fore.GREEN
info_color = Fore.YELLOW
highlight_color = Fore.MAGENTA
error_color = Fore.RED
reset_color = Style.RESET_ALL

def get_system_info():
    cpu_freq = psutil.cpu_freq().current
    ram_total = psutil.virtual_memory().total / (1024 ** 3)  # Convert bytes to GB
    cpu_usage = psutil.cpu_percent(interval=1)
    load_avg = os.getloadavg()
    return cpu_freq, ram_total, cpu_usage, load_avg

def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    return disk_usage.total / (1024 ** 3), disk_usage.used / (1024 ** 3), disk_usage.free / (1024 ** 3), disk_usage.percent

def get_network_info():
    network_info = psutil.net_if_addrs()
    return {interface: [addr.address for addr in addrs] for interface, addrs in network_info.items()}

def get_file_system_info():
    partitions = psutil.disk_partitions()
    file_systems = []
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        file_systems.append((partition.device, partition.mountpoint, partition.fstype, usage.total / (1024 ** 3), usage.used / (1024 ** 3), usage.free / (1024 ** 3)))
    return file_systems

def get_boot_time():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    return boot_time.strftime("%Y-%m-%d %H:%M:%S")

def get_uptime():
    uptime_seconds = (datetime.now() - datetime.fromtimestamp(psutil.boot_time())).total_seconds()
    return str(timedelta(seconds=int(uptime_seconds)))

def get_battery_info():
    if psutil.sensors_battery() is not None:
        battery = psutil.sensors_battery()
        return battery.percent, battery.power_plugged
    return None, None

def get_temperature_info():
    # This function might require platform-specific adjustments
    try:
        temp_info = psutil.sensors_temperatures()
        return temp_info
    except Exception:
        return None

def get_user_info():
    user = os.getlogin()
    home_dir = os.path.expanduser("~")
    return user, home_dir

def get_top_processes():
    processes = [(proc.info['pid'], proc.info['name'], proc.info['cpu_percent']) 
                 for proc in psutil.process_iter(['pid', 'name', 'cpu_percent'])]
    top_processes = sorted(processes, key=lambda x: x[2], reverse=True)[:5]
    return top_processes

def display_logo():
    logo = f"{logo_style}{logo_color}{logo_text}{reset_color}"
    print(f"{logo}\n{'=' * len(logo)}\n")

def display_system_info():
    cpu_freq, ram_total, cpu_usage, load_avg = get_system_info()
    system_info = (
        f"{section_color}System Information:{reset_color}\n"
        f"{info_color}CPU Frequency:{reset_color} {cpu_freq} MHz\n"
        f"{info_color}RAM Total:{reset_color} {ram_total:.2f} GB\n"
        f"{info_color}CPU Usage:{reset_color} {cpu_usage}%\n"
        f"{info_color}Load Average (1m, 5m, 15m):{reset_color} {load_avg[0]}, {load_avg[1]}, {load_avg[2]}\n"
    )
    print(system_info)

def display_disk_usage():
    total, used, free, percent = get_disk_usage()
    disk_info = (
        f"{section_color}Disk Usage:{reset_color}\n"
        f"{info_color}Total:{reset_color} {total:.2f} GB\n"
        f"{info_color}Used:{reset_color} {used:.2f} GB\n"
        f"{info_color}Free:{reset_color} {free:.2f} GB\n"
        f"{info_color}Percent Used:{reset_color} {percent}%\n"
    )
    print(disk_info)

def display_file_system_info():
    file_systems = get_file_system_info()
    fs_info = f"{section_color}File System Information:{reset_color}\n"
    for device, mountpoint, fstype, total, used, free in file_systems:
        fs_info += (
            f"{info_color}Device:{reset_color} {device}\n"
            f"{info_color}Mountpoint:{reset_color} {mountpoint}\n"
            f"{info_color}File System Type:{reset_color} {fstype}\n"
            f"{info_color}Total:{reset_color} {total:.2f} GB\n"
            f"{info_color}Used:{reset_color} {used:.2f} GB\n"
            f"{info_color}Free:{reset_color} {free:.2f} GB\n"
            f"{'-' * 40}\n"
        )
    print(fs_info)

def display_network_info():
    network_info = get_network_info()
    network_details = f"{section_color}Network Interfaces:{reset_color}\n"
    for interface, addresses in network_info.items():
        network_details += f"{info_color}{interface}:{reset_color} {', '.join(addresses)}\n"
    print(network_details)

def display_boot_time():
    boot_time = get_boot_time()
    print(f"{section_color}System Boot Time:{reset_color} {boot_time}")

def display_uptime():
    uptime = get_uptime()
    print(f"{section_color}System Uptime:{reset_color} {uptime}")

def display_battery_info():
    battery_percent, power_plugged = get_battery_info()
    if battery_percent is not None:
        print(f"{section_color}Battery Status:{reset_color} {battery_percent}% {'(Plugged In)' if power_plugged else '(Not Plugged In)'}")
    else:
        print(f"{section_color}Battery Status:{reset_color} Not Available")

def display_temperature_info():
    temp_info = get_temperature_info()
    if temp_info:
        print(f"{section_color}Temperature Info:{reset_color}")
        for key, temp_list in temp_info.items():
            for temp in temp_list:
                print(f"{info_color}{key}:{reset_color} {temp.current}°C")
    else:
        print(f"{section_color}Temperature Info:{reset_color} Not Available")

def display_user_info():
    user, home_dir = get_user_info()
    print(f"{section_color}Current User:{reset_color} {user}")
    print(f"{section_color}Home Directory:{reset_color} {home_dir}")

def display_top_processes():
    top_processes = get_top_processes()
    process_info = f"{section_color}Top 5 CPU-consuming Processes:{reset_color}\n"
    for pid, name, cpu_percent in top_processes:
        process_info += f"{info_color}PID:{reset_color} {pid} {info_color}Name:{reset_color} {name} {info_color}CPU Usage:{reset_color} {cpu_percent}%\n"
    print(process_info)

def clean():
    try:
        shutil.rmtree("result", ignore_errors=True)
        print(f"{highlight_color}Cleaned up the result directory.{reset_color}")
    except Exception as e:
        print(f"{error_color}Error during cleanup: {e}{reset_color}")

def display_footer():
    footer = (
        f"{highlight_color}Script executed successfully.{reset_color}\n"
        f"{Fore.WHITE}For more info, visit: {Fore.CYAN}https://example.com{reset_color}"
    )
    print(footer)

def main():
    display_logo()
    display_system_info()
    display_disk_usage()
    display_file_system_info()
    display_network_info()
    display_boot_time()
    display_uptime()
    display_battery_info()
    display_temperature_info()
    display_user_info()
    display_top_processes()
    clean()
    display_footer()

if __name__ == '__main__':
    main()
