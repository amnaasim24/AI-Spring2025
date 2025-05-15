import random

states = ['Sunny', 'Cloudy', 'Rainy']
transition_matrix = {
    'Sunny': [0.6, 0.3, 0.1],
    'Cloudy': [0.3, 0.4, 0.3],
    'Rainy': [0.2, 0.4, 0.4]
}

def simulate_weather(days=10, start='Sunny'):
    current = start
    sequence = [current]
    for _ in range(days):
        probs = transition_matrix[current]
        current = random.choices(states, weights=probs)[0]
        sequence.append(current)
    return sequence

rainy_count = 0
simulations = 1000

for _ in range(simulations):
    forecast = simulate_weather()
    if forecast.count('Rainy') >= 3:
        rainy_count += 1

estimated_prob = rainy_count / simulations
print(f"\nEstimated P(at least 3 Rainy days in 10): {estimated_prob}")