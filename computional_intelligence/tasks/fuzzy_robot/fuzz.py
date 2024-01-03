import matplotlib.pyplot as plt
from fuzzy_expert.variable import FuzzyVariable
from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.inference import DecompositionalInference


variables = {
    "s2": FuzzyVariable(
        universe_range=(0, 120),
        terms={
            "Far": [(60, 0), (100, 1)],
            "Close": [(20, 1),  (60, 0)],
        },
    ),
    "s3": FuzzyVariable(
        universe_range=(0, 120),
        terms={
            "Far": [(40, 0), (100, 1)],
            "Close": [(15, 1),  (40, 0)],
        },
    ),
    "s4": FuzzyVariable(
        universe_range=(0, 120),
        terms={
            "Far": [(60, 0), (100, 1)],
            "Close": [(20, 1),  (60, 0)],
        },
    ),
    "decision": FuzzyVariable(
        universe_range=(-1, 1),
        terms={
            "pos": [(0, 0), (1, 1)],
            "neg": [(-1, 1), (0, 0)],
            "front": [(-3, 0), (0, 1), (3, 0)],
        },
    ),
}



rules = [
    FuzzyRule(
        cf = 1,
        premise=[
            ("s3", "Far"),
            # ("AND", "s2", "Far"), # 45 degree right
            # ("OR", "s4", "Far"), # 45 degree left
        ],
        consequence=[("decision", "front")],
    ),
    FuzzyRule(
        premise=[
            ("s3" , 'Close'),
            ("OR", "s2", "Close"),
            # ("AND", "s4", "Close"),
        ],
        consequence=[("decision", "pos")],
    ),
    FuzzyRule(
        premise=[
            ("s3" , 'Close'),
            ("AND", "s4", "Close"),
        ],
        consequence=[("decision", "neg")],
    ),
]



model = DecompositionalInference(
    and_operator="min",
    or_operator="max",
    implication_operator="Rc",
    composition_operator="max-min",
    production_link="max",
    defuzzification_operator="cog",
)

# model(
#     variables=variables,
#     rules=rules,
#     s2=80,
#     s3=30,
#     s4=20,
# )