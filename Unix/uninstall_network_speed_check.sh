#!/bin/bash

# Stop and disable the timer
systemctl stop check_network_speed.timer
systemctl disable check_network_speed.timer

# Remove the timer unit file
rm /etc/systemd/system/check_network_speed.timer

# Remove the service unit file
rm /etc/systemd/system/check_network_speed.service

# Remove the bash script
rm /usr/local/bin/check_network_speed.sh

# Reload systemd
systemctl daemon-reload

# Remove the symbolic link
rm /etc/systemd/system/multi-user.target.wants/check_network_speed.timer

# Check the status of the timer
systemctl status check_network_speed.timer
