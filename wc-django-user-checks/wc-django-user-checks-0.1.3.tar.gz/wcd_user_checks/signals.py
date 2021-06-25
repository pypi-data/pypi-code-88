from django.dispatch import Signal


__all__ = 'state_changed',


# Arguments: "user_id", "items"
state_changed: Signal = Signal()
