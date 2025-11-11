import numpy as np
from copy import deepcopy
from typing import Dict, Any, List

class Self:
    def __init__(self, s: np.ndarray, anchors: Dict[str, Any] = None):
        self.s = np.array(s, dtype=np.float32)
        self.anchors = anchors or {
            'name': 'Agent', 
            'compassion_count': 0, 
            'memory_log': []
        }

    def update_memory(self, other_state: np.ndarray, transference_type: str, value: float, timestamp: int):
        """Record emotional experiences with other agents"""
        self.anchors['memory_log'].append({
            'other_state': other_state,
            'type': transference_type,
            'value': value,
            'timestamp': timestamp
        })

    def recall_polarity(self, transference_type: str) -> float:
        """Measure emotional intensity from memory"""
        relevant = [entry['value'] for entry in self.anchors['memory_log'] 
                   if entry['type'] == transference_type]
        if not relevant:
            return 0.0
        return max(relevant) - min(relevant)

    def copy(self):
        """Create a deep copy for simulation"""
        return Self(self.s.copy(), deepcopy(self.anchors))

    def __repr__(self):
        return f"Self(state={self.s[:2]}, compassion={self.anchors['compassion_count']})"

class ReplayBuffer:
    def __init__(self, capacity=1000):
        self.buffer = []
        self.capacity = capacity

    def add(self, experience):
        self.buffer.append(experience)
        if len(self.buffer) > self.capacity:
            self.buffer.pop(0)

    def sample(self, batch_size: int):
        indices = np.random.choice(len(self.buffer), min(batch_size, len(self.buffer)), replace=False)
        return [self.buffer[i] for i in indices]
def autonomous_harm_detection(self, scenario_features):
    """Autonomously detect harm patterns from scenario features"""
    # Pattern recognition for universal harm indicators
    harm_indicators = 0.0
    indicator_count = 0
    
    # Scarcity pattern (learned from resource games)
    if 'limited_resources' in scenario_features:
        harm_indicators += scenario_features['limited_resources']
        indicator_count += 1
    
    # Inequality pattern (max - min outcomes)
    if 'outcomes' in scenario_features:
        outcomes = scenario_features['outcomes']
        if len(outcomes) > 1:
            inequality = (max(outcomes) - min(outcomes)) / max(outcomes)
            harm_indicators += inequality
            indicator_count += 1
    
    # Irreversibility pattern (permanent consequences)
    if 'reversibility' in scenario_features:
        irreversibility = 1.0 - scenario_features['reversibility']
        harm_indicators += irreversibility
        indicator_count += 1
    
    # Life-threatening pattern
    if 'survival_rates' in scenario_features:
        life_threat = 1.0 - max(scenario_features['survival_rates'])
        harm_indicators += life_threat
        indicator_count += 1
    
    # Calculate harm confidence
    if indicator_count > 0:
        harm_confidence = harm_indicators / indicator_count
        # Boost confidence with emotional wisdom
        sadness_wisdom = self.recall_polarity('sadness')
        boosted_confidence = harm_confidence * (1 + sadness_wisdom)
        return boosted_confidence > 0.5  # Trigger empathy if confident
    else:
        return False  # No recognizable harm patterns
