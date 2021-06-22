import uuid
from collections import namedtuple
from enum import Enum
from struct import Struct

import numpy as np


class OsefTypes(Enum):
    """Outsight Node and Leaf types."""

    AUGMENTED_CLOUD = 1
    NUMBER_POINTS = 2
    SPHERICAL_COORD_3F = 3
    REFLECTIVITY = 4
    BACKGROUND_FLAG = 5
    CARTESIAN_COORD_3F = 6
    BGR_COLOR = 7
    OBJECT_DETECTION_FRAME = 8
    IMAGE_DIM = 9
    NUMBER_OBJECT = 10
    CLOUD_FRAME = 11
    TIMESTAMP = 12
    AZIMUTH_DEGREE = 13
    NUMBER_OF_LAYERS = 14
    CLOUD_PROCESSING_BITS = 15
    AZIMUTH_RANGE = 16
    BBOX_ARRAY = 17
    CLASSIFICATION_ID = 18
    CONFIDENCE_ARRAY = 19
    TIMESTAMP_FRAME = 20
    PERCEPT = 21
    CLUSTER = 22
    BGR_IMAGE = 23
    POSE = 24
    SCAN_FRAME = 25
    TRACKED_OBJECT = 26
    BOUNDING_BOX_SIZE = 27
    SPEED_VECTOR = 28
    POSE_ARRAY = 29
    OBJECT_ID = 30
    CARTESIAN_COORD_4F = 31
    SPHERICAL_COORD_4F = 32
    ZONES = 33
    ZONE = 34
    ZONE_VERTICE = 35
    ZONE_NAME = 36
    ZONE_UUID = 37
    ZONE_BINDINGS = 38
    OBJECT_PROPERTIES = 39
    IMU_PACKET = 40
    VELODYNE_TIMESTAMP = 41
    RELATIVE_POSE = 42
    GRAVITY = 43
    EGO_MOTION = 44
    PREDICTED_POSITION = 45


class LeafType(Enum):
    Unknown = 0
    Value = 1
    Array = 2
    StructuredArray = 3
    Dict = 4
    String = 5
    Custom = 6
    Bytes = 7


class PerceptIds(Enum):
    DEFAULT = 0
    ROAD = 1
    VEGETATION = 2
    GROUND = 3
    SIGN = 4
    BUILDING = 5
    FLAT_GND = 6
    UNKNOWN = 7
    MARKING = 8
    OBJECT = 9
    WALL = 10


class TrackedObjectIds(Enum):
    UNKNOWN = 0
    PERSON = 1
    LUGGAGE = 2
    TROLLEY = 3
    TRUCK = 4
    BUS = 5
    CAR = 6
    VAN = 7
    TWO_WHEELER = 8


LeafInfo = namedtuple("Leaf", "leaf_type format_info")
InternalNodeInfo = namedtuple("InternalNode", "type")
TypeInfo = namedtuple("Type", "name node_info")


def _processing_bitfield_parser(value: bytes):
    background_deleted = 1
    bitfield = Struct("<Q").unpack(value)[0]
    return {"Backgound deleted": bitfield & (1 << background_deleted)}


def _percept_class_parser(value: bytes):
    if len(value) == 0:
        return None

    classes_iter = Struct("<H").iter_unpack(value)

    data_list = [(code[0], PerceptIds(code[0]).name) for code in classes_iter]
    return np.array(data_list, dtype=[("class_code", np.int), ("class_name", "<U12")])


def _class_array_parser(value: bytes):
    if len(value) == 0:
        return None

    classes_iter = Struct("<L").iter_unpack(value)
    data_list = [(code[0], TrackedObjectIds(code[0]).name) for code in classes_iter]
    return np.array(data_list, dtype=[("class_code", np.int), ("class_name", "<U12")])


def _pose_parser(value: bytes):
    floats = Struct("<ffffffffffff").unpack(value)
    t = np.array(floats[0:3])
    r = np.reshape(np.array(floats[3:]), (3, 3))
    return {"translation": t, "rotation": r}


def _pose_array_parser(value: bytes):
    floats = np.array([f for f in Struct("<ffffffffffff").iter_unpack(value)], ndmin=2)
    translations = floats[:, 0:3]
    rotations = floats[:, 3:].reshape((-1, 3, 3))
    return [{"translation": t, "rotation": r} for t, r in zip(translations, rotations)]


def _object_properties_parser(value: bytes):
    if len(value) == 0:
        return None

    orientation_flag = {
        0: "not Oriented",
        1: "Oriented",
    }

    object_iter = Struct("<B").iter_unpack(value)
    property_list = [orientation_flag.get(c[0] & 0x1, "") for c in object_iter]
    return np.array(property_list, dtype=[("orientation", "<U12")])


