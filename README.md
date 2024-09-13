![2024-08-03_11-08](https://github.com/user-attachments/assets/e158142f-c6fa-4ce6-89b5-76bf5db7dc1d)


Skip Special Filesystems: Added a check to skip special file systems like swap and loop devices which arent mountable directories.
```
if fstype == "swap" || fstype == "loop" {
    continue
}
```
<h1>Example Output:
The script will produce output similar to this:
</h1>

```bash
CPU Information:
   - CPU Count: 4
   - CPU Frequency: 2.3 GHz
   - CPU Usage: 30%

Memory Information:
   - Total Memory: 8 GB
   - Available Memory: 5 GB
   - Memory Usage: 40%

Disk Information:
   - Total Disk Space: 256 GB
   - Used Disk Space: 120 GB
   - Free Disk Space: 136 GB

Network Information:
   - Network Interface: eth0
   - IP Address: 192.168.1.10
   - MAC Address: 00:1A:2B:3C:4D:5E
```


