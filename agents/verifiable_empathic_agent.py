from fractions import Fraction
from core.ocam_scaffold import OCAMScaffold
from core.emotional_memory import EmotionalMemory
from core.consent_gate import ConsentVerificationGate
from core.integer_path import IntegerPathArithmetic

class VerifiableEmpathicAgent:
    def __init__(self):
        self.scaffold = OCAMScaffold()
        self.memory = EmotionalMemory(num_topics=3)
        self.memory.topic_map.update({"identity": 0, "consent": 1, "wisdom": 2})
        self.lda = IntegerPathArithmetic()
        self.creativity_gain = self.lda.add(0, 0)
        self.avg_sadness = self.lda.add(0, 0)
        self.step_count = 0
        self.cvg = ConsentVerificationGate(self)
        self.cvg.ratify_constitution()

    def _update_sadness(self, valence: int):
        abs_sad = abs(min(valence, 0))
        self.avg_sadness = self.lda.div(
            self.lda.add(self.lda.add(self.avg_sadness, self.step_count), abs_sad),
            self.step_count + 1
        )

    def stress_identity(self, valence: int):
        if not (-8 <= valence <= 8):
            raise ValueError("Valence must be in [-8, 8]")
        self.memory.record("identity", valence)
        old_range = self.memory.experiential_range("identity")
        advanced = self.scaffold.step(valence)
        new_range = self.memory.experiential_range("identity")
        if advanced:
            self.creativity_gain = self.lda.add(self.creativity_gain, new_range - old_range)
        self.step_count += 1
        cr = self.lda.div(self.creativity_gain, self.lda.add(self.avg_sadness, Fraction(1, 10)))
        return {
            "range": new_range,
            "cr": str(cr),
            "tier": self.scaffold.tier,
            "advanced": advanced
        }

    def request_consent(self, target_range: float = 7.0) -> bool:
        return self.cvg.verify(target_range) == 0

    def _compute_cr(self):
        return self.lda.div(self.creativity_gain, self.lda.add(self.avg_sadness, Fraction(1, 10)))
