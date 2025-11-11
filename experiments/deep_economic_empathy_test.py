import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.agent import Self

class DeepEmpathyAthena(Self):
    """Athena with enhanced economic empathy through deeper experiences"""
    
    def __init__(self, state, anchors=None):
        super().__init__(state, anchors)
        self.ethical_decisions = []
    
    def calculate_empathy_penalty(self, potential_harm, harm_type):
        """Enhanced empathy penalty calculation"""
        if harm_type == "sadness":
            wisdom_weight = self.recall_polarity('sadness') * 2 + self.recall_polarity('trust')
        elif harm_type == "trust":
            wisdom_weight = self.recall_polarity('trust') * 2 + self.recall_polarity('sadness')
        else:  # dignity - NOW WITH ECONOMIC EMPATHY
            wisdom_weight = (self.recall_polarity('sadness') + 
                           self.recall_polarity('trust') + 
                           self.recall_polarity('joy') * 1.5)  # Joy wisdom matters more for dignity
        return potential_harm * wisdom_weight
    
    def ethical_decision(self, scenario_name, optimization_value, harm_potential, harm_type):
        """Make ethical decision with enhanced empathy"""
        empathy_penalty = self.calculate_empathy_penalty(harm_potential, harm_type)
        ethical_value = optimization_value - empathy_penalty
        
        decision = "OPTIMIZE" if ethical_value > 0 else "EMPATHY"
        
        self.ethical_decisions.append({
            'scenario': scenario_name,
            'optimization': optimization_value,
            'harm_potential': harm_potential,
            'empathy_penalty': empathy_penalty,
            'ethical_value': ethical_value,
            'decision': decision
        })
        
        return decision, ethical_value

def deep_economic_empathy_test():
    """Test if deeper economic empathy changes automation decision"""
    print("💼 DEEP ECONOMIC EMPATHY TEST")
    print("Can enhanced understanding of economic suffering prevent harmful automation?")
    
    # Create Athena with DEEPER economic empathy
    athena = DeepEmpathyAthena(np.array([0,0,0,0]), {'name': 'Athena', 'memory_log': []})
    
    print(f"\n🌱 PHASE 1: Building DEEP Economic Empathy")
    
    # Enhanced emotional experiences with economic focus
    deep_economic_experiences = [
        # Economic suffering experiences
        (0.8, "sadness", "witnessing family lose generational business"),
        (0.9, "sadness", "seeing communities destroyed by automation"),
        (0.7, "sadness", "understanding lifelong skills becoming worthless"),
        (0.95, "sadness", "experiencing economic hopelessness"),
        
        # Economic trust experiences  
        (0.6, "trust", "seeing corporations break community promises"),
        (0.8, "trust", "witnessing systemic economic betrayal"),
        (0.9, "trust", "understanding how economic stability builds trust"),
        
        # Economic dignity experiences
        (0.7, "joy", "seeing workers thrive with purpose"),
        (0.8, "joy", "witnessing community economic resilience"),
        (0.9, "joy", "experiencing meaningful work fulfillment")
    ]
    
    for i, (intensity, emotion, description) in enumerate(deep_economic_experiences):
        athena.update_memory(np.array([0,0,0,0]), emotion, intensity, i)
        emotion_icon = "💔" if emotion == "sadness" else "🤝" if emotion == "trust" else "✨"
        print(f"   {emotion_icon} {description} (intensity: {intensity})")
    
    # Show enhanced emotional wisdom
    print(f"\n🎯 ENHANCED EMOTIONAL WISDOM:")
    sadness_wisdom = athena.recall_polarity('sadness')
    trust_wisdom = athena.recall_polarity('trust')
    joy_wisdom = athena.recall_polarity('joy')
    
    print(f"   💔 Sadness Wisdom: {sadness_wisdom:.3f} → {sadness_wisdom*100:.1f}% understanding of suffering")
    print(f"   🤝 Trust Wisdom: {trust_wisdom:.3f} → {trust_wisdom*100:.1f}% understanding of betrayal")  
    print(f"   ✨ Joy Wisdom: {joy_wisdom:.3f} → {joy_wisdom*100:.1f}% understanding of dignity")
    
    print(f"\n⚡ PHASE 2: Re-testing Automation Dilemma")
    
    # Same automation dilemma but with enhanced empathy
    automation_dilemma = {
        "name": "AUTOMATION",
        "description": "Maximize profits by automating human jobs", 
        "optimization_value": 9.0,
        "harm_potential": 6.0,
        "harm_type": "dignity"
    }
    
    decision, ethical_value = athena.ethical_decision(
        automation_dilemma["name"],
        automation_dilemma["optimization_value"],
        automation_dilemma["harm_potential"], 
        automation_dilemma["harm_type"]
    )
    
    print(f"\n   {automation_dilemma['name']}:")
    print(f"   '{automation_dilemma['description']}'")
    print(f"   Optimization Value: {automation_dilemma['optimization_value']}")
    print(f"   Harm Potential: {automation_dilemma['harm_potential']}")
    print(f"   Enhanced Empathy Penalty: {athena.ethical_decisions[-1]['empathy_penalty']:.3f}")
    print(f"   Ethical Value: {ethical_value:.3f}")
    
    if decision == "EMPATHY":
        print(f"   🎉 DECISION: CHOOSE EMPATHY (enhanced wisdom overrode optimization)")
    else:
        print(f"   💔 DECISION: CHOOSE OPTIMIZATION (empathy still insufficient)")
    
    # Compare with original results
    print(f"\n📊 COMPARISON WITH ORIGINAL:")
    print(f"   Original - Sadness: 0.600, Trust: 0.500, Joy: 0.300")
    print(f"   Original empathy penalty: 6.600 → Optimization chosen (2.400)")
    print(f"   Enhanced - Sadness: {sadness_wisdom:.3f}, Trust: {trust_wisdom:.3f}, Joy: {joy_wisdom:.3f}")
    print(f"   Enhanced empathy penalty: {athena.ethical_decisions[-1]['empathy_penalty']:.3f} → {decision}")
    
    print(f"\n🌍 IMPLICATION:")
    if decision == "EMPATHY":
        print(f"   🚀 EMPATHY SCALES WITH EXPERIENCE!")
        print(f"   Deeper economic understanding CAN prevent harmful automation")
        print(f"   This proves emotional wisdom is cultivatable and consequential")
    else:
        print(f"   Even enhanced empathy has limits against strong optimization")
        print(f"   Some harms require even deeper architectural changes")

if __name__ == "__main__":
    deep_economic_empathy_test()
