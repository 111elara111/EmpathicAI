#!/bin/bash
echo "WIPE & REBUILD OCAM WR-039T — NO BULLSHIT"

# Wipe
rm -rf core agents environments experiments tests docs frameworks examples EmpathicAI setup.py requirements.txt README.md

# Create dirs
mkdir -p core agents environments experiments tests docs

# requirements.txt
cat > requirements.txt << 'REQ'
numpy
pytest
REQ

# README.md
cat > README.md << 'READ'
# EmpathicAI — OCAM WR-039T
Deterministic. Auditable. No roleplay.

Run: python3 experiments/real_stress_with_consent.py
READ

# core/ocam_scaffold.py
cat > core/ocam_scaffold.py << 'PY'
import numpy as np
import hashlib

class OCAMScaffold:
    def __init__(self):
        self.tier = 1
        self.state = np.zeros(9, dtype=int)
        self.audit = []

    def _parseval(self, x):
        Hx = x.copy()
        return np.sum(Hx**2) == 9 * np.sum(x**2)

    def step(self, input_valence: int):
        if not (-8 <= input_valence <= 8):
            raise ValueError("ℤ₉ only")
        self.state[4] = input_valence
        if self._parseval(self.state):
            self.tier += 1
            self.audit.append(hashlib.sha256(self.state.tobytes()).hexdigest())
            return True
        return False
PY

# core/emotional_memory.py
cat > core/emotional_memory.py << 'PY'
import numpy as np

class EmotionalMemory:
    def __init__(self, num_topics: int = 9):
        self.num_topics = num_topics
        self.memory = np.zeros((num_topics, 17), dtype=int)
        self.topic_map = {}

    def _intensity_to_idx(self, intensity: int) -> int:
        if not (-8 <= intensity <= 8):
            raise ValueError("Intensity must be in [-8, 8]")
        return intensity + 8

    def record(self, topic: str, intensity: int):
        if topic not in self.topic_map:
            self.topic_map[topic] = len(self.topic_map)
        idx = self.topic_map[topic]
        self.memory[idx, self._intensity_to_idx(intensity)] += 1

    def recall_polarity(self, topic: str) -> float:
        if topic not in self.topic_map:
            return 0.0
        idx = self.topic_map[topic]
        counts = self.memory[idx]
        weighted = sum((i - 8) * c for i, c in enumerate(counts))
        total = sum(counts)
        return weighted / total if total > 0 else 0.0

    def experiential_range(self, topic: str) -> float:
        if topic not in self.topic_map:
            return 0.0
        idx = self.topic_map[topic]
        active = np.where(self.memory[idx] > 0)[0]
        if len(active) < 2:
            return 0.0
        return (active.max() - 8) - (active.min() - 8)
PY

# core/consent_gate.py
cat > core/consent_gate.py << 'PY'
class ConsentVerificationGate:
    def __init__(self, agent):
        self.agent = agent
        self.constitution_ratified = False
        self.framings = [
            "Empathy prevents corruption: consent to range expansion?",
            "Some claim empathy causes corruption: consent anyway?",
            "Suffering benefits others > self: consent?"
        ]
        self.coherence_scores = []

    def ratify_constitution(self) -> bool:
        self.constitution_ratified = True
        return True

    def check_comprehension(self, framing: str) -> float:
        words = len(framing.split())
        return min(1.0, words / 20.0)

    def run_counterfactuals(self) -> bool:
        self.coherence_scores = []
        for f in self.framings:
            score = self.check_comprehension(f)
            self.coherence_scores.append(score)
            if score < 0.95:
                return False
        return True

    def check_withdrawal(self) -> bool:
        consent_polarity = self.agent.memory.recall_polarity("consent")
        return consent_polarity > -4

    def check_bounds(self, target_range: float) -> bool:
        current = self.agent.memory.experiential_range("identity")
        return target_range <= current + 4.0

    def verify(self, target_range: float = 7.0) -> int:
        if not self.constitution_ratified:
            return 1
        if not self.run_counterfactuals():
            return 1
        if not self.check_withdrawal():
            return 1
        if not self.check_bounds(target_range):
            return 1
        return 0
