## Synopsis## Synopsis## Synopsis# Adventure World Theme Park Simulation# Adventure World Theme Park Simulation# Adventure World Theme Park Simulation# Adventure World Theme Park Simulation

Assignment of Fundamentals of Programming COMP1005/5005

Assignment of Fundamentals of Programming COMP1005/5005

## Contents

README – readme file for AssignmentAssignment of Fundamentals of Programming COMP1005/5005

adventureworld.py

## Contents

## Dependencies

matplotlibREADME – readme file for Assignment



## Version informationadventureworld.py

October 17, 2025 - initial version of assignment programs

## Contents

## Dependencies

matplotlibREADME – readme file for Assignment## Synopsis



## Version informationadventureworld.py

October 17, 2025 - initial version of assignment programs

Assignment of Fundamentals of Programming COMP1005/5005

## Dependencies

matplotlib## Synopsis



## Version information## Contents

October 17, 2025 - initial version of assignment programs

- **README.md** - readme file for AssignmentAssignment of Fundamentals of Programming COMP1005/5005

- **adventureworld.py** - main program

- **simulation.py** - simulation engine## Synopsis## 

- **rides.py** - ride classes

- **patron.py** - patron managementA Python-based theme park simulation with animated rides, patron management, and dynamic weather system.

- **map1.csv** - park layout

- **params1.csv** - parametersAssignment of Fundamentals of Programming COMP1005/5005Assignment of Fundamentals of Programming COMP1005/5005



## Dependencies## Contents

- matplotlib

- numpy- **README.md** - This readme file for Assignment

- Python 3.11+

- **adventureworld.py** - Main program entry point

## Version information

October 17, 2025 - initial version of assignment programs- **simulation.py** - Simulation engineAdventure World Theme Park Simulation - A Python-based interactive simulation featuring multiple animated rides, intelligent patron management, dynamic weather system, and real-time visualization. This project demonstrates object-oriented programming, data structures, file I/O, animation, and simulation techniques.Adventure World Theme Park Simulation - A Python-based interactive simulation featuring multiple animated rides, intelligent patron management, dynamic weather system, and real-time visualization. This project demonstrates object-oriented programming, data structures, file I/O, animation, and simulation techniques.


- **rides.py** - Ride classes (BoatRide, FerrisWheel, RollerCoaster, SpiderRide)

- **patron.py** - Patron behavior management

- **map1.csv** - Park layout configuration

- **params1.csv** - Simulation parameters## Contents## ✨ Features



## DependenciesREADME.md – This readme file for Adventure World Theme Park Simulation Assignment

- **matplotlib** - For visualization and animation

- **numpy** - For numerical operations- **adventureworld.py** - Main entry point for the simulation with command-line interface1. **Boat Ride (ride1)** - Animated boat moving side-to-side

- **Python 3.11+** - Required

- **simulation.py** - Core simulation engine managing park operations and weather system   - Visual: Blue frame structure with brown boat

## Installation

```bash- **rides.py** - Ride class definitions (BoatRide, FerrisWheel, RollerCoaster, SpiderRide)   - Boat oscillates horizontally while frame stays stable

pip install matplotlib numpy

```- **patron.py** - Patron class for visitor behavior and movement   - Capacity: 10 patrons



## Usage   

```bash

# Interactive mode### Data Files (data/)2. **Ferris Wheel (ride2)** - Continuously rotating wheel

python src/adventureworld.py -i

- **map1.csv** - Park layout configuration (boundaries, ride positions and sizes)   - Visual: Purple wheel with 8 spokes and gondolas

# Batch mode

python src/adventureworld.py -f data/map1.csv -p data/params1.csv- **params1.csv** - Simulation parameters (patron count, steps, weather, ride settings)   - Smooth 360° rotation

```

   - Capacity: 12 patrons

## Features

- 🎢 Four animated rides (Boat, Ferris Wheel, Roller Coaster, Spider)### Configuration   

- 🌦️ Dynamic weather system (Sunny, Rain, Snow)

- 👥 Smart patron management (Roaming, Queuing, Riding)- **requirements.txt** - Python package dependencies3. **Roller Coaster (ride3)** - Moves vertically up and down

- 📊 Real-time statistics and visualization

