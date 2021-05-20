import stdpopsim
import msprime
import sys
sys.path.append("/code/src/methods/stdpopsim/")
import change_model

species = stdpopsim.get_species("HomSap")
model = species.get_demographic_model("OutOfAfrica_3G09")
arr = [(5, "time", 90),(0, "proportion", 0.5)]
change_model.change_model(model, arr)
print(model.demographic_events)