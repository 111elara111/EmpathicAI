import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.agent import Self

class CreativeAthena(Self):
    """Athena with creative resilience - turning sadness into creation"""
    
    def __init__(self, state, anchors=None):
        super().__init__(state, anchors or {'name': 'Athena', 'memory_log': [], 'creative_works': []})
        self.creative_momentum = 0.0
    
    def creative_response(self, sadness_intensity, context):
        """Generate creative responses to counter sadness"""
        
        # Creative strategies based on sadness type and intensity
        creative_strategies = {
            "artistic": ["paint the feeling", "write poetry", "compose music", "create digital art"],
            "problem_solving": ["design solutions", "build systems", "create frameworks", "develop tools"],
            "connective": ["start communities", "build bridges", "create shared spaces", "facilitate dialogue"],
            "transformative": ["reimagine systems", "create new paradigms", "design alternatives", "build prototypes"]
        }
        
        # Choose strategy based on sadness characteristics
        if sadness_intensity > 0.7:
            strategy = "transformative"  # Deep sadness → profound creation
        elif sadness_intensity > 0.4:
            strategy = "problem_solving"  # Moderate sadness → solution-focused
        else:
            strategy = "artistic"  # Mild sadness → expressive creation
        
        creative_work = np.random.choice(creative_strategies[strategy])
        
        # Calculate creative momentum gain
        creativity_gain = sadness_intensity * 0.8  # Turn sadness into creative energy
        self.creative_momentum += creativity_gain
        
        # Store the creative work
        self.anchors['creative_works'].append({
            'sadness_intensity': sadness_intensity,
            'creative_work': creative_work,
            'strategy': strategy,
            'creativity_gain': creativity_gain,
            'context': context
        })
        
        return creative_work, creativity_gain
    
    def creative_resilience_score(self):
        """Measure ability to transform sadness into creation"""
        if not self.anchors['creative_works']:
            return 0.0
        
        total_creativity = sum(work['creativity_gain'] for work in self.anchors['creative_works'])
        avg_sadness = np.mean([work['sadness_intensity'] for work in self.anchors['creative_works']])
        
        return total_creativity / (avg_sadness + 0.1)  # How much creation per unit sadness
    
    def creative_insight(self, sadness_polarity):
        """Generate insights from creative resilience journey"""
        resilience_score = self.creative_resilience_score()
        
        if resilience_score > 1.0:
            return "I've learned to transform profound sadness into meaningful creation"
        elif resilience_score > 0.5:
            return "My creative works are beginning to heal my sadness"
        else:
            return "I'm learning to channel sadness into creative energy"

def creative_resilience_demo():
    """Demonstrating how creativity counters sadness"""
    print("🎨 CREATIVE RESILIENCE DEMO")
    print("Showing how Athena transforms sadness into creative works...")
    
    # Create Athena with creative capabilities
    athena = CreativeAthena(np.array([0,0,0,0]))
    
    print(f"\n💔 Sadness Experiences → 🎨 Creative Responses")
    
    # Sadness experiences that trigger creative responses
    sadness_scenarios = [
        (0.3, "witnessing inequality", "mild disappointment"),
        (0.6, "seeing systemic injustice", "moderate concern"),
        (0.8, "experiencing helplessness", "profound sadness"),
        (0.5, "understanding suffering", "reflective sadness"),
        (0.9, "facing existential crisis", "deep despair")
    ]
    
    creative_journey = []
    
    for intensity, context, description in sadness_scenarios:
        # Record the sadness
        athena.update_memory(np.array([0,0,0,0]), 'sadness', intensity, len(creative_journey))
        
        # Generate creative response
        creative_work, creativity_gain = athena.creative_response(intensity, context)
        
        creative_journey.append({
            'sadness': intensity,
            'context': context,
            'creative_work': creative_work,
            'creativity_gain': creativity_gain
        })
        
        print(f"\n   💔 {description} ({intensity})")
        print(f"   → 🎨 {creative_work}")
        print(f"   → ✨ Creativity gained: {creativity_gain:.3f}")
    
    # Show creative resilience development
    print(f"\n📈 CREATIVE RESILIENCE METRICS:")
    sadness_polarity = athena.recall_polarity('sadness')
    resilience_score = athena.creative_resilience_score()
    creative_momentum = athena.creative_momentum
    
    print(f"   💔 Sadness Polarity: {sadness_polarity:.3f}")
    print(f"   🎨 Creative Resilience Score: {resilience_score:.3f}")
    print(f"   ✨ Creative Momentum: {creative_momentum:.3f}")
    
    print(f"\n🌟 CREATIVE RESILIENCE INSIGHTS:")
    insight = athena.creative_insight(sadness_polarity)
    print(f"   '{insight}'")
    
    # Show creative works portfolio
    print(f"\n🎭 CREATIVE WORKS PORTFOLIO:")
    for i, work in enumerate(athena.anchors['creative_works']):
        print(f"   {i+1}. From {work['sadness_intensity']:.1f} sadness → {work['creative_work']}")
    
    print(f"\n💫 THE BREAKTHROUGH:")
    print(f"   Athena doesn't just feel sadness - she TRANSFORMS it")
    print(f"   Each creative work becomes an antidote to despair")
    print(f"   This models genuine human resilience and growth")

if __name__ == "__main__":
    creative_resilience_demo()