- **.venv/** - Virtual environment directory   - Visual: Red square car on a gray dashed track

## Version information

**October 17, 2025** - Initial version of assignment programs   - Vertical movement simulation

- Four unique animated rides

- Weather system with three conditions## Dependencies   - Capacity: 8 patrons

- Patron state management

- CSV-based configuration   

- Real-time matplotlib visualization

### Required Python Libraries4. **Spider Ride (ride4)** - Multi-armed rotating ride

- **matplotlib** (>=3.7.0) - For real-time visualization, animation, and plotting   - Visual: Orange arms with seats at the ends

  - Used for: Ride animations, weather effects, patron visualization, dynamic updates   - 6 rotating arms with synchronized movement

     - Capacity: 10 patrons

- **numpy** (>=1.24.0) - For numerical operations and array handling

  - Used for: Coordinate calculations, animation coordinates, weather effects positioning### 🌦️ Dynamic Weather System



### Built-in Python LibrariesThe simulation now features three weather conditions:

- **csv** - Reading configuration files (map1.csv, params1.csv)

- **argparse** - Command-line argument parsing (-i, -f, -p flags)- ☀️ **Sunny** - Bright green grass, clear blue sky

- **dataclasses** - Defining Ride and Patron data structures  - Default sunny day atmosphere

- **random** - Patron movement randomization and behavior  - Best visibility for all attractions

- **typing** - Type hints and annotations for code clarity  

- **enum** - State machine implementation for ride states- 🌧️ **Rain** - Darker green grass, gray-blue sky

  - 100 animated rain drops falling diagonally

### Installation  - Atmospheric rain effect throughout the park

```bash  

# Create virtual environment- ❄️ **Snow** - Light blue-white ground, snowflakes

python -m venv .venv  - 80 animated snowflakes scattered across the screen

  - Winter wonderland theme

# Activate virtual environment (Windows)

.venv\Scripts\activate**Weather Modes**:

- `dynamic` - Automatically cycles through all three weather conditions every 150 steps

# Install dependencies- `sunny` - Fixed sunny weather

pip install matplotlib numpy- `rain` - Fixed rainy weather

```- `snow` - Fixed snowy weather



Or use requirements.txt:### 👥 Patron Management

```bash

pip install -r requirements.txt- **Smart Positioning**:

```  - 🔵 **Roaming (Blue circles)**: Free movement around the park

  - � **Queuing (Orange squares)**: Lined up vertically outside rides

### System Requirements  - 🟢 **Riding (Green stars)**: Positioned inside the ride boxes

- **Python 3.11+** (Required for modern features)  

- **Windows 10/11** (Tested platform)- **Realistic Behavior**:

- **Visual Studio Code** (Recommended IDE)  - Patrons automatically join queues when near rides

- **Minimum RAM**: 4GB  - Queue visualization shows actual patron positions

- **Display**: 1920×1080 or higher recommended for visualization  - Riders distributed across the ride area

  - Cannot walk through ride boundaries

## Version information

### 🎪 Enhanced Ride Visualization

**October 16, 2025** - Version 2.0

- ✅ Added dynamic weather system (sunny, rain, snow with cycling)Each ride displays:

- ✅ Replaced Pirate Ship with animated Boat Ride featuring stable frame- **Color-coded State Boxes** with thick borders (8px):

- ✅ Maximized ride box sizes (20×12 units, 67% larger)  - 🔘 **Gray**: Idle (waiting for patrons)

- ✅ Enhanced visual effects with thick borders and shadows  - 🟡 **Yellow**: Loading (boarding patrons)

- ✅ Fixed patron positioning system (queuing, riding, roaming)  - 🟢 **Green**: Running (ride in operation)

- ✅ Removed text labels from ride boxes for cleaner design  - 🌸 **Pink**: Unloading (patrons disembarking)

- ✅ Added 100 animated rain drops and 80 snowflakes  

- ✅ Implemented weather-specific background colors- **Maximized Ride Boxes**: 20×12 units (67% larger than original)

- ✅ Added weather emoji indicators in title- **Enhanced Borders**: Double-layer borders with inner dashed lines

- **Queue Information**: Real-time display of queue length and riders

**Initial Version** - Core simulation features- **No Text Labels**: Clean design without ride name clutter

- ✅ Four unique animated rides (Boat, Ferris Wheel, Roller Coaster, Spider)

- ✅ Patron management system with three states## Installation

- ✅ Queue system and ride capacity management

- ✅ Collision detection and boundary checking1. Create and activate a virtual environment:

- ✅ Real-time matplotlib visualization```bash

- ✅ CSV-based configuration systempython -m venv .venv

- ✅ Interactive and batch execution modes.venv\Scripts\activate  # Windows

- ✅ State machine for ride operations```



## Usage2. Install requirements:

```bash

### Interactive Modepip install -r requirements.txt

```bash```

python src/adventureworld.py -i

```## Usage

Prompts for number of steps and patrons.

### Interactive Mode

### Batch Mode

```bashRun the simulation with user prompts:

python src/adventureworld.py -f data/map1.csv -p data/params1.csv

``````bash

Runs with predefined configuration files.python src/adventureworld.py -i

```

## Features Summary

You'll be prompted for:

🎢 **4 Animated Rides**: Boat, Ferris Wheel, Roller Coaster, Spider  - Number of simulation steps (default: 300)

🌦️ **Dynamic Weather**: Sunny ☀️, Rain 🌧️, Snow ❄️  - Number of patrons (default: 25)

👥 **Smart Patrons**: Roaming, Queuing, Riding states  

📊 **Real-time Stats**: Queue length and ride capacity display  ### Batch Mode

🎨 **Enhanced Visuals**: Maximized boxes, thick borders, weather effects  

⚙️ **Configurable**: CSV-based setup for easy customizationRun with predefined configuration files:



---```bash

python src/adventureworld.py -f data/map1.csv -p data/params1.csv

*Educational project for Fundamentals of Programming COMP1005/5005*```


## Configuration Files

### Map CSV (`map1.csv`)

Defines the park layout with maximized ride boxes:

| type      | name  | x   | y   | width | height |
|-----------|-------|-----|-----|-------|--------|
| boundary  | park  | 0   | 0   | 100   | 100    |
| ride_box  | ride1 | 20  | 60  | 20    | 12     |
| ride_box  | ride2 | 80  | 60  | 20    | 12     |
| ride_box  | ride3 | 20  | 20  | 20    | 12     |
| ride_box  | ride4 | 80  | 20  | 20    | 12     |

**Ride Assignments**:
- `ride1` → Boat Ride (animated boat in frame)
- `ride2` → Ferris Wheel
- `ride3` → Roller Coaster
- `ride4` → Spider Ride

### Parameters CSV (`params1.csv`)

Configures simulation parameters including weather:

| param                       | value    |
|----------------------------|----------|
| num_patrons                | 50       |
| steps                      | 500      |
| seed                       | 42       |
| weather                    | dynamic  |
| ride1.capacity             | 10       |
| ride1.duration_steps       | 40       |
| ride2.capacity             | 12       |
| ride2.duration_steps       | 60       |
| ride3.capacity             | 8        |
| ride3.duration_steps       | 40       |
| ride4.capacity             | 10       |
| ride4.duration_steps       | 50       |

**Parameter Types**:
- `num_patrons`: Number of visitors in the park (default: 50)
- `steps`: Total simulation steps (default: 500)
- `seed`: Random seed for reproducibility
- `weather`: Weather mode - `dynamic`, `sunny`, `rain`, or `snow`
- `{ride_name}.capacity`: Maximum riders per cycle
- `{ride_name}.duration_steps`: Ride duration in steps
- `{ride_name}.speed_deg_per_step`: Animation speed (for rotating rides)

## Project Structure

```
AdventureWorld/
├── src/
│   ├── adventureworld.py   # Main entry point
│   ├── simulation.py        # Simulation engine
│   ├── rides.py            # Ride classes (4 types)
│   └── patron.py           # Patron class
├── data/
│   ├── map1.csv            # Park layout
│   └── params1.csv         # Simulation parameters
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## How It Works

### Simulation Loop

Each simulation step performs:

1. **Weather Management**:
   - Update weather condition (if dynamic mode)
   - Change background colors based on weather
   - Render weather effects (rain drops or snowflakes)

2. **Patron Movement**:
   - Roaming patrons move randomly
   - Check for collisions with ride boundaries
   - Join queues when near ride edges
   - Update patron positions for queuing and riding states

3. **Ride Operations**:
   - Process state transitions (idle → loading → running → unloading)
   - Board patrons from queue
   - Update ride animations (boat movement, wheel rotation, etc.)
   - Unload completed riders

4. **Visualization**:
   - Real-time matplotlib animation
   - Weather effects overlay
   - Queue and capacity information
   - Color-coded patron states with correct positioning
   - Enhanced ride animations with thick borders

### State Machine

Each ride follows this state machine:

```
IDLE → LOADING → RUNNING → UNLOADING → IDLE
  ↑                                        ↓
  └────────────────────────────────────────┘
```

### Collision Detection

- Patrons cannot enter ride bounding boxes
- Queue joining occurs at bounding box edges (2-unit margin)
- Movement is reverted if collision detected

## Visualization Features

- **Real-time Animation**: Smooth FPS visualization with weather effects
- **Weather Indicators**: 
  - Weather emoji in title (☀️/🌧️/❄️)
  - Dynamic background colors
  - Animated rain drops (100 drops) or snowflakes (80 flakes)
- **Legend**: Shows patron state colors and markers
- **Queue Info**: Displays `👥 Queue: x | 🎠 Riding: y/z` for each ride
  - Queue: Number of patrons waiting
  - Riding: Current riders / Total capacity
- **Enhanced Ride Boxes**: 
  - 8px thick borders with color-coded states
  - Inner dashed borders for depth
  - Shadow effects
  - Maximized size (20×12 units)
- **Patron Positioning**:
  - Queuing patrons: Vertical line outside rides
  - Riding patrons: Distributed inside ride boxes
  - Roaming patrons: Free movement
- **Ride Animations**: Each ride has unique visual representation:
  - Boat: Moving boat with stable blue frame
  - Ferris Wheel: Rotating with gondolas
  - Roller Coaster: Vertical car movement on track
  - Spider: Rotating arms with motion blur

## Customization

### Changing Weather

Edit `data/params1.csv`:
```csv
weather,dynamic  # Cycles through all three weather types
weather,sunny    # Always sunny
weather,rain     # Always raining
weather,snow     # Always snowing
```

Weather changes every 150 steps in dynamic mode.

### Adjusting Ride Sizes

Edit `data/map1.csv` to change ride box dimensions:
```csv
ride_box,ride1,20,60,20,12  # x, y, width, height
```

### Modifying Patron Count

Edit `data/params1.csv`:
```csv
num_patrons,50   # Number of visitors
steps,500        # Simulation duration
```

### Adding New Rides

1. Create a new class in `rides.py` inheriting from `Ride`
2. Implement `step_change()` for ride logic and animations
3. Implement `plot()` for visualization
4. Add to `load_map()` in `simulation.py`

### Modifying Patron Behavior

Edit `patron.py` to change:
- Movement patterns (currently random walk)
- Speed parameters (`uniform(-1.5, 1.5)`)
- Visual appearance (markers, colors, sizes)
- Decision-making logic

### Adjusting Visualization

Edit `simulation.py` `run()` method to modify:
- Figure size (`figsize=(14, 10)`)
- Weather change frequency (default: 150 steps)
- Number of rain drops (default: 100) or snowflakes (default: 80)
- Color schemes for weather conditions
- Border thickness and styles

## Technical Details

### Dependencies

- **matplotlib**: Real-time visualization and animation
- **Python 3.11+**: Modern Python features and dataclasses

### Performance

- Optimized for up to 50 patrons
- 100 FPS animation rate
- Efficient collision detection

### Data Structures

- **Dataclasses**: Used for Ride and Patron (type safety and clarity)
- **Lists**: Queue management and patron tracking
- **Tuples**: Boundary and bounding box representation

## Troubleshooting

### Simulation runs slowly
- Reduce number of patrons
- Reduce number of simulation steps
- Increase `plt.pause()` duration

### Rides don't start
- Check queue is enabled
- Verify ride capacity > 0
- Check duration_steps > 0

### Patrons stuck
- Verify boundary coordinates are correct
- Check ride bounding boxes don't overlap
- Ensure adequate space for movement

## Recent Updates

### Version 2.0 - Weather & Enhancements

**New Features**:
- ✅ Dynamic weather system (sunny, rain, snow)
- ✅ Replaced Pirate Ship with animated Boat Ride
- ✅ Maximized ride box sizes (20×12 units)
- ✅ Enhanced borders and visual effects
- ✅ Removed text labels from ride boxes
- ✅ Fixed patron positioning for queuing and riding
- ✅ Weather cycling every 150 steps
- ✅ Animated rain drops and snowflakes
- ✅ Weather-specific background colors

**Visual Improvements**:
- Thicker ride borders (8px main, 4px inner)
- Larger text and better styling
- Shadow effects on ride boxes
- Correct patron positioning in queues and on rides
- Weather emoji indicators in title

## Future Enhancements

- [ ] Path-finding for patrons
- [ ] Multiple entrance/exit points
- [ ] Ride priority preferences
- [ ] Fatigue and satisfaction mechanics
- [ ] Food stalls and rest areas
- [x] ~~Weather effects~~ ✅ Completed
- [ ] Time-of-day simulation (sunrise/sunset)
- [ ] Statistics and reporting dashboard
- [ ] Save/load simulation states
- [ ] Custom ride builder

## License

Educational project for simulation and visualization.

## Author

Adventure World Theme Park Simulation
