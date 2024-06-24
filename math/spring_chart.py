import numpy as np
import matplotlib.pyplot as plt

# Parameters for the spring oscillation
amplitude = 1.0  # Amplitude of the oscillation
frequency = 1.0  # Frequency of the oscillation
phase = 0.0      # Phase shift
time = np.linspace(0, 10, 500)  # Time array from 0 to 10 seconds

# Displacement as a function of time (simple harmonic motion)
displacement = amplitude * np.sin(2 * np.pi * frequency * time + phase)

# Plotting the spring oscillation
plt.figure(figsize=(10, 6))
plt.plot(time, displacement, label='Spring Oscillation', color='b')

# Adding titles and labels
plt.title('Spring Oscillation Chart')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.legend()

# Adding a grid
plt.grid(True)

# Save the figure as a PNG file
plt.savefig('spring_chart.png')

# Show the plot
plt.show()
