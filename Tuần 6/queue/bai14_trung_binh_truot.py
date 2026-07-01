from collections import deque


class HitCounter:
    def __init__(self, window=300):
        self.window = window
        self.events = deque()

    def hit(self, timestamp):
        self.events.append(timestamp)

    def get_hits(self, timestamp):
        while self.events and self.events[0] <= timestamp - self.window:
            self.events.popleft()
        return len(self.events)


class MovingAverage:
    def __init__(self, window):
        self.window = window
        self.values = deque()
        self.total = 0

    def add(self, value):
        self.values.append(value)
        self.total += value
        if len(self.values) > self.window:
            self.total -= self.values.popleft()

    def average(self):
        if not self.values:
            return 0
        return self.total / len(self.values)


hc = HitCounter(300)
hc.hit(1)
hc.hit(100)
hc.hit(200)
hc.hit(350)
print(f"Hits tai t=300: {hc.get_hits(300)}")
print(f"Hits tai t=400: {hc.get_hits(400)}")

ma = MovingAverage(3)
for v in [1, 2, 3, 4, 5]:
    ma.add(v)
    print(f"Trung binh truot: {ma.average():.2f}")
