from train import train
import torch
import os

if __name__ == "__main__":
    print("Running verification training (5 episodes)...")
    try:
        scores = train(n_episodes=5, max_t=200)
        print("Verification training complete.")
        
        # Check if model file exists (it might not if not solved, but let's check plot)
        if os.path.exists('plots/training_score.png'):
            print("Plot generated successfully.")
        else:
            print("Warning: Plot not generated.")
            
    except Exception as e:
        print(f"Verification failed: {e}")
