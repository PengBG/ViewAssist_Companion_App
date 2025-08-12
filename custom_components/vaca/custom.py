"""# Custom components for View Assist satellite integration with Wyoming events."""

from dataclasses import dataclass
from enum import StrEnum
import logging
from typing import Any

from wyoming.event import Event, Eventable

_LOGGER = logging.getLogger(__name__)

_CUSTOM_EVENT_TYPE = "custom-event"

ACTION_EVENT_TYPE = "action"
CAPABILITIES_EVENT_TYPE = "capabilities"
SETTINGS_EVENT_TYPE = "settings"
STATUS_EVENT_TYPE = "status"


class CustomActions(StrEnum):
    """Actions for media control."""

    MEDIA_PLAY_MEDIA = "play-media"
    MEDIA_PLAY = "play"
    MEDIA_PAUSE = "pause"
    MEDIA_STOP = "stop"
    MEDIA_SET_VOLUME = "set-volume"
    REFRESH = "refresh"
    TOAST_MESSAGE = "toast-message"
    WAKE = "wake"


@dataclass
class CustomEvent(Eventable):
    """Custom event class."""

    event_type: str
    """Type of the event."""

    event_data: dict[str, Any] | None = None
    """Data associated with the event."""

    @staticmethod
    def is_type(event_type: str) -> bool:
        """Check if the event type matches."""
        return event_type == _CUSTOM_EVENT_TYPE

    def event(self) -> Event:
        """Create an event for the custom event."""
        data = {"event_type": self.event_type}
        if self.event_data is not None:
            data.update(self.event_data)
        return Event(
            type=_CUSTOM_EVENT_TYPE,
            data=data,
        )

    @staticmethod
    def from_event(event: Event) -> "CustomEvent":
        """Create a CustomEvent instance from an event."""
        return CustomEvent(
            event_type=event.data.get("event_type"), event_data=event.data.get("data")
        )
