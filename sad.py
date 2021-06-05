import requests
from datetime import datetime, timedelta,time
import time as t
import discord_notify as dn
#update your discord bot link here
notifier = dn.Notifier("<link>")

while(True):
    now = datetime.utcnow().time()
    if(now>=time(17,50) and now<=time(23,5)): #The from and to time
        notifier.send("SAD", print_message=True)
        t.sleep(30) #time interval between each spam
