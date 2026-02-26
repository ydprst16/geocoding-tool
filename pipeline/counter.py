def create_status_counter():
    return {
        "SUCCESS": 0,
        "OUT_OF_KECAMATAN": 0,
        "OUT_OF_DUMAI": 0,
        "ERROR_REQUEST": 0,
        "EMPTY": 0,
        "OTHER": 0
    }

def update_counter(counter, status):
    if status in counter:
        counter[status] += 1
    else:
        counter["OTHER"] += 1