# PI Led Strip
Use a Raspberry PI Zero to control WS2811 indexable led strip over WiFi using a self hosted web page.

# Demo
Controlling 100 leds trough a local hosted webpage.  

![WebTree](./preview/demo.gif)

## Materials
- Raspberry PI W Zero Two
- 5V 6A Power Supply
- LED Pixel Module WS281
- Breadboard
- Wrires

# Setup
## Wriring
![Wiring](./preview/wiring.png)

## Raspberry PI Configuration
Enable SPI through the GUI or directly set `` in the rpi configuration file ``.

## Dependencies
Install dependencies to control WS2811 led strip.
```bash
pip install rpi-ws281x
pip install adafruit-circuitpython-neopixel
```
## Service
The following block is a service configuration file (`service_name.service`) example. `ExecStart` must be an executable program, you can set it up like this: `sudo chmod +x program.py`.

```bash
[Unit]
Description=Service description

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/Github/repo/main
ExecStart=/home/pi/Github/repo/main/./program.py
TimeoutSec=45s
Restart=always
RestartSec=20s

[Install]
WantedBy=multi-user.target
```

Here are some useful commads to set up the service vonfigured below.
```bash
# Symlink the service configuration to the default service location.
sudo ln -s /home/pi/Github/repo/services/service_name.service /etc/systemd/system

# Enable service (starts service automatically)
sudo systemctl enable service_name

# Disable service
sudo systemctl disable service_name

# Start service
sudo systemctl start service_name
sudo systemctl status service_name

# Stop service
sudo systemctl stop service_name
sudo systemctl status service_name

# Show services journal
sudo journalctl -f
```

# References
- [Python WS281x module](https://pypi.org/project/rpi-ws281x/)
- [Python NeoPixel module](https://docs.circuitpython.org/projects/neopixel/en/latest/)
- [Wiring](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring)
- [Using module](https://tutorials-raspberrypi.com/how-to-control-a-raspberry-pi-ws2801-rgb-led-strip/)
- [Video tutorial](https://www.youtube.com/watch?v=KJupt2LIjp4)
