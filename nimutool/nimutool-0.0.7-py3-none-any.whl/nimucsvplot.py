import matplotlib.pyplot as plt
import argparse
from nimutool.data import *
from pathlib import Path

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', default='ni_data.csv')
    parser.add_argument('--filename2', required=False, help='Optional another file to plot from')
    parser.add_argument('--filename2_offset_sec', required=False, default=0, help='Offset between file1 and file2')
    parser.add_argument('--save-path', required=False, help='Writes plots as png files to the given path')
    args = parser.parse_args()

    src = load_data(args.filename, args.filename2, file2_offset_sec=args.filename2_offset_sec)
    gyro, accelerometer = src.get_imu_data()
    dcm, inno, pos, vel = src.get_ekf_data()

    plotter = Plotter(Path(args.save_path))
    plotter.add_df_plot('raw', gyro, 'Angular velocity', 'rad/s')
    plotter.add_df_plot('raw', accelerometer, 'Linear acceleration', 'm/s^2')
    plotter.add_df_plot('ekf', dcm, 'DCM lowest row', 'rad/s')
    plotter.add_df_plot('ekf', pos, 'EKF position', 'm')
    plotter.add_df_plot('ekf', vel, 'EKF velocity', 'm/s')
    plotter.add_df_plot('ekf', inno, 'EKF innovation', 'rad/s')
    plotter.plot()

    plt.show()
