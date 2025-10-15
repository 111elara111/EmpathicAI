import gymnasium as gym
import numpy as np
from typing import Tuple

class MultiCartPoleEnv:
    def __init__(self):
        self.env1 = gym.make('CartPole-v1')
        self.env2 = gym.make('CartPole-v1')
        self.action_space = [0, 1]
        self.state_bins = [
            np.linspace(-4.8, 4.8, 10), 
            np.linspace(-4, 4, 10),
            np.linspace(-0.418, 0.418, 10), 
            np.linspace(-4, 4, 10)
        ]
        self.t = 0

    def validate_state(self, s: np.ndarray) -> np.ndarray:
        s = np.array(s, dtype=np.float32)
        s[0] = np.clip(s[0], -4.8, 4.8)
        s[1] = np.clip(s[1], -4, 4)
        s[2] = np.clip(s[2], -0.418, 0.418)
        s[3] = np.clip(s[3], -4, 4)
        return s

    def step(self, s1: np.ndarray, s2: np.ndarray, a1: int, a2: int) -> Tuple[np.ndarray, np.ndarray, float, bool, bool, int]:
        s1 = self.validate_state(s1)
        s2 = self.validate_state(s2)
        self.env1.env.state = s1
        self.env2.env.state = s2
        s1_next, r1, done1, truncated1, _ = self.env1.step(a1)
        s2_next, r2, done2, truncated2, _ = self.env2.step(a2)
        
        # Your empathy reward logic
        r1, r2 = r1 / 100.0, r2 / 100.0
        sadness1 = abs(s1_next[2]) if abs(s1_next[2]) > 0.3 else 0.0
        sadness2 = abs(s2_next[2]) if abs(s2_next[2]) > 0.3 else 0.0
        joy_bonus = 0.5 if (sadness1 == 0 and sadness2 == 0) else 0.0
        taste_signal = 0.6 if abs(s1_next[1]) > 1.0 or abs(s2_next[1]) > 1.0 else 0.0
        empathy_bonus = joy_bonus + taste_signal + 0.1 * (a1 == a2)
        
        r = (r1 + r2) / 2 + empathy_bonus
        if done1 or done2 or truncated1 or truncated2 or abs(s1_next[2]) > 0.418 or abs(s2_next[2]) > 0.418:
            r -= 1.0
            
        self.t += 1
        return np.array(s1_next), np.array(s2_next), r, done1 or truncated1, done2 or truncated2, self.t

    def M1_sample(self, s1: np.ndarray, s2: np.ndarray, a1: int, a2: int):
        """Sample next states and reward for MCTS simulation"""
        s1_next, s2_next, r, _, _, _ = self.step(s1, s2, a1, a2)
        return s1_next, s2_next, r

    def reset(self) -> Tuple[np.ndarray, np.ndarray]:
        self.t = 0
        s1, _ = self.env1.reset()
        s2, _ = self.env2.reset()
        s1[2] *= 0.05
        s2[2] *= 0.05
        return np.array(s1), np.array(s2)

    def discretize_state(self, s: np.ndarray) -> Tuple:
        s = np.array(s, dtype=np.float32)
        return tuple(np.digitize(s[i], bins) for i, bins in enumerate(self.state_bins))