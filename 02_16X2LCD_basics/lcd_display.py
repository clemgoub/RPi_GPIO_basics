from RPLCD.i2c import CharLCD
import time

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

for i in range(20):
	lcd.write_string('Hello, Clément!')
	lcd.clear()
	time.sleep(.1)
	lcd.write_string('Hello, Ángela!')
	lcd.clear()
	time.sleep(.1)

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