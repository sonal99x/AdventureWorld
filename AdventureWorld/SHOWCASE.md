# Showcase

## Key Features Demonstration

### 1. Animated Rides
Each ride has unique motion characteristics:

**BoatRide**
- Horizontal oscillation: boat moves left-right while frame stays fixed
- Animation range: ±3 units from center
- Visual: Blue frame with moving boat icon

**FerrisWheel**
- Continuous rotation: 360-degree circular motion
- Patron positioning: Distributed around wheel perimeter
- Animation: Smooth angular progression

**RollerCoaster**
- Vertical movement: Up-down wave motion
- Track simulation: Y-position varies dynamically
- Speed: Variable based on ride state

**SpiderRide**
- Radial spinning: Arms extend and rotate
- Multi-axis motion: Both rotation and extension
- Visual complexity: Most dynamic animation

### 2. Weather System
Three weather conditions with visual effects:

**Sunny** ☀️
- Clear yellow background (#FFFACD)
- Optimal visibility
- Default pleasant atmosphere

**Rain** 🌧️
- Gray background (#D3D3D3)
- 100 blue raindrops falling
- Vertical motion simulation

**Snow** ❄️
- Light gray background (#E8E8E8)
- 80 white snowflakes
- Gentle floating motion

**Dynamic Mode**
- Automatic cycling every 150 steps
- Smooth transitions between conditions
- Demonstrates environmental system

### 3. Patron Management
Visual state indicators:

**Roaming** (Blue circles ●)
- Random movement across park
- Autonomous pathfinding
- Searching for attractions

**Queuing** (Orange squares ■)
- Lined up at ride entrance
- Stacked vertically: size 10 markers
- Waiting for capacity

**Riding** (Green stars ★)
- Positioned on active ride
- Radial distribution around ride center
- Following ride animations

### 4. Visual Enhancements
Professional appearance:

**Ride Boxes**
- Size: 20×12 units (maximized footprint)
- Borders: 8px main + 4px inner for depth
- Shadows: Offset rectangles for 3D effect
- No text labels: Clean minimalist design

**Color Scheme**
- BoatRide: Blue (#4169E1)
- FerrisWheel: Red (#DC143C)
- RollerCoaster: Green (#228B22)
- SpiderRide: Purple (#9370DB)

## Usage Examples

### Interactive Mode
```bash
python src/adventureworld.py -i
```
Prompts for:
- Park layout file (map1.csv)
- Parameters file (params1.csv)
- Real-time user input during execution

### Batch Mode
```bash
python src/adventureworld.py -f data/map1.csv -p data/params1.csv
```
Automated execution:
- Pre-configured settings
- Continuous animation
- No user intervention required

### Testing
```bash
python test_rides_animation.py
```
Verification script:
- Tests all 4 ride animations
- Validates state transitions
- Confirms patron loading

## Screenshots Guide

### What to Observe
1. **Ride Animation**: Watch boat oscillate, wheel rotate, coaster wave
2. **Weather Changes**: Observe background and particle effects at steps 150, 300
3. **Patron Flow**: Track color changes as patrons queue and ride
4. **Queue Formation**: See orange squares stack at ride entrances
5. **Riding Positions**: Notice green stars distributed on active rides

## Performance Metrics

### Simulation Speed
- Steps per second: ~30
- Animation frame rate: ~30 FPS
- Responsiveness: Real-time interactive

### Capacity Handling
- BoatRide: 4 patrons
- FerrisWheel: 8 patrons
- RollerCoaster: 6 patrons
- SpiderRide: 4 patrons
- Total: 22 simultaneous riders

### Weather Effects
- Rain particles: 100
- Snow particles: 80
- Rendering overhead: <5% performance impact
