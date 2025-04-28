import time
import matplotlib.pyplot as plt

# Engine class
class Engine:
    def __init__(self):
        self.status = "off"
    
    def start(self):
        self.status = "running"
        print("Engine started")

    def run(self):
        print("Engine running")

    def shut_down(self):
        self.status = "off"
        print("Engine shut down")

# Rotor class
class Rotor:
    def __init__(self, rpm=0):
        self.rpm = rpm

    def spin(self):
        self.rpm = 500  # Default rotor speed
        print(f"Rotor spinning at {self.rpm} RPM")

    def stop(self):
        self.rpm = 0
        print("Rotor stopped")

# Transmission class
class Transmission:
    def __init__(self):
        self.status = "idle"

    def engage(self):
        self.status = "engaged"
        print("Transmission engaged")

    def disengage(self):
        self.status = "idle"
        print("Transmission disengaged")

# FuelSystem class
class FuelSystem:
    def __init__(self):
        self.fuel_level = 100  # in percentage

    def consume_fuel(self):
        self.fuel_level -= 0.5  # Consuming fuel every second
        if self.fuel_level < 0:
            self.fuel_level = 0
        print(f"Fuel level: {self.fuel_level}%")

    def refuel(self):
        self.fuel_level = 100
        print("Fuel tank refilled to 100%")

# Function to plot fuel usage
def plot_fuel_usage(times, fuel_levels):
    plt.plot(times, fuel_levels)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Fuel Level (%)')
    plt.title('Fuel Usage Over Time')
    plt.show()

# Main function
def main():
    engine = Engine()
    rotor = Rotor()
    transmission = Transmission()
    fuel_system = FuelSystem()

    times = []
    fuel_levels = []

    # Stage 1: Turning on the system
    print("Starting Helicopter System...")
    engine.start()
    rotor.spin()
    transmission.engage()

    start_time = time.time()
    elapsed_time = 0

    # Stage 2: Continual usage of the system in flight
    while elapsed_time < 10:  # Let's simulate 10 seconds of flight time
        elapsed_time = time.time() - start_time
        fuel_system.consume_fuel()
        times.append(elapsed_time)
        fuel_levels.append(fuel_system.fuel_level)
        time.sleep(1)  # Simulate the passage of time

    # Stage 3: Landing and shutting down
    print("\nLanding Helicopter...")
    rotor.stop()
    transmission.disengage()
    engine.shut_down()

    # Plot the fuel usage over time
    plot_fuel_usage(times, fuel_levels)

# Run the main function
if __name__ == "__main__":
    main()


