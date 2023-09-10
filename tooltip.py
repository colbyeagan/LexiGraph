import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]

fig, ax = plt.subplots()

# Create the line plot
line, = ax.plot(x, y, marker='o', linestyle='-')

# Function to display a tooltip when hovering over a data point
def display_tooltip(event):
    if event.inaxes == ax:
        # Convert data coordinates to display coordinates
        x_data, y_data = line.get_data()
        for i, xi in enumerate(x_data):
            if abs(event.xdata - xi) < 0.1 and abs(event.ydata - y_data[i]) < 0.1:
                tooltip_text = f'Price: ${y_data[i]}'
                ax.annotate(tooltip_text, (xi, y_data[i]), textcoords="offset points", xytext=(0, 10), ha='center')
                plt.draw()

# Function to remove the tooltip when the mouse moves away
def remove_tooltip(event):
    if event.inaxes == ax:
        for text in ax.texts:
            text.remove()
        plt.draw()

# Connect the event handlers
fig.canvas.mpl_connect('motion_notify_event', display_tooltip)
fig.canvas.mpl_connect('axes_leave_event', remove_tooltip)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph with Tooltips')

plt.show()  # Keep the plot window open
