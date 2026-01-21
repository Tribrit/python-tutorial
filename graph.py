
import matplotlib.pyplot as plt # type: ignore
import numpy as np

# Generate x values from -5 to 5
x = np.linspace(-5, 5, 100)

# Calculate y values (e^x)
y = np.exp(x)

# Create the plot
plt.plot(x, y, label='e^x')

# Customize the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Function')
plt.grid(True)
plt.legend()
plt.savefig("graph.pdf")

# Display the plot
plt.show()