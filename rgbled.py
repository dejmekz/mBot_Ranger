from lib.mBot import *

if __name__ == '__main__':
	bot = mBot()
	bot.startWithSerial("COM9")
	#bot.startWithHID()
	x = 1
	while(1):
		if x > 12:
			x = 1
		
		print(x)
		bot.doRGBLedOnBoard(x,100,0,0)
		sleep(1)
		bot.doRGBLedOnBoard(x,0,100,0)
		sleep(1)
		bot.doRGBLedOnBoard(x,0,0,0)
		x = x + 1