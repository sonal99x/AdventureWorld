import argparse
from simulation import Simulation
from rides import PirateShip
from patron import Patron

def run_interactive():
    print("Interactive mode")
    steps = int(input("How many steps? (e.g., 500): ") or "500")
    patrons = int(input("How many patrons? (e.g., 50): ") or "50")

    sim = Simulation()
    # default map with one ride
    sim.boundary = (0, 0, 100, 100)
    sim.rides.append(PirateShip("pirate_1", 50, 60, 12, 6))

    xmin, ymin, xmax, ymax = sim.boundary
    # Spawn patrons distributed across park
    import random
    for i in range(patrons):
        spawn_x = random.uniform(xmin + 5, xmax - 5)
        spawn_y = random.uniform(ymin + 5, ymax - 5)
        sim.patrons.append(Patron(f"P{i+1}", x=spawn_x, y=spawn_y))

    sim.steps = steps
    sim.run()

def run_batch(map_csv, params_csv):
    print("Batch mode")
    sim = Simulation()
    if map_csv:
        sim.load_map(map_csv)
    if params_csv:
        params = sim.load_params(params_csv)
        sim.apply_params(params)
    sim.run()

def main():
    parser = argparse.ArgumentParser(description="Adventure World")
    parser.add_argument("-i", "--interactive", action="store_true", help="interactive mode")
    parser.add_argument("-f", "--file", help="map CSV (batch mode)")
    parser.add_argument("-p", "--params", help="params CSV (batch mode)")
    args = parser.parse_args()

    if args.interactive:
        run_interactive()
    else:
        run_batch(args.file, args.params)

if __name__ == "__main__":
    main()
