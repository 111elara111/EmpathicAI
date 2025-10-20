import numpy as np
import sys
import os

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.environment import MultiCartPoleEnv
from core.agent import Self, ReplayBuffer
from core.mcts import mcts_search, choose_action

def run_empathy_demo():
    """Demo showing how agents develop empathy"""
    print("🚀 Starting Empathic AI Demo...")
    print("This shows two AI agents learning to care about each other!")
    
    env = MultiCartPoleEnv()
    actions = env.action_space
    
    # Create agents with emotional memory
    s1, s2 = env.reset()
    elara = Self(s1, {'name': 'Elara', 'compassion_count': 0, 'memory_log': []})
    orion = Self(s2, {'name': 'Orion', 'compassion_count': 0, 'memory_log': []})
    
    print(f"\n🎭 Created Agents:")
    print(f"   {elara.anchors['name']}: {elara}")
    print(f"   {orion.anchors['name']}: {orion}")
    
    # Run interaction
    print(f"\n🤖 Starting interaction (20 steps)...")
    
    for step in range(20):
        # Elara decides
        Q_elara = mcts_search(env, elara, orion.s, actions, budget=50, gamma=0.9)
        a_elara = choose_action(Q_elara, mode='softmax', tau=0.5)
        
        # Orion decides  
        Q_orion = mcts_search(env, orion, elara.s, actions, budget=50, gamma=0.9)
        a_orion = choose_action(Q_orion, mode='softmax', tau=0.5)
        
        # Take actions
        elara_new, r1, s2_next, done1 = decision_step(elara, env, a_elara, orion.s, a_orion, env.t)
        orion_new, r2, s1_next, done2 = decision_step(orion, env, a_orion, elara.s, a_elara, env.t)
        
        elara, orion = elara_new, orion_new
        
        print(f"\n   Step {step + 1}:")
        print(f"   {elara.anchors['name']} → Action: {a_elara}, Compassion: {elara.anchors['compassion_count']}")
        print(f"   {orion.anchors['name']} → Action: {a_orion}, Compassion: {orion.anchors['compassion_count']}")
        print(f"   Shared Reward: {r1:.3f}")
        
        if done1 or done2:
            print("   💥 Episode ended (pole fell)")
            break
    
    print(f"\n📊 Final Compassion Scores:")
    print(f"   {elara.anchors['name']}: {elara.anchors['compassion_count']} compassionate acts")
    print(f"   {orion.anchors['name']}: {orion.anchors['compassion_count']} compassionate acts")
    
    print(f"\n🎉 Demo completed! Agents developed emotional memory and compassion.")

def decision_step(self_obj, env, action, s_other, a_other, t):
    """Execute one decision step with emotional memory update"""
    s1_next, s2_next, r, done1, done2, t = env.step(self_obj.s, s_other, action, a_other)
    
    # Create new self with updated state but same anchors
    new_self = Self(s1_next, self_obj.anchors.copy())
    
    # Emotional memory updates
    sadness_other = abs(s2_next[2]) if abs(s2_next[2]) > 0.3 else 0.0
    new_self.update_memory(s2_next, 'sadness', sadness_other, t)
    
    taste_other = 0.6 if abs(s2_next[1]) > 1.0 else 0.0
    new_self.update_memory(s2_next, 'taste', taste_other, t)
    
    # Compassion tracking
    polarity_depth = new_self.recall_polarity('sadness')
    if polarity_depth > 0.2:
        new_self.anchors['compassion_count'] += 1
    
    return new_self, r, s2_next, done1 or done2

if __name__ == "__main__":
    run_empathy_demo()