import matplotlib.pyplot as plt


# This function takes x and y values and displays a line plot
def display_line(x_values, y_values):
    # Plot the x and y values as a line
    plt.plot(x_values, y_values)

    # Show the plot window
    plt.show()


# This function runs the task: prepares data and calls the display_line function
def run_task1():
    # Create a list of x values
    x_values = [1, 2, 3, 4, 5]

    # Create a list of y values (square of x)
    y_values = [1, 4, 9, 16, 25]

    # Call the display_line function with the x and y values
    display_line(x_values, y_values)


# This ensures the program runs only if this file is executed directly
if __name__ == "__main__":
    run_task1()
