# MiniAutomation
Automating using BeagleBone Black

![BBB](/img/bbb.JPG "BBB")

## BeagleBone Relay Cape
4x 15A @ 24VDC/12A @ 250VAC relays

I2C EEPROM

You can have this Cape from here:
https://beagleboard.org/capes


## How to use it directly:

```
python automate.py --relay1_on 22 --relay1_off 23 --relay2_on 23 --relay2_off 24 --relay3_on 24 --relay3_off 25 --relay4_on 25 --relay4_off 26
```

## How to run it at startup:

```
sudo crontab -e
```

Add the following:

```
@reboot sleep 30 && /home/debian/MiniAutomation/automate.sh
```

Make sure to start crond automatically at boot time:

```
sudo systemctl enable cron.service
sudo systemctl start cron.service
sudo systemctl stop cron.service
sudo systemctl restart cron.service
sudo systemctl status cron.service
```