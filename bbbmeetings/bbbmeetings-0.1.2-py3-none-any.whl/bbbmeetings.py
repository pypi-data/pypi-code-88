#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from typing import NewType, Optional, Tuple, Iterable, List, Union
import itertools

from bbbmeetings.helpers import timestamp_to_datetime, seconds_to_timedelta
from bbbmeetings.connection import get_meetings
from bbbmeetings.types import *



class BBBServers():
    """
    Multiple servers represented as one
    """
    def __init__(self, servers: List['BBBServer']):
        self.servers = servers

    @classmethod
    def from_list(cls, servers: List['BBBServer']) -> 'Self':
        if not isinstance(servers, list):
            servers = list(servers)
        return cls(servers)

    def add(cls, servers: Union['BBBServer', List['BBBServer']]) -> 'Self':
        if not isinstance(servers, list):
            servers = list(servers)
        for server in servers:
            self.servers.append(server)
        return self

    def update_meetings(self) -> 'Self':
        """
        Update the meeting details by sendign a request to the BBBServers BBB-API
        """
        for server in self.servers:
            server.update_meetings()
        return self

    @property
    def meetings(self) -> List['Meeting']:
        """
        Return a flat list of all meetings on all servers
        """
        if any([s.last_update is None for s in self.servers]):
            for server in self.servers:
                server.update_meetings()

        return list(itertools.chain.from_iterable([s.meetings for s in self.servers]))

    @property
    def people(self) -> int:
        """
        Returns the count of participants of a meeting
        """
        return sum([m.participantCount for m in self.meetings])

    @property
    def biggest_meeting(self) -> Optional['Meeting']:
        return max(self.meetings, key=lambda m: m.people)

    @property
    def smallest_meeting(self) -> Optional['Meeting']:
        return min(self.meetings, key=lambda m: m.people)

    @property
    def n_meetings(self) -> int:
        return len(self.meetings)

    @property
    def listeners(self) -> int:
        return sum([m.listenerCount for m in self.meetings])

    @property
    def connected_with_mic(self) -> int:
        return sum([m.voiceParticipantCount for m in self.meetings])

    @property
    def video_active(self) -> int:
        return sum([m.videoCount for m in self.meetings])

    @property
    def moderators(self) -> int:
        return sum([m.moderatorCount for m in self.meetings])

    @property
    def longest_duration(self) -> Optional['Meeting']:
        return max(self.meetings, key=lambda m: m.duration)

    @property
    def most_listeners(self) -> Optional['Meeting']:
        return max(self.meetings, key=lambda m: m.listeners)

    @property
    def most_video_active(self) -> Optional['Meeting']:
        return max(self.meetings, key=lambda m: m.video_active)

    @property
    def most_moderators(self) -> Optional['Meeting']:
        return max(self.meetings, key=lambda m: m.moderators)

    @property
    def attendees(self) -> List['Attendees']:
        return list(itertools.chain.from_iterable([m.attendees for m in self.meetings]))




