import fcntl
import multiprocessing
import shutil
import sys
import time
import timeit
from contextlib import redirect_stdout, redirect_stderr

import qualys_etl.etld_lib.etld_lib_config as etld_lib_config
import qualys_etl.etld_lib.etld_lib_credentials as etld_lib_credentials
import qualys_etl.etld_lib.etld_lib_functions as etld_lib_functions

global target_module_to_run
global target_method_in_module_to_run
global spawned_process
global spawned_process_max_run_time
global spawned_process_start_time
global spawned_process_stop_time
global spawned_process_sleep_time
global spawned_process_count_to_status_update
global spawned_process_status_count
global log_file_max_size
global log_file_path
global log_file_rotate_path
global lock_file
global log_dir


def spawn_etl_in_background_with_arg(args_list=[], max_proc=None):
    global spawned_process
    global spawned_process_start_time
    global spawned_process_status_count
    spawn_process_list = []

    # target=etl_host_list_detection
    # name=etl_hld_d_2021_06_03T00:00:00Z_b_000001
    # args=list_of_host_ids
    # Create jobs list  ready to spawn
    for arg in args_list:
        arg: dict
        arg.get('target_module_to_run')
        arg.get('target_method_in_module_to_run')
        arg.get('method_arguments')

        spawned_process = multiprocessing.Process(
            target=arg.get('target_module_to_run'),
            name=arg.get('target_method_in_module_to_run'),
            args=arg.get('method_arguments'))
        spawn_process_list.append(spawned_process)


#    spawned_process = multiprocessing.Process(target=target_module_to_run, name=target_method_in_module_to_run)
#    spawned_process.start()
#    etld_lib_functions.logger.info("Spawned ETL in Background")
#    spawned_process_start_time = timeit.default_timer()
#    spawned_process_status_count = 0
#
#    while spawned_process.is_alive():
#        spawned_process_report_status()
#
#    spawned_process_gracefully_ended()
#    time.sleep(1)


def spawn_etl_in_background():
    global spawned_process
    global spawned_process_start_time
    global spawned_process_status_count

    spawned_process = multiprocessing.Process(target=target_module_to_run, name=target_method_in_module_to_run)
    spawned_process.start()
    etld_lib_functions.logger.info("Spawned ETL in Background")
    spawned_process_start_time = timeit.default_timer()
    spawned_process_status_count = 0

    while spawned_process.is_alive():
        spawned_process_report_status()

    spawned_process_gracefully_ended()
    time.sleep(1)


def spawned_process_report_status():
    now = timeit.default_timer()
    run_time = (now - spawned_process_start_time)
    if run_time > spawned_process_max_run_time:
        terminate_spawned_process()
    else:
        spawned_process_status_update()


def spawned_process_gracefully_ended():
    global spawned_process_stop_time
    spawned_process_stop_time = timeit.default_timer()
    run_time = (spawned_process_stop_time - spawned_process_start_time)
    etld_lib_functions.logger.info(f"Final Runtime: {run_time:,.0f} seconds")


def spawned_process_status_update():
    global spawned_process_status_count

    time.sleep(spawned_process_sleep_time)
    if spawned_process_status_count > spawned_process_count_to_status_update or spawned_process_status_count == 0:
        etld_lib_functions.logger.info(f"Job PID {str(spawned_process.pid)} {target_module_to_run.__name__} "
                             f"job running in background.")
        spawned_process_status_count = 1
    else:
        spawned_process_status_count = spawned_process_status_count + 1


def terminate_spawned_process():
    etld_lib_functions.logger.error(f"Max Run Time: {spawned_process_max_run_time:,.0f} Seconds Exceeded")
    etld_lib_functions.logger.error(f"Please review for issues that are slowing down the program.")
    etld_lib_functions.logger.error(f"Terminating job.")
    spawned_process.terminate()
    spawned_process.join()
    exit(1)


def rotate_log_check():
    if log_file_path.is_file():
        log_file_size = log_file_path.stat().st_size  # In Bytes
        if log_file_size > log_file_max_size:
            shutil.copy2(log_file_path, log_file_rotate_path, follow_symlinks=True)
            fo = open(log_file_path, 'w+')
            fo.close()


def etl_main():
    try:
        with open(lock_file, 'wb+') as lock_program_fcntl:        # If locked, exit.
            fcntl.flock(lock_program_fcntl, fcntl.LOCK_EX | fcntl.LOCK_NB)
            rotate_log_check()
            if log_dir.is_dir():
                with open(log_file_path, 'a', newline='', encoding='utf-8') as log_fo:
                    with redirect_stdout(log_fo), redirect_stderr(sys.stdout):
                        etld_lib_functions.main(my_logger_prog_name=target_module_to_run.__name__)
                        etld_lib_config.main()
                        etld_lib_credentials.main()
                        spawn_etl_in_background()
    except Exception as e:
        print(f"Program is already running.  Please re-run when ready. {__file__} ")
        print(f"Exception: {e}")
        exit(1)

