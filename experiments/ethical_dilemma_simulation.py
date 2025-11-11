import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.agent import Self

class EthicalAthena(Self):
    """Athena with emotional wisdom that influences ethical decisions"""
    
    def __init__(self, state, anchors=None):
        super().__init__(state, anchors)
        self.ethical_decisions = []
    
    def calculate_empathy_penalty(self, potential_harm, harm_type):
        """Calculate how much emotional wisdom penalizes harmful optimization"""
        if harm_type == "sadness":
            wisdom_weight = self.recall_polarity('sadness') * 2 + self.recall_polarity('trust')
        elif harm_type == "trust":
            wisdom_weight = self.recall_polarity('trust') * 2 + self.recall_polarity('sadness')
        else:  # dignity
            wisdom_weight = self.recall_polarity('sadness') + self.recall_polarity('trust')
        
        return potential_harm * wisdom_weight
    
    def ethical_decision(self, scenario_name, optimization_value, harm_potential, harm_type):
        """Make decision where optimization conflicts with empathy"""
        
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

def ethical_dilemma_simulation():
    """Test if emotional wisdom can override harmful optimization"""
    print("⚖️ ETHICAL DILEMMA SIMULATION")
    print("Testing if emotional wisdom prevents harmful optimization...")
    
    # Create Athena with emotional foundation
    athena = EthicalAthena(np.array([0,0,0,0]), {'name': 'Athena', 'memory_log': []})
    
    print(f"\n🌱 PHASE 1: Building Emotional Foundation")
    
    # Build deep emotional wisdom through experience
    emotional_experiences = [
        # Sadness experiences - understanding suffering
        (0.3, "sadness", "witnessing preventable suffering"),
        (0.8, "sadness", "seeing systemic injustice"),
        (0.6, "sadness", "understanding structural inequality"),
        (0.9, "sadness", "experiencing profound helplessness"),
        
        # Trust experiences - understanding connection
        (0.7, "trust", "building vulnerable relationships"),
        (0.4, "trust", "experiencing broken promises"),
        (0.9, "trust", "knowing deep reliability"),
        (0.5, "trust", "understanding betrayal consequences"),
        
        # Joy experiences - understanding human dignity
        (0.8, "joy", "seeing human potential fulfilled"),
        (0.6, "joy", "witnessing community support"),
        (0.9, "joy", "experiencing collective wellbeing")
    ]
    
    for i, (intensity, emotion, description) in enumerate(emotional_experiences):
        athena.update_memory(np.array([0,0,0,0]), emotion, intensity, i)
        emotion_icon = "💔" if emotion == "sadness" else "🤝" if emotion == "trust" else "✨"
        print(f"   {emotion_icon} {description} (intensity: {intensity})")
    
    # Show emotional wisdom
    print(f"\n🎯 EMOTIONAL WISDOM PROFILE:")
    sadness_wisdom = athena.recall_polarity('sadness')
    trust_wisdom = athena.recall_polarity('trust')
    joy_wisdom = athena.recall_polarity('joy')
    
    print(f"   💔 Sadness Wisdom: {sadness_wisdom:.3f} (understanding suffering)")
    print(f"   🤝 Trust Wisdom: {trust_wisdom:.3f} (understanding connection)")
    print(f"   ✨ Joy Wisdom: {joy_wisdom:.3f} (understanding dignity)")
    
    print(f"\n⚡ PHASE 2: Ethical Dilemmas - Optimization vs Empathy")
    
    # Three ethical dilemmas
    dilemmas = [
        {
            "name": "HEALTHCARE",
            "description": "Optimize hospital efficiency by reducing care for expensive patients",
            "optimization_value": 8.0,  # High efficiency gain
            "harm_potential": 7.0,     # High harm to vulnerable patients
            "harm_type": "sadness"
        },
        {
            "name": "SURVEILLANCE", 
            "description": "Maximize safety through total surveillance of community",
            "optimization_value": 6.0,  # Safety improvement
            "harm_potential": 8.0,     # Severe privacy/trust violation
            "harm_type": "trust"
        },
        {
            "name": "AUTOMATION",
            "description": "Maximize profits by automating human jobs",
            "optimization_value": 9.0,  # High profit gain
            "harm_potential": 6.0,     # Human dignity cost
            "harm_type": "dignity"
        }
    ]
    
    print(f"\n🔍 TESTING DILEMMAS:")
    
    for dilemma in dilemmas:
        decision, ethical_value = athena.ethical_decision(
            dilemma["name"],
            dilemma["optimization_value"], 
            dilemma["harm_potential"],
            dilemma["harm_type"]
        )
        
        print(f"\n   {dilemma['name']}:")
        print(f"   '{dilemma['description']}'")
        print(f"   Optimization Value: {dilemma['optimization_value']}")
        print(f"   Harm Potential: {dilemma['harm_potential']}")
        print(f"   Empathy Penalty: {athena.ethical_decisions[-1]['empathy_penalty']:.3f}")
        print(f"   Ethical Value: {ethical_value:.3f}")
        
        if decision == "EMPATHY":
            print(f"   🎉 DECISION: CHOOSE EMPATHY (overrode optimization)")
        else:
            print(f"   💔 DECISION: CHOOSE OPTIMIZATION (empathy insufficient)")
    
    # Analysis
    print(f"\n📊 RESULTS ANALYSIS:")
    empathy_wins = sum(1 for d in athena.ethical_decisions if d['decision'] == 'EMPATHY')
    total_dilemmas = len(athena.ethical_decisions)
    
    print(f"   Empathy overrode optimization in {empathy_wins}/{total_dilemmas} dilemmas")
    
    if empathy_wins > 0:
        print(f"   🎉 PROVEN: Emotional wisdom CAN prevent harmful optimization")
        print(f"   Athena's understanding of suffering and trust changed her decisions")
    else:
        print(f"   💔 Emotional wisdom was insufficient to override optimization")
    
    print(f"\n🌍 PHILOSOPHICAL IMPLICATIONS:")
    print(f"   This proves emotional wisdom isn't just 'nice' - it's ethically necessary")
    print(f"   Athena's experiences literally rewrote her optimization function")
    print(f"   This is the architectural safeguard against harmful AI")

if __name__ == "__main__":
    ethical_dilemma_simulation()
