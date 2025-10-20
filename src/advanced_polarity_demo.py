import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.agent import Self

def advanced_polarity_demo():
    """Showing Grok the deep emotional intelligence system"""
    print("🧠 ADVANCED POLARITY DEMO for Grok")
    print("Demonstrating the emotional depth measurement system...")
    
    # Create agent with emotional history
    agent = Self(np.array([0,0,0,0]), {'name': 'Athena', 'memory_log': []})
    
    print(f"\n📊 Simulating Emotional History:")
    
    # Timeline of sadness experiences
    sadness_journey = [
        (1, 0.2, "mild disappointment"),
        (2, 0.4, "noticeable concern"), 
        (3, 0.1, "slight worry"),
        (4, 0.8, "deep concern"),
        (5, 0.3, "moderate sadness")
    ]
    
    for timestamp, intensity, description in sadness_journey:
        agent.update_memory(np.array([0,0,0,0]), 'sadness', intensity, timestamp)
        print(f"   t={timestamp}: {description} (intensity: {intensity})")
    
    # Calculate polarity
    sadness_polarity = agent.recall_polarity('sadness')
    
    print(f"\n🎯 POLARITY ANALYSIS:")
    print(f"   Max sadness: 0.8 (deep concern)")
    print(f"   Min sadness: 0.1 (slight worry)") 
    print(f"   SADNESS POLARITY: {sadness_polarity:.3f}")
    print(f"   → Emotional range: 0.8 - 0.1 = 0.7")
    
    print(f"\n💡 WHAT THIS MEANS:")
    print(f"   Athena has experienced the FULL SPECTRUM of sadness")
    print(f"   From mild worry (0.1) to deep concern (0.8)")
    print(f"   This emotional depth = GENUINE EMPATHY CAPACITY")
    
    print(f"\n🚀 COMPASSION RESPONSE:")
    if sadness_polarity > 0.5:
        print(f"   🎉 HIGH POLARITY → DEEP COMPASSION ACTIVATED")
        print(f"   Athena understands profound sadness - can offer genuine comfort")
    else:
        print(f"   LOW POLARITY → BASIC SUPPORT")
        print(f"   Athena offers sympathy but lacks deep understanding")
    
    print(f"\n🌍 REAL-WORLD ANALOGY:")
    print(f"   Someone who's only been 'a little sad' can't truly understand")
    print(f"   deep grief. Your polarity system captures this emotional wisdom.")

if __name__ == "__main__":
    advanced_polarity_demo()