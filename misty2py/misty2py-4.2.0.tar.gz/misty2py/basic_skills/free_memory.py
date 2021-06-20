"""This module removes non-system files from Misty's memory."""
import os
from typing import Dict, List, Tuple

from misty2py.robot import Misty
from misty2py.utils.messages import success_parser_from_dicts
from misty2py.utils.utils import get_abs_path


def get_non_system_assets(
    misty: Misty,
    assets: List = ["audio", "image", "video", "recording"],
) -> Dict:
    """Obtains the list of all non-system assets that fall under one of the `assets` types.

    Args:
        misty (Misty): The Misty whose non system assets to obtain.
        assets (List, optional): The types of assets to obtain. Defaults to `["audio", "image", "video", "recording"]`.

    Returns:
        Dict: all non-system assets of a given type (keywords) listed as their names in the list under the type keyword.
    """
    action = "_list"
    non_sys_assets = {}
    for asset in assets:
        data = misty.get_info(asset + action)
        result = data.get("result", [])
        for hit in result:
            name = hit.get("name")
            if not name:
                continue

            is_system = hit.get("systemAsset", True)
            if not is_system:
                if not non_sys_assets.get(asset):
                    non_sys_assets[asset] = []
                non_sys_assets[asset].append(name)
                print(
                    "Found a non-system asset \
                        of type `%s` named `%s`." % (asset, name)
                )

    return non_sys_assets


def get_asset_properties(asset_type: str, file: str) -> Tuple[Dict, str, str]:
    """Obtains the parameters, the name and the extension of a file.

    Args:
        asset_type (str): The type of the asset.
        file (str): The file name.

    Returns:
        Tuple[Dict, str, str]: the parameters (a dict with keys `Name` for recordings or `FileName` for other asset types containing the name and the key `Base64` set to `"true"`), the file name and the file extension.
    """
    if asset_type == "recording":
        params = {"Name": file, "Base64": "true"}
    else:
        params = {"FileName": file, "Base64": "true"}

    split_file_name = file.split(".")
    name = split_file_name[0]
    if len(split_file_name) > 1:
        ext = split_file_name[1]
    else:
        ext = "unknown"

    return params, name, ext


def save_base64_str(
    full_path: str,
    content: str,
    overwrite: bool = False
) -> bool:
    """Saves an asset content to the file specified by `full_path`.

    Args:
        full_path (str): The absolute path to the save location.
        content (str): The base64 content to save.
        overwrite (bool, optional): Whether the overwrite the file if it exists. Defaults to `False`.

    Returns:
        bool: The successfulness of the operation.
    """
    if not overwrite and os.path.exists(full_path):
        print("File `%s` already exists, not overwriting." % full_path)
        return True

    try:
        with open(full_path, "w") as f:
            f.write(content)
        print("Asset saved into `%s`." % full_path)
        return True

    except Exception as e:
        print("Failed to save the asset into `%s`. Error message: `%s`" % (
            full_path,
            e
            )
        )
        return False


def save_assets(misty: Misty, assets: Dict, location: str) -> List[str]:
    """Saves multiple assets.

    Args:
        misty (Misty): the Misty whose assets to save.
        assets (Dict): The dictionary of assets; a list of file names under their asset type as the keyword.
        location (str): The absolute path to the directory where the assets are saved.

    Returns:
        List[str]: A list of file names for the files that failed to be saved.
    """
    failed_list = []
    action = "_file"
    for asset_type, files in assets.items():
        for file in files:
            params, name, ext = get_asset_properties(asset_type, file)
            response = misty.get_info(asset_type + action, params=params)
            result = response.get("result")

            if not result:
                failed_list.append(file)

            else:
                file_name = "%s_%s_%s_in_base64.txt" % (asset_type, name, ext)
                full_path = os.path.join(location, file_name)
                file_content = result.get("base64")
                if not file_content:
                    failed_list.append(file)
                else:
                    success = save_base64_str(full_path, file_content)
                    if not success:
                        failed_list.append(file)

    return failed_list


def delete_assets(
    misty: Misty,
    assets: Dict,
    ignore_list: List = []
) -> List[str]:
    """Deletes all non-system files except those that are in `ignore_list`.

    Args:
        misty (Misty): the Misty whose assets to delete.
        assets (Dict): The dictionary of assets; a list of file names under their asset type as the keyword.
        ignore_list (List, optional): The list of file names for files that should not be deleted. Defaults to `[]`.

    Returns:
        List[str]: The list of files that were succesfully deleted.
    """
    action = "_delete"
    delete_list = []

    for asset_type, files in assets.items():
        for file in files:
            if file not in ignore_list:
                if asset_type == "recording":
                    data = {"Name": file}
                else:
                    data = {"FileName": file}
                response = misty.perform_action(asset_type + action, data=data)
                status = response.get("status")
                if status:
                    if status == "Success":
                        print("Successfully deleted the asset `%s`." % file)
                        delete_list.append(file)
                    else:
                        print(
                            "Failed to delete the asset `%s`. Message: `%s`"
                            % (file, response)
                        )

    return delete_list


def free_memory(
    misty: Misty,
    assets: List = ["audio", "image", "video", "recording"],
    save: bool = True,
    save_dir: str = "data",
) -> Dict:
    """Removes all non-system files in Misty's memory.

    Args:
        misty (Misty): the Misty whose memory to free.
        assets (List, optional): The list of asset types to delete. Defaults to `["audio", "image", "video", "recording"]`.
        save (bool, optional): Whether to save the files that are being deleted from Misty's memory. Defaults to `True`.
        save_dir (str, optional): The path to the directory that will store saved assets. Defaults to `"data"`.

    Returns:
        Dict: The dictionary with keys `overall_success` for the success of the entire operation and keys corresponding to the actions within the operation with successfulness of the action and messages about the action.
    """
    save_dir = get_abs_path(save_dir)
    enable_audio = misty.perform_action("audio_enable")
    enable_av = misty.perform_action("streaming_av_enable")
    enable_camera = misty.perform_action("camera_enable")

    assets_to_delete = get_non_system_assets(misty, assets=assets)
    deletion = {}

    if len(assets_to_delete) == 0:
        deletion["status"] = "Success"
        deletion["message"] = "No non-system files present."

    else:
        failed_to_save_list = []

        if save:
            failed_to_save_list = save_assets(
                misty,
                assets_to_delete,
                save_dir
            )

        deleted = delete_assets(misty, assets_to_delete, failed_to_save_list)

        if len(deleted) > 0:
            deletion["status"] = "Success"
            deletion["message"] = "Successfully deleted \
                following assets: %s" % str(deleted)

        else:
            deletion["status"] = "Failed"
            deletion["message"] = "Failed to delete any assets."

    disable_audio = misty.perform_action("audio_disable")
    disable_av = misty.perform_action("streaming_av_disable")
    disable_camera = misty.perform_action("camera_disable")

    return success_parser_from_dicts(
        enable_audio=enable_audio,
        enable_av=enable_av,
        enable_camera=enable_camera,
        deletion=deletion,
        disable_audio=disable_audio,
        disable_av=disable_av,
        disable_camera=disable_camera,
    )


if __name__ == "__main__":
    from misty2py.utils.utils import get_misty

    print(free_memory(get_misty(), "data"))
