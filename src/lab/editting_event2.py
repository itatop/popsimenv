import stdpopsim

species = stdpopsim.get_species("HomSap")
model = species.get_demographic_model("OutOfAfrica_3G09")
for i in range(len(model.demographic_events)):
    e = model.demographic_events[i]
    if e.type == "mass_migration":
        if e.source == 1 and e.dest == 0 and e.proportion == 1.0:
            print (e.time)
            model.demographic_events[i].time = 190e3 / model.generation_time
            print("changed!")
            print (model.demographic_events[i].time)
            break
