taskkill /F /IM "vmware.exe"
taskkill /F /IM "vmware-tray.exe"
net stop VMwareHostd
sc config VMwareHostd start= disabled
net stop VMUSBArbService
sc config VMUSBArbService start= disabled
net stop VMAuthdService
sc config VMAuthdService start= disabled
net stop VMnetDHCP
sc config VMnetDHCP start= disabled
net stop "VMware NAT Service"
sc config "VMware NAT Service" start= disabled
netsh interface set interface "VMware Network Adapter VMnet1" DISABLED
netsh interface set interface "VMware Network Adapter VMnet8" DISABLED