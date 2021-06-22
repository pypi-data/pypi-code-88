from . import config_file_parser
import os
import shutil
import hashlib
import time


"""
{
    "release_mode":"False",
    "project_id":"SFW-00C0000",
    "firmware_version":"V1.0.0.1b2",
    "before_bin_file_path":"C:\\user_path\\telink\\ruiyun_passthrough\\TLSR825X_Tmodule\\8258_module\\8258_module.bin",
    "project_path":"C:\\user_path\\telink\\ruiyun_passthrough\\TLSR825X_Tmodule\\",
    "change_log":"1.balabal;2.baxxxx;3.sadasda"
}
"""


output_file_template = """
固件名称：{}
固件MD5：{}
生成日期：{}
修改内容：{}
"""



class standard_gen:
    def __init__(self,config_file_path):
        self._json_parser = config_file_parser.config_file_parser(config_file_path + '/fw_standard_config.json')

    def check(self):
        if self._json_parser.parser() == 1:
            return 1
        return 0

    def get_file_md5(self,file_path):
        with open(file_path,"rb") as f:
            data = f.read()
            ret_md5 = hashlib.md5(data).hexdigest()
            return ret_md5

    def check_new_file_right(self,before_md5,new_file_path):
        file_tmp_md5 = self.get_file_md5(new_file_path)
        if before_md5 == file_tmp_md5:
            return 0
        return 1

    def get_local_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())


    def do_work(self):
        release_flag = False
        # judge uotput path
        output_path = ""
        if self._json_parser.get_json_data("release_mode") == "True":
            output_path = "proj_release"
            release_flag = True
        else:
            output_path = "proj_debug"

        # check output path is exist
        if os.path.exists(os.path.join(self._json_parser.get_json_data("project_path"),output_path)) == False:
            os.mkdir(os.path.join(self._json_parser.get_json_data("project_path"),output_path))
        
        # get before bin file crc32
        before_file_md5 = self.get_file_md5(self._json_parser.get_json_data("before_bin_file_path"))

        # cp file and change name
        new_file_path = os.path.join(self._json_parser.get_json_data("project_path"),output_path)
        new_file_name = self._json_parser.get_json_data("project_id") + "_" + self._json_parser.get_json_data("firmware_version") + ".bin"
        shutil.copy(self._json_parser.get_json_data("before_bin_file_path"),os.path.join(new_file_path,new_file_name))

        if self.check_new_file_right(before_file_md5,os.path.join(new_file_path,new_file_name)) == 1:
            print("error:copy happend error.quit.")
            return 1

        # return if release flag is false
        if release_flag == False:
            return 0

        # generate log file context
        log_context = output_file_template.format(new_file_name,before_file_md5,self.get_local_time(),self._json_parser.get_json_data("change_log"))
        # print(log_context)

        # output log context to log file
        release_path = os.path.join(self._json_parser.get_json_data("project_path"),output_path)
        log_file_path = os.path.join(release_path,"project_fw_log.txt")
        with open(log_file_path,"a+") as f:
            f.write(log_context)

        # set release_mode to False
        self._json_parser.save_json_entity_to_file()






        


        

        



        

        
        






