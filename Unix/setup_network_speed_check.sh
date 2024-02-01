#!/bin/bash

# Create the bash script
cat << 'EOF' > /usr/local/bin/check_network_speed.sh
#!/bin/bash

# Check if debug mode is enabled
if [[ "$1" == "debug" ]]; then
    DEBUG=true
fi

# Function to echo with a timestamp
echo_timestamp() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

# Function to reset the interface
reset_interface() {
    echo_timestamp "Resetting interface..."
    ifconfig enp0s31f6 down
    ifconfig enp0s31f6 up
}

# Run ethtool command and check the output for "Speed: 1000Mb/s"
if ethtool enp0s31f6 | grep -q "Speed: 1000Mb/s"; then
    echo_timestamp "Speed is already set to 1000Mb/s"
else
    echo_timestamp "Speed is not 1000Mb/s"
    if [[ "$DEBUG" != "true" ]]; then
        reset_interface
    else
        echo_timestamp "Debug mode enabled. Interface will not be reset."
    fi
fi
EOF

# Set permissions for the script
chmod +x /usr/local/bin/check_network_speed.sh

# Create the systemd service unit file
cat << 'EOF' > /etc/systemd/system/check_network_speed.service
[Unit]
Description=Check and reset network speed if not 1000Mb/s
After=network.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/check_network_speed.sh

[Install]
WantedBy=multi-user.target
EOF

# Create the systemd timer unit file
cat << 'EOF' > /etc/systemd/system/check_network_speed.timer
[Unit]
Description=Run check_network_speed.sh every 10 minutes

[Timer]
OnBootSec=1min
OnUnitActiveSec=10min
Unit=check_network_speed.service

[Install]
WantedBy=timers.target
EOF

# Reload systemd
systemctl daemon-reload

# Enable and start the timer
systemctl enable --now check_network_speed.timer

# Check the status of the timer
systemctl status check_network_speed.timer
