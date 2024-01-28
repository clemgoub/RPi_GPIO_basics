from RPLCD.i2c import CharLCD
import time

# create lcd object with write address.
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()

# define sleep time for tuning
st = 0.1
# Animation
for i in range(20):
	# frame 1
	lcd.write_string('      **        ')
	lcd.cursor_pos = (1,0)
	lcd.write_string('  (--------)    ')
	time.sleep(st)
	lcd.clear()
	# frame 2
	lcd.write_string('      **  C     ')
	lcd.cursor_pos = (1,0)
	lcd.write_string(' (----------)   ')
	time.sleep(st)
	lcd.clear()
	# frame 3 (same as 1)
	lcd.write_string('      **  CR    ')
	lcd.cursor_pos = (1,0)
	lcd.write_string('  (--------)    ')
	time.sleep(st)
	lcd.clear()
	# frame 4
	lcd.write_string('      **  CRO   ')
	lcd.cursor_pos = (1,0)
	lcd.write_string('   (------)     ')
	time.sleep(st)
	lcd.clear()
	# frame 5
	lcd.write_string('      **  CROA  ')
	lcd.cursor_pos = (1,0)
	lcd.write_string('    (----)      ')
	time.sleep(st)
	lcd.clear()
	# frame 6 (4)
	lcd.write_string('      **  CROAC!')
	lcd.cursor_pos = (1,0)
	lcd.write_string('   (------)   ')
	time.sleep(st)
	lcd.clear()
	# frame 7 (3, 1)
	lcd.write_string('      **  CROAC ')
	lcd.cursor_pos = (1,0)
	lcd.write_string('  (--------)  ')
	time.sleep(st)
	lcd.clear()
	# frame 8 (2)
	lcd.write_string('      **  CROAC!')
	lcd.cursor_pos = (1,0)
	lcd.write_string(' (----------) ')
	time.sleep(st)
	lcd.clear()

# Goodbye routine
lcd.write_string('Goodbye!')
time.sleep(1)
lcd.clear()