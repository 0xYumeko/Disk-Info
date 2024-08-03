Skip Special Filesystems: Added a check to skip special file systems like swap and loop devices which arent mountable directories.
```
if fstype == "swap" || fstype == "loop" {
    continue
}
```
