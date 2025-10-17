import csv
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from rides import BoatRide, PirateShip, FerrisWheel, RollerCoaster, SpiderRide
from patron import Patron

class Simulation:
    def __init__(self):
        self.boundary = (0, 0, 100, 100)  # xmin, ymin, xmax, ymax
        self.rides = []
        self.patrons = []
        self.steps = 300
        self.weather = "sunny"  # sunny, rain, snow

    def load_map(self, map_csv_path: str):
        with open(map_csv_path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                t = row["type"]
                if t == "boundary":
                    self.boundary = (
                        float(row["x"]),
                        float(row["y"]),
                        float(row["x"]) + float(row["width"]),
                        float(row["y"]) + float(row["height"]),
                    )
                elif t == "ride_box":
                    name = row["name"]
                    x, y = float(row["x"]), float(row["y"])
                    w, h = float(row["width"]), float(row["height"])
                    if name == "ride1":
                        self.rides.append(BoatRide(name, x, y, w, h))
                    elif name == "ride2":
                        self.rides.append(FerrisWheel(name, x, y, w, h))
                    elif name == "ride3":
                        self.rides.append(RollerCoaster(name, x, y, w, h))
                    elif name == "ride4":
                        self.rides.append(SpiderRide(name, x, y, w, h))
                # entrances/exits ignored in this minimal version

    def load_params(self, params_csv_path: str):
        params = {}
        with open(params_csv_path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                params[row["param"]] = row["value"]
        return params

    def apply_params(self, params):
        random.seed(int(params.get("seed", "0")))
        self.steps = int(params.get("steps", "300"))
        self.weather_mode = params.get("weather", "dynamic")  # dynamic, sunny, rain, snow
        self.weather = "sunny"  # Current weather state

        num_patrons = int(params.get("num_patrons", "20"))
        xmin, ymin, xmax, ymax = self.boundary
        
        # Spawn patrons distributed across the park for crowd effect
        for i in range(num_patrons):
            # Random positions across the entire park
            spawn_x = random.uniform(xmin + 5, xmax - 5)
            spawn_y = random.uniform(ymin + 5, ymax - 5)
            self.patrons.append(Patron(f"P{i+1}", x=spawn_x, y=spawn_y))

        for r in self.rides:
            cap = params.get(f"{r.name}.capacity")
            dur = params.get(f"{r.name}.duration_steps")
            spd = params.get(f"{r.name}.speed_deg_per_step")
            if cap: r.capacity = int(cap)
            if dur: r.duration_steps = int(dur)
            if spd: 
                r.speed_deg_per_step = int(spd)

    @staticmethod
    def _inside_bbox(x, y, bbox):
        xmin, ymin, xmax, ymax = bbox
        return xmin <= x <= xmax and ymin <= y <= ymax

    def step_once(self):
        xmin, ymin, xmax, ymax = self.boundary
        for p in self.patrons:
            if p.state == "roaming":
                # Try to move the patron
                old_x, old_y = p.x, p.y
                p.move(xmin, xmax, ymin, ymax)
                
                # Check if patron is near any ride (expanded queue area)
                for r in self.rides:
                    rx_min, ry_min, rx_max, ry_max = r.bbox()
                    queue_margin = 8.0  # Even larger queue detection area for crowds
                    
                    # Check if patron is near the ride (within queue area)
                    near_x = rx_min - queue_margin <= p.x <= rx_max + queue_margin
                    near_y = ry_min - queue_margin <= p.y <= ry_max + queue_margin
                    
                    if near_x and near_y:
                        # Check if they're not inside the ride (keep them outside)
                        inside = self._inside_bbox(p.x, p.y, r.bbox())
                        
                        if inside:
                            # Move them to the nearest edge
                            p.x, p.y = old_x, old_y
                        else:
                            # Join the queue with HIGH probability for crowds
                            import random
                            if random.random() < 0.6:  # 60% chance per step - more aggressive
                                p.state = "queuing"
                                r.queue.append(p)
                        break

        for r in self.rides:
            r.step_change()

    def run(self):
        plt.ion()
        fig, ax = plt.subplots(figsize=(14, 10))
        fig.patch.set_facecolor('#e8f4f8')  # Light blue background
        
        for step in range(self.steps):
            self.step_once()
            
            # Dynamic weather system - cycle through weather conditions
            if self.weather_mode == "dynamic":
                if step % 150 == 0:  # Change weather every 150 steps
                    weather_options = ["sunny", "rain", "snow"]
                    self.weather = weather_options[(step // 150) % 3]
            else:
                self.weather = self.weather_mode  # Use fixed weather from params

            ax.clear()
            
            # Set background color based on weather
            if self.weather == "rain":
                ax.set_facecolor('#6B8E6B')  # Darker green for rain
                fig.patch.set_facecolor('#A9B5C4')  # Gray-blue for rain
            elif self.weather == "snow":
                ax.set_facecolor('#E8F4F8')  # Light blue-white for snow
                fig.patch.set_facecolor('#F0F8FF')  # Alice blue for snow
            else:  # sunny
                ax.set_facecolor('#90EE90')  # Light green grass color
                fig.patch.set_facecolor('#e8f4f8')  # Light blue background
            
            xmin, ymin, xmax, ymax = self.boundary
            ax.set_xlim(xmin - 10, xmax + 10)
            ax.set_ylim(ymin - 10, ymax + 10)
            ax.set_aspect('equal')
            
            # Draw weather effects FIRST (behind everything)
            if self.weather == "rain":
                # Draw rain drops
                for _ in range(100):
                    rx = random.uniform(xmin - 10, xmax + 10)
                    ry = random.uniform(ymin - 10, ymax + 10)
                    ax.plot([rx, rx - 1], [ry, ry - 3], color='#4682B4', linewidth=1.5, alpha=0.6)
            elif self.weather == "snow":
                # Draw snow flakes
                for _ in range(80):
                    sx = random.uniform(xmin - 10, xmax + 10)
                    sy = random.uniform(ymin - 10, ymax + 10)
                    ax.plot(sx, sy, marker='*', markersize=6, color='white', 
                           markeredgecolor='lightblue', markeredgewidth=0.5, alpha=0.8)
            
            # Beautiful title with styling and weather indicator
            weather_emoji = {"sunny": "☀️", "rain": "🌧️", "snow": "❄️"}
            title_text = f'🎢 Adventure World Theme Park 🎡 {weather_emoji.get(self.weather, "")}'
            ax.text(50, 115, title_text, 
                   ha="center", va="center", fontsize=20, weight='bold',
                   bbox=dict(boxstyle='round,pad=1', facecolor='#FFD700', 
                            edgecolor='#FF6347', linewidth=3),
                   color='#8B0000')
            
            # Step counter with styling
            step_text = f'Step: {step + 1}/{self.steps}'
            ax.text(50, 108, step_text, ha="center", va="center", 
                   fontsize=12, weight='bold',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                            edgecolor='blue', linewidth=2))
            
            ax.set_xlabel("X Position", fontsize=12, weight='bold')
            ax.set_ylabel("Y Position", fontsize=12, weight='bold')
            ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

            # Draw beautiful boundary with double border
            boundary_rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, 
                                            fill=False, linewidth=4, edgecolor='#8B4513')
            ax.add_patch(boundary_rect)
            boundary_rect2 = patches.Rectangle((xmin-1, ymin-1), xmax - xmin + 2, ymax - ymin + 2, 
                                             fill=False, linewidth=2, edgecolor='#D2691E', 
                                             linestyle='--')
            ax.add_patch(boundary_rect2)
            
            # Add entrance marker
            entrance_rect = patches.FancyBboxPatch((45, -3), 10, 3,
                                                   boxstyle="round,pad=0.1",
                                                   facecolor='#32CD32', edgecolor='darkgreen',
                                                   linewidth=2)
            ax.add_patch(entrance_rect)
            ax.text(50, -1.5, '🚪 ENTRANCE', ha="center", va="center",
                   fontsize=10, weight='bold', color='white')

            # Draw rides with enhanced visuals
            for r in self.rides:
                r.plot(ax)
                # Enhanced queue info with background
                queue_text = f'👥 Queue: {len(r.queue)} | 🎠 Riding: {len(r.on_ride)}/{r.capacity}'
                bbox_color = {'idle': '#D3D3D3', 'loading': '#FFD700', 
                             'running': '#90EE90', 'unloading': '#FFB6C1'}.get(r.state, '#D3D3D3')
                ax.text(r.x, r.y - r.bbox_h/2 - 4, queue_text, 
                       ha="center", va="top", fontsize=9, weight='bold',
                       bbox=dict(boxstyle='round,pad=0.5', facecolor=bbox_color, 
                                edgecolor='black', linewidth=1.5))
                
                # Position queuing patrons in a line near the ride
                for i, p in enumerate(r.queue):
                    p.x = r.x - r.bbox_w/2 - 2
                    p.y = r.y + r.bbox_h/2 - i * 1.5  # Stack them vertically
                
                # Position riding patrons inside the ride
                for i, p in enumerate(r.on_ride):
                    # Spread riders across the ride area
                    radius = min(r.bbox_w, r.bbox_h) / 4
                    p.x = r.x + radius * (i % 3 - 1)  # Distribute horizontally
                    p.y = r.y + radius * (i // 3 - 0.5)  # Distribute vertically
            
            # Draw patrons with enhanced styling
            for p in self.patrons:
                p.plot(ax)
            
            # Enhanced legend with icons
            from matplotlib.lines import Line2D
            legend_elements = [
                Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', 
                       markersize=10, label='🚶 Roaming', markeredgecolor='darkblue', markeredgewidth=2),
                Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', 
                       markersize=10, label='⏳ Queuing', markeredgecolor='darkorange', markeredgewidth=2),
                Line2D([0], [0], marker='o', color='w', markerfacecolor='green', 
                       markersize=10, label='🎢 Riding', markeredgecolor='darkgreen', markeredgewidth=2)
            ]
            legend = ax.legend(handles=legend_elements, loc='upper right', fontsize=11,
                             framealpha=0.95, edgecolor='black', fancybox=True, shadow=True)
            legend.get_frame().set_facecolor('#FFFACD')
            
            # Add statistics panel
            total_queuing = sum(1 for p in self.patrons if p.state == "queuing")
            total_riding = sum(1 for p in self.patrons if p.state == "riding")
            total_roaming = sum(1 for p in self.patrons if p.state == "roaming")
            
            stats_text = f'📊 Statistics\n'
            stats_text += f'Roaming: {total_roaming}\n'
            stats_text += f'Queuing: {total_queuing}\n'
            stats_text += f'Riding: {total_riding}'
            
            ax.text(-8, 85, stats_text, fontsize=10, weight='bold',
                   bbox=dict(boxstyle='round,pad=0.8', facecolor='#FFF8DC',
                            edgecolor='#8B4513', linewidth=2),
                   verticalalignment='top', family='monospace')

            plt.tight_layout()
            plt.pause(0.01)

        plt.ioff()
        plt.show()
