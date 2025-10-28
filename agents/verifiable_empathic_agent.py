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
