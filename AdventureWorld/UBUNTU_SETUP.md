# Adventure World - Ubuntu Setup Guide

## Prerequisites

### 1. Install Python 3.11+
```bash
# Update package list
sudo apt update

# Install Python 3.11 or higher
sudo apt install python3.11 python3.11-venv python3-pip

# Verify installation
python3.11 --version
```

### 2. Install System Dependencies
```bash
# Install matplotlib dependencies
sudo apt install python3-tk

# Install additional libraries for plotting
sudo apt install libfreetype6-dev libpng-dev
```

## Installation Steps

### 1. Transfer Files to Ubuntu
You can transfer the AdventureWorld folder using one of these methods:

**Option A: USB Drive**
```bash
# Mount USB and copy
cp -r /media/username/USB/AdventureWorld ~/
```

**Option B: Git** (if you have a repository)
```bash
git clone <repository-url>
cd AdventureWorld
```

**Option C: SCP from Windows** (if both systems are networked)
```bash
# Run from Ubuntu
scp -r username@windows-ip:C:/Users/PC/Desktop/AdventureWorld ~/
```

**Option D: Shared Folder** (if using VM)
- Already accessible in your shared folder location

### 2. Navigate to Project Directory
```bash
cd ~/AdventureWorld
```

### 3. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 4. Install Python Dependencies
```bash
# Install required packages
pip install -r requirements.txt

# Or install manually
pip install matplotlib numpy
```

## Running the Simulation

### Interactive Mode
```bash
# From project root
python3 src/adventureworld.py -i
```

### Batch Mode
```bash
# Run with configuration files
python3 src/adventureworld.py -f data/map1.csv -p data/params1.csv
```

### Test Scripts
```bash
# Test ride animations
python3 test_rides_animation.py

# Test simulation
python3 test_simulation.py

# Test visuals
python3 test_visual.py
```

## File Path Differences

### Windows vs Linux Paths
The Python code should work without modification because it uses:
- **Forward slashes** in code (platform-independent)
- **os.path.join()** for path construction
- Relative paths (not absolute Windows paths)

### Verify CSV Files
```bash
# Check data files exist
ls -l data/
# Should show: map1.csv, params1.csv
```

## Troubleshooting

### Issue 1: matplotlib backend error
```bash
# If you get "no display name" error
export DISPLAY=:0

# Or use non-interactive backend
echo "backend: TkAgg" > ~/.config/matplotlib/matplotlibrc
```

### Issue 2: Permission denied
```bash
# Make scripts executable
chmod +x src/adventureworld.py
chmod +x test_*.py
```

### Issue 3: Module not found
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install --upgrade matplotlib numpy
```

### Issue 4: Display issues on headless server
```bash
# Install virtual display
sudo apt install xvfb

# Run with virtual display
xvfb-run python3 src/adventureworld.py -f data/map1.csv -p data/params1.csv
```

## Performance Notes

### Ubuntu vs Windows
- **Faster execution**: Linux typically runs Python faster
- **Better matplotlib**: Native rendering without Windows overhead
- **Resource usage**: Lower memory footprint on Linux

### Optimization for Ubuntu
```bash
# Use PyPy for faster execution (optional)
sudo apt install pypy3
pypy3 -m pip install matplotlib numpy
pypy3 src/adventureworld.py -f data/map1.csv -p data/params1.csv
```

## Quick Start Commands

```bash
# One-line setup and run
cd ~/AdventureWorld && \
python3 -m venv venv && \
source venv/bin/activate && \
pip install matplotlib numpy && \
python3 src/adventureworld.py -f data/map1.csv -p data/params1.csv
```

## File Structure Verification

```bash
# Verify all files are present
tree -L 2
# Or
find . -type f -name "*.py" -o -name "*.csv" -o -name "*.md"
```

Expected structure:
```
AdventureWorld/
├── src/
│   ├── adventureworld.py
│   ├── simulation.py
│   ├── rides.py
│   └── patron.py
├── data/
│   ├── map1.csv
│   └── params1.csv
├── test_rides_animation.py
├── test_simulation.py
├── test_visual.py
├── requirements.txt
└── README.md
```

## Environment Variables (Optional)

```bash
# Add to ~/.bashrc for convenience
echo 'alias adventure="cd ~/AdventureWorld && source venv/bin/activate"' >> ~/.bashrc
source ~/.bashrc

# Now you can just type:
adventure
python3 src/adventureworld.py -f data/map1.csv -p data/params1.csv
```

## Deactivation

```bash
# When finished, deactivate virtual environment
deactivate
```

## Notes

- **No code changes needed**: The Python code is cross-platform compatible
- **matplotlib works better on Linux**: Native window management
- **CSV files**: Work identically on both systems
- **Line endings**: If you see issues, run: `dos2unix src/*.py data/*.csv`

## Success Verification

You should see:
1. matplotlib window opens
2. Title: "🎡 Adventure World Theme Park 🎢"
3. Four rides with animations
4. Patron movement (blue circles)
5. Weather effects (if dynamic mode)
6. Real-time step counter

Enjoy running Adventure World on Ubuntu! 🐧🎢
