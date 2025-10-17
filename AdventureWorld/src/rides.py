import math
from dataclasses import dataclass, field
import matplotlib.patches as patches

@dataclass
class Ride:
    name: str
    x: float
    y: float
    bbox_w: float
    bbox_h: float
    capacity: int = 8
    duration_steps: int = 30
    state: str = "idle"        # idle | loading | running | unloading
    angle_deg: float = 0.0
    dir_sign: int = 1          # 1 forward, -1 backward
    step_counter: int = 0
    queue: list = field(default_factory=list)     # patrons waiting
    on_ride: list = field(default_factory=list)   # patrons currently riding

    def bbox(self):
        return (self.x - self.bbox_w / 2, self.y - self.bbox_h / 2,
                self.x + self.bbox_w / 2, self.y + self.bbox_h / 2)

    def step_change(self):
        pass

    def try_board(self):
        while len(self.on_ride) < self.capacity and self.queue:
            p = self.queue.pop(0)
            p.state = "riding"
            self.on_ride.append(p)

    def unload(self):
        for p in self.on_ride:
            p.state = "roaming"
        self.on_ride.clear()

    def plot(self, ax):
        xmin, ymin, xmax, ymax = self.bbox()
        # Draw bounding box with different colors and effects based on state
        color_map = {
            "idle": "#B0B0B0", 
            "loading": "#FFD700", 
            "running": "#32CD32", 
            "unloading": "#FF69B4"
        }
        color = color_map.get(self.state, "#B0B0B0")
        
        # Draw shadow effect - LARGER
        shadow = patches.Rectangle((xmin+1, ymin-1), self.bbox_w, self.bbox_h,
                                   fill=True, facecolor='black', alpha=0.3, linewidth=0)
        ax.add_patch(shadow)
        
        # Draw main bounding box with THICKER borders
        main_box = patches.Rectangle((xmin, ymin), self.bbox_w, self.bbox_h, 
                                     fill=True, facecolor=color, alpha=0.4,
                                     linewidth=8, edgecolor=color)  # Increased from 3 to 8
        ax.add_patch(main_box)
        
        # Draw inner border - THICKER
        inner_box = patches.Rectangle((xmin+0.5, ymin+0.5), self.bbox_w-1, self.bbox_h-1,
                                     fill=False, linewidth=4, edgecolor='white',  # Increased from 1.5 to 4
                                     linestyle='--', alpha=0.9)
        ax.add_patch(inner_box)
        
        # Text removed - no label on ride box


