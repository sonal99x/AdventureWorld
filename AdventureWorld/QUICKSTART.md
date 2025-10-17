# Quick Start Guide - Adventure World

## Installation (One-Time Setup)

```powershell
# Navigate to project directory
cd C:\Users\PC\Desktop\AdventureWorld

# Activate virtual environment
.venv\Scripts\activate

# Install dependencies (if not already installed)
pip install -r requirements.txt
```

## Running the Simulation

### Option 1: Interactive Mode (Easiest)

```powershell
cd src
python adventureworld.py -i
```

**You'll be prompted for:**
- Number of steps (press Enter for default: 300)
- Number of patrons (press Enter for default: 25)

**What you'll see:**
- A matplotlib window with animated simulation
- Blue dots (roaming patrons)
- Orange dots (queuing patrons)
- Green dots (riding patrons)
- One Pirate Ship ride in the center

### Option 2: Batch Mode (Full Features)

```powershell
cd src
python adventureworld.py -f ..\data\map1.csv -p ..\data\params1.csv
```

**What you'll see:**
- All 4 rides operating:
  - Pirate Ship (top-left)
  - Ferris Wheel (top-right)
  - Roller Coaster (bottom-left)
  - Spider Ride (bottom-right)
- 25 patrons moving around
- Real-time queue and rider counts
- 300 simulation steps

## Understanding the Display

### Patron Colors
- 🔵 **Blue dots** = Walking around (roaming)
- 🟠 **Orange dots** = Waiting in line (queuing)
- 🟢 **Green dots** = On a ride (riding)

### Ride Bounding Boxes
- **Gray border** = Ride is idle (waiting for patrons)
- **Yellow border** = Loading patrons onto ride
- **Green border** = Ride is running
- **Red border** = Unloading patrons

### Queue Information
Text below each ride shows: `Q:5 R:8/10`
- `Q:5` = 5 patrons in queue
- `R:8/10` = 8 riders currently on ride (capacity: 10)

## Customizing the Simulation

### Edit Parameters (`data/params1.csv`)

```csv
param,value
num_patrons,50          # Change to 50 patrons
steps,600               # Change to 600 steps
seed,42                 # Random seed
ride1.capacity,15       # Pirate Ship holds 15 people
ride1.duration,60       # Ride lasts 60 steps
```

### Edit Map Layout (`data/map1.csv`)

```csv
type,name,x,y,width,height
boundary,park,0,0,150,150    # Larger park
ride_box,ride1,30,90,15,8    # Different position
```

## Common Commands

### Run with custom files
```powershell
python adventureworld.py -f my_map.csv -p my_params.csv
```

### Quick test (interactive)
```powershell
python adventureworld.py -i
# Press Enter twice for defaults
```

### Multiple runs with different seeds
Edit `params1.csv` and change `seed` value between runs for different random patterns.

## Keyboard Shortcuts During Simulation

- **Close Window** = Stop simulation
- The simulation will auto-close after all steps complete

## Troubleshooting

### "matplotlib not found"
```powershell
pip install matplotlib
```

### Simulation too fast
Edit `simulation.py`, line with `plt.pause(0.01)`, change to:
```python
plt.pause(0.05)  # Slower
```

### Simulation too slow
Edit `params1.csv`, reduce:
- `num_patrons` to 10-15
- `steps` to 100-200

### Window doesn't appear
- Check that matplotlib backend is working
- Try running in a different terminal
- Ensure virtual environment is activated

## What to Watch For

### Successful Simulation Shows:
- ✅ Patrons moving randomly (blue dots)
- ✅ Patrons joining queues near rides (turn orange)
- ✅ Rides loading patrons (yellow border)
- ✅ Rides operating with animation (green border)
- ✅ Patrons becoming riders (turn green)
- ✅ Rides unloading (red border)
- ✅ Patrons returning to roaming (turn blue)

### Ride Animations:
- **Pirate Ship**: Swinging boom arm with ship
- **Ferris Wheel**: Rotating wheel with spokes
- **Roller Coaster**: Car moving up track
- **Spider Ride**: 6 rotating arms

## Example Session

```powershell
PS C:\Users\PC\Desktop\AdventureWorld> .venv\Scripts\activate
(.venv) PS C:\Users\PC\Desktop\AdventureWorld> cd src
(.venv) PS C:\Users\PC\Desktop\AdventureWorld\src> python adventureworld.py -f ..\data\map1.csv -p ..\data\params1.csv
Batch mode
[Matplotlib window opens with animation]
[Simulation runs for 300 steps]
[Window remains open when complete]
```

## Tips for Best Results

1. **Start with defaults**: Run batch mode first to see all features
2. **Watch the patterns**: Notice how patrons naturally gather at rides
3. **Monitor queues**: See which rides are most popular
4. **Experiment**: Try different parameter values
5. **Multiple windows**: Run multiple simulations side-by-side with different configs

## Next Steps

After running the basic simulation:
1. Try modifying patron count (10, 25, 50)
2. Adjust ride durations (faster/slower)
3. Change ride capacities (more/fewer riders)
4. Experiment with different park layouts
5. Add more rides by editing `map1.csv`

Enjoy your Adventure World simulation! 🎢🎡🎠
