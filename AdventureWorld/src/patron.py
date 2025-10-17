import random
from dataclasses import dataclass

@dataclass
class Patron:
    name: str
    x: float
    y: float
    state: str = "roaming"  # roaming | queuing | riding

    def move(self, xmin=0, xmax=100, ymin=0, ymax=100):
        if self.state != "roaming":
            return
        # Larger random walk for more dynamic movement and crowd formation
        self.x += random.uniform(-1.5, 1.5)
        self.y += random.uniform(-1.5, 1.5)
        self.x = max(xmin, min(xmax, self.x))
        self.y = max(ymin, min(ymax, self.y))

    def plot(self, ax):
        # Color code by state with better styling
        if self.state == "roaming":
            color = "blue"
            marker = "o"
            size = 8
            edge = 'darkblue'
        elif self.state == "queuing":
            color = "orange"
            marker = "s"  # Square for queuing
            size = 10
            edge = 'darkorange'
        else:  # riding
            color = "green"
            marker = "*"  # Star for riding
            size = 12
            edge = 'darkgreen'
        
        ax.plot(self.x, self.y, marker=marker, markersize=size, color=color,
               markeredgecolor=edge, markeredgewidth=1.5)
