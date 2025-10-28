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
