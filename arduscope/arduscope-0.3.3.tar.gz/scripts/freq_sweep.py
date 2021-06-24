import numpy as np
import matplotlib.pyplot as plt
from arduscope import Arduscope, fit_signal, sine, UnfittableDataError
from arduscope.wave_generator import WaveGenerator


# Nuevo generador de funciones
wg = WaveGenerator(duration=20)

# Propiedades del canal 1
wg.channel1.amplitude = 1.0     # Amplitud (0.0 a 1.0)
wg.channel1.frequency = 100     # Frecuencia (1 a 4000 en Hz)
wg.channel1.phase = 0           # Fase en radianes
wg.channel1.waveform = "sine"   # "sine", "square", "triangle"
wg.channel1.enabled = True      # Canal encendido / apagado

# Propiedades del canal 2
wg.channel2.enabled = False

# Contexto para conectar / desconectar el Arduscopio
with Arduscope(port='/dev/ttyUSB0') as arduino:
    # Configura los parámetros del Arduscopio
    arduino.trigger_value = 2.5  # Valor de trigger
    arduino.amplitude = 5.0  # Amplitud máxima de la señal medida
    arduino.n_channels = 2  # Cantidad de canales
    arduino.trigger_channel = "A0"  # Modo del trigger
    arduino.trigger_offset = 0.0  # Offset del trigger

    # Barrido de fase
    for frequency in np.linspace(200, 700, 11):
        # Configura la frecuencia del canal 1
        wg.channel1.frequency = frequency
        # Configura la frecuencia de adquisición del Arduscopio
        arduino.frequency = min([max([500, int(frequency) * 20]), 10000])

        # Inicia la reproducción del sonido
        with wg.play():
            # Inicia la adquisición
            arduino.start_acquire()
            # Espera 50 pantallas
            arduino.wait_until(n_screens=50)
            # Detiene la adquisición
            arduino.stop_acquire()
            # Transfiere las mediciones a un contenedor
            measure = arduino.measure
            measure.save(f"datos_{int(frequency)}.csv", overwrite=True)

            # Grafica los canales (con el mejor ajuste disponible)
            fig: plt.Figure
            ax: plt.Axes
            fig, ax = plt.subplots(1, 1, figsize=(8, 6))

            fit_results = []
            for i in range(arduino.n_channels):
                # Coordenada x (con el offset correspondiente a cada canal)
                x = measure.x[i]
                # Coordenada y promediada en las 50 pantallas
                y = measure.channels[i][0:50].mean(axis=0)

                # Intenta realizar un ajuste
                try:
                    params, stds, rmse, = fit_signal(sine, x, y)
                except (UnfittableDataError, RuntimeError):
                    # Si el ajuste falla reporta la situación
                    print(f"\nEl canal {i} no pudo ser ajustado\n")
                    fit_results.append(None)
                    continue

                # Almacena los parámetros del ajuste
                fit_results.append((params, stds, rmse))

                # Grafica el ajuste, los datos y usa el RMSE para dibujar errores
                x_fit = np.linspace(min(x), max(x), num=x.size*20)
                y_fit = sine(x_fit, *params)
                ax.plot(x, y, ls='', marker='o', color=f"C{i}")
                ax.plot(x_fit, y_fit, color=f"C{i}")
                ax.fill_between(x_fit, y_fit-rmse, y_fit+rmse, color=f"C{i}", alpha=0.3)

                # Imprime los resultados
                print(f'\nCanal A{i} para {frequency:.2f}Hz:\n'
                      f'  Amplitud:    {params[0]} +/- {stds[0]}\n'
                      f'  Frecuencia:  {params[1]} +/- {stds[1]}\n'
                      f'  Fase:        {params[2]} +/- {stds[2]}\n'
                      f'  Offset:      {params[3]} +/- {stds[3]}')

            plt.tight_layout()
            plt.show()

            # Borra el buffer antes de comenzar la siguiente medición
            arduino.clear_buffer()

with open("ajustes.txt", mode='w') as file:
    for result in fit_results:
        if result is not None:
            params, stds, rmse = result
            a, f, p, o = params
            error_a, error_f, error_p, error_o = stds
            file.write(f"{a} {f} {p} {o} "
                       f"{error_a} {error_f} {error_p} {error_o} {rmse}\n")
