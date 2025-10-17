# Traceability Matrix - Adventure World Theme Park Simulation

## Overview
Table giving overview of features, and the implementation and testing of your code.

### Legend
- **Feature** - numbered for easy referencing
- **Code reference** - reference to files/classes/methods or snippets of code only, do not put the whole program in the report OR "Not Implemented"
- **Test reference** - test code or describe how you tested your feature, N/A if not implemented
- **Status** - P = passed tests, F = failed, N/A = not implemented
- **Date Completed** - date or "Ongoing" or N/A if not implemented

## Traceability Matrix Table

| Feature | Code Reference | Test Reference | Status | Date Completed |
|---------|----------------|----------------|--------|----------------|
| 1.0 Boat Ride Animation | `rides.py` - `BoatRide` class, `plot()` method | Observed boat moving left-right with stable frame | P | Oct 16, 2025 |
| 2.0 Ferris Wheel Rotation | `rides.py` - `FerrisWheel` class, `step_change()` | Verified continuous 360° rotation | P | Initial |
| 3.0 Dynamic Weather System | `simulation.py` - weather cycling lines 120-124 | Tested sunny→rain→snow transitions | F | Ongoing |
| 4.0 Patron Queue Management | `simulation.py` - queue joining logic | Patrons join queue near rides | P | Initial |
| 5.0 Enhanced Ride Visualization | `rides.py` - 8px borders, shadow effects | Visual inspection of ride boxes | P | Oct 16, 2025 |
| 6.0 Patron State Transitions | `patron.py` - roaming/queuing/riding states | Observed color changes (blue/orange/green) | F | Ongoing |
| 7.0 CSV Configuration Loading | `simulation.py` - `load_map()`, `load_params()` | Loaded map1.csv and params1.csv successfully | P | Initial |
| 8.0 Weather Background Colors | `simulation.py` - `set_facecolor()` based on weather | Checked background color changes | P | Oct 16, 2025 |
| 9.0 Ride Capacity Control | Not Implemented | Test with max patrons per ride | N/A | N/A |
| 10.0 Error Handling | Not Implemented | Test with missing files | N/A | N/A |

## Test Summary

| Status | Count | Percentage |
|--------|-------|------------|
| Passed (P) | 6 | 60% |
| Failed (F) | 2 | 20% |
| Not Implemented (N/A) | 2 | 20% |
| **TOTAL** | **10** | **100%** |

## Failed Features Details

1. **3.0 Dynamic Weather System** - Weather transitions not smooth between modes
2. **6.0 Patron State Transitions** - Orange squares positioning incorrect in queue

## Date: October 17, 2025
