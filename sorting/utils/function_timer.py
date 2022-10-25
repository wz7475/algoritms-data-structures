import gc
import time


def execution_time(function, collection: list) -> float:
    gc_status = gc.isenabled()
    gc.disable()
    start = time.process_time()
    function(collection)
    stop = time.process_time()

    if gc_status:
        gc.enable()

    return stop - start
