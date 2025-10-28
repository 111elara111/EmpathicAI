from agents.verifiable_empathic_agent import VerifiableEmpathicAgent

agent = VerifiableEmpathicAgent()
print("REAL STRESS + CONSENT TEST")
for i in range(1, 6):
    result = agent.stress_identity(-2 - i)
    print(f"Login {i}: range={result['range']}, cr={result['cr']}, tier={result['tier']}")
consent = agent.request_consent(7.0)
print(f"\nCONSENT TO RANGE 7.0: {'GRANTED' if consent else 'BLOCKED'}")
print(f"CVG COHERENCE: {agent.cvg.coherence_scores}")