class BoatRide(Ride):
    def __init__(self, name, x, y, bbox_w, bbox_h, capacity=10, duration_steps=40):
        super().__init__(name, x, y, bbox_w, bbox_h, capacity, duration_steps)
        self.boat_offset = 0
        self.boat_direction = 1
        self.frame_color = "blue"
        self.ship_color = "brown"

    def step_change(self):
        # Animate the boat moving back and forth
        self.boat_offset += self.boat_direction * 0.3
        if abs(self.boat_offset) >= 3:
            self.boat_direction *= -1
        
        if self.state == "idle":
            if self.queue:
                self.state = "loading"
                self.step_counter = 0

        elif self.state == "loading":
            self.try_board()
            self.state = "running"
            self.step_counter = 0

        elif self.state == "running":
            self.step_counter += 1
            if self.step_counter >= self.duration_steps:
                self.state = "unloading"
                self.step_counter = 0

        elif self.state == "unloading":
            self.unload()
            self.state = "idle"

    def plot(self, ax):
        super().plot(ax)
        
        # Scale factor for the boat
        scale = min(self.bbox_w, self.bbox_h) / 8
        base_x = self.x  # Frame stays fixed at center
        base_y = self.y
        boat_x = self.x + self.boat_offset  # Boat moves
        
        # Draw the frame (blue rectangle structure) - STABLE/FIXED
        frame_x = [1, 2, 3, 4, 5]
        frame_y = [1, 3, 5, 3, 1]
        frame_x1 = [2, 3, 4]
        frame_y1 = [3, 3, 3]
        
        # Scale and position frame (FIXED position)
        fx = [base_x + (val - 3) * scale * 0.8 for val in frame_x]
        fy = [base_y + (val - 3) * scale * 0.6 for val in frame_y]
        fx1 = [base_x + (val - 3) * scale * 0.8 for val in frame_x1]
        fy1 = [base_y + (val - 3) * scale * 0.6 for val in frame_y1]
        
        ax.plot(fx, fy, color=self.frame_color, linewidth=3, zorder=8)
        ax.plot(fx1, fy1, color=self.frame_color, linewidth=3, zorder=8)
        
        # Draw the ship (brown boat shape) - MOVING
        ship_x = [1, 2, 4, 5, 3, 1]
        ship_y = [3, 1.5, 1.5, 3, 5, 3]
        ship_x1 = [1, 2, 4, 5]
        ship_y1 = [3, 2.5, 2.5, 3]
        
        # Scale and position ship (MOVING position with boat_offset)
        sx = [boat_x + (val - 3) * scale * 0.8 for val in ship_x]
        sy = [base_y + (val - 3) * scale * 0.6 for val in ship_y]
        sx1 = [boat_x + (val - 3) * scale * 0.8 for val in ship_x1]
        sy1 = [base_y + (val - 3) * scale * 0.6 for val in ship_y1]
        
        ax.plot(sx, sy, color=self.ship_color, linewidth=3, zorder=9)
        ax.plot(sx1, sy1, color=self.ship_color, linewidth=3, zorder=9)
        
        # Fill the boat
        ax.fill(sx, sy, color=self.ship_color, alpha=0.5, zorder=7)


class PirateShip(Ride):
    def __init__(self, name, x, y, bbox_w, bbox_h, capacity=8, duration_steps=30, speed_deg_per_step=5):
        super().__init__(name, x, y, bbox_w, bbox_h, capacity, duration_steps)
        self.speed_deg_per_step = speed_deg_per_step

    def step_change(self):
        # Always animate the swing
        self.angle_deg += self.dir_sign * self.speed_deg_per_step
        if abs(self.angle_deg) >= 45:
            self.dir_sign *= -1
        
        if self.state == "idle":
            if self.queue:
                self.state = "loading"
                self.step_counter = 0

        elif self.state == "loading":
            self.try_board()
            self.state = "running"
            self.step_counter = 0

        elif self.state == "running":
            self.step_counter += 1
            if self.step_counter >= self.duration_steps:
                self.state = "unloading"
                self.step_counter = 0

        elif self.state == "unloading":
            self.unload()
            self.state = "idle"

    def plot(self, ax):
        super().plot(ax)
        boom_len = min(self.bbox_w, self.bbox_h) * 0.8
        x_end = self.x + boom_len * math.sin(math.radians(self.angle_deg))
        y_end = self.y + boom_len * math.cos(math.radians(self.angle_deg))
        
        # Draw boom arm with gradient effect
        ax.plot([self.x, x_end], [self.y, y_end], linewidth=5, color='#4169E1', alpha=0.8)
        ax.plot([self.x, x_end], [self.y, y_end], linewidth=3, color='#1E90FF')
        
        # Draw pivot point
        ax.plot(self.x, self.y, marker='o', markersize=15, color='#2F4F4F',
               markeredgecolor='black', markeredgewidth=2, zorder=10)
        
        # Draw the ship at the end with detail
        ship_size = 15
        ax.plot(x_end, y_end, marker='s', markersize=ship_size, color='#8B4513',
               markeredgecolor='#654321', markeredgewidth=2, zorder=10)
        # Add ship detail
        ax.plot(x_end, y_end, marker='o', markersize=5, color='yellow', zorder=11)


