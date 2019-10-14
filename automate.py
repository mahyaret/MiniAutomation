from time import sleep
import Adafruit_BBIO.GPIO as GPIO
from argparse import ArgumentParser
import time;


on_time_error_constant = 1
off_time_error_constnt = 2


print "Written by Mahyar Abdeetedal"

localtime = time.localtime(time.time())
print "Local current time :", localtime


parser = ArgumentParser()
parser.add_argument("--relay1_on", dest="r1_on")
parser.add_argument("--relay1_off", dest="r1_off")

parser.add_argument("--relay2_on", dest="r2_on")
parser.add_argument("--relay2_off", dest="r2_off")

parser.add_argument("--relay3_on", dest="r3_on")
parser.add_argument("--relay3_off", dest="r3_off")

parser.add_argument("--relay4_on", dest="r4_on")
parser.add_argument("--relay4_off", dest="r4_off")

args = parser.parse_args()

r1_off = int(args.r1_off)
r2_off = int(args.r2_off)
r3_off = int(args.r3_off)
r4_off = int(args.r4_off)

r1_on = int(args.r1_on)
r2_on = int(args.r2_on)
r3_on = int(args.r3_on)
r4_on = int(args.r4_on)


if r1_off<0 | r1_off>24:
	print("Off time is not in range for relay1")
	args.r1_off = off_time_error_constant
if r2_off<0 | r2_off>24:
        print("Off time is not in range for relay2")
        r2_off = off_time_error_constant  
if r3_off<0 | r3_off>24:
        print("Off time is not in range for relay3")
        r3_off = off_time_error_constant  
if r4_off<0 | r4_off>24:
        print("Off time is not in range for relay4")
        r4_off = off_time_error_constant  

if r1_on<0 | r1_on>24:
        print("On time is not in range for relay1")
        r1_on = on_time_error_constant  
if r2_on<0 | r2_on>24:
        print("On time is not in range for relay2")
        r2_on = on_time_error_constant  
if r3_on<0 | r3_on>24:
        print("On time is not in range for relay3")
        r3_on = on_time_error_constant  
if r4_on<0 | r4_on>24:
        print("On time is not in range for relay4")
        args.r4_on = on_time_error_constant  

if r1_on >= r1_off:
	print("On time should be before Off time for relay 1")
	r1_on = r1_off - on_time_error_constant
if r2_on >= r2_off:
        print("On time should be before Off time for relay 2")
	r2_on = r2_off - on_time_error_constant
if r3_on >= r3_off:
        print("On time should be before Off time for relay 3")
	r3_on = r3_off - on_time_error_constant
if r4_on >= r4_off:
        print("On time should be before Off time for relay 4")
	r4_on = r4_off - on_time_error_constant

relay1 = "P9_41"
relay2 = "P9_42"
relay3 = "P9_30"
relay4 = "P9_27"

GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.setup(relay4, GPIO.OUT)


while True:
	localtime = time.localtime(time.time())
	try:
		if localtime.tm_hour == r1_on:
    			GPIO.output(relay1, GPIO.HIGH)
		if localtine.tm_hour == r1_off:
			GPIO.output(relay1, GPIO.LOW)	
  	except:
    		# print('Relay 1 error!')
    		pass	
	

	try:
                if localtime.tm_hour == r2_on:
                        GPIO.output(relay2, GPIO.HIGH)
                if localtine.tm_hour == r2_off:
                        GPIO.output(relay2, GPIO.LOW)
        except:
                # print('Relay 2 error!')
                pass


  	try:
                if localtime.tm_hour == r3_on:
                        GPIO.output(relay3, GPIO.HIGH)
                if localtine.tm_hour == r3_off:
                        GPIO.output(relay3, GPIO.LOW)
        except:
                # print('Relay 3 error!')
                pass



	try:
                if localtime.tm_hour == r4_on:
                        GPIO.output(relay4, GPIO.HIGH)
                if localtine.tm_hour == r4_off:
                        GPIO.output(relay4, GPIO.LOW)
        except:
                # print('Relay 4 error!')
                pass
	sleep(600)
GPIO.cleanup()