class BBBServer():
    """
    Represents a single Endpoint of the BBB-API (with a host address and a secret)
    The hostname could be something like "https://bbb.example.org/" while the secret
    is bascially a random string
    """
    def __init__(self, host, secret):
        self.host = host
        self.secret = secret
        self._meetings = []
        self.last_update = None

    @classmethod
    def from_dict(cls, d: dict):
        """
        Allows things like:
        ```
        s = BBBServer.from_dict({"host":"https://bbb.example.org", "secret":"12345"})
        ```
        """
        host   = d["host"]
        secret = d["secret"]
        return cls(host, secret)

    def update_meetings(self) -> 'Self':
        """
        Update the meeting details by sendign a request to the BBBServers BBB-API
        """
        self._meetings = get_meetings(self.host, self.secret)
        self.last_update = datetime.now()
        return self

    @property
    def meetings(self) -> List['Meeting']:
        if self.last_update is None:
            self.update_meetings()
        return self._meetings

    @property
    def people(self) -> int:
        """
        Returns the count of participants of a meeting
        """
        return sum([m.people for m in self.meetings])

    @property
    def biggest_meeting(self) -> Optional['Meeting']:
        return max(self.meetings, key=lambda m: m.people)

    @property
    def smallest_meeting(self) -> Optional['Meeting']:
        return min(self.meetings, key=lambda m: m.people)

    @property
    def n_meetings(self) -> int:
        return len(self.meetings)

    @property
    def listeners(self) -> int:
        return sum([m.listeners for m in self.meetings])

    @property
    def connected_with_mic(self) -> int:
        return sum([m.connected_with_mic for m in self.meetings])

    @property
    def video_active(self) -> int:
        return sum([m.cideo_active for m in self.meetings])

    @property
    def moderators(self) -> int:
        return sum([m.moderators for m in self.meetings])

    @property
    def longest_duration(self) -> Optional['Meeting']:
        return max(self.meetings, key=lambda m: m.duration)

    @property
    def most_listeners(self) -> Optional['Meeting']:
        return max(self.meetings, key=lambda m: m.listeners)

    @property
    def most_video_active(self) -> Optional['Meeting']:
        return max(self.meetings, key=lambda m: m.video_active)

    @property
    def most_moderators(self) -> Optional['Meeting']:
        return max(self.meetings, key=lambda m: m.moderators)

    @property
    def attendees(self) -> List['Attendees']:
        return list(itertools.chain.from_iterable([m.attendees for m in self.meetings]))





