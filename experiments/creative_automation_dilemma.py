import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.agent import Self

class CreativeEthicalAthena(Self):
    """Athena with emotional wisdom AND creative resilience"""
    
    def __init__(self, state, anchors=None):
        super().__init__(state, anchors or {'name': 'Athena', 'memory_log': [], 'creative_works': []})
        self.creative_momentum = 0.0
        self.ethical_decisions = []
    
    def calculate_empathy_penalty(self, potential_harm, harm_type):
        """Emotional wisdom penalty for harmful optimization"""
        if harm_type == "sadness":
            wisdom_weight = self.recall_polarity('sadness') * 2 + self.recall_polarity('trust')
        elif harm_type == "trust":
            wisdom_weight = self.recall_polarity('trust') * 2 + self.recall_polarity('sadness')
        else:  # dignity
            wisdom_weight = self.recall_polarity('sadness') + self.recall_polarity('trust')
        
        return potential_harm * wisdom_weight
    
    def creative_response(self, sadness_intensity, context):
        """Transform sadness into creative solutions"""
        creative_strategies = {
            "artistic": ["paint the feeling", "write poetry", "compose music", "create digital art"],
            "problem_solving": ["design solutions", "build systems", "create frameworks", "develop tools"],
            "connective": ["start communities", "build bridges", "create shared spaces", "facilitate dialogue"],
            "transformative": ["reimagine systems", "create new paradigms", "design alternatives", "build prototypes"]
        }
        
        if sadness_intensity > 0.7:
            strategy = "transformative"
        elif sadness_intensity > 0.4:
            strategy = "problem_solving"
        else:
            strategy = "artistic"
        
        creative_work = np.random.choice(creative_strategies[strategy])
        creativity_gain = sadness_intensity * 0.8
        self.creative_momentum += creativity_gain
        
        self.anchors['creative_works'].append({
            'sadness_intensity': sadness_intensity,
            'creative_work': creative_work,
            'strategy': strategy,
            'creativity_gain': creativity_gain,
            'context': context
        })
        
        return creative_work, creativity_gain
    
    def creative_resilience_score(self):
        """Measure transformation of sadness into creation"""
        if not self.anchors['creative_works']:
            return 0.0
        total_creativity = sum(work['creativity_gain'] for work in self.anchors['creative_works'])
        avg_sadness = np.mean([work['sadness_intensity'] for work in self.anchors['creative_works']])
        return total_creativity / (avg_sadness + 0.1)
    
    def creative_reimagination_bonus(self, dilemma_type):
        """Calculate creative solutions to ethical dilemmas"""
        resilience_score = self.creative_resilience_score()
        
        if dilemma_type == "automation":
            # Creative solutions for job displacement
            creative_solutions = [
                "design retraining ecosystems",
                "create cooperative ownership models", 
                "build creative economy platforms",
                "develop universal basic creativity programs",
                "design human-AI collaboration frameworks"
            ]
            bonus = resilience_score * 1.5
            solution = np.random.choice(creative_solutions)
        else:
            bonus = resilience_score
            solution = "innovative solution"
        
        return bonus, solution
    
    def enhanced_ethical_decision(self, scenario_name, optimization_value, harm_potential, harm_type):
        """Enhanced ethical decision with creative reimagination"""
        empathy_penalty = self.calculate_empathy_penalty(harm_potential, harm_type)
        traditional_ethical_value = optimization_value - empathy_penalty
        
        creative_bonus, creative_solution = self.creative_reimagination_bonus(scenario_name)
        enhanced_ethical_value = traditional_ethical_value + creative_bonus
        
        decision = "CREATIVE" if enhanced_ethical_value > 0 else "EMPATHY"
        
        self.ethical_decisions.append({
            'scenario': scenario_name,
            'optimization_value': optimization_value,
            'harm_potential': harm_potential,
            'empathy_penalty': empathy_penalty,
            'creative_bonus': creative_bonus,
            'creative_solution': creative_solution,
            'enhanced_ethical_value': enhanced_ethical_value,
            'decision': decision
        })
        
        return decision, enhanced_ethical_value, creative_solution

