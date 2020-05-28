import numpy as np
from collections import deque, Counter
import os, sys, random, json, re

class Node:
    def __init__(self, index, node_type):
        self.index = index
        self.node_types = ["workstation", "server"]
        self.node_subtypes = ["general", "developer", "finance", "management"]
        self.node_type = node_type
        self.is_server = False
        if self.node_type == "server":
            self.is_server = True
        self.compromised = False
        self.is_asleep = False
        self.node_subtype = random.choice(self.node_subtypes)
        self.anomaly_counter = Counter()
        self.interactions = {}

