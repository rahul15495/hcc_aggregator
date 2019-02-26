import importlib
import multiprocessing as mp

handler= None

def handler_wrapper(q,*args):
    
    handler= importlib.import_module('handler')

    args=args[0][0]
    out = handler.get_scores(**args)
    q.put(out)

def single_month_score_predcitor(**kwargs):

    q= mp.Queue()

    process=mp.Process(target=handler_wrapper, args=(q,[kwargs]) )

    process.start()
    
    out =q.get()

    process.join()

    return out


def aggregate_score_predcitor(**kwargs):
    print(kwargs)
    
    return 0

#https://stackoverflow.com/questions/17503909/select-a-module-using-importlib-and-use-in-multiprocessing-functions