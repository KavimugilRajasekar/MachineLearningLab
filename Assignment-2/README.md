# SMART CLASSROOM ENERGY OPTIMIZATION SYSTEM 
### Reinforcement Learning (Q-Learning Based AI Simulation)

---

## Author
**KAVIMUGIL R - 2303717710421023**

---

## 📌 Project Overview

The **Smart Classroom Energy Optimization System** is an AI-based simulation project that uses **Reinforcement Learning (Q-Learning)** to intelligently manage classroom devices such as:

- 💡 Lights  
- 🌀 Fans  

The system learns optimal behavior over time to:
- Reduce unnecessary electricity consumption
- Maintain student comfort
- Automatically decide device states based on environment conditions

> ⚠️ Note: This project does NOT use real IoT hardware.  
> Instead, it simulates sensor data using Python.

---

## 🧠 Core Idea

The AI agent behaves like a smart controller inside a classroom. It:

1. Observes the classroom environment  
2. Takes an action (fan/light control)  
3. Receives a reward or penalty  
4. Learns from experience using Q-learning  

Over time, it improves decision-making without explicit programming rules.

---

## 🌍 Simulated Environment

The classroom environment is represented using 3 main parameters:

### 👨 Students
- `0` → No students present  
- `1` → Students present  

### 🌡 Temperature
- `0` → COOL  
- `1` → HOT  

### 💡 Brightness
- `0` → BRIGHT  
- `1` → DARK  

---

## 📦 State Representation

Each state is a tuple:
