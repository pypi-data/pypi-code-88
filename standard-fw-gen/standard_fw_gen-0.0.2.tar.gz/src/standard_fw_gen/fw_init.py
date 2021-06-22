import argparse



template = r"""
{
    "release_mode":"False",
    "project_id":"SFW-00C0000",
    "firmware_version":"V1.0.0.1b2",
    "before_bin_file_path":"C:\\user_path\\telink\\ruiyun_passthrough\\TLSR825X_Tmodule\\8258_module\\8258_module.bin",
    "project_path":"C:\\user_path\\telink\\ruiyun_passthrough\\TLSR825X_Tmodule\\",
    "change_log":"1.balabal;2.baxxxx;3.sadasda"
}
"""


def add_arguments(parser:argparse.ArgumentParser) -> None:
    pass


def run(option:argparse.Namespace) -> int:
    with open("fw_standard_config.json","w") as f:
        f.write(template)
    print("standard_fw_gen init success.enjoy it.")