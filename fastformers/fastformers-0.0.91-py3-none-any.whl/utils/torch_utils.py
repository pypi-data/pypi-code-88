def neg_inf(fp16: bool) -> float:
    return -65504. if fp16 else -1e20
