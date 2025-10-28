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