class Meeting():
    """
    A Meeting represents all the data the BBB-API returns about a Meeting
    """
    def __init__(self, name, meetingID, internalMeetingID, createTime, voiceBridge, dialNumber, attendeePW, moderatorPW, running, hasUserJoined, recording, hasBeenForciblyEnded, startTime, endTime, participantCount, listenerCount, voiceParticipantCount, videoCount, maxUsers, moderatorCount, attendees, isBreakout, parentRoom, breakoutRooms):
        self.name              = name
        self.meetingID         = meetingID
        self.internalMeetingID = internalMeetingID
        self.createTime        = createTime
        self.voiceBridge       = voiceBridge
        self.dialNumber        = dialNumber
        self.attendeePW        = attendeePW
        self.moderatorPW       = moderatorPW
        self.running           = running
        self.hasUserJoined     = hasUserJoined
        self.recording         = recording
        self.hasBeenForciblyEnded = hasBeenForciblyEnded
        self.startTime         = startTime
        self.endTime           = endTime
        self.participantCount  = participantCount
        self.listenerCount     = listenerCount
        self.voiceParticipantCount = voiceParticipantCount
        self.videoCount        = videoCount
        self.maxUsers          = maxUsers
        self.moderatorCount    = moderatorCount
        self.attendees         = attendees
        self.isBreakout        = isBreakout
        self.parentRoom        = parentRoom
        self.breakoutRooms     = breakoutRooms

    @classmethod
    def from_dict(cls, d: dict):
        name                   = d["meetingName"]
        meetingID              = d["meetingID"]
        internalMeetingID      = d["internalMeetingID"]
        createTime             = timestamp_to_datetime(d["createTime"])
        voiceBridge            = d["voiceBridge"]
        dialNumber             = d["dialNumber"]
        attendeePW             = d["attendeePW"]
        moderatorPW            = d["moderatorPW"]
        running                = d["running"] == "true"
        hasUserJoined          = d["hasUserJoined"] == "true"
        recording              = d["recording"] == "true"
        hasBeenForciblyEnded   = d["hasBeenForciblyEnded"] == "true"
        startTime              = timestamp_to_datetime(d["startTime"])
        endTime                = timestamp_to_datetime(d["endTime"])
        participantCount       = int(d["participantCount"])
        listenerCount          = int(d["listenerCount"])
        voiceParticipantCount  = int(d["voiceParticipantCount"])
        videoCount             = int(d["videoCount"])
        maxUsers               = int(d["maxUsers"])
        moderatorCount         = int(d["moderatorCount"])
        attendees              = []
        if d["attendees"] is not None:
            for x in d["attendees"].values():
                if isinstance(x, list):
                    for i in x:
                        attendees.append(Attendee.from_dict(i))
                else:
                    attendees.append(Attendee.from_dict(x))

        isBreakout             = d["isBreakout"] == "true"
        parentRoom = None
        breakoutRooms = []
        if isBreakout:
            parentRoom = d["parentMeetingID"]
        elif "breakoutRooms" in d.keys():
            for x in d["breakoutRooms"].values():
                if isinstance(x, list):
                    for i in x:
                        breakoutRooms.append(i)
                else:
                    breakoutRooms.append(x)

            
        return cls(name, meetingID, internalMeetingID, createTime, voiceBridge, dialNumber, attendeePW, moderatorPW, running, hasUserJoined, recording, hasBeenForciblyEnded, startTime, endTime, participantCount, listenerCount, voiceParticipantCount, videoCount, maxUsers, moderatorCount, attendees, isBreakout, parentRoom, breakoutRooms)

    def __str__(self):
        s = f"""Meeting
    name:                  {self.name}
    meetingID:             {self.meetingID}
    internalMeetingID:     {self.internalMeetingID}
    createTime:            {self.createTime}
    voiceBridge:           {self.voiceBridge}
    dialNumber:            {self.dialNumber}
    attendeePW:            {self.attendeePW}
    moderatorPW:           {self.moderatorPW}
    running:               {self.running}
    duration:              {self.duration}
    hasUserJoined:         {self.hasUserJoined}
    recording:             {self.recording}
    hasBeenForciblyEnded:  {self.hasBeenForciblyEnded}
    startTime:             {self.startTime}
    endTime:               {self.endTime}
    participantCount:      {self.participantCount}
    listenerCount:         {self.listenerCount}
    voiceParticipantCount: {self.voiceParticipantCount}
    videoCount:            {self.videoCount}
    maxUsers:              {self.maxUsers}
    moderatorCount:        {self.moderatorCount}
    attendees:             {', '.join([a.fullName for a in self.attendees])}
    isBreakout:            {self.isBreakout}
    parentRoom:            {self.parentRoom}
    breakoutRooms:         {', '.join([x for x in self.breakoutRooms])}
    """
        return s

    def __repr__(self):
        return str(self)

    @property
    def duration(self) -> timedelta:
        return datetime.now() - self.startTime

    @property
    def people(self) -> int:
        return self.participantCount

    @property
    def listeners(self) -> int:
        return self.listenerCount

    @property
    def connected_with_mic(self) -> int:
        return self.voiceParticipantCount

    @property
    def video_active(self) -> int:
        return  self.videoCount

    @property
    def moderators(self) -> int:
        return self.moderatorCount



class Attendee():
    """
    An Attendee is someone who is joined to a Meeting, as represented by the BBB-API
    """
    def __init__(self, userID, fullName, role, isPresenter, isListeningOnly, hasJoinedVoice, hasVideo, clientType):
        self.userID          = userID
        self.fullName        = fullName
        self.role            = role
        self.isPresenter     = isPresenter
        self.isListeningOnly = isListeningOnly
        self.hasJoinedVoice  = hasJoinedVoice
        self.hasVideo        = hasVideo
        self.clientType      = clientType

    @classmethod
    def from_dict(cls, d: dict):
        userID           = d["userID"]
        fullName         = d["fullName"]
        role             = d["role"]
        isPresenter      = d["isPresenter"] == "true"
        isListeningOnly  = d["isListeningOnly"] == "true"
        hasJoinedVoice   = d["hasJoinedVoice"] == "true"
        hasVideo         = d["hasVideo"] == "true"
        clientType       = d["clientType"]

        return cls(userID, fullName, role, isPresenter, isListeningOnly, hasJoinedVoice, hasVideo, clientType)

    @property
    def name(self) -> Optional[str]:
        return self.fullName
