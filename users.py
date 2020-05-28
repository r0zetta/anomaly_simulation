import numpy as np
from collections import deque, Counter
import os, sys, random, json, re

class User:
    def __init__(self, index, user_type, user_subtype):
        self.index = index
        self.worker_types = ["scheduled", "sporadic", "morning", "evening", "workaholic"]
        self.favourites = []
        self.user_type = user_type
        self.user_subtype = user_subtype
        self.is_admin = False
        if self.user_type == "admin":
            self.is_admin = True
            self.worker_type = "sporadic"
        else:
            self.worker_type = random.choice(self.worker_types)
        self.sleeps_nights = False
        self.sleeps_weekends = False
        self.works_weekends = False
        if self.worker_type in ["sporadic", "workaholic"]:
            self.works_weekends = True
        if random.random() > 0.9:
            self.sleeps_nights = True
        if self.sleeps_nights == True:
            self.sleeps_weekends = True
        else:
            if random.random() > 0.9:
                self.sleeps_weekends = True
        self.working = True
        self.compromised = False

    def set_favourites(self, favourites):
        self.favourites = list(favourites)

    def add_favourite(self, index):
        self.favourites.append(index)

    def set_work_time(self, chrono):
        self.work_time = []
        weekend = chrono.is_weekend()
        if weekend == True and self.worker_type not in ["sporadic", "workaholic"]:
            return
        if self.worker_type == "scheduled":
            logon = 8
            logoff = 16
            self.work_time = range(logon, logoff)
        elif self.worker_type == "morning":
            logon = random.randint(6, 8)
            logoff = logon + random.randint(6, 8)
            self.work_time = range(logon, logoff)
        elif self.worker_type == "evening":
            logon = random.randint(11, 13)
            logoff = logon + random.randint(6, 8)
            self.work_time = range(logon, logoff)
        elif self.worker_type == "workaholic":
            logon = random.randint(0, 10)
            logoff = logon + random.randint(10, 12)
            self.work_time = range(logon, logoff)
        elif self.worker_type == "sporadic":
            logon1 = random.randint(0, 12)
            logoff1 = logon1 + random.randint(5, 8)
            logon2 = logoff1 + random.randint(1, 3)
            logoff2 = logon2 + random.randint(1, 3)
            self.work_time = list(range(logon1, logoff1))
            self.work_time.extend(range(logon2, logoff2))

    def is_working(self, chrono):
        if chrono.current_hour in self.work_time:
            return True
        return False

