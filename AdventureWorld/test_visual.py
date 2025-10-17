"""
Quick visual test to verify all 4 rides are working
Shows a short 50-step simulation with all rides
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from simulation import Simulation

def test_all_rides():
    """Run a quick test with all 4 rides"""
    print("=" * 60)
    print("TESTING ALL 4 RIDES")
    print("=" * 60)
    print()
    
    sim = Simulation()
    sim.load_map("data/map1.csv")
    
    print(f"✓ Loaded {len(sim.rides)} rides from map:")
    for i, ride in enumerate(sim.rides, 1):
        print(f"  {i}. {ride.__class__.__name__} ('{ride.name}')")
    print()
    
    params = sim.load_params("data/params1.csv")
    print(f"✓ Loaded {len(params)} parameters")
    print()
    
    sim.apply_params(params)
    print(f"✓ Created {len(sim.patrons)} patrons")
    print()
    
    # Check ride configurations
    print("Ride Configurations:")
    for ride in sim.rides:
        print(f"  {ride.name}:")
        print(f"    - Type: {ride.__class__.__name__}")
        print(f"    - Capacity: {ride.capacity}")
        print(f"    - Duration: {ride.duration_steps} steps")
        if hasattr(ride, 'speed_deg_per_step'):
            print(f"    - Speed: {ride.speed_deg_per_step}°/step")
        print(f"    - State: {ride.state}")
    print()
    
    print(f"Running {sim.steps} simulation steps...")
    print("Close the matplotlib window when you're done observing.")
    print()
    print("What to look for:")
    print("  ✓ Pirate Ship - Should swing back and forth")
    print("  ✓ Ferris Wheel - Should rotate continuously")
    print("  ✓ Roller Coaster - Should move up and down")
    print("  ✓ Spider Ride - Should spin with 6 arms")
    print("  ✓ Patrons should turn orange when queuing")
    print("  ✓ Patrons should turn green when riding")
    print("  ✓ Ride borders change color with state")
    print()
    
    sim.run()
    
    print("=" * 60)
    print("TEST COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    test_all_rides()
