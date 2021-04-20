# defines the named model for modifying purposes
# this one is the exact same model, for testing before modifying
# to be called:
# model = OutOfAfrica_3G09Ex6.build_model(OutOfAfrica_3G09Ex6.build_model_params())

import math
import msprime
import stdpopsim

# return a dict of the listed parameters
def build_model_params():
    # First we set out the maximum likelihood values of the various parameters
    # given in Table 1.
    N_A = 7300
    N_AF = 12300
    N_B = 2100
    N_EU0 = 1000
    N_AS0 = 510
    r_EU = 0.004   # 0.4% EU growth
    r_AS = 0.0055  # 0.55% AS growth
    # Migration rates during the various epochs.
    m_AF_B = 25e-5
    m_AF_EU = 3e-5
    m_AF_AS = 1.9e-5
    m_EU_AS = 9.6e-5
    # Times in Table 1 are provided in years, calculated on the assumption
    # of 25 years per generation: we need to convert back into generations.
    generation_time = 25
    T_AF = 220e3 / generation_time
    T_B = 140e3 / generation_time
    T_EU_AS = 21.2e3 / generation_time
    # We need to work out the starting (diploid) population sizes based on
    # the growth rates provided for these two populations
    N_EU = N_EU0 / math.exp(-r_EU * T_EU_AS)
    N_AS = N_AS0 / math.exp(-r_AS * T_EU_AS)
    # Population IDs correspond to their indexes in the population
    # configuration array. Therefore, we have 0=YRI, 1=CEU and 2=CHB
    # initially.
    population_configurations = [
        msprime.PopulationConfiguration(
            initial_size=N_AF),
        msprime.PopulationConfiguration(
            initial_size=N_EU, growth_rate=r_EU),
        msprime.PopulationConfiguration(
            initial_size=N_AS, growth_rate=r_AS)
    ]
    migration_matrix = [
        [      0, m_AF_EU, m_AF_AS],
        [m_AF_EU,       0, m_EU_AS],
        [m_AF_AS, m_EU_AS,       0],
    ]
    demographic_events = [
        # CEU and CHB merge into B with rate changes at T_EU_AS
        msprime.MassMigration(
            time=T_EU_AS, source=2, destination=1, proportion=1.0),
        msprime.MigrationRateChange(time=T_EU_AS, rate=0),
        msprime.MigrationRateChange(
            time=T_EU_AS, rate=m_AF_B, matrix_index=(0, 1)),
        msprime.MigrationRateChange(
            time=T_EU_AS, rate=m_AF_B, matrix_index=(1, 0)),
        msprime.PopulationParametersChange(
            time=T_EU_AS, initial_size=N_B, growth_rate=0, population_id=1),
        # Population B merges into YRI at T_B
        msprime.MassMigration(
            time=T_B, source=1, destination=0, proportion=1.0),
        msprime.MigrationRateChange(time=T_B, rate=0),   # NB THIS EVENT WAS MISSING!!!!
        # Size changes to N_A at T_AF
        msprime.PopulationParametersChange(
            time=T_AF, initial_size=N_A, population_id=0)
    ]
    return {
        'population_configurations':population_configurations,
        'migration_matrix':migration_matrix,
        'demographic_events':demographic_events}
    
    # creates the model, modifed as mentioned in the prev func
def build_model(mod_model_params):
    species = stdpopsim.get_species("HomSap")
    realModel = species.get_demographic_model("OutOfAfrica_3G09")
    
    id = realModel.id
    description = realModel.description
    long_description = realModel.long_description
    populations = realModel.populations
    citations = realModel.citations
    generation_time = realModel.generation_time

    # parameter value definitions based on modified model
    
    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=generation_time,
        population_configurations=mod_model_params["population_configurations"],
        migration_matrix=mod_model_params["migration_matrix"],
        demographic_events=mod_model_params["demographic_events"],
    )