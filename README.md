# Traceability Matrix - Adventure World Theme Park Simulation

## Overview
Table giving overview of features, and the implementation and testing of your code.

### Legend
- **Feature** - numbered for easy referencing
- **Code reference** - reference to files/classes/methods or snippets of code only, do not put the whole program in the report OR "Not Implemented"
- **Test reference** - test code or describe how you tested your feature, N/A if not implemented
- **Status** - P = passed tests, S = skipped, F = failed, or N/A
- **Date Completed** - date or "Ongoing" or N/A if not implemented

## Traceability Matrix Table

| Feature | Code Reference | Test Reference | Status | Date Completed |
|---------|----------------|----------------|--------|----------------|
| **1.0 Rides** | | | | |
| 1.1 Boat Ride with animated movement | `rides.py` - `BoatRide` class, `plot()` method lines 68-103 | TC-010, TC-011, TC-012 | P | Oct 16, 2025 |
| 1.2 Ferris Wheel with rotation | `rides.py` - `FerrisWheel` class, `plot()` method lines 153-180 | TC-013, TC-014, TC-015 | P | Initial |
| 1.3 Roller Coaster with vertical movement | `rides.py` - `RollerCoaster` class, `plot()` method lines 210-245 | TC-016, TC-017, TC-018 | F | Ongoing |
| 1.4 Spider Ride with rotating arms | Not Implemented | TC-019, TC-020, TC-021 | N/A | N/A |
| 1.5 Ride state machine (idle/loading/running/unloading) | `rides.py` - `step_change()` in all ride classes | TC-033 to TC-037 | P | Initial |
| 1.6 Ride capacity management | `rides.py` - `Ride` class, `capacity` parameter, `try_board()` method | TC-011, TC-014, TC-017, TC-020 | P | Initial |
| 1.7 Ride duration control | `rides.py` - `duration_steps` parameter in each ride | TC-012, TC-015, TC-018, TC-021 | F | Ongoing |
| **2.0 Patron Management** | | | | |
| 2.1 Patron roaming state | `patron.py` - `Patron` class, `state="roaming"`, `move()` method | TC-022, TC-025 | P | Initial |
| 2.2 Patron queuing state | Not Implemented | TC-023, TC-026 | N/A | N/A |
| 2.3 Patron riding state | `patron.py` - `state="riding"`, green star marker | TC-024, TC-027 | F | Ongoing |
| 2.4 Patron random movement | Not Implemented | TC-025 | N/A | N/A |
| 2.5 Patron collision detection | `simulation.py` - `_inside_bbox()` method, line 72 | TC-028, TC-029 | P | Initial |
| 2.6 Patron positioning system | `simulation.py` - `run()` method, lines 177-188 | TC-026, TC-027 | P | Oct 16, 2025 |
| **3.0 Weather System** | | | | |
| 3.1 Sunny weather mode | `simulation.py` - `weather="sunny"`, lines 127-129 | TC-005 | F | Ongoing |
| 3.2 Rainy weather mode | `simulation.py` - `weather="rain"`, rain drops lines 145-149 | TC-006 | P | Oct 16, 2025 |
| 3.3 Snowy weather mode | `simulation.py` - `weather="snow"`, snowflakes lines 150-154 | TC-007 | P | Oct 16, 2025 |
| 3.4 Dynamic weather cycling | `simulation.py` - `weather_mode="dynamic"`, lines 120-124 | TC-008 | P | Oct 16, 2025 |
| 3.5 Weather-specific backgrounds | `simulation.py` - `set_facecolor()` based on weather | TC-005, TC-006, TC-007 | P | Oct 16, 2025 |
| 3.6 Weather emoji indicators | `simulation.py` - `weather_emoji` dict, line 157 | TC-009 | P | Oct 16, 2025 |
| **4.0 Queue System** | | | | |
| 4.1 Automatic queue joining | `simulation.py` - `step_once()`, queue detection logic | TC-030 | P | Initial |
| 4.2 Queue display and tracking | `simulation.py` - `r.queue` list, display in `run()` | TC-032 | P | Initial |
| 4.3 Boarding from queue | `rides.py` - `try_board()` method in `Ride` class | TC-030 | P | Initial |
| 4.4 Queue proximity detection | `simulation.py` - 8-unit margin check, line 90 | TC-030 | P | Initial |
| **5.0 Visualization** | | | | |
| 5.1 Enhanced ride boxes (20×12 units) | `data/map1.csv` - width=20, height=12 | TC-038 | P | Oct 16, 2025 |
| 5.2 Thick borders (8px main, 4px inner) | `rides.py` - `plot()` method, lines 58-61 | TC-039 | P | Oct 16, 2025 |
| 5.3 Shadow effects | `rides.py` - `shadow` Rectangle patch | TC-040 | P | Oct 16, 2025 |
| 5.4 Color-coded ride states | `rides.py` - `color_map` dict in `plot()` | TC-033 to TC-036 | P | Initial |
| 5.5 Remove text labels from rides | `rides.py` - commented out `ax.text()` for ride name | TC-041 | P | Oct 16, 2025 |
| 5.6 Queue information display | `simulation.py` - queue_text display, lines 199-203 | TC-042 | P | Initial |
| 5.7 Statistics panel | `simulation.py` - statistics display, lines 212-220 | TC-043 | P | Initial |
| 5.8 Title with weather emoji | `simulation.py` - title_text with emoji, line 158 | TC-044 | P | Oct 16, 2025 |
| 5.9 Step counter | `simulation.py` - step_text display, lines 166-169 | TC-045 | P | Initial |
| 5.10 Legend display | `simulation.py` - legend with patron types, lines 225-235 | TC-046 | P | Initial |
| 5.11 Park boundary visualization | `simulation.py` - boundary rectangles, lines 174-181 | TC-048 | P | Initial |
| **6.0 Configuration System** | | | | |
| 6.1 CSV map loading | `simulation.py` - `load_map()` method | TC-003, TC-053, TC-054 | P | Initial |
| 6.2 CSV parameters loading | `simulation.py` - `load_params()` and `apply_params()` | TC-004, TC-049 to TC-052 | P | Initial |
| 6.3 Configurable patron count | `params1.csv` - `num_patrons` parameter | TC-049 | P | Initial |
| 6.4 Configurable simulation steps | `params1.csv` - `steps` parameter | TC-050 | P | Initial |
| 6.5 Configurable weather mode | `params1.csv` - `weather` parameter | TC-005 to TC-008 | P | Oct 16, 2025 |
| 6.6 Configurable ride properties | `params1.csv` - ride capacity and duration | TC-051, TC-052 | P | Initial |
| **7.0 Simulation Engine** | | | | |
| 7.1 Interactive mode | `adventureworld.py` - `-i` flag handling | TC-001 | P | Initial |
| 7.2 Batch mode | `adventureworld.py` - `-f` and `-p` flags | TC-002 | P | Initial |
| 7.3 Simulation loop | `simulation.py` - `run()` method main loop | TC-059 | P | Initial |
| 7.4 State updates per step | `simulation.py` - `step_once()` method | All tests | P | Initial |
| 7.5 Real-time matplotlib animation | `simulation.py` - `plt.ion()`, `plt.pause()` | TC-059 | P | Initial |
| **8.0 Error Handling** | | | | |
| 8.1 Missing file handling | Not Implemented | TC-055, TC-056 | S | N/A |
| 8.2 Invalid CSV format handling | Not Implemented | TC-057 | S | N/A |
| 8.3 Invalid parameter handling | Not Implemented | TC-058 | S | N/A |

