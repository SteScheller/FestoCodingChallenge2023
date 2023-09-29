from enum import Flag


class State(Flag):
    inactive = False
    disabled = False
    quiet = False
    standby = False
    idle = False
    safe = False
    active = True
    live = True
    armed = True
    ready = True
    primed = True
    unsafe = True

    @staticmethod
    def is_state_value(word: str) -> bool:
        return word in State.__members__


def compute_state(log=str) -> State:
    state = State.inactive
    for w in [w.strip() for w in log.split(" ")]:
        if State.is_state_value(w):
            state = State[w]
        else:
            state = State(not state)
    return state
