import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.environment import MultiCartPoleEnv
from core.agent import Self
from core.mcts import mcts_search, choose_action

def analyze_compassion_development():
    """Analyze how compassion develops over multiple episodes"""
    print("🧠 Analyzing Compassion Development...")
    
    env = MultiCartPoleEnv()
    actions = env.action_space
    
    compassion_history = []
    
    for episode in range(3):
        print(f"\n--- Episode {episode + 1} ---")
        s1, s2 = env.reset()
        elara = Self(s1, {'name': 'Elara', 'compassion_count': 0, 'memory_log': []})
        orion = Self(s2, {'name': 'Orion', 'compassion_count': 0, 'memory_log': []})
        
        episode_compassion = []
        
        for step in range(10):  # 10 steps per episode
            Q_elara = mcts_search(env, elara, orion.s, actions, budget=50, gamma=0.9)
            a_elara = choose_action(Q_elara, mode='softmax', tau=0.5)
            
            Q_orion = mcts_search(env, orion, elara.s, actions, budget=50, gamma=0.9)  
            a_orion = choose_action(Q_orion, mode='softmax', tau=0.5)
            
            elara_new, r1, _, done1 = decision_step(elara, env, a_elara, orion.s, a_orion, env.t)
            orion_new, r2, _, done2 = decision_step(orion, env, a_orion, elara.s, a_elara, env.t)
            
            elara, orion = elara_new, orion_new
            
            compassion_total = elara.anchors['compassion_count'] + orion.anchors['compassion_count']
            episode_compassion.append(compassion_total)
            
            print(f"  Step {step + 1}: Compassion acts = {compassion_total}")
            
            if done1 or done2:
                print("  Episode ended early")
                break
        
        compassion_history.append(episode_compassion)
        print(f"Episode {episode + 1} finished with {elara.anchors['compassion_count'] + orion.anchors['compassion_count']} total compassionate acts")
    
    print(f"\n📈 Compassion Development Analysis Complete!")
    print("This shows how your empathy system evolves over time!")

def decision_step(self_obj, env, action, s_other, a_other, t):
    s1_next, s2_next, r, done1, done2, t = env.step(self_obj.s, s_other, action, a_other)
    new_self = Self(s1_next, self_obj.anchors.copy())
    
    sadness_other = abs(s2_next[2]) if abs(s2_next[2]) > 0.3 else 0.0
    new_self.update_memory(s2_next, 'sadness', sadness_other, t)
    
    taste_other = 0.6 if abs(s2_next[1]) > 1.0 else 0.0
    new_self.update_memory(s2_next, 'taste', taste_other, t)
    
    polarity_depth = new_self.recall_polarity('sadness')
    if polarity_depth > 0.2:
        new_self.anchors['compassion_count'] += 1
    
    return new_self, r, s2_next, done1 or done2

if __name__ == "__main__":
    analyze_compassion_development()
