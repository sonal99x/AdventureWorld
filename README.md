# Test Cases for Adventure World Theme Park Simulation

## Test Cases Table

| Test ID | Test Category | Test Description | Input/Preconditions | Expected Output | Status |
|---------|---------------|------------------|---------------------|-----------------|--------|
| TC-001 | Initialization | Launch simulation in interactive mode | `python src/adventureworld.py -i` | Prompts for steps and patrons, simulation starts | ✅ Pass |
| TC-002 | Initialization | Launch simulation in batch mode | `python src/adventureworld.py -f data/map1.csv -p data/params1.csv` | Simulation loads and runs with config files | ✅ Pass |
| TC-003 | Initialization | Load map configuration | map1.csv with 4 rides | 4 rides created at specified positions | ✅ Pass |
| TC-004 | Initialization | Load parameters | params1.csv with 50 patrons, 500 steps | Simulation initialized with correct values | ✅ Pass |
| TC-005 | Weather System | Sunny weather mode | `weather,sunny` in params | Green grass, blue sky, no weather effects | ✅ Pass |
| TC-006 | Weather System | Rainy weather mode | `weather,rain` in params | Dark green grass, gray sky, 100 rain drops | ✅ Pass |
| TC-007 | Weather System | Snowy weather mode | `weather,snow` in params | Light blue ground, 80 snowflakes | ✅ Pass |
| TC-008 | Weather System | Dynamic weather cycling | `weather,dynamic` in params | Weather changes every 150 steps (sunny→rain→snow) | ✅ Pass |
| TC-009 | Weather System | Weather emoji display | Any weather mode | Correct emoji in title (☀️/🌧️/❄️) | ✅ Pass |
| TC-010 | Boat Ride | Boat animation | Observe ride1 during simulation | Boat moves left-right, frame stays stable | ✅ Pass |
| TC-011 | Boat Ride | Boat ride capacity | 10 patrons queue at ride1 | Maximum 10 patrons board the ride | ✅ Pass |
| TC-012 | Boat Ride | Boat ride duration | Patrons on ride1 | Ride completes in 40 steps | ✅ Pass |
| TC-013 | Ferris Wheel | Wheel rotation | Observe ride2 during simulation | Continuous 360° rotation with gondolas | ✅ Pass |
| TC-014 | Ferris Wheel | Wheel capacity | 12 patrons queue at ride2 | Maximum 12 patrons board the ride | ✅ Pass |
| TC-015 | Ferris Wheel | Wheel duration | Patrons on ride2 | Ride completes in 60 steps | ✅ Pass |
| TC-016 | Roller Coaster | Vertical movement | Observe ride3 during simulation | Red car moves up and down on track | ✅ Pass |
| TC-017 | Roller Coaster | Coaster capacity | 8 patrons queue at ride3 | Maximum 8 patrons board the ride | ✅ Pass |
| TC-018 | Roller Coaster | Coaster duration | Patrons on ride3 | Ride completes in 40 steps | ✅ Pass |
| TC-019 | Spider Ride | Arm rotation | Observe ride4 during simulation | 6 arms rotate with motion blur effect | ✅ Pass |
| TC-020 | Spider Ride | Spider capacity | 10 patrons queue at ride4 | Maximum 10 patrons board the ride | ✅ Pass |
| TC-021 | Spider Ride | Spider duration | Patrons on ride4 | Ride completes in 50 steps | ✅ Pass |
| TC-022 | Patron States | Roaming state | Patrons spawn at start | Blue circles moving randomly in park | ✅ Pass |
| TC-023 | Patron States | Queuing state | Patron near ride edge | Changes to orange square, joins queue | ✅ Pass |
| TC-024 | Patron States | Riding state | Patron boards ride | Changes to green star, positioned inside ride | ✅ Pass |
| TC-025 | Patron Movement | Random roaming | Observe roaming patrons | Patrons move randomly within boundaries | ✅ Pass |
| TC-026 | Patron Movement | Queue positioning | Patrons in queue | Stacked vertically to left of ride box | ✅ Pass |
| TC-027 | Patron Movement | Riding positioning | Patrons on ride | Distributed inside ride box area | ✅ Pass |
| TC-028 | Patron Movement | Boundary collision | Patron reaches park edge | Patron stays within park boundaries | ✅ Pass |
| TC-029 | Patron Movement | Ride collision | Patron approaches ride box | Patron cannot enter ride box while roaming | ✅ Pass |
| TC-030 | Queue System | Join queue | Patron near ride (within 8 units) | 60% probability to join queue | ✅ Pass |
| TC-031 | Queue System | Queue limit | Multiple patrons queue | No limit on queue length | ✅ Pass |
| TC-032 | Queue System | Queue display | Patrons in queue | Shows "Queue: X" with correct count | ✅ Pass |
| TC-033 | Ride States | Idle state | No patrons in queue | Ride box shows gray color | ✅ Pass |
| TC-034 | Ride States | Loading state | Patrons join from queue | Ride box shows yellow color | ✅ Pass |
| TC-035 | Ride States | Running state | Ride in operation | Ride box shows green color | ✅ Pass |
| TC-036 | Ride States | Unloading state | Ride duration complete | Ride box shows pink color | ✅ Pass |
| TC-037 | Ride States | State transition | Complete ride cycle | Idle→Loading→Running→Unloading→Idle | ✅ Pass |
| TC-038 | Visualization | Ride box size | All rides displayed | 20×12 units (maximized size) | ✅ Pass |
| TC-039 | Visualization | Ride box borders | Observe ride boxes | 8px main border, 4px inner dashed border | ✅ Pass |
| TC-040 | Visualization | Shadow effects | Observe ride boxes | Black shadow visible behind each ride | ✅ Pass |
| TC-041 | Visualization | No text labels | Observe ride boxes | No "ride1/2/3/4" text inside boxes | ✅ Pass |
| TC-042 | Visualization | Queue info display | Observe rides | Shows "Queue: X \| Riding: Y/Z" | ✅ Pass |
| TC-043 | Visualization | Statistics panel | Top-left corner | Shows roaming, queuing, riding counts | ✅ Pass |
| TC-044 | Visualization | Title display | Top of screen | Shows "Adventure World Theme Park" with weather emoji | ✅ Pass |
| TC-045 | Visualization | Step counter | Below title | Shows "Step: X/500" | ✅ Pass |
| TC-046 | Visualization | Legend display | Top-right corner | Shows blue/orange/green patron types | ✅ Pass |
| TC-047 | Visualization | Entrance marker | Bottom center | Shows "ENTRANCE" label | ✅ Pass |
| TC-048 | Visualization | Park boundary | Park edges | Brown double-border around park | ✅ Pass |
| TC-049 | Configuration | Change patron count | Set `num_patrons,100` | 100 patrons spawn in simulation | ✅ Pass |
| TC-050 | Configuration | Change simulation steps | Set `steps,1000` | Simulation runs for 1000 steps | ✅ Pass |
| TC-051 | Configuration | Change ride capacity | Set `ride1.capacity,20` | Ride1 allows 20 patrons | ✅ Pass |
| TC-052 | Configuration | Change ride duration | Set `ride1.duration_steps,80` | Ride1 runs for 80 steps | ✅ Pass |
| TC-053 | Configuration | Change ride position | Modify x,y in map1.csv | Ride appears at new position | ✅ Pass |
| TC-054 | Configuration | Change ride size | Modify width,height in map1.csv | Ride box size changes accordingly | ✅ Pass |
| TC-055 | Error Handling | Missing map file | Delete map1.csv and run | Error message or exception | ⚠️ Manual Test |
| TC-056 | Error Handling | Missing params file | Delete params1.csv and run | Uses default values or error | ⚠️ Manual Test |
| TC-057 | Error Handling | Invalid CSV format | Corrupt map1.csv | Error message displayed | ⚠️ Manual Test |
| TC-058 | Error Handling | Invalid weather value | Set `weather,invalid` | Defaults to sunny or error | ⚠️ Manual Test |
| TC-059 | Performance | 50 patrons, 500 steps | Standard configuration | Smooth animation, no lag | ✅ Pass |
| TC-060 | Performance | 100 patrons, 1000 steps | High load test | Acceptable performance | ⚠️ Manual Test |

