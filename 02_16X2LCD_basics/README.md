# RPi 4 x 16X2 LCD display basics

This projects follows https://medium.com/@thedyslexiccoder/how-to-set-up-a-raspberry-pi-4-with-lcd-display-using-i2c-backpack-189a0760ae15

## Material

- Rpi 4
- 16X2 LCD screen
- 6x jumper cables
- 10k pot (backlight)

## Notes

### Initial config of RPi

- 1. Activate the I2C interface in Preference/Rpi_configuration/
- 2. reboot
- 3. install `i2c-tools` and `smbus`
 ```sh
 sudo apt-get install -y i2c-tools python3-smbus
 ```
- 4. Check if i2c kernel module is already loaded
```sh
lsmod | grep i2c_
```
Check that `i2c-bcm2835`, `i2c-bcm2708` and `i2c-dev` shows up, otherwise add them to `/etc/modules`
- 5. `sudo reboot`

### Let's get into it

1. This scans for a connected i2c device

```sh
sudo i2cdetect -y 1
```

Should display:

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- 27 -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

2. Install python libraries

```sh
sudo pip3 install RPLCD smbus2
```

--> there was initially an error `error: externally-managed-environment` due to the os wanting to be sole package manager. Can be bypassed with:

```sh
sudo mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED.old
```
> just remove `.old` to restore old behavior

Then `sudo pip3 install RPLCD smbus2` worked.

### Code

For the rest, everything will be in the scripts of this repo

### Breadboard

With 10K pot for backlight intensity
![](https://github.com/clemgoub/RPi_GPIO_basics/blob/main/02_16X2LCD_basics/lcd_breadboard.jpg?raw=true)

