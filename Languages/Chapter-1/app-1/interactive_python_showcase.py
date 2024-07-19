import sys
import random
import time
from datetime import datetime

# Check Python version
if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 6):
    print("This script requires Python 3.6 or higher.")
    sys.exit(1)

# Try to import matplotlib, but continue if it's not available
try:
    import matplotlib.pyplot as plt
    matplotlib_available = True
except ImportError:
    print("matplotlib is not installed. Visualization features will be disabled.")
    matplotlib_available = False
except Exception as e:
    print(f"An error occurred while importing matplotlib: {e}")
    matplotlib_available = False
else:
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

    # Access the missing attributes
    Figure
    FigureCanvas

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

    def demonstrate_data_analysis(self):
        self.generate_data()
        avg, max_val, min_val = self.analyze_data()
        print(f"\nGenerated data: {self.data}")
        print(f"Average: {avg:.2f}")
        print(f"Maximum: {max_val}")
        print(f"Minimum: {min_val}")

    def demonstrate_advanced_features(self):
        even_squares = [x**2 for x in self.data if x % 2 == 0]
        print(f"Squares of even numbers: {even_squares}")
        avg = sum(self.data) / len(self.data)
        sorted_data = sorted(self.data, key=lambda x: abs(x - avg))
        print(f"Data sorted by distance from mean: {sorted_data}")

    def demonstrate_error_handling(self):
        try:
            result = 10 / 0
            print(f"Result: {result}")  # This line demonstrates using the result variable
        except ZeroDivisionError as e:
            print(f"Caught a division error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def demonstrate_file_operations(self):
        try:
            with open("python_demo_log.txt", "w") as f:
                f.write(f"Log created at {datetime.now()}\n")
                f.write(f"Data analyzed: {self.data}\n")
            print("Log file 'python_demo_log.txt' has been created.")
        except IOError as e:
            print(f"Unable to create log file: {e}")

    def run_showcase(self):
        while True:
            self.print_fancy_header("Python Showcase Menu")
            print("1. Data Analysis")
            print("2. Data Visualization")
            print("3. Advanced Python Features")
            print("4. Error Handling")
            print("5. File Operations")
            print("6. Countdown Timer")
            print("7. Exit")
            
            choice = input("Enter your choice (1-7): ")
            
            if choice == '1':
                self.print_fancy_header("Data Analysis")
                self.demonstrate_data_analysis()
            elif choice == '2':
                self.print_fancy_header("Data Visualization")
                self.visualize_data()
            elif choice == '3':
                self.print_fancy_header("Advanced Python Features")
                self.demonstrate_advanced_features()
            elif choice == '4':
                self.print_fancy_header("Error Handling")
                self.demonstrate_error_handling()
            elif choice == '5':
                self.print_fancy_header("File Operations")
                self.demonstrate_file_operations()
            elif choice == '6':
                self.print_fancy_header("Countdown Timer")
                seconds = int(input("Enter number of seconds for countdown: "))
                self.countdown_timer(seconds)
            elif choice == '7':
                self.print_fancy_header("Thank You!")
                print("This concludes the Python Showcase. Explore the code to learn more!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        showcase = PythonShowcase()
        showcase.run_showcase()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please report this issue along with the error message above.")