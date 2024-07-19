import sys

# Check Python version
if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 6):
    print("This script requires Python 3.6 or higher.")
    sys.exit(1)

import random
import time
from datetime import datetime

# Try to import matplotlib, but continue if it's not available
try:
    import matplotlib.pyplot as plt
    matplotlib_available = True
except ImportError:
    print("matplotlib is not installed. Visualization features will be disabled.")
    matplotlib_available = False

class PythonShowcase:
    def __init__(self):
        self.data = []

    @staticmethod
    def print_fancy_header(text):
        """Print a fancy header with ASCII art."""
        print("\n" + "=" * 50)
        print(f"{'*' * 5} {text.upper()} {'*' * 5}")
        print("=" * 50)

    def generate_data(self):
        """Generate random data and store it."""
        self.data = [random.randint(1, 100) for _ in range(20)]

    def analyze_data(self):
        """Analyze the generated data."""
        average = sum(self.data) / len(self.data)
        maximum = max(self.data)
        minimum = min(self.data)
        return average, maximum, minimum

    def visualize_data(self):
        """Create a simple plot of the data."""
        if matplotlib_available:
            try:
                plt.figure(figsize=(10, 6))
                plt.plot(self.data, marker='o')
                plt.title("Random Data Visualization")
                plt.xlabel("Index")
                plt.ylabel("Value")
                plt.grid(True)
                plt.savefig("data_visualization.png")
                plt.close()
                print("A plot has been saved as 'data_visualization.png'")
            except Exception as e:
                print(f"An error occurred while creating the plot: {e}")
        else:
            print("Visualization skipped: matplotlib is not available.")

    @staticmethod
    def countdown_timer(seconds):
        """Display a countdown timer."""
        for i in range(seconds, 0, -1):
            print(f"\rCountdown: {i:02d} seconds", end="", flush=True)
            time.sleep(1)
        print("\rCountdown complete!      ")

    def run_showcase(self):
        self.print_fancy_header("Welcome to Python Showcase")
        print("This script demonstrates various Python features with visual enhancements.")

        # Data generation and analysis
        self.generate_data()
        avg, max_val, min_val = self.analyze_data()

        print(f"\nGenerated data: {self.data}")
        print(f"Average: {avg:.2f}")
        print(f"Maximum: {max_val}")
        print(f"Minimum: {min_val}")

        # Visualizing data
        self.print_fancy_header("Data Visualization")
        self.visualize_data()

        # Demonstrating list comprehension and lambda functions
        self.print_fancy_header("Advanced Python Features")
        even_squares = [x**2 for x in self.data if x % 2 == 0]
        print(f"Squares of even numbers: {even_squares}")

        sorted_data = sorted(self.data, key=lambda x: abs(x - avg))
        print(f"Data sorted by distance from mean: {sorted_data}")

        # Demonstrating error handling
        self.print_fancy_header("Error Handling")
        try:
            result = 10 / 0
        except ZeroDivisionError as e:
            print(f"Caught an error: {e}")

        # Demonstrating context manager
        self.print_fancy_header("Context Manager")
        try:
            with open("python_demo_log.txt", "w") as f:
                f.write(f"Log created at {datetime.now()}\n")
                f.write(f"Data analyzed: {self.data}\n")
            print("Log file 'python_demo_log.txt' has been created.")
        except IOError as e:
            print(f"Unable to create log file: {e}")

        # Interactive countdown
        self.print_fancy_header("Interactive Countdown")
        self.countdown_timer(5)

        self.print_fancy_header("Thank You!")
        print("This concludes the Python Showcase. Explore the code to learn more!")

if __name__ == "__main__":
    try:
        showcase = PythonShowcase()
        showcase.run_showcase()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please report this issue along with the error message above.")