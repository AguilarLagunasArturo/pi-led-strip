#!/usr/bin/env python3

import time
from rpi_ws281x import PixelStrip, Color
import argparse

class PiLedController():

    TYPE_PWM = 18 # GPIO pin connected to the pixels (18 uses PWM!).
    TYPE_SPI = 10 # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).

    def __init__(
        self,
        led_count,                      # Amount of leds to control
        led_strip_pin=None,             # Number of LED pixels
        led_hz_frequency=1_150_000,     # LED signal frequency in hertz (usually 800khz)
        led_dma=0,                      # DMA channel to use for generating signal (try 10)
        led_brightness=200,             # Set to 0 for darkest and 255 for brightest
        led_invert=False,               # True to invert the signal (when using NPN transistor level shift)
        led_strip_channel=0             # set to '1' for GPIOs 13, 19, 41, 45 or 53
    ):
        # LED strip configuration:
        if led_strip_pin:
            self.LED_PIN = led_strip_pin
        self.LED_PIN = PiLedController.TYPE_SPI
        self.LED_COUNT = led_count
        self.LED_FREQ_HZ = led_hz_frequency
        self.LED_DMA = led_dma
        self.LED_BRIGHTNESS = led_brightness
        self.LED_INVERT = led_invert
        self.LED_CHANNEL = led_strip_channel

        # Create NeoPixel object with appropriate configuration
        self.strip = PixelStrip(
        	self.LED_COUNT,
        	self.LED_PIN,
        	self.LED_FREQ_HZ,
        	self.LED_DMA,
        	self.LED_INVERT,
        	self.LED_BRIGHTNESS,
        	self.LED_CHANNEL
    	)

        # Intialize the library
        self.strip.begin()



    # Define functions which animate LEDs in various ways.
    def colorWipe(self, rgb, wait_ms=50, custom_range=None):
        if custom_range:
            selected_range = custom_range
        else:
            selected_range = range(self.strip.numPixels())
        color = Color(rgb[0], rgb[1], rgb[2])
        """Wipe color across display a pixel at a time."""
        for i in selected_range:
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms / 1000.0)


    def theaterChase(self, rgb, wait_ms=50, iterations=10):
        color = Color(rgb[0], rgb[1], rgb[2])
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, color)
                self.strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)


    def wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)


    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256 * iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, wheel((i + j) & 255))
            self.strip.show()
            time.sleep(wait_ms / 1000.0)


    def rainbowCycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256 * iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, wheel(
                    (int(i * 256 / self.strip.numPixels()) + j) & 255))
            self.strip.show()
            time.sleep(wait_ms / 1000.0)


    def theaterChaseRainbow(self, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, wheel((i + j) % 255))
                self.strip.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i + q, 0)

## Main program logic follows:
#if __name__ == '__main__':
#
#    led_strip = PiLedController(100)
#
#    try:
#        led_strip.colorWipe((0, 0, 0), 10)
#        while True:
#            led_strip.colorWipe((20, 0, 0))  # Red wipe
#            led_strip.colorWipe((0, 20, 0))  # Green wipe
#            led_strip.colorWipe((0, 0, 20))  # Blue wipe
#            #rainbow(strip)
#            #rainbowCycle(strip)
#            #theaterChaseRainbow(strip)
#    except KeyboardInterrupt:
#        if args.clear:
#            colorWipe((0, 0, 0), 10)
