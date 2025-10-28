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
