import gymnasium as gym
import torch
import numpy as np
import matplotlib.pyplot as plt
import os
from src.agent import Agent

def evaluate(model_path='models/checkpoint.pth', n_episodes=5):
    """
    Evaluates the trained agent.
    """
    env = gym.make('CartPole-v1', render_mode='human')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    agent = Agent(state_size=state_size, action_size=action_size, seed=0)
    
    # Load trained weights
    if not os.path.exists(model_path):
        if os.path.exists('models/final.pth'):
            print(f"Model {model_path} not found. Loading models/final.pth instead.")
            model_path = 'models/final.pth'
    
    if torch.cuda.is_available():
        agent.qnetwork_local.load_state_dict(torch.load(model_path))
    else:
        agent.qnetwork_local.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        
    for i in range(n_episodes):
        state, _ = env.reset()
        score = 0
        while True:
            action = agent.act(state) # Greedy action
            next_state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            state = next_state
            score += reward
            if done:
                break
        print(f"Episode {i+1}: Score = {score}")
    
    env.close()

if __name__ == "__main__":
    try:
        evaluate()
    except FileNotFoundError:
        print("Model file not found. Please run train.py first.")
