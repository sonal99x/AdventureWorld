"""
Test script to verify rides are animating correctly
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from simulation import Simulation
import time

def test_animation():
    print("Loading simulation...")
    sim = Simulation()
    sim.load_map("data/map1.csv")
    params = sim.load_params("data/params1.csv")
    sim.apply_params(params)
    
    print(f"\nLoaded {len(sim.rides)} rides:")
    for i, ride in enumerate(sim.rides, 1):
        print(f"{i}. {ride.__class__.__name__} - {ride.name}")
        print(f"   Initial angle: {ride.angle_deg if hasattr(ride, 'angle_deg') else 'N/A'}")
        print(f"   State: {ride.state}")
        print(f"   Queue: {len(ride.queue)}")
        print(f"   On ride: {len(ride.on_ride)}")
    
    print("\nSimulating 10 steps without patrons to test animation...")
    for step in range(10):
        for ride in sim.rides:
            ride.step_change()
        
        if step % 3 == 0:
            print(f"\nStep {step}:")
            for ride in sim.rides:
                angle = ride.angle_deg if hasattr(ride, 'angle_deg') else 'N/A'
                print(f"  {ride.name}: state={ride.state}, angle={angle}")
    
    print("\n" + "="*60)
    print("Adding patrons to queues and testing ride operations...")
    print("="*60)
    
    # Add patrons to each ride's queue
    for i, ride in enumerate(sim.rides):
        for j in range(min(3, ride.capacity)):
            patron = sim.patrons[i * 3 + j] if (i * 3 + j) < len(sim.patrons) else None
            if patron:
                patron.state = "queuing"
                ride.queue.append(patron)
        print(f"\n{ride.name}: Added {len(ride.queue)} patrons to queue")
    
    print("\nSimulating 20 steps with patrons...")
    for step in range(20):
        for ride in sim.rides:
            ride.step_change()
        
        if step in [0, 5, 10, 15, 19]:
            print(f"\nStep {step}:")
            for ride in sim.rides:
                angle = ride.angle_deg if hasattr(ride, 'angle_deg') else 'N/A'
                y_pos = ride.y_position if hasattr(ride, 'y_position') else 'N/A'
                print(f"  {ride.name}:")
                print(f"    State: {ride.state}")
                print(f"    Angle: {angle}")
                print(f"    Y-pos: {y_pos}")
                print(f"    Queue: {len(ride.queue)}, On ride: {len(ride.on_ride)}")
    
    print("\n" + "="*60)
    print("Animation test complete!")
    print("="*60)

if __name__ == "__main__":
    test_animation()
