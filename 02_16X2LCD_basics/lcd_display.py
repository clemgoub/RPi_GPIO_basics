from RPLCD.i2c import CharLCD
import time

# create lcd object with write address.
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

# Loop of messages
for i in range(20):
	lcd.write_string('Hello, Clément!')
	time.sleep(1)
	lcd.clear()
	lcd.write_string('Hello, Ángela!')
	time.sleep(1)
	lcd.clear()

# Goodbye routine
lcd.write_string('Goodbye!')
time.sleep(1)
lcd.clear()
lcd.write_string('3!')
time.sleep(1)
lcd.clear()
lcd.write_string('2!')
time.sleep(1)
lcd.clear()
lcd.write_string('1!')
time.sleep(1)
lcd.clear()
lcd.write_string('POOF!')
time.sleep(1)
lcd.clear()