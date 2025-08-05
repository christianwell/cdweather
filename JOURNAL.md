# [slack help thread with over 800 replies](https://hackclub.slack.com/archives/C08Q1H6D79B/p1753263231925269
# start jul 23rd 
# 11:33 AM
I asked on the highway which sensors I should use, and quickly got an answer that I should use BME280, so that's the one I went with
# 12:51 PM 
In my first schematic try, I was told to look up Lookup I2C communication, but I did not listen 
![schematic](https://hc-cdn.hel1.your-objectstorage.com/s/v3/12de001196c04f2b84216886db209086e8654ef0_image.png) 
# 3:43 pm 
I wanted to redo, but when I asked if this was fine, I got told to use net labels and pull-ups on the I2C line, but I did not, cuz I got told it's fine without
(comes back to hunt me)
![schematic2](https://hc-cdn.hel1.your-objectstorage.com/s/v3/7af9a0fb9cac4c0c9c3ff72a1070fb790a8f1c3d_image.png)

# 8:31 pm
So I planned to make this send as an API, BUT what I did not think of was that the Xiao RP2040 does not have wifi, so I had to find a new MCU. I end up using a esp ESP32 C3 Super Mini Development Board
# 9:48 PM 
I made this PCB, you see, but got told "NO 90deg ANGLES " and I should use line 45
![pcb](https://hc-cdn.hel1.your-objectstorage.com/s/v3/7af9a0fb9cac4c0c9c3ff72a1070fb790a8f1c3d_image.png)
![pcb](
# 10:17 PM
Got told "All your wires should NOT be 90 degrees,"  so I had to redo
![pcb](https://hc-cdn.hel1.your-objectstorage.com/s/v3/7701d2ca63e1bcf58b1c0394f84f39fe715822b2_image.png)

# jul 24th
# 10:45 am
Got told I still have some 90 ° angles, so I had to redo
![pcb](https://hc-cdn.hel1.your-objectstorage.com/s/v3/1439f19e54ec6cdd92cd26cc27464c68705dfda5_image.png)

# jul 25th
# 10:45 am
I got told I had to add pull-ups, so I tried, but it was not right 
![pcb](https://hc-cdn.hel1.your-objectstorage.com/s/v3/645806c019f18b36fa5388106746f5180daafed0_image.png)
# 6:30 PM
I FINALLY DID PULL UPS RIGHT ONTO PCB
![pcb](https://hc-cdn.hel1.your-objectstorage.com/s/v3/b89c96fd7dbdf7164aa5afa0ef3b11c601c8df95_image.png)

# 7:54 pm 
I had some errors I did before, like no sharp trace, but I ended up making this, BUT I had to optimize
![pcb](https://hc-cdn.hel1.your-objectstorage.com/s/v3/3792d98f8a0a3c6bb42c1b290a7c9f986a7f5f9f_image.png)

# 9:14 PM
I had one thing wrong via as someone says, and I quickly fixed it.
![pcb](https://hc-cdn.hel1.your-objectstorage.com/s/v3/3792d98f8a0a3c6bb42c1b290a7c9f986a7f5f9f_image.png)


# 3d case
3d case took me maybe 1/2hours cuz I know what I was doing
