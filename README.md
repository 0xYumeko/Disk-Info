![2024-08-03_11-08](https://github.com/user-attachments/assets/e158142f-c6fa-4ce6-89b5-76bf5db7dc1d)


Skip Special Filesystems: Added a check to skip special file systems like swap and loop devices which arent mountable directories.
```
if fstype == "swap" || fstype == "loop" {
    continue
}
```
