import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generate_sample_means(distribution, sample_size, num_samples):
    sample_means = []
    for _ in range(num_samples):
        if distribution == "uniform":
            sample = np.random.uniform(0, 1, sample_size)
        elif distribution == "exponential":
            sample = np.random.exponential(1, sample_size)
        elif distribution == "binomial":
            sample = np.random.binomial(10, 0.5, sample_size)
        sample_means.append(np.mean(sample))
    return sample_means


def animate_clt(distribution, max_sample_size, num_samples):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].set_title("Original Distribution")
    ax[1].set_title("Sample Means Distribution")
    
    if distribution == "uniform":
        data = np.random.uniform(0, 1, 10000)
    elif distribution == "exponential":
        data = np.random.exponential(1, 10000)
    elif distribution == "binomial":
        data = np.random.binomial(10, 0.5, 10000)
    ax[0].hist(data, bins=50, color="skyblue", alpha=0.7)
    
    def update(frame):
        ax[1].clear()
        sample_means = generate_sample_means(distribution, frame + 1, num_samples)
        ax[1].hist(sample_means, bins=50, color="orange", alpha=0.7)
        ax[1].set_title(f"Sample Size: {frame + 1}")

    anim = FuncAnimation(fig, update, frames=max_sample_size, interval=300)
    plt.show()

distribution = "uniform"  # Choose "uniform", "exponential", or "binomial"
max_sample_size = 1000
num_samples = 10000

animate_clt(distribution, max_sample_size, num_samples)