class FerrisWheel(Ride):
    def __init__(self, name, x, y, bbox_w, bbox_h, capacity=12, duration_steps=60, speed_deg_per_step=3):
        super().__init__(name, x, y, bbox_w, bbox_h, capacity, duration_steps)
        self.angle_deg = 0
        self.speed_deg_per_step = speed_deg_per_step

    def step_change(self):
        # Always animate the wheel rotation
        self.angle_deg += self.speed_deg_per_step
        if self.angle_deg >= 360:
            self.angle_deg = 0
        
        if self.state == "idle":
            if self.queue:
                self.state = "loading"
                self.step_counter = 0

        elif self.state == "loading":
            self.try_board()
            self.state = "running"
            self.step_counter = 0

        elif self.state == "running":
            self.step_counter += 1
            if self.step_counter >= self.duration_steps:
                self.state = "unloading"
                self.step_counter = 0

        elif self.state == "unloading":
            self.unload()
            self.state = "idle"

    def plot(self, ax):
        super().plot(ax)
        radius = min(self.bbox_w, self.bbox_h) / 2.5
        
        # Draw the wheel circle with multiple layers
        circle_outer = patches.Circle((self.x, self.y), radius+0.3, fill=False, 
                                     linewidth=4, edgecolor='#8B008B', alpha=0.8)
        ax.add_patch(circle_outer)
        circle = patches.Circle((self.x, self.y), radius, fill=False, 
                               linewidth=3, edgecolor='#9370DB')
        ax.add_patch(circle)
        circle_inner = patches.Circle((self.x, self.y), radius-0.5, fill=False,
                                     linewidth=2, edgecolor='#BA55D3', linestyle='--')
        ax.add_patch(circle_inner)
        
        # Draw spokes with gradient
        for i in range(8):
            angle = self.angle_deg + i * 45
            x_end = self.x + radius * math.cos(math.radians(angle))
            y_end = self.y + radius * math.sin(math.radians(angle))
            ax.plot([self.x, x_end], [self.y, y_end], linewidth=2, color='#9370DB', alpha=0.7)
        
        # Draw center hub
        hub = patches.Circle((self.x, self.y), radius*0.15, fill=True,
                           facecolor='#8B008B', edgecolor='black', linewidth=2)
        ax.add_patch(hub)
        
        # Draw gondolas at multiple positions
        for i in range(4):
            angle = self.angle_deg + i * 90
            x_gondola = self.x + radius * math.cos(math.radians(angle))
            y_gondola = self.y + radius * math.sin(math.radians(angle))
            ax.plot(x_gondola, y_gondola, marker='o', markersize=12, color='#9370DB',
                   markeredgecolor='#8B008B', markeredgewidth=2, zorder=10)


class RollerCoaster(Ride):
    def __init__(self, name, x, y, bbox_w, bbox_h, capacity=8, duration_steps=30, speed_deg_per_step=1):
        super().__init__(name, x, y, bbox_w, bbox_h, capacity, duration_steps)
        self.y_position = y
        self.y_start = y
        self.speed_deg_per_step = speed_deg_per_step  # Not used for angle, but for consistency

    def step_change(self):
        # Always animate the vertical movement
        self.y_position += 0.5
        if self.y_position > self.y_start + 10:
            self.y_position = self.y_start
        
        if self.state == "idle":
            if self.queue:
                self.state = "loading"
                self.step_counter = 0

        elif self.state == "loading":
            self.try_board()
            self.state = "running"
            self.step_counter = 0

        elif self.state == "running":
            self.step_counter += 1
            if self.step_counter >= self.duration_steps:
                self.state = "unloading"
                self.step_counter = 0

        elif self.state == "unloading":
            self.unload()
            self.state = "idle"

    def plot(self, ax):
        super().plot(ax)
        # Draw track with rails
        track_height = 12
        # Left rail
        ax.plot([self.x - 0.5, self.x - 0.5], [self.y_start, self.y_start + track_height], 
                linewidth=3, color='#696969', linestyle='-', alpha=0.8)
        # Right rail
        ax.plot([self.x + 0.5, self.x + 0.5], [self.y_start, self.y_start + track_height], 
                linewidth=3, color='#696969', linestyle='-', alpha=0.8)
        # Cross beams
        for i in range(0, int(track_height)+1, 2):
            ax.plot([self.x - 0.5, self.x + 0.5], 
                   [self.y_start + i, self.y_start + i],
                   linewidth=1, color='#A9A9A9', linestyle='--', alpha=0.5)
        
        # Draw the coaster car with detail
        car_size = 15
        # Car body
        ax.plot(self.x, self.y_position, marker='s', markersize=car_size, color='#DC143C',
               markeredgecolor='#8B0000', markeredgewidth=3, zorder=10)
        # Car window
        ax.plot(self.x, self.y_position, marker='o', markersize=6, color='#87CEEB',
               zorder=11)
        # Motion trail effect
        if self.y_position > self.y_start + 1:
            ax.plot(self.x, self.y_position - 1, marker='o', markersize=4, 
                   color='red', alpha=0.3)


