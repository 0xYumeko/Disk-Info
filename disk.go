package main

import (
	"fmt"
	"github.com/fatih/color"
	"github.com/shirou/gopsutil/cpu"
	"github.com/shirou/gopsutil/disk"
	"github.com/shirou/gopsutil/mem"
	"github.com/shirou/gopsutil/net"
	"os"
	"time"
)

func displayLogo() {
	// Define color styles
	blue := color.New(color.FgCyan).SprintFunc()
	bold := color.New(color.Bold).SprintFunc()

	// Logo and styling
	logo := bold(blue("0xYumeko"))
	fmt.Println(logo)
	fmt.Println("====================================")
}

func displaySystemInfo() {
	cpuInfos, _ := cpu.Info()
	cpuUsage, _ := cpu.Percent(time.Second, false)
	memInfo, _ := mem.VirtualMemory()

	cpuFreq := cpuInfos[0].Mhz
	cpuUsagePercent := cpuUsage[0]
	ramTotal := memInfo.Total / (1024 * 1024 * 1024) // GB
	ramUsed := memInfo.Used / (1024 * 1024 * 1024)  // GB

	// Define color styles
	green := color.New(color.FgGreen).SprintFunc()
	yellow := color.New(color.FgYellow).SprintFunc()

	fmt.Printf("%s System Information:\n", green("System Information"))
	fmt.Printf("CPU Frequency: %d MHz\n", cpuFreq)
	fmt.Printf("CPU Usage: %.2f%%\n", cpuUsagePercent)
	fmt.Printf("RAM Total: %.2f GB\n", float64(ramTotal))
	fmt.Printf("RAM Used: %.2f GB\n", float64(ramUsed))
}

func displayDiskUsage() {
	partitions, _ := disk.Partitions(false)
	for _, partition := range partitions {
		diskUsage, _ := disk.Usage(partition.Mountpoint)
		total := diskUsage.Total / (1024 * 1024 * 1024) // GB
		free := diskUsage.Free / (1024 * 1024 * 1024)  // GB
		used := diskUsage.Used / (1024 * 1024 * 1024)   // GB

		// Define color styles
		green := color.New(color.FgGreen).SprintFunc()
		yellow := color.New(color.FgYellow).SprintFunc()

		fmt.Printf("%s Disk Usage:\n", green("Disk Usage"))
		fmt.Printf("Mountpoint: %s\n", partition.Mountpoint)
		fmt.Printf("Total: %.2f GB\n", float64(total))
		fmt.Printf("Used: %.2f GB\n", float64(used))
		fmt.Printf("Free: %.2f GB\n", float64(free))
		fmt.Println("------------------------------------")
	}
}

func displayNetworkInfo() {
	interfaces, _ := net.Interfaces()

	// Define color styles
	green := color.New(color.FgGreen).SprintFunc()
	yellow := color.New(color.FgYellow).SprintFunc()

	fmt.Printf("%s Network Interfaces:\n", green("Network Interfaces"))
	for _, iface := range interfaces {
		fmt.Printf("%s: %s\n", yellow(iface.Name), iface.Addrs)
	}
}

func displayBootTime() {
	bootTime := time.Now().Add(-time.Duration(time.Since(time.Now())).Hours())
	fmt.Printf("%s System Boot Time:\n", color.New(color.FgGreen).SprintFunc())
	fmt.Println(bootTime.Format("2006-01-02 15:04:05"))
}

func displayUptime() {
	uptime := time.Since(time.Now()).Hours()
	fmt.Printf("%s System Uptime:\n", color.New(color.FgGreen).SprintFunc())
	fmt.Printf("%f hours\n", uptime)
}

func displayBatteryInfo() {
	// Battery information is OS-specific and not available directly in Go
	fmt.Printf("%s Battery Info:\n", color.New(color.FgGreen).SprintFunc())
	fmt.Println("Not available in this script.")
}

func displayTemperatureInfo() {
	// Temperature information is OS-specific and not available directly in Go
	fmt.Printf("%s Temperature Info:\n", color.New(color.FgGreen).SprintFunc())
	fmt.Println("Not available in this script.")
}

func displayUserInfo() {
	user, _ := os.UserHomeDir()
	fmt.Printf("%s Current User:\n", color.New(color.FgGreen).SprintFunc())
	fmt.Printf("Home Directory: %s\n", user)
}

func displayTopProcesses() {
	// Top processes information is OS-specific and not available directly in Go
	fmt.Printf("%s Top 5 CPU-consuming Processes:\n", color.New(color.FgGreen).SprintFunc())
	fmt.Println("Not available in this script.")
}

func clean() {
	// Implement cleanup logic if necessary
	fmt.Println(color.New(color.FgMagenta).Sprint("Cleaning up..."))
}

func displayFooter() {
	fmt.Println(color.New(color.FgCyan).Sprint("Script executed successfully."))
}

func main() {
	displayLogo()
	displaySystemInfo()
	displayDiskUsage()
	displayNetworkInfo()
	displayBootTime()
	displayUptime()
	displayBatteryInfo()
	displayTemperatureInfo()
	displayUserInfo()
	displayTopProcesses()
	clean()
	displayFooter()
}
