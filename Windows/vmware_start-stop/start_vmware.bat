sc config VMUSBArbService start= demand
net start VMUSBArbService
sc config VMAuthdService start= demand
net start VMAuthdService
sc config VMwareHostd start= demand
net start VMwareHostd
sc config VMnetDHCP start= demand
net start VMnetDHCP
sc config "VMware NAT Service" start= demand
net start "VMware NAT Service"
netsh interface set interface "VMware Network Adapter VMnet1" ENABLED
netsh interface set interface "VMware Network Adapter VMnet8" ENABLED
cd "%PROGRAMFILES(x86)%\VMware\VMware Workstation"
start vmware.exe