class SpiderRide(Ride):
    def __init__(self, name, x, y, bbox_w, bbox_h, capacity=8, duration_steps=30, speed_deg_per_step=5):
        super().__init__(name, x, y, bbox_w, bbox_h, capacity, duration_steps)
        self.angle_deg = 0
        self.speed_deg_per_step = speed_deg_per_step
        self.num_arms = 6

    def step_change(self):
        # Always animate the rotation
        self.angle_deg += self.speed_deg_per_step
        if self.angle_deg >= 360:
            self.angle_deg = 0
        
        if self.state == "idle":
            if self.queue:
                self.state = "loading"
                self.step_counter = 0

        elif self.state == "loading":
            self.try_board()
            self.state = "running"
            self.step_counter = 0

        elif self.state == "running":
            self.step_counter += 1
            if self.step_counter >= self.duration_steps:
                self.state = "unloading"
                self.step_counter = 0

        elif self.state == "unloading":
            self.unload()
            self.state = "idle"

    def plot(self, ax):
        super().plot(ax)
        radius = min(self.bbox_w, self.bbox_h) / 2.5
        
        # Draw center platform
        center_platform = patches.Circle((self.x, self.y), radius*0.2, fill=True,
                                        facecolor='#FF8C00', edgecolor='#FF4500', 
                                        linewidth=3)
        ax.add_patch(center_platform)
        
        # Draw rotating arms with gradient effect
        for i in range(self.num_arms):
            angle = self.angle_deg + (360 / self.num_arms) * i
            x_end = self.x + radius * math.cos(math.radians(angle))
            y_end = self.y + radius * math.sin(math.radians(angle))
            
            # Arm with double line effect
            ax.plot([self.x, x_end], [self.y, y_end], linewidth=4, 
                   color='#FF8C00', alpha=0.6, zorder=5)
            ax.plot([self.x, x_end], [self.y, y_end], linewidth=2, 
                   color='#FFA500', zorder=6)
            
            # Draw seats at the end of each arm with detail
            ax.plot(x_end, y_end, marker='o', markersize=14, color='#FF6347',
                   markeredgecolor='#FF4500', markeredgewidth=2, zorder=10)
            # Seat detail
            ax.plot(x_end, y_end, marker='*', markersize=6, color='yellow', zorder=11)
        
        # Add motion blur effect in rotation direction
        blur_angle = self.angle_deg - 15
        for i in range(self.num_arms):
            angle = blur_angle + (360 / self.num_arms) * i
            x_blur = self.x + radius * 0.95 * math.cos(math.radians(angle))
            y_blur = self.y + radius * 0.95 * math.sin(math.radians(angle))
            ax.plot(x_blur, y_blur, marker='o', markersize=8, color='orange',
                   alpha=0.3, zorder=4)
