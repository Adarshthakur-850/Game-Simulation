# Deep RL Game Simulation (DQN)

## Overview
This project implements a Deep Q-Network (DQN) agent to solve the **CartPole-v1** environment from OpenAI Gym. The agent learns to balance a pole on a cart by interacting with the environment and learning from rewards.

## Project Structure
```
Game Simulation/
├── models/             # Saved model weights
├── plots/              # Training curves
├── src/
│   ├── model.py        # Neural Network architecture
│   ├── memory.py       # Replay Buffer
│   ├── agent.py        # DQN Agent Logic
├── train.py            # Training script
├── evaluate.py         # Evaluation/Rendering script
├── requirements.txt
└── README.md
```

## Setup
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Train the Agent**:
   ```bash
   python train.py
   ```
   - Trains the agent for up to 2000 episodes (or until solved).
   - Saves model to `models/checkpoint.pth`.
   - Saves reward plot to `plots/training_score.png`.

2. **Evaluate/Watch the Agent**:
   ```bash
   python evaluate.py
   ```
   - Loads the trained model.
   - Renders the agent playing the game in a window.

## Parameters
- **Algorithm**: DQN (Deep Q-Network)
- **Experience Replay**: Buffer size 100,000
- **Target Network**: Soft updates ($\tau=1e-3$)
- **Action Selection**: Epsilon-Greedy (Starts at 1.0, decays to 0.01)
