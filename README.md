# The Omega-Game
The Omega Game - a small text game for Onion Omega 2+ controlled with usb gamepad!

![alt text][screenshot]

# Requirements
- iBuffalo classic usb gamepad [link](https://www.amazon.com/Buffalo-iBuffalo-Classic-Gamepad-BSGP801GY/dp/B002B9XB0E)
- omega-python-evdev library [link](https://github.com/pleft/omega2-python-evdev)

# Installation

On your Onion Omega 2:
- Download the Omega python evdev package: `wget https://github.com/pleft/omega2-python-evdev/raw/master/packages/python-evdev_0.4.7-1_mipsel_24kc.ipk`
- Install it: `opkg python-evdev_0.4.7-1_mipsel_24kc.ipk install`
- Download the game: `wget https://raw.githubusercontent.com/pleft/omegagame/master/omegagame.py`
- Run it: `./omegagame.py` or `python omegagame.py`


[screenshot]: https://github.com/pleft/omegagame/raw/master/IMG_1894.JPG "OmegaGame for Onion Omega 2+"
