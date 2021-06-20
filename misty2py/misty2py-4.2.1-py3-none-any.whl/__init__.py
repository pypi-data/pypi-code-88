"""Misty2py is a Python package for Misty II development using [Misty's REST API](https://docs.mistyrobotics.com/misty-ii/rest-api/api-reference/).

## Features
Misty2py can be used to:

- **perform actions** via sending a `POST` or `DELETE` requests to Misty's API;
- **obtain information** via sending a `GET` request to Misty's API;
- **receive streams of data** via subscribing to event types on Misty's Websockets API.

Misty2py uses following concepts:

- **action keywords** - keywords for endpoints of Misty's API that correspond to performing actions;
- **information keywords** - keywords for endpoints of Misty's API that correspond to retrieving information;
- **data shortcuts** - keywords for commonly used data that is supplied to Misty's API as the body of a `POST` request.

## Installation

### Poetry

To install misty2py, run `pip install misty2py`.

### From source

- If this is your first time using `misty2py` from source, do following:

  - Get Poetry (`python -m pip install poetry`) if you do not have it yet.
  - Copy `.env.example` to `.env`.
  - Replace the placeholder values in the new `.env` file.
  - Run `poetry install` to obtain all dependencies.

- Run the desired script via `poetry run python -m [name]` where `[name]` is the placeholder for the module location (in Python notation).
- If the scripts run but your Misty does not seem to respond, you have most likely provided an incorrect IP address for `MISTY_IP_ADDRESS` in `.env`.
- Pytests can be run via `poetry run pytest .`.
- The coverage report can be obtained via `poetry run pytest --cov-report html --cov=misty2py tests` for HTML output or via `poetry run pytest --cov=misty2py tests` for terminal output.

## Contribute

This project is not currently open for contributions. However, you can report issues via the [Issues Tracker](https://github.com/ChrisScarred/misty2py/issues) and inspect the [Source Code](https://github.com/ChrisScarred/misty2py).

## License

This project is licensed under the MIT License.

## Usage

### Getting started

- Start by making **a new instance** of `misty2py.robot`'s `Misty` by `misty_robot = Misty("ip_address_here")`
  - Substitute `ip_address_here` with the IP address of your Misty.
  - `misty2py.utils.env_loader` module contains `EnvLoader` class that can be used to load Misty's IP from the .env file in your project's home directory:
    - Create the `.env` file and write `MISTY_IP_ADDRESS="[ip_address_here]"` in it.
    - Initialise an `EnvLoader` object via `env_loader = EnvLoader()`; this loads the environment variables.
    - Use `env_loader.get_ip()` to obtain the IP address.
- Use the method `misty_robot.perform_action()` to tell Misty to **perform an action**.
- Use the method `misty_robot.get_info()` to tell Misty to **return information**.
- Use the method `misty_robot.event()` to initialise, obtain and stop **continuous streams of data** from Misty's event types.

### Obtaining information

Obtaining digital information is handled by `misty2py.robot::get_info` method.

`misty2py.robot::get_info` has following arguments:

- `info_name` - *required;* the string information keyword corresponding to an endpoint in Misty's API;
- `params` - *optional;* a dictionary of parameter name and parameter value pairs, defaults to `{}`.

### Performing actions

Performing physical and digital actions including removal of non-system files is handled by `misty2py.robot::perform_action()` method.

`misty2py.robot::perform_action()` has following arguments:

- `action_name` - *required;* the string action keyword corresponding to an endpoint in Misty's API;
- `data` - *optional;* the data to pass to the request as a dictionary or a data shortcut (string), defaults to `{}`.

### Event types

To obtain event data in Misty's framework, it is required to **subscribe** to an event type on Misty's websocket server. Misty's websocket server then streams data to the websocket client, in this implementation via a separate thread. To **access this data,** `misty2py.robot::event` method must be called with `"get_data"` parameter from the main thread. When data are no longer required to be streamed to the client, an event type can be **unsubscribed** to kill the event thread.

#### Subscription

Subscribe to an event via `misty2py.robot::event` with the parameter `"subscribe"` and following keyword arguments:

- `type` - *required;* event type string as documented in [Event Types Docs](https://docs.mistyrobotics.com/misty-ii/robot/sensor-data/ "Misty Robotics Event Types").
- `name` - *optional;* a custom event name string; must be unique.
- `return_property` - *optional;* the property to return from Misty's websockets; all properties are returned if return_property is not supplied.
- `debounce` - *optional;* the interval in ms at which new information is sent; defaults to 250.
- `len_data_entries` - *optional;* the maximum number of data entries to keep (discards in fifo style); defaults to 10.
- `event_emitter` - *optional;* an event emitter function which emits an event upon message recieval. Supplies the message content as an argument.

#### Accessing the data and the log

Access the data of an event or its log via `misty2py.robot::event` with the parameter `"get_data"` or `"get_log"` and a keyword argument `name` (the name of the event).

#### Unsubscribing

Unsubscribe from an event via `misty2py.robot::event` with the parameter `"unsubscribe"` and a keyword argument `name` (the name of the event).

#### Basic events usage example

```python
import time

from misty2py.robot import Misty
from misty2py.utils.env_loader import EnvLoader

env_loader = EnvLoader

m = Misty(env_loader.get_ip())

d = m.event("subscribe", type = "BatteryCharge")
e_name = d.get("event_name")

time.sleep(1)

d = m.event("get_data", name = e_name)

d = m.event("unsubscribe", name = e_name)
```

#### Event emitter usage example

```python
import time
from pymitter import EventEmitter

from misty2py.robot import Misty
from misty2py.utils.env_loader import EnvLoader

env_loader = EnvLoader

m = Misty(env_loader.get_ip())
ee = EventEmitter()
event_name = "myevent_001"

@ee.on(event_name)
def listener(data):
    print(data)

d = m.event("subscribe", type = "BatteryCharge", 
            name = event_name, event_emitter = ee)

time.sleep(2)

d = m.event("unsubscribe", name = event_name)
```

### Adding custom keywords and shortcuts

Custom keywords and shortcuts can be passed to a Misty object while declaring a new instance by using the optional arguments:

- `custom_info` for custom information keywords (a dictionary with keys being the information keywords and values being the endpoints),
- `custom_actions` for custom action keywords (a dictionary with keys being the action keywords and values being a dictionary `{"endpoint" : "edpoint_value", "method" : "method_value"}` where `method_value` is either `post` or `delete`),
- `custom_data` for custom data shortcuts (a dictionary with keys being the data shortcuts and values being the dictionary of data values).

An example:

```python
custom_allowed_infos = {
    "hazards_settings": "api/hazards/settings"
}

custom_allowed_data = {
    "amazement": {
        "FileName": "s_Amazement.wav"
    },
    "red": {
        "red": "255",
        "green": "0",
        "blue": "0"
    }
}

custom_allowed_actions = {
    "audio_play" : {
        "endpoint" : "api/audio/play",
        "method" : "post"
    },
    "delete_audio" : {
        "endpoint" : "api/audio",
        "method" : "delete"
    }
}

misty_robot = Misty("0.0.0.0", 
    custom_info=custom_allowed_infos, 
    custom_actions=custom_allowed_actions, 
    custom_data=custom_allowed_data)
```


## Default Keywords and Shortcuts

<details> 
  <summary>List of supported action keywords</summary>

<ul>
<li><code>led</code> for <strong>post</strong> request to <code>api/led</code> endpoint</li>
<li><code>led_trans</code> for <strong>post</strong> request to <code>api/led/transition</code> endpoint</li>
<li><code>notification_settings</code> for <strong>post</strong> request to <code>api/notification/settings</code> endpoint</li>
<li><code>audio_upload</code> for <strong>post</strong> request <code>api/audio</code> to endpoint</li>
<li><code>audio_play</code> for <strong>post</strong> request to <code>api/audio/play</code> endpoint</li>
<li><code>audio_pause</code> for <strong>post</strong> request to <code>api/audio/pause</code> endpoint</li>
<li><code>audio_stop</code> for <strong>post</strong> request to <code>api/audio/stop</code> endpoint</li>
<li><code>audio_delete</code> for <strong>delete</strong> request to <code>api/audio</code> endpoint</li>
<li><code>audio_record_start</code> for <strong>post</strong> request to <code>api/audio/record/start</code> endpoint</li>
<li><code>audio_record_stop</code> for <strong>post</strong> request to <code>api/audio/record/stop</code> endpoint</li>
<li><code>audio_disable</code> for <strong>post</strong> request to <code>api/services/audio/disable</code> endpoint</li>
<li><code>audio_enable</code> for <strong>post</strong> request to <code>api/services/audio/enable</code> endpoint</li>
<li><code>image_upload</code> for <strong>post</strong> request to <code>api/images</code> endpoint</li>
<li><code>image_show</code> for <strong>post</strong> request to <code>api/images/display</code> endpoint</li>
<li><code>image_settings</code> for <strong>post</strong> request to <code>api/images/settings</code> endpoint</li>
<li><code>image_delete</code> for <strong>delete</strong> request to <code>api/images</code> endpoint</li>
<li><code>text_show</code> for <strong>post</strong> request to <code>api/text/display</code> endpoint</li>
<li><code>text_settings</code> for <strong>post</strong> request to <code>api/text/settings</code> endpoint</li>
<li><code>video_upload</code> for <strong>post</strong> request to <code>api/videos</code> endpoint</li>
<li><code>video_show</code> for <strong>post</strong> request to <code>api/videos/display</code> endpoint</li>
<li><code>video_settings</code> for <strong>post</strong> request to <code>api/videos/settings</code> endpoint</li>
<li><code>video_delete</code> for <strong>delete</strong> request to <code>api/videos</code> endpoint</li>
<li><code>blink_mapping_delete</code> for <strong>delete</strong> request to <code>api/blink/images</code> endpoint</li>
<li><code>slam_enable</code> for <strong>post</strong> request to <code>api/services/slam/enable</code> endpoint</li>
<li><code>slam_disable</code> for <strong>post</strong> request to <code>api/services/slam/disable</code> endpoint</li>
<li><code>slam_sensors_reset</code> for <strong>post</strong> request to <code>api/slam/reset</code> endpoint</li>
<li><code>slam_mapping_start</code> for <strong>post</strong> request to <code>api/slam/map/start</code> endpoint</li>
<li><code>slam_mapping_stop</code> for <strong>post</strong> request to <code>api/slam/map/stop</code> endpoint</li>
<li><code>slam_map_current</code> for <strong>post</strong> request to <code>api/slam/map/current</code> endpoint</li>
<li><code>slam_map_rename</code> for <strong>post</strong> request to <code>api/slam/map/rename</code> endpoint</li>
<li><code>slam_infrared_settings</code> for <strong>post</strong> request to <code>api/slam/settings/ir</code> endpoint</li>
<li><code>slam_visible_settings</code> for <strong>post</strong> request to <code>api/slam/settings/visible</code> endpoint</li>
<li><code>slam_map_delete</code> for <strong>delete</strong> request to <code>api/slam/map</code> endpoint</li>
<li><code>slam_docking_locate_start</code> for <strong>post</strong> request to <code>api/slam/docking/start</code> endpoint</li>
<li><code>slam_docking_locate_stop</code> for <strong>post</strong> request to <code>api/slam/docking/stop</code> endpoint</li>
<li><code>streaming_slam_start</code> for <strong>post</strong> request to <code>api/slam/streaming/start</code> endpoint</li>
<li><code>streaming_slam_stop</code> for <strong>post</strong> request to <code>api/slam/streaming/stop</code> endpoint</li>
<li><code>slam_track_start</code> for <strong>post</strong> request to <code>api/slam/track/start</code> endpoint</li>
<li><code>slam_track_stop</code> for <strong>post</strong> request to <code>api/slam/track/stop</code> endpoint</li>
<li><code>recording_start</code> for <strong>post</strong> request to <code>api/videos/recordings/start</code> endpoint</li>
<li><code>recording_stop</code> for <strong>post</strong> request to <code>api/videos/recordings/stop</code> endpoint</li>
<li><code>recording_rename</code> for <strong>post</strong> request to <code>api/videos/recordings/rename</code> endpoint</li>
<li><code>recording_delete</code> for <strong>delete</strong> request to <code>api/videos/recordings</code> endpoint</li>
<li><code>face_detection_start</code> for <strong>post</strong> request to <code>api/faces/detection/start</code> endpoint</li>
<li><code>face_detection_stop</code> for <strong>post</strong> request to <code>api/faces/detection/stop</code> endpoint</li>
<li><code>face_recognition_start</code> for <strong>post</strong> request to <code>api/faces/recognition/start</code> endpoint</li>
<li><code>face_recognition_stop</code> for <strong>post</strong> request to <code>api/faces/recognition/stop</code> endpoint</li>
<li><code>face_train_start</code> for <strong>post</strong> request to <code>api/faces/training/start</code> endpoint</li>
<li><code>face_train_cancel</code> for <strong>post</strong> request to <code>api/faces/training/cancel</code> endpoint</li>
<li><code>face_delete</code> for <strong>delete</strong> request to <code>api/faces</code> endpoint</li>
<li><code>skill_upload</code> for <strong>post</strong> request to <code>api/skills</code> endpoint</li>
<li><code>skill_start</code> for <strong>post</strong> request to <code>api/skills/start</code> endpoint</li>
<li><code>skills_reload</code> for <strong>post</strong> request to <code>api/skills/reload</code> endpoint</li>
<li><code>skill_load</code> for <strong>post</strong> request to <code>api/skills/load</code> endpoint</li>
<li><code>skill_cancel</code> for <strong>post</strong> request to <code>api/skills/cancel</code> endpoint</li>
<li><code>skill_delete</code> for <strong>delete</strong> request to <code>api/skills</code> endpoint</li>
<li><code>wifi_add</code> for <strong>post</strong> request to <code>api/networks/create</code> endpoint</li>
<li><code>wifi_connect</code> for <strong>post</strong> request to <code>api/networks</code> endpoint</li>
<li><code>wifi_delete</code> for <strong>delete</strong> request to <code>api/networks</code> endpoint</li>
<li><code>wifi_hotspot_start</code> for <strong>post</strong> request to <code>api/networks/hotspot/start</code> endpoint</li>
<li><code>wifi_hotspot_stop</code> for <strong>post</strong> request to <code>api/networks/hotspot/stop</code> endpoint</li>
<li><code>write_serial</code> for <strong>post</strong> request to <code>api/serial</code> endpoint</li>
<li><code>event_listener</code> for <strong>post</strong> request to <code>api/skills/event</code> endpoint</li>
<li><code>website_show</code> for <strong>post</strong> request to <code>api/webviews/display</code> endpoint</li>
<li><code>website_settings</code> for <strong>post</strong> request to <code>api/webviews/settings</code> endpoint</li>
<li><code>blink_on</code> for <strong>post</strong> request to <code>api/blink</code> endpoint</li>
<li><code>blink_settings</code> for <strong>post</strong> request to <code>api/blink/settings</code> endpoint</li>
<li><code>display_settings</code> for <strong>post</strong> request to <code>api/display/settings</code> endpoint</li>
<li><code>flashlight_on</code> for <strong>post</strong> request to <code>api/flashlight</code> endpoint</li>
<li><code>speak</code> for <strong>post</strong> request to <code>api/tts/speak</code> endpoint</li>
<li><code>speak_stop</code> for <strong>post</strong> request to <code>api/tts/stop</code> endpoint</li>
<li><code>speech_capture</code> for <strong>post</strong> request to <code>api/audio/speech/capture</code> endpoint</li>
<li><code>drive</code> for <strong>post</strong> request to <code>api/drive</code> endpoint</li>
<li><code>drive_arc</code> for <strong>post</strong> request to <code>api/drive/arc</code> endpoint</li>
<li><code>drive_heading</code> for <strong>post</strong> request to <code>api/drive/hdt</code> endpoint</li>
<li><code>drive_time</code> for <strong>post</strong> request to <code>api/drive/time</code> endpoint</li>
<li><code>drive_track</code> for <strong>post</strong> request to <code>api/drive/track</code> endpoint</li>
<li><code>drive_stop</code> for <strong>post</strong> request to <code>api/drive/stop</code> endpoint</li>
<li><code>drive_to_loc</code> for <strong>post</strong> request to <code>api/drive/coordinates</code> endpoint</li>
<li><code>drive_on_path</code> for <strong>post</strong> request to <code>api/drive/path</code> endpoint</li>
<li><code>halt</code> for <strong>post</strong> request to <code>api/halt</code> endpoint</li>
<li><code>arm_move</code> for <strong>post</strong> request to <code>api/arms</code> endpoint</li>
<li><code>arms_move</code> for <strong>post</strong> request to <code>api/arms/set</code> endpoint</li>
<li><code>head_move</code> for <strong>post</strong> request to <code>api/head</code> endpoint</li>
<li><code>hazard_settings</code> for <strong>post</strong> request to <code>api/hazard/updatebasesettings</code> endpoint</li>
<li><code>streaming_av_start</code> for <strong>post</strong> request to <code>api/avstreaming/start</code> endpoint</li>
<li><code>streaming_av_stop</code> for <strong>post</strong> request to <code>api/avstreaming/stop</code> endpoint</li>
<li><code>streaming_av_disable</code> for <strong>post</strong> request to <code>api/services/avstreaming/disable</code> endpoint</li>
<li><code>streaming_av_enable</code> for <strong>post</strong> request to <code>api/services/avstreaming/enable</code> endpoint</li>
<li><code>keyphrase_recognition_start</code> for <strong>post</strong> request to <code>api/audio/keyphrase/start</code> endpoint</li>
<li><code>keyphrase_recognition_stop</code> for <strong>post</strong> request to <code>api/audio/keyphrase/stop</code> endpoint</li>
<li><code>update_allow</code> for <strong>post</strong> request to <code>api/system/update/allow</code> endpoint</li>
<li><code>update_perform</code> for <strong>post</strong> request to <code>api/system/update</code> endpoint</li>
<li><code>update_perform_targeted</code> for <strong>post</strong> request to <code>api/system/update/component</code> endpoint</li>
<li><code>update_prevent</code> for <strong>post</strong> request to <code>api/system/update/prevent</code> endpoint</li>
<li><code>error_text_clear</code> for <strong>post</strong> request to <code>api/text/error/clear</code> endpoint</li>
<li><code>camera_disable</code> for <strong>post</strong> request to <code>api/services/camera/disable</code> endpoint</li>
<li><code>camera_enable</code> for <strong>post</strong> request to <code>api/services/camera/enable</code> endpoint</li>
<li><code>restart</code> for <strong>post</strong> request to <code>api/reboot</code> endpoint</li>
<li><code>volume_settings</code> for <strong>post</strong> request to <code>api/audio/volume</code> endpoint</li>
<li><code>logs_settings</code> for <strong>post</strong> request to <code>api/logs/level</code> endpoint</li>
<li><code>websocket_settings</code> for <strong>post</strong> request to <code>api/websocket/version</code> endpoint</li>
<li><code>external_request</code> for <strong>post</strong> request to <code>api/request</code> endpoint</li>
</ul>
</details>

<details> 
  <summary>List of supported information keywords</summary>

<ul>
<li><code>audio_file</code> for <strong>get</strong> request to <code>api/audio</code> endpoint</li>
<li><code>audio_list</code> for <strong>get</strong> request to <code>api/audio/list</code> endpoint</li>
<li><code>audio_status</code> for <strong>get</strong> request to <code>api/services/audio</code> endpoint</li>
<li><code>image_file</code> for <strong>get</strong> request to <code>api/images</code> endpoint</li>
<li><code>image_list</code> for <strong>get</strong> request to <code>api/images/list</code> endpoint</li>
<li><code>video_file</code> for <strong>get</strong> request to <code>api/videos</code> endpoint</li>
<li><code>video_list</code> for <strong>get</strong> request to <code>api/videos/list</code> endpoint</li>
<li><code>av_status</code> for <strong>get</strong> request to <code>api/services/avstreaming</code> endpoint</li>
<li><code>sensor_values</code> for <strong>get</strong> request to <code>api/serial</code> endpoint</li>
<li><code>map_file</code> for <strong>get</strong> request to <code>api/slam/map</code> endpoint</li>
<li><code>current_map_id</code> for <strong>get</strong> request to <code>api/slam/map/current</code> endpoint</li>
<li><code>map_id_list</code> for <strong>get</strong> request to <code>api/slam/map/ids</code> endpoint</li>
<li><code>slam_diagnostics</code> for <strong>get</strong> request to <code>api/slam/diagnostics</code> endpoint</li>
<li><code>slam_path</code> for <strong>get</strong> request to <code>api/slam/path</code> endpoint</li>
<li><code>slam_status</code> for <strong>get</strong> request to <code>api/slam/status</code> endpoint</li>
<li><code>slam_enabled</code> for <strong>get</strong> request to <code>api/services/slam</code> endpoint</li>
<li><code>picture_depth</code> for <strong>get</strong> request to <code>api/cameras/depth</code> endpoint</li>
<li><code>picture_fisheye</code> for <strong>get</strong> request to <code>api/cameras/fisheye</code> endpoint</li>
<li><code>picture_rgb</code> for <strong>get</strong> request to <code>api/cameras/rgb</code> endpoint</li>
<li><code>faces_known</code> for <strong>get</strong> request to <code>api/faces</code> endpoint</li>
<li><code>recording_file</code> for <strong>get</strong> request to <code>api/videos/recordings</code> endpoint</li>
<li><code>recording_list</code> for <strong>get</strong> request to <code>api/videos/recordings/list</code> endpoint</li>
<li><code>skills_running</code> for <strong>get</strong> request to <code>api/skills/running</code> endpoint</li>
<li><code>skills_known</code> for <strong>get</strong> request to <code>api/skills</code> endpoint</li>
<li><code>wifis_available</code> for <strong>get</strong> request to <code>api/networks/scan</code> endpoint</li>
<li><code>wifis_saved</code> for <strong>get</strong> request to <code>api/networks</code> endpoint</li>
<li><code>battery_status</code> for <strong>get</strong> request to <code>api/battery</code> endpoint</li>
<li><code>camera_status</code> for <strong>get</strong> request to <code>api/services/camera</code> endpoint</li>
<li><code>blink_settings</code> for <strong>get</strong> request to <code>api/blink/settings</code> endpoint</li>
<li><code>hazards_settings</code> for <strong>get</strong> request to <code>api/hazards/settings</code> endpoint</li>
<li><code>camera_settings</code> for <strong>get</strong> request to <code>api/camera</code> endpoint</li>
<li><code>slam_visible_settings</code> for <strong>get</strong> request to <code>api/slam/settings/visible</code> endpoint</li>
<li><code>slam_infrared_settings</code> for <strong>get</strong> request to <code>api/slam/settings/ir</code> endpoint</li>
<li><code>update_settings</code> for <strong>get</strong> request to <code>api/system/update/settings</code> endpoint</li>
<li><code>device</code> for <strong>get</strong> request to <code>api/device</code> endpoint</li>
<li><code>help</code> for <strong>get</strong> request to <code>api/help</code> endpoint</li>
<li><code>log</code> for <strong>get</strong> request to <code>api/logs</code> endpoint</li>
<li><code>log_level</code> for <strong>get</strong> request to <code>api/logs/level</code> endpoint</li>
<li><code>update_available</code> for <strong>get</strong> request to <code>api/system/updates</code> endpoint</li>
<li><code>websockets</code> for <strong>get</strong> request to <code>api/websockets</code> endpoint</li>
<li><code>websocket_version</code> for <strong>get</strong> request to <code>api/websocket/version</code></li>
</ul>
</details>

<details> 
  <summary>List of supported data shortcuts</summary>

<ul>
<li><code>led_off</code> for <code>{&quot;red&quot;: &quot;0&quot;, &quot;green&quot;: &quot;0&quot;, &quot;blue&quot;: &quot;0&quot;}</code></li>
<li><code>white_light</code> for <code>{&quot;red&quot;: &quot;255&quot;, &quot;green&quot;: &quot;255&quot;, &quot;blue&quot;: &quot;255&quot;}</code></li>
<li><code>red_light</code> for <code>{&quot;red&quot;: &quot;255&quot;, &quot;green&quot;: &quot;0&quot;, &quot;blue&quot;: &quot;0&quot;}</code></li>
<li><code>green_light</code> for <code>{&quot;red&quot;: &quot;0&quot;, &quot;green&quot;: &quot;255&quot;, &quot;blue&quot;: &quot;0&quot;}</code></li>
<li><code>blue_light</code> for <code>{&quot;red&quot;: &quot;0&quot;, &quot;green&quot;: &quot;0&quot;, &quot;blue&quot;: &quot;255&quot;}</code></li>
<li><code>yellow_light</code> for <code>{&quot;red&quot;: &quot;255&quot;, &quot;green&quot;: &quot;255&quot;, &quot;blue&quot;: &quot;0&quot;}</code></li>
<li><code>cyan_light</code> for <code>{&quot;red&quot;: &quot;0&quot;, &quot;green&quot;: &quot;255&quot;, &quot;blue&quot;: &quot;255&quot;}</code></li>
<li><code>magenta_light</code> for <code>{&quot;red&quot;: &quot;255&quot;, &quot;green&quot;: &quot;0&quot;, &quot;blue&quot;: &quot;255&quot;}</code></li>
<li><code>orange_light</code> for <code>{&quot;red&quot;: &quot;255&quot;, &quot;green&quot;: &quot;125&quot;, &quot;blue&quot;: &quot;0&quot;}</code></li>
<li><code>lime_light</code> for <code>{&quot;red&quot;: &quot;125&quot;, &quot;green&quot;: &quot;255&quot;, &quot;blue&quot;: &quot;0&quot;}</code></li>
<li><code>aqua_light</code> for <code>{&quot;red&quot;: &quot;0&quot;, &quot;green&quot;: &quot;255&quot;, &quot;blue&quot;: &quot;125&quot;}</code></li>
<li><code>azure_light</code> for <code>{&quot;red&quot;: &quot;0&quot;, &quot;green&quot;: &quot;125&quot;, &quot;blue&quot;: &quot;255&quot;}</code></li>
<li><code>violet_light</code> for <code>{&quot;red&quot;: &quot;125&quot;, &quot;green&quot;: &quot;0&quot;, &quot;blue&quot;: &quot;255&quot;}</code></li>
<li><code>pink_light</code> for <code>{&quot;red&quot;: &quot;255&quot;, &quot;green&quot;: &quot;0&quot;, &quot;blue&quot;: &quot;125&quot;}</code></li>
<li><code>low_volume</code> for <code>{&quot;Volume&quot;: &quot;5&quot;}</code></li>
<li><code>image_admiration</code> for <code>{&quot;FileName&quot;: &quot;e_Admiration.jpg&quot;}</code></li>
<li><code>image_aggressiveness</code> for <code>{&quot;FileName&quot;: &quot;e_Aggressiveness.jpg&quot;}</code></li>
<li><code>image_amazement</code> for <code>{&quot;FileName&quot;: &quot;e_Amazement.jpg&quot;}</code></li>
<li><code>image_anger</code> for <code>{&quot;FileName&quot;: &quot;e_Anger.jpg&quot;}</code></li>
<li><code>image_concerned</code> for <code>{&quot;FileName&quot;: &quot;e_ApprehensionConcerned.jpg&quot;}</code></li>
<li><code>image_contempt</code> for <code>{&quot;FileName&quot;: &quot;e_Contempt.jpg&quot;}</code></li>
<li><code>image_content_left</code> for <code>{&quot;FileName&quot;: &quot;e_ContentLeft.jpg&quot;}</code></li>
<li><code>image_content_right</code> for <code>{&quot;FileName&quot;: &quot;e_ContentRight.jpg&quot;}</code></li>
<li><code>image_content_default</code> for <code>{&quot;FileName&quot;: &quot;e_DefaultContent.jpg&quot;}</code></li>
<li><code>image_disgust</code> for <code>{&quot;FileName&quot;: &quot;e_Disgust.jpg&quot;}</code></li>
<li><code>image_disoriented</code> for <code>{&quot;FileName&quot;: &quot;e_Disoriented.jpg&quot;}</code></li>
<li><code>image_hilarious</code> for <code>{&quot;FileName&quot;: &quot;e_EcstacyHilarious.jpg&quot;}</code></li>
<li><code>image_starry_eyed</code> for <code>{&quot;FileName&quot;: &quot;e_EcstacyStarryEyed.jpg&quot;}</code></li>
<li><code>image_fear</code> for <code>{&quot;FileName&quot;: &quot;e_Fear.jpg&quot;}</code></li>
<li><code>image_grief</code> for <code>{&quot;FileName&quot;: &quot;e_Grief.jpg&quot;}</code></li>
<li><code>image_joy_1</code> for <code>{&quot;FileName&quot;: &quot;e_Joy.jpg&quot;}</code></li>
<li><code>image_joy_2</code> for <code>{&quot;FileName&quot;: &quot;e_Joy2.jpg&quot;}</code></li>
<li><code>image_goofy_1</code> for <code>{&quot;FileName&quot;: &quot;e_JoyGoofy.jpg&quot;}</code></li>
<li><code>image_goofy_2</code> for <code>{&quot;FileName&quot;: &quot;e_JoyGoofy2.jpg&quot;}</code></li>
<li><code>image_goofy_3</code> for <code>{&quot;FileName&quot;: &quot;e_JoyGoofy3.jpg&quot;}</code></li>
<li><code>image_love</code> for <code>{&quot;FileName&quot;: &quot;e_Love.jpg&quot;}</code></li>
<li><code>image_rage_1</code> for <code>{&quot;FileName&quot;: &quot;e_Rage.jpg&quot;}</code></li>
<li><code>image_rage_2</code> for <code>{&quot;FileName&quot;: &quot;e_Rage2.jpg&quot;}</code></li>
<li><code>image_rage_3</code> for <code>{&quot;FileName&quot;: &quot;e_Rage3.jpg&quot;}</code></li>
<li><code>image_rage_4</code> for <code>{&quot;FileName&quot;: &quot;e_Rage4.jpg&quot;}</code></li>
<li><code>image_remorse</code> for <code>{&quot;FileName&quot;: &quot;e_RemorseShame.jpg&quot;}</code></li>
<li><code>image_sadness</code> for <code>{&quot;FileName&quot;: &quot;e_Sadness.jpg&quot;}</code></li>
<li><code>image_sleping_1</code> for <code>{&quot;FileName&quot;: &quot;e_Sleeping.jpg&quot;}</code></li>
<li><code>image_sleeping_2</code> for <code>{&quot;FileName&quot;: &quot;e_SleepingZZZ.jpg&quot;}</code></li>
<li><code>image_sleepy_1</code> for <code>{&quot;FileName&quot;: &quot;e_Sleepy.jpg&quot;}</code></li>
<li><code>image_sleepy_2</code> for <code>{&quot;FileName&quot;: &quot;e_Sleepy2.jpg&quot;}</code></li>
<li><code>image_sleepy_3</code> for <code>{&quot;FileName&quot;: &quot;e_Sleepy3.jpg&quot;}</code></li>
<li><code>image_sleepy_4</code> for <code>{&quot;FileName&quot;: &quot;e_Sleepy4.jpg&quot;}</code></li>
<li><code>image_surprise</code> for <code>{&quot;FileName&quot;: &quot;e_Surprise.jpg&quot;}</code></li>
<li><code>image_system_black_screen</code> for <code>{&quot;FileName&quot;: &quot;e_SystemBlackScreen.jpg&quot;}</code></li>
<li><code>image_system_blink_large</code> for <code>{&quot;FileName&quot;: &quot;e_SystemBlinkLarge.jpg&quot;}</code></li>
<li><code>image_system_blink_standard</code> for <code>{&quot;FileName&quot;: &quot;e_SystemBlinkStandard.jpg&quot;}</code></li>
<li><code>image_system_camera</code> for <code>{&quot;FileName&quot;: &quot;e_SystemCamera.jpg&quot;}</code></li>
<li><code>image_system_flash</code> for <code>{&quot;FileName&quot;: &quot;e_SystemFlash.jpg&quot;}</code></li>
<li><code>image_system_gear_prompt</code> for <code>{&quot;FileName&quot;: &quot;e_SystemGearPrompt.jpg&quot;}</code></li>
<li><code>image_system_logo_prompt</code> for <code>{&quot;FileName&quot;: &quot;e_SystemLogoPrompt.jpg&quot;}</code></li>
<li><code>image_terror_1</code> for <code>{&quot;FileName&quot;: &quot;e_Terror.jpg&quot;}</code></li>
<li><code>image_terror_2</code> for <code>{&quot;FileName&quot;: &quot;e_Terror2.jpg&quot;}</code></li>
<li><code>image_terror_left</code> for <code>{&quot;FileName&quot;: &quot;e_TerrorLeft.jpg&quot;}</code></li>
<li><code>image_terror_right</code> for <code>{&quot;FileName&quot;: &quot;e_TerrorRight.jpg&quot;}</code></li>
<li><code>sound_acceptance</code> for <code>{&quot;FileName&quot;: &quot;s_Acceptance.wav&quot;}</code></li>
<li><code>sound_amazement_1</code> for <code>{&quot;FileName&quot;: &quot;s_Amazement.wav&quot;}</code></li>
<li><code>sound_amazement_2</code> for <code>{&quot;FileName&quot;: &quot;s_Amazement2.wav&quot;}</code></li>
<li><code>sound_anger_1</code> for <code>{&quot;FileName&quot;: &quot;s_Anger.wav&quot;}</code></li>
<li><code>sound_anger_2</code> for <code>{&quot;FileName&quot;: &quot;s_Anger2.wav&quot;}</code></li>
<li><code>sound_anger_3</code> for <code>{&quot;FileName&quot;: &quot;s_Anger3.wav&quot;}</code></li>
<li><code>sound_anger_4</code> for <code>{&quot;FileName&quot;: &quot;s_Anger4.wav&quot;}</code></li>
<li><code>sound_annoyance_1</code> for <code>{&quot;FileName&quot;: &quot;s_Annoyance.wav&quot;}</code></li>
<li><code>sound_annoyance_2</code> for <code>{&quot;FileName&quot;: &quot;s_Annoyance2.wav&quot;}</code></li>
<li><code>sound_annoyance_3</code> for <code>{&quot;FileName&quot;: &quot;s_Annoyance3.wav&quot;}</code></li>
<li><code>sound_annoyance_4</code> for <code>{&quot;FileName&quot;: &quot;s_Annoyance4.wav&quot;}</code></li>
<li><code>sound_awe_1</code> for <code>{&quot;FileName&quot;: &quot;s_Awe.wav&quot;}</code></li>
<li><code>sound_awe_2</code> for <code>{&quot;FileName&quot;: &quot;s_Awe2.wav&quot;}</code></li>
<li><code>sound_awe_3</code> for <code>{&quot;FileName&quot;: &quot;s_Awe3.wav&quot;}</code></li>
<li><code>sound_boredom</code> for <code>{&quot;FileName&quot;: &quot;s_Boredom.wav&quot;}</code></li>
<li><code>sound_disapproval</code> for <code>{&quot;FileName&quot;: &quot;s_Disapproval.wav&quot;}</code></li>
<li><code>sound_disgust_1</code> for <code>{&quot;FileName&quot;: &quot;s_Disgust.wav&quot;}</code></li>
<li><code>sound_disgust_2</code> for <code>{&quot;FileName&quot;: &quot;s_Disgust2.wav&quot;}</code></li>
<li><code>sound_disgust_3</code> for <code>{&quot;FileName&quot;: &quot;s_Disgust3.wav&quot;}</code></li>
<li><code>sound_disoriented_1</code> for <code>{&quot;FileName&quot;: &quot;s_DisorientedConfused.wav&quot;}</code></li>
<li><code>sound_disoriented_2</code> for <code>{&quot;FileName&quot;: &quot;s_DisorientedConfused2.wav&quot;}</code></li>
<li><code>sound_disoriented_3</code> for <code>{&quot;FileName&quot;: &quot;s_DisorientedConfused3.wav&quot;}</code></li>
<li><code>sound_disoriented_4</code> for <code>{&quot;FileName&quot;: &quot;s_DisorientedConfused4.wav&quot;}</code></li>
<li><code>sound_disoriented_5</code> for <code>{&quot;FileName&quot;: &quot;s_DisorientedConfused5.wav&quot;}</code></li>
<li><code>sound_disoriented_6</code> for <code>{&quot;FileName&quot;: &quot;s_DisorientedConfused6.wav&quot;}</code></li>
<li><code>sound_distraction</code> for <code>{&quot;FileName&quot;: &quot;s_Distraction.wav&quot;}</code></li>
<li><code>sound_ecstacy_1</code> for <code>{&quot;FileName&quot;: &quot;s_Ecstacy.wav&quot;}</code></li>
<li><code>sound_ecstacy_2</code> for <code>{&quot;FileName&quot;: &quot;s_Ecstacy2.wav&quot;}</code></li>
<li><code>sound_fear</code> for <code>{&quot;FileName&quot;: &quot;s_Fear.wav&quot;}</code></li>
<li><code>sound_grief_1</code> for <code>{&quot;FileName&quot;: &quot;s_Grief.wav&quot;}</code></li>
<li><code>sound_grief_2</code> for <code>{&quot;FileName&quot;: &quot;s_Grief2.wav&quot;}</code></li>
<li><code>sound_grief_3</code> for <code>{&quot;FileName&quot;: &quot;s_Grief3.wav&quot;}</code></li>
<li><code>sound_grief_4</code> for <code>{&quot;FileName&quot;: &quot;s_Grief4.wav&quot;}</code></li>
<li><code>sound_joy_1</code> for <code>{&quot;FileName&quot;: &quot;s_Joy.wav&quot;}</code></li>
<li><code>sound_joy_2</code> for <code>{&quot;FileName&quot;: &quot;s_Joy2.wav&quot;}</code></li>
<li><code>sound_joy_3</code> for <code>{&quot;FileName&quot;: &quot;s_Joy3.wav&quot;}</code></li>
<li><code>sound_joy_4</code> for <code>{&quot;FileName&quot;: &quot;s_Joy4.wav&quot;}</code></li>
<li><code>sound_loathing</code> for <code>{&quot;FileName&quot;: &quot;s_Loathing.wav&quot;}</code></li>
<li><code>sound_love</code> for <code>{&quot;FileName&quot;: &quot;s_Love.wav&quot;}</code></li>
<li><code>sound_phrase_bye_bye</code> for <code>{&quot;FileName&quot;: &quot;s_PhraseByeBye.wav&quot;}</code></li>
<li><code>sound_phrase_evil</code> for <code>{&quot;FileName&quot;: &quot;s_PhraseEvilAhHa.wav&quot;}</code></li>
<li><code>sound_phrase_hello</code> for <code>{&quot;FileName&quot;: &quot;s_PhraseHello.wav&quot;}</code></li>
<li><code>sound_phrase_no</code> for <code>{&quot;FileName&quot;: &quot;s_PhraseNoNoNo.wav&quot;}</code></li>
<li><code>sound_phrase_oopsy</code> for <code>{&quot;FileName&quot;: &quot;s_PhraseOopsy.wav&quot;}</code></li>
<li><code>sound_phrase_ow</code> for <code>{&quot;FileName&quot;: &quot;s_PhraseOwOwOw.wav&quot;}</code></li>
<li><code>sound_phrase_oww</code> for <code>{&quot;FileName&quot;: &quot;s_PhraseOwwww.wav&quot;}</code></li>
<li><code>sound_phrase_uh</code> for <code>{&quot;FileName&quot;: &quot;s_PhraseUhOh.wav&quot;}</code></li>
<li><code>sound_rage</code> for <code>{&quot;FileName&quot;: &quot;s_Rage.wav&quot;}</code></li>
<li><code>sound_sadness_1</code> for <code>{&quot;FileName&quot;: &quot;s_Sadness.wav&quot;}</code></li>
<li><code>sound_sadness_2</code> for <code>{&quot;FileName&quot;: &quot;s_Sadness2.wav&quot;}</code></li>
<li><code>sound_sadness_3</code> for <code>{&quot;FileName&quot;: &quot;s_Sadness3.wav&quot;}</code></li>
<li><code>sound_sadness_4</code> for <code>{&quot;FileName&quot;: &quot;s_Sadness4.wav&quot;}</code></li>
<li><code>sound_sadness_5</code> for <code>{&quot;FileName&quot;: &quot;s_Sadness5.wav&quot;}</code></li>
<li><code>sound_sadness_6</code> for <code>{&quot;FileName&quot;: &quot;s_Sadness6.wav&quot;}</code></li>
<li><code>sound_sadness_7</code> for <code>{&quot;FileName&quot;: &quot;s_Sadness7.wav&quot;}</code></li>
<li><code>sound_sleepy_1</code> for <code>{&quot;FileName&quot;: &quot;s_Sleepy.wav&quot;}</code></li>
<li><code>sound_sleepy_2</code> for <code>{&quot;FileName&quot;: &quot;s_Sleepy2.wav&quot;}</code></li>
<li><code>sound_sleepy_3</code> for <code>{&quot;FileName&quot;: &quot;s_Sleepy3.wav&quot;}</code></li>
<li><code>sound_sleepy_4</code> for <code>{&quot;FileName&quot;: &quot;s_Sleepy4.wav&quot;}</code></li>
<li><code>sound_sleepy_snore</code> for <code>{&quot;FileName&quot;: &quot;s_SleepySnore.wav&quot;}</code></li>
<li><code>sound_camera_shutter</code> for <code>{&quot;FileName&quot;: &quot;s_SystemCameraShutter.wav&quot;}</code></li>
<li><code>sound_failure</code> for <code>{&quot;FileName&quot;: &quot;s_SystemFailure.wav&quot;}</code></li>
<li><code>sound_success</code> for <code>{&quot;FileName&quot;: &quot;s_SystemSuccess.wav&quot;}</code></li>
<li><code>sound_wake</code> for <code>{&quot;FileName&quot;: &quot;s_SystemWakeWord.wav&quot;}</code></li>
</ul>
</details>
"""
