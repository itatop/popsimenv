"""
model changer func
"""
import dadi
import msprime

def change_model(model, changes_arr):
    gen_time = model.generation_time
    for truple in changes_arr:
        setattr(model.demographic_events[truple[0]], truple[1], truple[2])
        if truple[1] == 'time':
            model.demographic_events[truple[0]].time /= gen_time
