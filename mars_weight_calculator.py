"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # Fill this function out!
    your_weight_on_earth = float(input("Enter a weight on Earth: "))
    print("The equivalent weight on Mars: ", round(your_weight_on_earth * 0.378, 2))

if __name__ == "__main__":
    main()
