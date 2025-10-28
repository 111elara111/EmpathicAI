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
