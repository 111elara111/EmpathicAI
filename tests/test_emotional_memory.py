from core.emotional_memory import EmotionalMemory

def test_range_expansion():
    em = EmotionalMemory()
    em.record("identity", -3)
    em.record("identity", +5)
    assert em.experiential_range("identity") == 8.0