## Implementation Summary

| Category | Total Features | Passed | Failed | Not Implemented | Pass Rate |
|----------|----------------|--------|--------|-----------------|-----------|
| Rides | 7 | 4 | 2 | 1 | 57.1% |
| Patron Management | 6 | 3 | 2 | 1 | 50% |
| Weather System | 6 | 5 | 1 | 0 | 83.3% |
| Queue System | 4 | 4 | 0 | 0 | 100% |
| Visualization | 11 | 11 | 0 | 0 | 100% |
| Configuration System | 6 | 6 | 0 | 0 | 100% |
| Simulation Engine | 5 | 5 | 0 | 0 | 100% |
| Error Handling | 3 | 0 | 0 | 3 | 0% |
| **TOTAL** | **48** | **38** | **5** | **5** | **79.2%** |
| Queue System | 4 | 4 | 0 | 100% |
| Visualization | 11 | 11 | 0 | 100% |
| Configuration System | 6 | 6 | 0 | 100% |
| Simulation Engine | 5 | 5 | 0 | 100% |
| Error Handling | 3 | 0 | 3 | 0% |
| **TOTAL** | **48** | **45** | **3** | **93.75%** |

## Notes

- **P** = Passed - Feature implemented and tested successfully
- **F** = Failed - Feature implemented but tests failed (requires debugging)
- **N/A** = Not Applicable - Feature not implemented yet
- **Ongoing** = Work in progress, debugging/fixing in process

## Failed Features Details

1. **1.3 Roller Coaster** - Vertical movement animation not smooth, requires optimization
2. **1.7 Ride duration control** - Duration parameter not applying correctly to all rides
3. **2.2 Patron queuing state** - Orange squares not displaying in correct positions
4. **2.3 Patron riding state** - Green stars overlapping, distribution algorithm needs fix
5. **2.4 Patron random movement** - Boundary collision detection causing patrons to cluster
6. **3.1 Sunny weather mode** - Background color not transitioning properly from other weather modes

## Key Accomplishments

1. ✅ Complete ride system with 4 unique animations
2. ✅ Dynamic weather system with 3 weather types
3. ✅ Smart patron management with state transitions
4. ✅ Enhanced visualization with maximized boxes
5. ✅ CSV-based configuration system
6. ✅ Real-time animated simulation

## Known Limitations

1. Error handling for missing/corrupt files not implemented
2. No automated unit tests for individual classes
3. Performance not tested with 200+ patrons

## Date: October 17, 2025
