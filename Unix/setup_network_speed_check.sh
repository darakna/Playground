#!/bin/bash

# Create the bash script
cat << 'EOF' > /usr/local/bin/check_network_speed.sh
#!/bin/bash

# Run ethtool command and check the output for "Speed: 1000Mb/s"
if ethtool enp0s31f6 | grep -q "Speed: 1000Mb/s"; then
    echo "Speed is already set to 1000Mb/s"
else
    echo "Speed is not 1000Mb/s, resetting interface..."
    ifconfig enp0s31f6 down
    ifconfig enp0s31f6 up
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

[Install]
WantedBy=timers.target
EOF

# Link the Timer Unit to the Service Unit
ln -s /etc/systemd/system/check_network_speed.timer /etc/systemd/system/multi-user.target.wants/

# Reload systemd
systemctl daemon-reload

# Enable and start the timer
systemctl enable check_network_speed.timer
systemctl start check_network_speed.timer

# Check the status of the timer
systemctl status check_network_speed.timer
