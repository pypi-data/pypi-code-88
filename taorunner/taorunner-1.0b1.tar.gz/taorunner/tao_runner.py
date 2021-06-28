# Author: Botao Yu
import os
from . import runner_utils


class TaoRunner(object):
    def __init__(self, task_file, log_dir='log', save_task_log=False):
        assert os.path.isfile(task_file), "Task file that contains the tasks to do (%s) does not exist." % task_file
        self.task_file = task_file

        os.makedirs(log_dir, exist_ok=True)
        self.log_dir = log_dir

        self.log_file = os.path.join(self.log_dir, 'runner.log')

        self.save_task_log = save_task_log
        if self.save_task_log:
            self.task_log_dir = os.path.join(self.log_dir, 'task_log')
            os.makedirs(self.task_log_dir, exist_ok=True)
        else:
            self.task_log_dir = None

    def run(self):
        command = None
        command_md5 = None

        try:
            while True:
                command = runner_utils.get_command_and_update_command_file(self.task_file)
                if command is None:
                    break

                command_md5 = runner_utils.get_md5_value(command)

                current_time = runner_utils.get_time_str()
                log_line = '[%s] Start running command (%s): %s' % (current_time, command_md5, command)
                print(log_line)
                with open(self.log_file, 'a+') as f:
                    f.write(log_line + '\n')

                if self.save_task_log:
                    task_log_path = os.path.join(self.task_log_dir,
                                                 'task-log_%s_%s.log' % (current_time.replace(':', '-').replace(' ', '-'),
                                                                     command_md5))
                    real_command = command + ' | tee %s' % task_log_path
                else:
                    real_command = command

                self.run_command(real_command)

                log_line = '[%s] Done running command (%s): %s' % (runner_utils.get_time_str(), command_md5, command)
                print(log_line)
                with open(self.log_file, 'a+') as f:
                    f.write(log_line + '\n')

                command = None
                command_md5 = None

        except KeyboardInterrupt:
            log_line = '[%s] KeyboardInterrupt when running command (%s): %s' % (runner_utils.get_time_str(),
                                                                                 command_md5, command)
            print(log_line)
            with open(self.log_file, 'a+') as f:
                f.write(log_line + '\n')
            raise
        except Exception:
            log_line = '[%s] Error and exit when running command (%s): %s' % (runner_utils.get_time_str(),
                                                                              command_md5, command)
            print(log_line)
            with open(self.log_file, 'a+') as f:
                f.write(log_line + '\n')
            raise
        finally:
            log_line = '[%s] Runner done.' % (runner_utils.get_time_str(),)
            print(log_line)
            with open(self.log_file, 'a+') as f:
                f.write(log_line + '\n')

    @staticmethod
    def run_command(command):
        os.system(command)
