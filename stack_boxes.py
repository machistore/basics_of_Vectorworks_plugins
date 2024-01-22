# Purpose: Create a stack of boxes in Vectorworks
# Author: Katsutoshi Machida
# Date: 2024-01-22
# Python Version: 3.9.2
# Vectorworks Version: 2023
# License: MIT License
# Notes: This script is intended to be run from within Vectorworks
#  using the Vectorworks Python Scripting tool. It will not run
#  in a standalone Python interpreter.
#  This script was written for a specific purpose and may not
#  work in all cases. Use at your own risk.
#  This script is provided as-is without any warranty.
import vs

def stack_rectangles(num_rectangles, x_length, y_length, z_height): # Define function
    for i in range(num_rectangles): # Loop through rectangles
        vs.BeginXtrd(i * z_height, (i + 1) * z_height) # Begin extrude
        vs.Rect(0, 0, x_length, y_length) # Draw rectangle
        vs.EndXtrd() # End extrude

stack_rectangles(5, 910, 1820, 24) # Call function

