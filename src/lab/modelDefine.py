# defining a new model for stdpopsim
import stdpopsim
def _model_func_name():
    id = "FILL ME"
    description = "FILL ME"
    long_description = """
    FILL ME
    """
    populations = [
        stdpopsim.Population(id="FILL ME", description="FILL ME"),
    ]
    citations = [
        stdpopsim.Citation(
            author="FILL ME",
            year="FILL ME",
            doi="FILL ME",
            reasons={stdpopsim.CiteReason.DEM_MODEL},
        )
    ]

    generation_time = "FILL ME"

    # parameter value definitions based on published values

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=generation_time,
        population_configurations=["FILL ME"],
        migration_matrix=["FILL ME"],
        demographic_events=["FILL ME"],
    )
