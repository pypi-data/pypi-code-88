# coding: utf-8
# /usr/bin/env python3
import asyncio

from typing import Any, Dict, Iterable, List, Sequence, Set, TYPE_CHECKING, Tuple
from piaf.agent import Agent, AgentState
from piaf.comm import (
    ACLMessage,
    AID,
    MT_NOT,
    MT_OR,
    MT_PERFORMATIVE,
    Performative,
)
from piaf.behavior import Behavior

if TYPE_CHECKING:
    import piaf.comm
    import piaf.platform


class AMSService(Agent):
    """
    Special agent providing Agent Management Services.

    Add link to Fipa specification.
    """

    VALID_MSG_TEMPLATE = MT_OR(
        MT_PERFORMATIVE(Performative.REQUEST), MT_PERFORMATIVE(Performative.CANCEL)
    )

    SEARCH_FUNC = "request"

    def __init__(
        self,
        aid: "piaf.comm.AID",
        platform: "piaf.platform.AgentPlatform",
        *args,
        **kwargs,
    ):
        """
        Create a new AMS Agent with the provided information.

        :param aid: this agent's identifier
        :param platform: the platform where this AMS agent is deployed
        """
        super().__init__(aid, platform, *args, **kwargs)

        # Store ongoing tasks
        self.tasks: "Dict[str, asyncio.Future]" = dict()

        # Add behaviors
        self.add_behavior(HandleRequestBehavior(self))
        self.add_behavior(HandleInvalidMessageBehavior(self))

    def send_not_understood_message(self, request: "ACLMessage", reason: str) -> None:
        """
        Send a `NOT_UNDERSTOOD` message.

        :param request: the request message to reply to.
        :param reason: a text message explaining why we reply with `NOT_UNDERSTOOD`
        """
        self.send(
            ACLMessage.Builder()
            .performative(Performative.NOT_UNDERSTOOD)
            .receiver(request.sender)
            .conversation_id(request.conversation_id)
            .content([request, reason])
            .build()
        )

    def send_refuse_message(self, request: "ACLMessage", reason: str) -> None:
        """
        Send a `REFUSE` message.

        :param request: the request message to reply to.
        :param reason: a text message explaining why we reply with `REFUSE`
        """
        self.send(
            ACLMessage.Builder()
            .performative(Performative.REFUSE)
            .receiver(request.sender)
            .conversation_id(request.conversation_id)
            .content([request, reason])
            .build()
        )

    def send_inform_message(self, request: "ACLMessage", content: Any) -> None:
        """
        Send an `INFORM` message.

        :param request: the request message to reply to.
        :param content: the content of the `INFORM` message
        """
        self.send(
            ACLMessage.Builder()
            .performative(Performative.INFORM)
            .receiver(request.sender)
            .conversation_id(request.conversation_id)
            .content(content)
            .build()
        )


