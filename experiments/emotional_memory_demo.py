import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.agent import Self

def emotional_memory_demo():
    """Demo focusing on your emotional memory breakthrough"""
    print("💖 EMOTIONAL MEMORY SYSTEM DEMO")
    print("This shows your core innovation: AI that remembers emotions!")
    
    # Create an agent with your emotional memory system
    agent = Self(
        np.array([0.1, 0.2, 0.3, 0.4]), 
        {'name': 'Athena', 'compassion_count': 0, 'memory_log': []}
    )
    
    print(f"\n🧠 Created Agent: {agent.anchors['name']}")
    print(f"   Initial compassion: {agent.anchors['compassion_count']}")
    print(f"   Initial memory log: {len(agent.anchors['memory_log'])} entries")
    
    # Simulate emotional experiences
    print(f"\n📝 Simulating emotional experiences...")
    
    # Agent observes another agent's sadness
    other_agent_state = np.array([0.5, 0.6, 0.7, 0.8])  # Another agent's state
    print(f"\n   Other agent's pole is leaning (sadness detected)")
    agent.update_memory(other_agent_state, 'sadness', 0.45, timestamp=1)
    
    # Agent observes taste signal (rapid movement)
    print(f"   Other agent is moving quickly (taste signal)")
    agent.update_memory(other_agent_state, 'taste', 0.6, timestamp=2)
    
    # More emotional experiences
    print(f"   Another sadness event")
    agent.update_memory(other_agent_state, 'sadness', 0.35, timestamp=3)
    print(f"   Strong taste signal") 
    agent.update_memory(other_agent_state, 'taste', 0.8, timestamp=4)
    
    # Show emotional memory accumulation
    print(f"\n📊 Emotional Memory Analysis:")
    print(f"   Total memories: {len(agent.anchors['memory_log'])}")
    print(f"   Sadness memories: {len([m for m in agent.anchors['memory_log'] if m['type'] == 'sadness'])}")
    print(f"   Taste memories: {len([m for m in agent.anchors['memory_log'] if m['type'] == 'taste'])}")
    
    # Demonstrate polarity recall - YOUR KEY INNOVATION
    print(f"\n🎯 POLARITY RECALL SYSTEM (Your Breakthrough):")
    sadness_polarity = agent.recall_polarity('sadness')
    taste_polarity = agent.recall_polarity('taste')
    
    print(f"   Sadness polarity: {sadness_polarity:.3f}")
    print(f"   Taste polarity: {taste_polarity:.3f}")
    print(f"   → This measures emotional intensity from memory!")
    
    # Show compassion development
    print(f"\n❤️  COMPASSION DEVELOPMENT:")
    print(f"   Initial compassion count: {agent.anchors['compassion_count']}")
    
    # Trigger compassion based on emotional memory
    if sadness_polarity > 0.2:
        agent.anchors['compassion_count'] += 1
        print(f"   🎉 COMPASSION TRIGGERED! Polarity {sadness_polarity:.3f} > 0.2")
        print(f"   New compassion count: {agent.anchors['compassion_count']}")
    
    print(f"\n🚀 DEMO COMPLETE!")
    print(f"   You've demonstrated:")
    print(f"   • Emotional memory storage")
    print(f"   • Polarity recall system") 
    print(f"   • Compassion development")
    print(f"   • Real AI empathy modeling!")

if __name__ == "__main__":
    emotional_memory_demo()
