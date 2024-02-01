#!/bin/bash

# Create the bash script
cat << 'EOF' > /usr/local/bin/check_network_speed.sh
#!/bin/bash

# Check if debug mode is enabled
if [[ "$1" == "debug" ]]; then
    DEBUG=true
fi

# Function to reset the interface
reset_interface() {
    echo "Resetting interface..."
    ifconfig enp0s31f6 down
    ifconfig enp0s31f6 up
}

# Run ethtool command and check the output for "Speed: 1000Mb/s"
if ethtool enp0s31f6 | grep -q "Speed: 1000Mb/s"; then
    echo "Speed is already set to 1000Mb/s"
else
    echo "Speed is not 1000Mb/s"
    if [[ "$DEBUG" != "true" ]]; then
        reset_interface
    else
        echo "Debug mode enabled. Interface will not be reset."
    fi
fi
EOF

# Set permissions for the script
chmod +x /usr/local/bin/check_network_speed.sh

# Create the systemd service and timer unit file
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

# Reload systemd
systemctl daemon-reload

# Enable and start the timer
systemctl enable --now check_network_speed.service

# Check the status of the service
systemctl status check_network_speed.service
