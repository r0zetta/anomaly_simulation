import numpy as np
from collections import deque, Counter
import os, sys, random, json, re

class Chrono:
    def __init__(self):
        self.hours_per_day = 24
        self.ticks_per_hour = 6
        self.current_day = 1
        self.current_hour = 0
        self.current_tick = 0
        self.tick = 0

    def is_weekend(self):
        if self.current_day % 6 == 0 or self.current_day % 7 == 0:
            return True
        return False

    def increment_chrono(self):
        day_changed = False
        self.tick += 1
        self.current_tick += 1
        if self.current_tick >= self.ticks_per_hour:
            self.current_tick = 0
            self.current_hour += 1
            if self.current_hour >= self.hours_per_day:
                self.current_hour = 0
                self.current_day += 1
                day_changed = True
        return day_changed

    def print_chrono(self):
        msg = ""
        msg += "Day: " + "%03d"%self.current_day
        msg += " Hour: " + "%02d"%self.current_hour
        msg += " Min: " + "%02d"%(self.current_tick*10)
        return msg


