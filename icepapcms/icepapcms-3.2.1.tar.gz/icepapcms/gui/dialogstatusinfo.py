from PyQt5 import QtGui, uic
import re
from pkg_resources import resource_filename


class DialogStatusInfo(QtGui.QDialog):

    def __init__(self, parent, icepapsys, addr):
        QtGui.QDialog.__init__(self, parent)
        ui_filename = resource_filename('icepaposc.ui', 'dialogstatusinfo.ui')
        self.ui = self
        uic.loadUi(ui_filename, baseinstance=self.ui)

        self.icepapsys = icepapsys
        self.driver = icepapsys[addr]
        self.icepapAddress = icepapsys[addr].addr
        host = self.icepapsys._comm.host
        windows_name = 'Status Info  |  {}  |  {} {}'.format(host, addr,
                                                             self.driver.name)
        self.setWindowTitle(windows_name)
        self.show()
        self._connect_signals()
        self._do_vstatus()
        self.allDriversCommands = ['?cfg extdisable',
                                   '?ver info',
                                   '?power',
                                   '?positions',
                                   '?warning',
                                   '?alarm',
                                   '?isg ?ssierrtoggles',
                                   '#isg ssiwarningrst',
                                   'm ?ver info',
                                   'm ?rdispol',
                                   '?vstatus DISABLE',
                                   '?vstatus STOPCODE'
                                   ]
        for cmd in self.allDriversCommands:
            self.ui.cbAllDrivers.addItem(cmd)

        self.version_keys = [
            'CONTROLLER',
            'DSP',
            'FPGA',
            'MCPU1',
            'MCPU0',
            'MCPU2',
            'DRIVER']
        reg_exp = "({})\\s*:\\s*(\\d+\\.\\d+)".format(
            "|".join(self.version_keys))
        self.version_reg_exp = re.compile(reg_exp, re.VERBOSE)

    def _connect_signals(self):
        self.ui.btnUpdate.clicked.connect(self._do_vstatus)
        self.ui.btnUpdate.setDefault(False)
        self.ui.btnUpdate.setAutoDefault(False)
        self.ui.txt1Command.returnPressed.connect(self._send_command)
        self.ui.cbAllDrivers.activated.connect(self._send_command_to_drivers)

    def _do_vstatus(self):
        val = ""
        try:
            val = self.driver.vstatus
        except Exception as e:
            print(e)
        self.ui.textBrowser.setText(val)

    def _send_command(self):
        val = ""
        comm = ""
        try:

            comm = "" + str(self.ui.txt1Command.text())
            print(comm)
            val = self.driver.vstatus
            val = self.driver.send_cmd(comm)
            val = ' '.join(val)
            val = comm.upper() + " " + val
            print(val)
        except Exception as e:
            print(e)
        self.ui.textBrowser.setText(comm + "\n" + val)

    def _send_command_to_drivers(self):
        sel = self.ui.cbAllDrivers.currentText()
        sel_split = sel.split(' ')
        txt = ''
        if sel == '?positions':
            header = 'dr name axis absenc encin inpos tgtenc'
            txt = header + '\n'
            # for driver in self.driver.getDriversAlive():
            for driver in self.icepapsys.find_axes(only_alive=True):
                try:
                    val0 = self.icepapsys[driver].name
                    val1 = self.icepapsys[driver].pos
                    val2 = self.icepapsys[driver].enc_absenc
                    val3 = self.icepapsys[driver].enc_encin
                    val4 = self.icepapsys[driver].enc_inpos
                    val5 = self.icepapsys[driver].get_cfg('TGTENC')
                    val5 = val5['TGTENC']
                    if val0 == '':
                        val0 = 'noname'
                    txt = '{} {} {} {} {} {} {} {}\n'.format(txt, driver,
                                                             val0, val1, val2,
                                                             val3, val4, val5)
                    self.ui.textBrowser.setText(txt)
                except Exception as e:
                    print(e)
        elif sel == '?ver info':
            # for driver in self.driver.getDriversAlive():
            for driver in self.icepapsys.find_axes(only_alive=True):
                try:
                    val = self._get_version_info_dict(driver)
                    txt = '{} {} {}\n'.format(txt, driver, (val))
                    self.ui.textBrowser.setText(txt)
                except Exception as e:
                    print(e)
            self.ui.textBrowser.setText(txt)
        elif sel == 'm ?ver info':
            for contr in self._get_racks_alive():
                try:
                    val = self._get_version_info_dict(contr)
                    txt = '{} {} {}\n'.format(txt, contr, val)
                    self.ui.textBrowser.setText(txt)
                except Exception as e:
                    print(e)
            self.ui.textBrowser.setText(txt)
        elif sel.startswith('?vstatus') and len(sel_split) == 2:
            # for driver in self.driver.getDriversAlive():
            for driver in self.icepapsys.find_axes(only_alive=True):
                try:
                    comm = '{}:{}'.format(driver, '?vstatus')
                    val_lines = self.icepapsys.send_cmd(comm)
                    for ll in val_lines:
                        if sel_split[1] in ll:
                            txt = '{} {} {}\n'.format(txt, driver, ll)
                    self.ui.textBrowser.setText(txt)
                except Exception as e:
                    print(e)
            self.ui.textBrowser.setText(txt)
        elif sel.startswith('m '):
            print('master')
            contr_comm = sel.replace('m ', '')
            for contr in self._get_racks_alive():
                try:
                    comm = '{}:{}'.format(contr, contr_comm)
                    # val = self.driver.sendWriteReadCommand(comm)
                    val = self.icepapsys.send_cmd(comm)
                    val = ' '.join(val)
                    val = comm.upper() + " " + val
                    txt = '{} {} {}\n'.format(txt, contr, val)
                    self.ui.textBrowser.setText(txt)
                except Exception as e:
                    print(e)
            self.ui.textBrowser.setText(txt)
        else:
            for driver in self.icepapsys.find_axes(only_alive=True):
                try:
                    comm = '{}:{}'.format(driver,
                                          self.ui.cbAllDrivers.currentText())
                    val = self.icepapsys.send_cmd(comm)
                    val = ' '.join(val)
                    val = comm.upper() + " " + val
                    txt = '{} {} {}\n'.format(txt, driver, val)
                    self.ui.textBrowser.setText(txt)
                except Exception as e:
                    print(e)
            self.ui.textBrowser.setText(txt)

    def _get_version_info_dict(self, addr):
        command = "{}:?VER INFO".format(addr)
        ans = self.icepapsys.send_cmd(command)
        info = self.version_reg_exp.findall(str(ans))
        return dict(info)

    def _get_racks_alive(self):
        racks = []
        rackMask = 0
        try:
            rackMask = int(self.icepapsys.send_cmd('?sysstat')[0], 16)
        except BaseException:
            pass
        for rack in range(16):
            if (rackMask & (1 << rack)) != 0:
                racks.append(rack)
        return racks
