# WolScript
Python script for Wake-On-LAN devices by mail, runned with CRON.

## Description
Simple Python script for wake-up devices by looking a defined mail address, useful when ISPs blocking the MagicPacket sended over internet. The idea is to run this script one time for minute for 24h a day.

## Installation
Is sufficent to clone the repository in a destination folder:
```
git clone https://github.com/Jacopx/WolScript.git
cd WolScript
```
ensure that the `MailCheck.py` is executable, otherwise run:
```
chmod 775 MailCheck.py
```
This script need only one lib [wakeonlan](https://pypi.python.org/pypi/wakeonlan/0.2.2) that can be installed manually by the link provided or using the command
```
pip install wakeonlan
```
Is also necessary to add the mail addresses, used like destination address, and the password in the apposite variables and the MAC address of the device that you need to wake.

Now is time to define the cronjob, run the command:
```
crontab -e
```
and past this string:
```
*/1 * * * * python ~/pathtofolder/WolScript/MailCheck.py >> ~/pathtofolder/WolScript/wake.log
```
this string will run the script every minutes of the day. It will also print a little log file to look for problem or the mail and the time of the wake-up.

## Using
The operation need to use this script are really simple; the user only need to sand an email to the address writed in the script with the object `WOL` and nothing else. This will wake the device and print a log with something like this:
```
19/10 13:20 - WOL Packet Sended (Jacopo Nasi <jacopo.nasi@gmail.com>)
```

## Authors
* **Jacopo Nasi** - [Jacopx](https://github.com/Jacopx)