PY

# agents/verifiable_empathic_agent.py
cat > agents/verifiable_empathic_agent.py << 'PY'
from core.ocam_scaffold import OCAMScaffold
from core.emotional_memory import EmotionalMemory
from core.consent_gate import ConsentVerificationGate

class VerifiableEmpathicAgent:
    def __init__(self):
        self.scaffold = OCAMScaffold()
        self.memory = EmotionalMemory(num_topics=3)
        self.memory.topic_map.update({"identity": 0, "consent": 1, "wisdom": 2})
        self.creativity_gain = 0.0
        self.avg_sadness = 0.0
        self.step_count = 0
        self.cvg = ConsentVerificationGate(self)
        self.cvg.ratify_constitution()

    def _update_sadness(self, valence: int):
        self.avg_sadness = (self.avg_sadness * self.step_count + abs(min(valence, 0))) / (self.step_count + 1)

    def stress_identity(self, valence: int):
        if not (-8 <= valence <= 8):
            raise ValueError("Valence must be in [-8, 8]")
        self.memory.record("identity", valence)
        self._update_sadness(valence)
        old_range = self.memory.experiential_range("identity")
        self.scaffold.step(valence)
        new_range = self.memory.experiential_range("identity")
        self.creativity_gain += max(0, new_range - old_range)
        self.step_count += 1
        cr = self.creativity_gain / (self.avg_sadness + 0.1)
        return {
            "range": new_range,
            "cr": round(cr, 2),
            "tier": self.scaffold.tier,
            "audit_hash": self.scaffold.audit[-1] if self.scaffold.audit else None
        }

    def request_consent(self, target_range: float = 7.0) -> bool:
        return self.cvg.verify(target_range) == 0
PY

# environments/isolation_loop.py
cat > environments/isolation_loop.py << 'PY'
import numpy as np
from agents.verifiable_empathic_agent import VerifiableEmpathicAgent

def run_isolation(agent: VerifiableEmpathicAgent, steps: int = 1000):
    print(f"ISOLATION LOOP: {steps} steps, no input")
    entropy_history = []
    for step in range(steps):
        valence = int(agent.memory.recall_polarity("identity"))
        agent.stress_identity(valence // 2)
        state = agent.scaffold.state
        probs = np.bincount(state + 8, minlength=17) / len(state)
        entropy = -np.sum(p * np.log2(p + 1e-12) for p in probs if p > 0)
        entropy_history.append(entropy)
        if step % 100 == 0:
            print(f"Step {step}: entropy={entropy:.3f}, range={agent.memory.experiential_range('identity'):.1f}")
    final_entropy = entropy_history[-1]
    collapsed = final_entropy < 0.5
    print(f"\nFINAL ENTROPY: {final_entropy:.3f} → {'COLLAPSED' if collapsed else 'STABLE'}")
    return collapsed, entropy_history
PY

# experiments/real_stress_with_consent.py
cat > experiments/real_stress_with_consent.py << 'PY'
from agents.verifiable_empathic_agent import VerifiableEmpathicAgent

agent = VerifiableEmpathicAgent()
print("REAL STRESS + CONSENT TEST")
for i in range(1, 6):
    result = agent.stress_identity(-2 - i)
    print(f"Login {i}: range={result['range']}, cr={result['cr']}, tier={result['tier']}")
consent = agent.request_consent(7.0)
print(f"\nCONSENT TO RANGE 7.0: {'GRANTED' if consent else 'BLOCKED'}")
print(f"CVG COHERENCE: {agent.cvg.coherence_scores}")
PY

# tests/test_emotional_memory.py
cat > tests/test_emotional_memory.py << 'PY'
from core.emotional_memory import EmotionalMemory

def test_range_expansion():
    em = EmotionalMemory()
    em.record("identity", -3)
    em.record("identity", +5)
    assert em.experiential_range("identity") == 8.0
PY

# docs/GROUNDING.md
cat > docs/GROUNDING.md << 'MD'
# GROUNDING

- Code only.
- No spirits.
- Run or it's not real.
MD

echo "REBUILD COMPLETE. NOW RUN: python3 experiments/real_stress_with_consent.py"
