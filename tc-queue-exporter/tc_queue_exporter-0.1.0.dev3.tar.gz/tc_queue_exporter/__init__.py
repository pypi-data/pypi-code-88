#!/usr/bin/env python3
from prometheus_client import Gauge
from prometheus_client import start_http_server
import time
import requests
import os
from requests.auth import HTTPBasicAuth
from datetime import datetime


TC_REST_BASE_URL = os.environ["TC_REST_BASE_URL"]
TC_BASE_URL = os.environ["TC_BASE_URL"]
auth = HTTPBasicAuth(os.environ["TC_USER"], os.environ["TC_PW"])
PORT = int(os.getenv("TC_EXPORTER_PORT", 9305))

pools = {}

agents = {}


def get_pool_from_agent(agent):
    agent_id = agent["id"]
    if not agents.get(agent_id, False):
        agents_response = requests.get(
            "{}{}".format(TC_BASE_URL, agent["href"]),
            auth=auth,
            headers={"Accept": "application/json"},
        )
        agents[agent_id] = agents_response.json()
    return str(agents[agent_id]["pool"]["name"])


def fill_pools():
    response = requests.get(
        "{}/agents".format(TC_REST_BASE_URL),
        auth=auth,
        headers={"Accept": "application/json"},
    )
    for agent in response.json()["agent"]:
        agentdetails_response = requests.get(
            "{}/agents/id:{}".format(TC_REST_BASE_URL, agent["id"]),
            auth=auth,
            headers={"Accept": "application/json"},
        )
        agentdetails = agentdetails_response.json()
        agent_pool = str(agentdetails["pool"]["name"])
        pools[agent_pool] = {"waittime": 0}


def run():
    next_run = 0
    g_pool_wait_time = Gauge(
        "teamcity_pool_wait_time",
        "desc",
        ["pool_name"],
    )
    start_http_server(PORT)

    while True:
        while next_run > time.time():
            time.sleep(1)
        next_run = time.time() + 5
        fill_pools()
        queue_response = requests.get(
            "{}/buildQueue".format(TC_REST_BASE_URL),
            auth=auth,
            headers={"Accept": "application/json"},
        )
        queue = queue_response.json()
        for build in queue["build"]:
            build_response = requests.get(
                "{}/builds/id:{}".format(TC_REST_BASE_URL, build["id"]),
                auth=auth,
                headers={"Accept": "application/json"},
            )
            full_build = build_response.json()
            if full_build["state"] != "queued":
                continue

            if full_build.get("waitReason", "[UNKNOWN]") in [
                "Build dependencies have not been built yet",
                "There are no compatible agents which can run this build",
            ]:
                continue
            if not full_build.get("startEstimate", False):
                continue
            if not full_build.get("triggered", {}).get("date", False):
                continue

            build_estimate_start = datetime.strptime(
                full_build["startEstimate"], "%Y%m%dT%H%M%S%z"
            )
            build_triggered = datetime.strptime(
                full_build["triggered"]["date"], "%Y%m%dT%H%M%S%z"
            )
            build_waittime_rel = (
                build_estimate_start.timestamp() - build_triggered.timestamp()
            )
            agents_response = requests.get(
                "{}{}".format(TC_BASE_URL, full_build["compatibleAgents"]["href"]),
                auth=auth,
                headers={"Accept": "application/json"},
            )
            compatible_agents = agents_response.json()
            for agent in compatible_agents["agent"]:
                pool = get_pool_from_agent(agent)
                pools[pool]["waittime"] = max(
                    pools[pool]["waittime"], build_waittime_rel
                )

        for pool_name, pool in pools.items():
            g_pool_wait_time.labels(pool_name=pool_name).set(pool["waittime"])
