from lib.mBot import *

#https://github.com/ML-Studi0/MBot

if __name__ == '__main__':
	bot = mBot()
	bot.startWithSerial("COM9")
	#bot.startWithHID()
	speed = 1024
	bot.doMove(0,0)
	sleep(1)
	while(1):
		print('forward')
		bot.doRGBLedOnBoard(3,0,100,0)
		bot.doRGBLedOnBoard(9,0,0,0)
		bot.doMove(speed,speed)
		sleep(10)
		print('stop')
		bot.doRGBLedOnBoard(3,100,0,0)
		bot.doMove(0,0)
		sleep(5)
		print('backward')
		bot.doRGBLedOnBoard(3,0,0,0)
		bot.doRGBLedOnBoard(9,0,100,0)
		bot.doMove(-speed,-speed)
		sleep(10)
		print('stop')
		bot.doRGBLedOnBoard(9,100,0,0)
		bot.doMove(0,0)
		sleep(5)