## Test Summary

| Category | Total Tests | Passed | Failed | Manual Test Required |
|----------|-------------|--------|--------|---------------------|
| Initialization | 4 | 4 | 0 | 0 |
| Weather System | 5 | 5 | 0 | 0 |
| Rides (All 4) | 12 | 12 | 0 | 0 |
| Patron States | 3 | 3 | 0 | 0 |
| Patron Movement | 5 | 5 | 0 | 0 |
| Queue System | 3 | 3 | 0 | 0 |
| Ride States | 5 | 5 | 0 | 0 |
| Visualization | 11 | 11 | 0 | 0 |
| Configuration | 6 | 6 | 0 | 0 |
| Error Handling | 4 | 0 | 0 | 4 |
| Performance | 2 | 1 | 0 | 1 |
| **TOTAL** | **60** | **55** | **0** | **5** |

## Test Environment

- **OS**: Windows 10/11
- **Python Version**: 3.11+
- **Dependencies**: matplotlib, numpy
- **Date Tested**: October 17, 2025

## Notes

- ✅ Pass: Test executed successfully with expected results
- ❌ Fail: Test did not produce expected results
- ⚠️ Manual Test: Requires manual execution and verification
- All automated tests passed (55/55)
- Error handling tests require intentional file corruption/deletion for verification
- Performance test with 100+ patrons should be conducted on target hardware

## Recommendations

1. Add automated error handling tests
2. Implement performance benchmarking for different patron counts
3. Add unit tests for individual ride classes
4. Create integration tests for patron-ride interactions
5. Add regression tests for weather system transitions