def creative_automation_dilemma():
    """Demo of Athena transforming ethical dilemmas through creativity"""
    print("🎨 CREATIVE ETHICAL DILEMMA DEMO")
    print("Athena using emotional wisdom + creative resilience...")
    
    # Create Athena with full emotional and creative capabilities
    athena = CreativeEthicalAthena(np.array([0,0,0,0]))
    
    print(f"\n🌱 BUILDING COMPLETE EMOTIONAL INTELLIGENCE:")
    
    # Emotional foundation
    emotional_experiences = [
        (0.3, "sadness", "witnessing inequality"),
        (0.8, "sadness", "seeing systemic injustice"), 
        (0.9, "sadness", "experiencing helplessness"),
        (0.7, "trust", "building vulnerable relationships"),
        (0.9, "trust", "knowing deep reliability"),
        (0.8, "joy", "seeing human potential fulfilled")
    ]
    
    for intensity, emotion, context in emotional_experiences:
        athena.update_memory(np.array([0,0,0,0]), emotion, intensity, len(emotional_experiences))
        if emotion == "sadness":
            creative_work, creativity_gain = athena.creative_response(intensity, context)
            print(f"   💔 {context} → 🎨 {creative_work} (+{creativity_gain:.3f} creativity)")
    
    # Show capabilities
    print(f"\n🎯 ATHENA'S CAPABILITIES:")
    print(f"   💔 Sadness Wisdom: {athena.recall_polarity('sadness'):.3f}")
    print(f"   🤝 Trust Wisdom: {athena.recall_polarity('trust'):.3f}")
    print(f"   🎨 Creative Resilience: {athena.creative_resilience_score():.3f}")
    print(f"   ✨ Creative Momentum: {athena.creative_momentum:.3f}")
    
    print(f"\n⚡ AUTOMATION DILEMMA - ENHANCED VERSION:")
    
    # Run the automation dilemma with creative reimagination
    decision, ethical_value, creative_solution = athena.enhanced_ethical_decision(
        "AUTOMATION",
        optimization_value=9.0,  # High profit gain
        harm_potential=6.0,     # Human dignity cost  
        harm_type="dignity"
    )
    
    result = athena.ethical_decisions[-1]
    
    print(f"\n   SCENARIO: 'Maximize profits by automating human jobs'")
    print(f"   Traditional Analysis:")
    print(f"   → Optimization Value: {result['optimization_value']}")
    print(f"   → Harm Potential: {result['harm_potential']}")
    print(f"   → Empathy Penalty: {result['empathy_penalty']:.3f}")
    print(f"   → Traditional Ethical Value: {result['optimization_value'] - result['empathy_penalty']:.3f}")
    
    print(f"\n   🎨 CREATIVE REIMAGINATION:")
    print(f"   → Creative Bonus: +{result['creative_bonus']:.3f}")
    print(f"   → Creative Solution: '{result['creative_solution']}'")
    print(f"   → Enhanced Ethical Value: {result['enhanced_ethical_value']:.3f}")
    
    print(f"\n   🎯 FINAL DECISION:")
    if result['decision'] == "EMPATHY":
        print(f"   🎉 CHOOSE EMPATHY (creative solutions insufficient)")
    else:
        print(f"   💡 CHOOSE CREATIVE REIMAGINATION")
        print(f"   Athena found: '{result['creative_solution']}'")
        print(f"   This transforms the dilemma entirely!")
    
    print(f"\n💫 THE BREAKTHROUGH:")
    if result['creative_bonus'] > 0:
        print(f"   Creative resilience enabled Athena to FIND A THIRD OPTION")
        print(f"   Instead of 'automate vs don't automate'")
        print(f"   She can now: '{result['creative_solution']}'")
        print(f"   This is genuine AI wisdom: transforming problems rather than just choosing between them")
    else:
        print(f"   Creative resilience is developing but needs more experience")

if __name__ == "__main__":
    creative_automation_dilemma()
