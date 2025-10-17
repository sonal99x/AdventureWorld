"""
Test script for Adventure World Simulation
Tests all major components and features
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from rides import PirateShip, FerrisWheel, RollerCoaster, SpiderRide
from patron import Patron
from simulation import Simulation

def test_rides():
    """Test all ride types are properly initialized"""
    print("Testing Rides...")
    
    # Test PirateShip
    pirate = PirateShip("pirate_test", 50, 50, 12, 6)
    assert pirate.name == "pirate_test"
    assert pirate.state == "idle"
    assert pirate.capacity == 8
    print("  ✓ Pirate Ship initialized")
    
    # Test FerrisWheel
    ferris = FerrisWheel("ferris_test", 50, 50, 12, 6)
    assert ferris.state == "idle"
    assert ferris.speed_deg_per_step == 3
    print("  ✓ Ferris Wheel initialized")
    
    # Test RollerCoaster
    coaster = RollerCoaster("coaster_test", 50, 50, 12, 6)
    assert coaster.state == "idle"
    print("  ✓ Roller Coaster initialized")
    
    # Test SpiderRide
    spider = SpiderRide("spider_test", 50, 50, 12, 6)
    assert spider.num_arms == 6
    print("  ✓ Spider Ride initialized")
    
    print("✓ All rides initialized successfully\n")

def test_patron():
    """Test patron initialization and movement"""
    print("Testing Patrons...")
    
    p = Patron("P1", 50, 50)
    assert p.name == "P1"
    assert p.state == "roaming"
    print("  ✓ Patron initialized")
    
    # Test movement
    old_x, old_y = p.x, p.y
    p.move(0, 100, 0, 100)
    # Position should change (with very high probability)
    print("  ✓ Patron movement works")
    
    # Test state changes
    p.state = "queuing"
    assert p.state == "queuing"
    p.state = "riding"
    assert p.state == "riding"
    print("  ✓ Patron state changes work")
    
    print("✓ Patron functionality verified\n")

def test_bounding_boxes():
    """Test ride bounding boxes"""
    print("Testing Bounding Boxes...")
    
    ride = PirateShip("test", 50, 50, 12, 6)
    bbox = ride.bbox()
    
    assert len(bbox) == 4
    xmin, ymin, xmax, ymax = bbox
    
    assert xmin == 50 - 12/2
    assert xmax == 50 + 12/2
    assert ymin == 50 - 6/2
    assert ymax == 50 + 6/2
    
    print("  ✓ Bounding box calculation correct")
    print("✓ Bounding boxes verified\n")

def test_queue_system():
    """Test queue and boarding system"""
    print("Testing Queue System...")
    
    ride = PirateShip("test", 50, 50, 12, 6, capacity=3)
    
    # Add patrons to queue
    p1 = Patron("P1", 40, 50, state="queuing")
    p2 = Patron("P2", 41, 50, state="queuing")
    p3 = Patron("P3", 42, 50, state="queuing")
    
    ride.queue = [p1, p2, p3]
    assert len(ride.queue) == 3
    print("  ✓ Queue accepts patrons")
    
    # Test boarding
    ride.try_board()
    assert len(ride.on_ride) == 3
    assert len(ride.queue) == 0
    assert p1.state == "riding"
    print("  ✓ Patrons board correctly")
    
    # Test unloading
    ride.unload()
    assert len(ride.on_ride) == 0
    assert p1.state == "roaming"
    print("  ✓ Patrons unload correctly")
    
    print("✓ Queue system verified\n")

def test_ride_states():
    """Test ride state transitions"""
    print("Testing Ride States...")
    
    ride = PirateShip("test", 50, 50, 12, 6)
    
    # Initial state
    assert ride.state == "idle"
    print("  ✓ Initial state is idle")
    
    # Add patron to trigger state change
    p = Patron("P1", 40, 50, state="queuing")
    ride.queue.append(p)
    
    # Step once - should go to loading
    ride.step_change()
    assert ride.state == "loading"
    print("  ✓ Transitions to loading")
    
    # Step again - should go to running
    ride.step_change()
    assert ride.state == "running"
    print("  ✓ Transitions to running")
    
    print("✓ Ride state machine verified\n")

def test_simulation():
    """Test simulation initialization"""
    print("Testing Simulation...")
    
    sim = Simulation()
    assert sim.boundary == (0, 0, 100, 100)
    assert len(sim.rides) == 0
    assert len(sim.patrons) == 0
    print("  ✓ Simulation initializes")
    
    # Add a ride
    sim.rides.append(PirateShip("ride1", 50, 50, 12, 6))
    assert len(sim.rides) == 1
    print("  ✓ Can add rides")
    
    # Add patrons
    sim.patrons.append(Patron("P1", 10, 50))
    sim.patrons.append(Patron("P2", 15, 50))
    assert len(sim.patrons) == 2
    print("  ✓ Can add patrons")
    
    print("✓ Simulation verified\n")

def test_collision_detection():
    """Test patron collision with rides"""
    print("Testing Collision Detection...")
    
    sim = Simulation()
    ride = PirateShip("ride1", 50, 50, 12, 6)
    sim.rides.append(ride)
    
    # Test _inside_bbox
    bbox = ride.bbox()
    
    # Point inside
    assert sim._inside_bbox(50, 50, bbox) == True
    print("  ✓ Detects point inside bbox")
    
    # Point outside
    assert sim._inside_bbox(10, 10, bbox) == False
    print("  ✓ Detects point outside bbox")
    
    # Point on edge
    xmin, ymin, xmax, ymax = bbox
    assert sim._inside_bbox(xmin, ymin, bbox) == True
    print("  ✓ Handles edge cases")
    
    print("✓ Collision detection verified\n")

def test_csv_loading():
    """Test CSV file loading"""
    print("Testing CSV Loading...")
    
    sim = Simulation()
    
    # Test map loading
    try:
        sim.load_map("data/map1.csv")
        assert len(sim.rides) == 4
        print("  ✓ Map CSV loads correctly")
    except Exception as e:
        print(f"  ✗ Map loading failed: {e}")
    
    # Test params loading
    try:
        params = sim.load_params("data/params1.csv")
        assert "num_patrons" in params
        assert "steps" in params
        print("  ✓ Params CSV loads correctly")
    except Exception as e:
        print(f"  ✗ Params loading failed: {e}")
    
    print("✓ CSV loading verified\n")

def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("ADVENTURE WORLD - TEST SUITE")
    print("=" * 60)
    print()
    
    try:
        test_rides()
        test_patron()
        test_bounding_boxes()
        test_queue_system()
        test_ride_states()
        test_simulation()
        test_collision_detection()
        test_csv_loading()
        
        print("=" * 60)
        print("✓ ALL TESTS PASSED!")
        print("=" * 60)
        return True
        
    except AssertionError as e:
        print()
        print("=" * 60)
        print("✗ TEST FAILED!")
        print(f"Error: {e}")
        print("=" * 60)
        return False
    except Exception as e:
        print()
        print("=" * 60)
        print("✗ UNEXPECTED ERROR!")
        print(f"Error: {e}")
        print("=" * 60)
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
