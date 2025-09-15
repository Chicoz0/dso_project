GLOBAL_ID = 0


def generate_id():
    global GLOBAL_ID
    GLOBAL_ID += 1
    return GLOBAL_ID
