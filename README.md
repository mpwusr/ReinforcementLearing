# Reinforcement Learning in Python

This repository contains a Python implementation of a reinforcement learning (RL) algorithm for a robot navigating a maze, as described in the Medium article *"Hands-On Introduction to Reinforcement Learning in Python"* by Neha Desaraju. The code provided in the article has been debugged and improved to ensure proper functionality. The project demonstrates the core concepts of reinforcement learning, including Q-learning, and explores the impact of hyperparameters on the learning process.

## Project Overview

The program simulates a robot learning to navigate a maze using a Q-learning algorithm. The robot interacts with the environment, receiving rewards or penalties based on its actions, and updates its knowledge (Q-table) to make better decisions over time. The maze navigation task serves as a practical example to illustrate RL principles such as states, actions, rewards, and exploration vs. exploitation.

The code includes:
- A debugged implementation of the Q-learning algorithm.
- A maze environment where the robot learns to find the optimal path.
- Configurable hyperparameters: **learning rate (`alpha`)** and **random factor (`random_factor`)**.

The repository answers two key questions about the impact of hyperparameters:
1. How does changing the `random_factor` affect the robot’s learning process?
2. How does changing the `learning rate` affect the robot’s learning process?

## Setup Instructions

### Prerequisites
- Python 3.x
- Required libraries: `numpy` (for matrix operations)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mpwusr/ReinforcementLearning.git
   cd ReinforcementLearning
   ```
2. Install dependencies:
   ```bash
   pip install numpy
   ```
3. Run the main script:
   ```bash
   python main.py
   ```

### Files
- `main.py`: The main script containing the Q-learning algorithm, maze environment, and training loop.
- Other supporting files (if applicable): Debugged versions of any additional scripts from the article.

## Usage

The `main.py` script initializes the maze, sets up the Q-table, and trains the robot using Q-learning. The default hyperparameters are:
- `alpha = 0.1` (learning rate)
- `random_factor = 0.25` (probability of taking a random action)

To experiment with different hyperparameter values:
1. Open `main.py`.
2. Modify the `alpha` or `random_factor` variables.
3. Run the script to observe changes in the robot’s learning behavior.

The script outputs metrics such as the number of steps taken per episode and whether the robot successfully navigates the maze or gets lost.

## Hyperparameter Analysis

The following sections address the two questions about hyperparameters, based on experiments with the debugged code.

### 1. How does changing the `random_factor` affect the robot’s learning process?

The `random_factor` determines the probability that the robot takes a random action (exploration) instead of choosing the action with the highest Q-value (exploitation). Its impact on learning is as follows:

- **High `random_factor` (e.g., 0.5 or higher)**:
  - The robot explores more frequently, trying new paths in the maze.
  - This can lead to slower convergence because the robot spends more time taking suboptimal actions.
  - However, it may discover better paths in complex mazes, avoiding getting stuck in local optima.
  - Downside: Excessive randomness can prevent the robot from learning a stable policy, causing it to get lost or take longer to navigate the maze.

- **Low `random_factor` (e.g., 0.1 or lower)**:
  - The robot favors exploitation, choosing actions based on current Q-values.
  - This leads to faster convergence to a policy, as the robot quickly learns to follow known rewarding paths.
  - Downside: The robot may miss better paths due to insufficient exploration, potentially settling for suboptimal solutions.

- **Default (`random_factor = 0.25`)**:
  - Strikes a balance between exploration and exploitation.
  - The robot learns efficiently in most cases, navigating the maze within a reasonable number of episodes without getting lost.

**Conclusion**: A moderate `random_factor` (like 0.25) is ideal for the maze task, allowing enough exploration to find good paths while ensuring steady progress toward learning an optimal policy. Too high a value slows learning, while too low a value risks suboptimal paths.

### 2. How does changing the `learning rate` affect the robot’s learning process?

The `learning rate` (`alpha`) controls how much the Q-values are updated based on new information. Its impact on learning is as follows:

- **High `learning rate` (e.g., 0.5 or higher)**:
  - The robot prioritizes new rewards over past knowledge, leading to rapid updates to the Q-table.
  - This can accelerate learning in simple mazes, as the robot quickly adapts to new information.
  - Downside: High values can cause instability, as the Q-values may fluctuate too much, leading to erratic behavior or failure to converge. The robot may struggle to settle on a consistent policy.

- **Low `learning rate` (e.g., 0.01 or lower)**:
  - The robot updates Q-values slowly, relying more on past knowledge.
  - This leads to stable but slow learning, requiring more episodes to navigate the maze successfully.
  - Downside: In dynamic or complex mazes, the robot may take too long to adapt to new patterns, potentially getting stuck or lost.

- **Default (`alpha = 0.1`)**:
  - Provides a balanced approach, allowing the robot to learn steadily without drastic swings in Q-values.
  - The robot typically converges to an optimal policy within a reasonable number of episodes, successfully navigating the maze.

**Conclusion**: A moderate `learning rate` (like 0.1) is effective for the maze task, enabling the robot to learn reliably without instability or excessive delay. Higher values risk erratic learning, while lower values slow down progress.

## Results

With the default settings (`alpha = 0.1`, `random_factor = 0.25`), the robot learns to navigate the maze efficiently in most runs, typically converging within a few hundred episodes. Adjusting the hyperparameters allows users to observe trade-offs between exploration/exploitation and learning speed/stability.

## Future Improvements

- Add visualization of the maze and the robot’s path to better understand its learning process.
- Implement an epsilon-decay strategy for `random_factor` to reduce exploration over time.
- Experiment with additional RL algorithms (e.g., SARSA) or more complex maze environments.

## References

- Desaraju, Neha. *"Hands-On Introduction to Reinforcement Learning in Python"*. Medium.
- Debugged code based on the original implementation from the article.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
