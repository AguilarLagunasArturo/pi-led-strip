# PI Led Strip
Control WS2811 indexable led strip over WiFi using a self hosted web page.

#
```bash
# Configure service
ln -s /home/pi/Github/pi-led-strip/services/service_name.service /etc/systemd/system

# Enable service (starts service automatically)
systemctl enable service_name

# Disable service
systemctl disable service_name

# Start service
systemctl start service_name
systemctl status service_name

# Stop service
systemctl stop service_name
systemctl status service_name

# Show services journal
journalctl -f
```