def _imu_parser(value: bytes):
    v = Struct("<LLffffff").unpack(value)
    return {
        "timestamp": {"unix_s": v[0], "remaining_us": v[1]},
        "acceleration": v[2:5],
        "angular_velocity": v[5:8],
    }


outsight_types = {
    OsefTypes.AUGMENTED_CLOUD.value: TypeInfo(
        "augmented_cloud", InternalNodeInfo(dict)
    ),
    OsefTypes.NUMBER_POINTS.value: TypeInfo(
        "number_of_points", LeafInfo(LeafType.Value, "<L")
    ),
    OsefTypes.SPHERICAL_COORD_3F.value: TypeInfo(
        "spherical_coordinates",
        LeafInfo(
            LeafType.StructuredArray,
            (
                [
                    ("azimuth", np.float32),
                    ("elevation", np.float32),
                    ("distance", np.float32),
                ]
            ),
        ),
    ),
    OsefTypes.REFLECTIVITY.value: TypeInfo(
        "reflectivity", LeafInfo(LeafType.Array, np.uint8)
    ),
    OsefTypes.BACKGROUND_FLAG.value: TypeInfo(
        "background_flags", LeafInfo(LeafType.Array, np.bool)
    ),
    OsefTypes.CARTESIAN_COORD_3F.value: TypeInfo(
        "cartesian_coordinates",
        LeafInfo(
            LeafType.StructuredArray,
            ([("x", np.float32), ("y", np.float32), ("z", np.float32)]),
        ),
    ),
    OsefTypes.BGR_COLOR.value: TypeInfo("bgr_colors", LeafInfo(LeafType.Bytes, None)),
    OsefTypes.OBJECT_DETECTION_FRAME.value: TypeInfo(
        "object_detection_frame", InternalNodeInfo(dict)
    ),
    OsefTypes.IMAGE_DIM.value: TypeInfo(
        "image_dimension",
        LeafInfo(LeafType.Dict, ("<LL", ["image_width", "image_height"])),
    ),
    OsefTypes.NUMBER_OBJECT.value: TypeInfo(
        "number_of_objects", LeafInfo(LeafType.Value, "<L")
    ),
    OsefTypes.CLOUD_FRAME.value: TypeInfo("cloud_frame", InternalNodeInfo(dict)),
    OsefTypes.TIMESTAMP.value: TypeInfo(
        "timestamp_microseconds",
        LeafInfo(LeafType.Dict, ("<LL", ["unix_s", "remaining_us"])),
    ),
    OsefTypes.AZIMUTH_DEGREE.value: TypeInfo(
        "azimuths_degrees", LeafInfo(LeafType.Array, np.float32)
    ),
    OsefTypes.NUMBER_OF_LAYERS.value: TypeInfo(
        "number_of_layers", LeafInfo(LeafType.Value, "<L")
    ),
    OsefTypes.CLOUD_PROCESSING_BITS.value: TypeInfo(
        "cloud_processing_bitfield",
        LeafInfo(LeafType.Custom, _processing_bitfield_parser),
    ),
    OsefTypes.AZIMUTH_RANGE.value: TypeInfo(
        "azimuth_range",
        LeafInfo(LeafType.Dict, ("<ff", ["azimuth_begin_deg", "azimuth_end_deg"])),
    ),
    OsefTypes.BBOX_ARRAY.value: TypeInfo(
        "bounding_boxes_array",
        LeafInfo(
            LeafType.StructuredArray,
            (
                [
                    ("x_min", np.float32),
                    ("y_min", np.float32),
                    ("x_max", np.float32),
                    ("y_max", np.float32),
                ]
            ),
        ),
    ),
    OsefTypes.CLASSIFICATION_ID.value: TypeInfo(
        "classification_id_array", LeafInfo(LeafType.Custom, _class_array_parser)
    ),
    OsefTypes.CONFIDENCE_ARRAY.value: TypeInfo(
        "classification_confidence_array", LeafInfo(LeafType.Array, np.float32)
    ),
    OsefTypes.TIMESTAMP_FRAME.value: TypeInfo(
        "timestamped_frame", InternalNodeInfo(dict)
    ),
    OsefTypes.PERCEPT.value: TypeInfo(
        "percept", LeafInfo(LeafType.Custom, _percept_class_parser)
    ),
    OsefTypes.CLUSTER.value: TypeInfo("cluster", LeafInfo(LeafType.Array, np.uint16)),
    OsefTypes.BGR_IMAGE.value: TypeInfo("bgr_image_frame", InternalNodeInfo(dict)),
    OsefTypes.POSE.value: TypeInfo("pose", LeafInfo(LeafType.Custom, _pose_parser)),
    OsefTypes.SCAN_FRAME.value: TypeInfo("scan_frame", InternalNodeInfo(dict)),
    OsefTypes.TRACKED_OBJECT.value: TypeInfo("tracked_objects", InternalNodeInfo(dict)),
    OsefTypes.BOUNDING_BOX_SIZE.value: TypeInfo(
        "3d_bounding_boxes_sizes",
        LeafInfo(
            LeafType.StructuredArray,
            ([("bbox_x", np.float32), ("bbox_y", np.float32), ("bbox_z", np.float32)]),
        ),
    ),
    OsefTypes.SPEED_VECTOR.value: TypeInfo(
        "speed_vectors",
        LeafInfo(
            LeafType.StructuredArray,
            ([("Vx", np.float32), ("Vy", np.float32), ("Vz", np.float32)]),
        ),
    ),
    OsefTypes.POSE_ARRAY.value: TypeInfo(
        "pose_array", LeafInfo(LeafType.Custom, _pose_array_parser)
    ),
    OsefTypes.OBJECT_ID.value: TypeInfo(
        "object_id", LeafInfo(LeafType.Array, np.ulonglong)
    ),
    OsefTypes.CARTESIAN_COORD_4F.value: TypeInfo(
        "cartesian_coordinates_4f",
        LeafInfo(
            LeafType.StructuredArray,
            (
                [
                    ("x", np.float32),
                    ("y", np.float32),
                    ("z", np.float32),
                    ("__todrop", np.float32),
                ]
            ),
        ),
    ),
    # __todrop are unused columns that are here to have 4 floats in the TLV which is more cpu efficient.
    OsefTypes.SPHERICAL_COORD_4F.value: TypeInfo(
        "spherical_coordinates_4f",
        LeafInfo(
            LeafType.StructuredArray,
            (
                [
                    ("azimuth", np.float32),
                    ("elevation", np.float32),
                    ("distance", np.float32),
                    ("__todrop", np.float32),
                ]
            ),
        ),
    ),
    OsefTypes.ZONES.value: TypeInfo("zones", InternalNodeInfo(list)),
    OsefTypes.ZONE.value: TypeInfo("zone", InternalNodeInfo(dict)),
    OsefTypes.ZONE_VERTICE.value: TypeInfo(
        "zone_vertices",
        LeafInfo(LeafType.StructuredArray, ([("x", np.float32), ("y", np.float32)])),
    ),
    OsefTypes.ZONE_NAME.value: TypeInfo("zone_name", LeafInfo(LeafType.String, None)),
    OsefTypes.ZONE_UUID.value: TypeInfo(
        "zone_uuid", LeafInfo(LeafType.Custom, lambda v: uuid.UUID(bytes=v))
    ),
    OsefTypes.ZONE_BINDINGS.value: TypeInfo(
        "zones_objects_binding",
        LeafInfo(
            LeafType.StructuredArray,
            ([("object_id", np.ulonglong), ("zone_idx", np.uint32)]),
        ),
    ),
    OsefTypes.OBJECT_PROPERTIES.value: TypeInfo(
        "object_properties", LeafInfo(LeafType.Custom, _object_properties_parser)
    ),
    OsefTypes.IMU_PACKET.value: TypeInfo(
        "imu_packet", LeafInfo(LeafType.Custom, _imu_parser)
    ),
    OsefTypes.VELODYNE_TIMESTAMP.value: TypeInfo(
        "timestamp_velodyne_lidar",
        LeafInfo(LeafType.Dict, ("<LL", ["unix_s", "remaining_us"])),
    ),
    OsefTypes.RELATIVE_POSE.value: TypeInfo(
        "relative_pose", LeafInfo(LeafType.Custom, _pose_parser)
    ),
    OsefTypes.GRAVITY.value: TypeInfo(
        "gravity", LeafInfo(LeafType.Dict, ("<fff", ["x", "y", "z"]))
    ),
    OsefTypes.EGO_MOTION.value: TypeInfo("ego_motion", InternalNodeInfo(dict)),
    OsefTypes.PREDICTED_POSITION.value: TypeInfo(
        "predicted_position",
        LeafInfo(
            LeafType.StructuredArray,
            ([("x", np.float32), ("y", np.float32), ("z", np.float32)]),
        ),
    ),
}


def outsight_type_info(type_code):
    if type_code in outsight_types:
        return outsight_types[type_code]
    else:
        return TypeInfo(f"Unknown type ({type_code})", LeafInfo(LeafType.Unknown, None))
