"""
===========================================================
SMART CLASSROOM ENERGY OPTIMIZATION SYSTEM
Using Reinforcement Learning (Q-Learning)

Author  : KAVIMUGIL R
Language: Python
GUI     : Flask Web Application

===========================================================

PROJECT IDEA
------------

This project simulates a smart classroom.

The classroom contains:
- Lights
- Fan

The AI Agent learns:
- When to turn ON devices
- When to turn OFF devices

Goal:
- Save electricity
- Maintain student comfort

IMPORTANT:
-----------
This project DOES NOT use real IoT hardware.

Instead:
We simulate IoT sensor values using Python.

Example:
- Temperature sensor
- Brightness sensor
- Student occupancy sensor

All are generated virtually.

===========================================================
HOW REINFORCEMENT LEARNING WORKS HERE
===========================================================

The AI repeatedly performs:

1. Observe classroom condition
2. Choose an action
3. Receive reward/penalty
4. Learn best action

===========================================================
STATE EXAMPLES
===========================================================

State = (
    students_present,
    temperature_level,
    brightness_level
)

Example:
(1, "HOT", "DARK")

Means:
- Students are present
- Room is hot
- Room is dark

===========================================================
ACTIONS
===========================================================

0 -> Fan OFF, Light OFF
1 -> Fan ON,  Light OFF
2 -> Fan OFF, Light ON
3 -> Fan ON,  Light ON

===========================================================
REWARD LOGIC
===========================================================

GOOD:
- Students comfortable
- Electricity saved

BAD:
- Wasting power
- Students uncomfortable

===========================================================
"""

# =========================================================
# IMPORT REQUIRED LIBRARIES
# =========================================================

import random
import numpy as np
import time

# =========================================================
# DEFINE POSSIBLE STATES
# =========================================================

states = []

for students in [0, 1]:
    for temperature in [0, 1]:
        for brightness in [0, 1]:
            states.append((students, temperature, brightness))

# =========================================================
# ACTION DEFINITIONS
# =========================================================

actions = {
    0: (0, 0),
    1: (1, 0),
    2: (0, 1),
    3: (1, 1),
}

# =========================================================
# CREATE Q-TABLE
# =========================================================

q_table = np.zeros((len(states), len(actions)))

# =========================================================
# Q-LEARNING PARAMETERS
# =========================================================

learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.2

# =========================================================
# HELPER FUNCTION
# =========================================================

def get_state_index(state):
    return states.index(state)

# =========================================================
# REWARD FUNCTION
# =========================================================

def calculate_reward(state, action):

    students, temperature, brightness = state
    fan, light = actions[action]

    reward = 0

    if students == 1:

        if temperature == 1 and fan == 1:
            reward += 10
        if temperature == 1 and fan == 0:
            reward -= 10

        if brightness == 1 and light == 1:
            reward += 10
        if brightness == 1 and light == 0:
            reward -= 10

    else:

        if fan == 0:
            reward += 5
        if light == 0:
            reward += 5
        if fan == 1:
            reward -= 5
        if light == 1:
            reward -= 5

    return reward

# =========================================================
# TRAINING THE AI AGENT
# =========================================================

episodes = 2000

print("\n================ TRAINING STARTED ================\n")

for episode in range(episodes):

    current_state = random.choice(states)
    state_index = get_state_index(current_state)

    if random.uniform(0, 1) < epsilon:
        action = random.randint(0, 3)
    else:
        action = np.argmax(q_table[state_index])

    reward = calculate_reward(current_state, action)

    next_state = random.choice(states)
    next_state_index = get_state_index(next_state)

    old_value = q_table[state_index, action]
    next_max = np.max(q_table[next_state_index])

    q_table[state_index, action] = old_value + learning_rate * (
        reward + discount_factor * next_max - old_value
    )

    # Detailed training log (every 200 episodes)
    if episode % 200 == 0:
        print(f"Episode {episode}")
        print(f"State        : {current_state}")
        print(f"Action       : {action} -> {actions[action]}")
        print(f"Reward       : {reward}")
        print(f"Q-Value Updated: {q_table[state_index]}")
        print("-" * 50)

print("\n================ TRAINING COMPLETED ================\n")

# =========================================================
# CONSOLE SIMULATION (REPLACES FLASK UI)
# =========================================================

def simulate_system(steps=20):

    print("\n================ LIVE SIMULATION ================\n")

    for step in range(steps):

        state = random.choice(states)
        state_index = get_state_index(state)

        action = np.argmax(q_table[state_index])
        fan_state, light_state = actions[action]

        reward = calculate_reward(state, action)

        students, temperature, brightness = state

        print(f"STEP {step + 1}")
        print(f"State -> Students:{students}, Temp:{temperature}, Bright:{brightness}")
        print(f"Action -> Fan:{fan_state}, Light:{light_state}")
        print(f"Reward -> {reward}")
        print(f"Q Row -> {q_table[state_index]}")
        print("=" * 60)

        time.sleep(0.5)

# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    simulate_system(steps=25)