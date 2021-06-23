from __future__ import annotations

from asyncio import sleep
from logging import getLogger, INFO, WARN
from math import nan
from typing import NewType, Union

from mavsdk.mission import MissionItem, MissionPlan
from mavsdk.system import System
from mavsdk.telemetry import LandedState
from mavsdk.geofence import Point, Polygon

from .commands import Command
from .mission import Geofence, Mission, Waypoint, FenceType

ConnectedSystem = NewType("ConnectedSystem", System)
ReadySystem = NewType("ReadySystem", ConnectedSystem)
RunningSystem = NewType("RunningSystem", ReadySystem)
WaitingSystem = NewType("WaitingSystem", RunningSystem)
LandedSystem = NewType("LandedSystem", RunningSystem)
FinishedSystem = Union[WaitingSystem, LandedSystem]


def _mk_item(waypoint: Waypoint) -> MissionItem:
    return MissionItem(
        waypoint.lat,
        waypoint.lon,
        waypoint.alt,
        5,
        True,
        nan,
        nan,
        MissionItem.CameraAction.NONE,
        nan,
        nan,
    )


def _conv_fence_type(fence_type: FenceType) -> Polygon.FenceType:
    if fence_type is FenceType.EXCLUSIVE:
        return Polygon.FenceType.EXCLUSION
    elif fence_type is FenceType.INCLUSIVE:
        return Polygon.FenceType.INCLUSION
    else:
        raise ValueError(f"unknown fence type {fence_type}")


def _mk_fence(geofence: Geofence) -> Polygon:
    points = [Point(vertex.lat, vertex.lon) for vertex in geofence.vertices]
    fence_type = _conv_fence_type(geofence.fence_type)

    return Polygon(points, fence_type)


async def connect(drone: System, address: str) -> ConnectedSystem:
    await drone.connect(system_address=address)

    async for state in drone.core.connection_state():
        if state.is_connected:
            break

    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            break

    return ConnectedSystem(drone)


async def upload(drone: ConnectedSystem, mission: Mission) -> ReadySystem:
    mission_items = [_mk_item(waypoint) for waypoint in mission.waypoints]
    mission_plan = MissionPlan(mission_items)
    geofences = [_mk_fence(geofence) for geofence in mission.geofences]

    await Command(lambda: drone.mission.upload_mission(mission_plan))

    if len(geofences) > 0:
        await Command(lambda: drone.geofence.upload_geofence(geofences))

    await Command(
        lambda: drone.param.set_param_float("NAV_ACC_RAD", mission.acceptance_radius),
    )

    return ReadySystem(drone)


async def start(drone: ReadySystem) -> RunningSystem:
    await Command(lambda: drone.action.arm())
    await Command(lambda: drone.mission.start_mission())

    return RunningSystem(drone)


async def landed(drone: RunningSystem) -> LandedSystem:
    await Command(lambda: drone.action.land())

    async for state in drone.telemetry.landed_state():
        if state is LandedState.ON_GROUND:
            break

        await sleep(0.05)

    return LandedSystem(drone)


async def finished(drone: RunningSystem, land: bool = False) -> FinishedSystem:
    while not await drone.mission.is_mission_finished():
        await sleep(0.05)

    if land:
        return await landed(drone)

    return WaitingSystem(drone)


async def execute(mission: Mission, drone: System, sys_addr: str, verbose: bool) -> FinishedSystem:
    logger = getLogger("px4ctl")
    logger.setLevel(INFO if verbose else WARN)

    connected_drone = await connect(drone, sys_addr)
    logger.info("Connected to drone")

    ready_drone = await upload(connected_drone, mission)
    logger.info("Uploaded mission")

    running_drone = await start(ready_drone)
    logger.info("Started mission")

    finished_drone = await finished(running_drone, land=False)
    logger.info("Finished mission")

    return finished_drone
