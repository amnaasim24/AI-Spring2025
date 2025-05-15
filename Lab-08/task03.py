from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianModel([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue'),
    ('Disease', 'Chills')
])

cpd_disease = TabularCPD('Disease', 2, [[0.3], [0.7]], state_names={'Disease': ['Flu', 'Cold']})

cpd_fever = TabularCPD('Fever', 2, [[0.9, 0.5], [0.1, 0.5]], evidence=['Disease'], evidence_card=[2],
                       state_names={'Fever': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']})

cpd_cough = TabularCPD('Cough', 2, [[0.8, 0.6], [0.2, 0.4]], evidence=['Disease'], evidence_card=[2],
                       state_names={'Cough': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']})

cpd_fatigue = TabularCPD('Fatigue', 2, [[0.7, 0.3], [0.3, 0.7]], evidence=['Disease'], evidence_card=[2],
                         state_names={'Fatigue': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']})

cpd_chills = TabularCPD('Chills', 2, [[0.6, 0.4], [0.4, 0.6]], evidence=['Disease'], evidence_card=[2],
                        state_names={'Chills': ['Yes', 'No'], 'Disease': ['Flu', 'Cold']})

model.add_cpds(cpd_disease, cpd_fever, cpd_cough, cpd_fatigue, cpd_chills)
assert model.check_model()

infer = VariableElimination(model)

print("\nP(Disease | Fever=Yes, Cough=Yes):")
result1 = infer.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes'})
print(result1)

print("\nP(Disease | Fever=Yes, Cough=Yes, Chills=Yes):")
result2 = infer.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes', 'Chills': 'Yes'})
print(result2)

print("\nP(Fatigue=Yes | Disease=Flu):")
result3 = infer.query(variables=['Fatigue'], evidence={'Disease': 'Flu'})
print(result3)