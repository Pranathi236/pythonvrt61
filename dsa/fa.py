from collections import deque
import matplotlib.pyplot as plt
class openmic:
    def __init__(self):
        self.performers =[]
        self.audience = set()
        self.queue =