#!/usr/bin/env python3
from huskylib import HuskyLensLibrary
import time
import sys

hl = HuskyLensLibrary("SERIAL", "/dev/ttyAMA0", 9600)

while True:
    blocks = hl.requestAll()
    
    if not blocks:
        print("No objects detected")
        time.sleep(0.3)
        continue
        
    largest_area = 0
    chosen_id = None
        
    for block in blocks:
        if block.ID in (1, 2):
            area = block.width * block.height
            
            if block.ID != 0:
                print(f"ID:{block.ID} Area:{area}")
            
            if area > largest_area:
                largest_area = area
                chosen_id = block.ID
    
    if chosen_id == 1:
        print("Go Right (Red)")
    elif chosen_id == 2:
        print("Go Left (Green)")
        
    print("-----------------")    
    time.sleep(0.3)
