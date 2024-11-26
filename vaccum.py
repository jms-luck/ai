
class VacuumCleanerAgent:
    def __init__(self):
        self.environment = {
            'A': 'Clean',
            'B': 'Dirty'
        }
        self.current_location = 'A'

    def sense(self):
        return self.environment[self.current_location]

    def act(self):
        if self.sense() == 'Dirty':
            print(f"Location {self.current_location} is Dirty. Cleaning...")
            self.environment[self.current_location] = 'Clean'
            print(f"Location {self.current_location} is now Clean.")
        else:
            print(f"Location {self.current_location} is already Clean. Moving...")
            self.move()

    def move(self):
        self.current_location = 'B' if self.current_location == 'A' else 'A'
        print(f"Moved to location {self.current_location}.")

    def run(self, steps=5):
        for step in range(steps):
            print(f"\nStep {step + 1}:")
            self.act()

if __name__ == "__main__":
    agent = VacuumCleanerAgent()
    agent.run(steps=5)
