import matplotlib.pyplot as plt
from arduscope import Arduscope
from arduscope import ArduscopeMeasure

with Arduscope(port='/dev/ttyUSB0') as arduino:
    arduino.frequency = 5000
    arduino._trigger_tol
    arduino.pulse_width = 0.2
    arduino.trigger_value = 1.0
    arduino.amplitude = 5.0
    arduino.n_channels = 2
    arduino.trigger_channel = "A0"
    arduino.trigger_offset = 0.0

    arduino.start_acquire()
    arduino.live_plot()
    arduino.clear_buffer()
    arduino.wait_until(n_screens=10, timeout=None)

measure = arduino.measure

measure.save("data.csv")  # Formato CSV (separado por comas)
measure.save("data.npz")  # Formato NPZ (array comprimido de Numpy)
measure.save("data.json")  # Formato JSON (objeto de JavaScript)

x_a0 = measure.x[0]
x_a1 = measure.x[1]
y_a0_mean = measure.channels[0].mean(axis=0)
y_a1_mean = measure.channels[1].mean(axis=0)
y_a0_std = measure.channels[0].std(axis=0)
y_a1_std = measure.channels[1].std(axis=0)

ax: plt.Axes
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(measure.x[0], measure.channels[0].mean(axis=0), label='a0')
ax.plot(measure.x[1], measure.channels[1].mean(axis=0), label='a1')
ax.axhline(trigger, label=trigger_label, ls="dashed")
ax.set_title(f"Trigger: {measure.trigger_ch}")

plt.show()

# measure.save("data.csv")
# measure.save("data.npz")
# measure.save("data.json")

measure = ArduscopeMeasure.load("data.csv")

