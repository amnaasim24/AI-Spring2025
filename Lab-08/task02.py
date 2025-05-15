from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# I = Intelligence  |  S = Study Hours  |  D = Difficulty  |  G = Grade  |  P = Pass

model = BayesianModel([
    ('I', 'G'),
    ('S', 'G'),
    ('D', 'G'),
    ('G', 'P')
])

cpd_intelligence = TabularCPD('I', 2, [[0.7], [0.3]], state_names={'I': ['High', 'Low']})
cpd_study = TabularCPD('S', 2, [[0.6], [0.4]], state_names={'S': ['Sufficient', 'Insufficient']})
cpd_difficulty = TabularCPD('D', 2, [[0.6], [0.4]], state_names={'D': ['Easy', 'Hard']})

cpd_grade = TabularCPD(
    'G', 3,
    values=[
        [0.8, 0.6, 0.5, 0.3, 0.4, 0.2, 0.2, 0.1],
        [0.15, 0.25, 0.3, 0.4, 0.4, 0.4, 0.4, 0.3],
        [0.05, 0.15, 0.2, 0.3, 0.2, 0.4, 0.4, 0.6]
    ],
    evidence=['I', 'S', 'D'],
    evidence_card=[2, 2, 2],
    state_names={
        'G': ['A', 'B', 'C'],
        'I': ['High', 'Low'],
        'S': ['Sufficient', 'Insufficient'],
        'D': ['Easy', 'Hard']
    }
)

cpd_pass = TabularCPD(
    'P', 2,
    values=[[0.95, 0.8, 0.5], [0.05, 0.2, 0.5]],
    evidence=['G'],
    evidence_card=[3],
    state_names={'P': ['Yes', 'No'], 'G': ['A', 'B', 'C']}
)

model.add_cpds(cpd_intelligence, cpd_study, cpd_difficulty, cpd_grade, cpd_pass)
assert model.check_model()

infer = VariableElimination(model)
result = infer.query(variables=['Pass'], evidence={'I': 'High', 'S': 'Sufficient', 'D': 'Hard'})
print(result)