class HandleRequestBehavior(Behavior):
    """Behavior designed to handle the Request protocols act."""

    def done(self) -> bool:
        """Infinit behavior."""
        return False

    async def action(self) -> None:
        """
        Behavior blocks until a valid message (ie validate template :cvar:`AMSService.VALID_MSG_TEMPLATE`) is found.

        Once a message matches, we probe the act and the content to decide what to do.
        """
        # Get next handled message
        msg = await self.agent.receive(AMSService.VALID_MSG_TEMPLATE)
        acl_msg = msg.acl_message

        # Request -> new conversation
        if acl_msg.performative == Performative.REQUEST:

            # If message content is invalid, stop processing
            if not self._check_message_content(acl_msg):
                return

            # Otherwise find the function
            if acl_msg.content[0] == AMSService.SEARCH_FUNC:
                self.agent.tasks[acl_msg.conversation_id] = asyncio.ensure_future(
                    self._handleSearchRequest(acl_msg)
                )

            # Unsupported function
            else:
                self.agent.send_refuse_message(
                    acl_msg, f"Unsupported function: {acl_msg.content[0]}"
                )

        # Cancel -> check if existing conversation
        else:
            try:
                self.agent.tasks[acl_msg.conversation_id].cancel()
                self.agent.send_inform_message(acl_msg, acl_msg)
            except KeyError:
                self.agent.send_not_understood_message(
                    acl_msg, f"Unexpected Act: {acl_msg.performative}"
                )

    async def _handleSearchRequest(self, request: "ACLMessage"):
        """Execute the `search` function if possible and send the reply."""
        # Make sure we have the search_constraints argument
        try:
            search_constraints = request.content[1]
        except IndexError:
            self.agent.send_refuse_message(
                request, "Missing argument: search_constraints"
            )
            return

        # Make sure the argument has the right type
        if not isinstance(search_constraints, AMSAgentDescription):
            self.agent.send_refuse_message(
                request, f"Unexpected-argument: {request.content[1]}"
            )
            return

        am = self.agent._platform.agent_manager
        agents = am.get_agents(search_constraints.state)
        agt_descriptions = []

        # Perform the search
        if search_constraints.name is not None:
            if search_constraints.name in agents:
                agt_descriptions.append(
                    AMSAgentDescription(
                        search_constraints.name,
                        None,
                        am.get_state(search_constraints.name),
                    )
                )

        else:
            agt_descriptions = [
                AMSAgentDescription(agent, None, am.get_state(agent))
                for agent in agents
            ]

        # Send the result
        self.agent.send_inform_message(request, agt_descriptions)

    def _check_message_content(self, msg: "ACLMessage") -> bool:
        """
        Check the content of the provided message.

        * Not a sequence      -> NOT_UNDERSTOOD, unsupported-value
        * Length == 0         -> REFUSE, missing-parameter
        * First param not str -> REFUSE, unrecognized-parameter-value

        :param msg: message to check
        :return: True if message is ok, False otherwise
        """
        content = msg.content
        result = False

        if not isinstance(content, (Tuple, List, Set)):
            self.agent.send_not_understood_message(msg, "Unsupported value: content")

        elif len(content) == 0:
            self.agent.send_refuse_message(msg, "Missing parameter: function_name")

        elif not isinstance(content[0], str):
            self.agent.send_refuse_message(
                msg, f"Unrecognized parameter value: function_name, {content[0]}"
            )

        else:
            result = True

        return result


class HandleInvalidMessageBehavior(Behavior):
    """
    Handle all messages not matching the template defined in :class:`AMSService`.

    If such message is found then this behavior sends a `NOT_UNDERSTOOD` message.
    """

    def done(self) -> bool:
        """Infinite behavior."""
        return False

    async def action(self) -> None:
        """Wait for messages and send `NOT_UNDERSTOOD` message."""
        msg = await self.agent.receive(MT_NOT(AMSService.VALID_MSG_TEMPLATE))
        self.agent.send_not_understood_message(
            msg.acl_message, f"Unsupported Act: {msg.acl_message.performative}"
        )


class AMSAgentDescription:
    """
    :class:`AMSAgentDescription` objects are returned when querying the AMS agent about agents in the platform.

    It is part of the fipa-agent-management ontology. See http://fipa.org/specs/fipa00023/SC00023K.html.
    """

    def __init__(self, name: AID, ownership: str, state: AgentState) -> None:
        self.name: AID = name
        self.ownership: str = ownership
        self.state: AgentState = state


class AgentPlatformService:
    """
    Description of a platform service.

    It is part of the fipa-agent-management ontology. See http://fipa.org/specs/fipa00023/SC00023K.html.
    """

    def __init__(self, name: str, type: str, addresses: Sequence[str]) -> None:
        self.name: str = name
        self.type: str = type
        self.addresses: Sequence[str] = addresses


class AgentPlatformDescription:
    """
    Description of the AgentPlatform.

    It is part of the fipa-agent-management ontology. See http://fipa.org/specs/fipa00023/SC00023K.html.
    """

    def __init__(self, name: str, ap_services: Set[AgentPlatformService]) -> None:
        self.name: str = name
        self.ap_services: Set[AgentPlatformService] = ap_services


class Property:
    """
    :class:`Property` objects are usefull for specifying parameter/value pairs.

    Part of the fipa-agent-management ontology. See http://fipa.org/specs/fipa00023/SC00023K.html.
    """

    def __init__(self, name: str, value: Any) -> None:
        self.name: str = name
        self.value: Any = value
