#  Copyright (c) 2020 Rocky Bernstein


def whileelsestmt(
    self, lhs: str, n: int, rule, ast, tokens: list, first: int, last: int
) -> bool:
    return False
    if tokens[last] == "COME_FROM_LOOP":
        last -= 1
    elif tokens[last - 1] == "COME_FROM_LOOP":
        last -= 2
    if tokens[last] not in ("JUMP_BACK", "CONTINUE"):
        # These indicate inside a loop, but token[last]
        # should not be in a loop.
        # FIXME: Not quite right: refine by using target
        return True

    # if SETUP_LOOP target spans the else part, then this is
    # not whileelse.
    last += 1
    # 3.8+ Doesn't have SETUP_LOOP
    return self.version < 3.8 and tokens[first].attr > tokens[last].off2int()
