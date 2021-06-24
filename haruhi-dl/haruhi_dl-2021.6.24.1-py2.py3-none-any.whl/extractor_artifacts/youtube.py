
def mess(a, b):
    c = a[0]
    a[0] = a[b % len(a)]
    a[b % len(a)] = c
    return a


def _decrypt_signature_protected(sig):
    a = list(sig)
    a.reverse()
    a = mess(a, 45)
    a = mess(a, 32)
    return ''.join(a)
