#!/bin/bash

# Stop and disable the service
systemctl stop check_network_speed.service
systemctl disable check_network_speed.service

# Remove the service unit file
rm /etc/systemd/system/check_network_speed.service

# Remove the bash script
rm /usr/local/bin/check_network_speed.sh

# Reload systemd
systemctl daemon-reload

# Check the status of the service
systemctl status check_network_speed.service
