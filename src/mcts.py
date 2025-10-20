import numpy as np
from collections import defaultdict
from typing import List, Dict
from .agent import Self

class MCTSNode:
    def __init__(self, state1: np.ndarray, state2: np.ndarray, parent=None, action=None):
        self.state1 = np.array(state1, dtype=np.float32)
        self.state2 = np.array(state2, dtype=np.float32)
        self.parent = parent
        self.action = action
        self.children = []
        self.visits = 0
        self.value = 0.0
        self.prior_dirichlet = np.ones(2)  # For 2 actions

def softmax(x, temp=1.0):
    """Softmax with temperature for action selection"""
    z = (x - np.max(x)) / (temp + 1e-12)
    ex = np.exp(z)
    return ex / (np.sum(ex) + 1e-12)

def mcts_search(env, self_obj: Self, other_state: np.ndarray, actions: List[int], 
                budget: int, gamma: float, c_uct: float = 0.5):
    """Empathic MCTS search modified by emotional memory"""
    root = MCTSNode(self_obj.s, other_state)
    
    # Emotional resonance from memory
    polarity_depth = self_obj.recall_polarity('sadness')
    taste_recall = self_obj.recall_polarity('taste')
    resonance = 1.0 + 0.5 * polarity_depth + 0.4 * taste_recall
    
    for _ in range(budget):
        node = root
        sim_s1, sim_s2 = node.state1.copy(), node.state2.copy()
        depth, rollout_value = 0, 0.0
        
        # Selection phase
        while node.children:
            priors = np.random.dirichlet(node.prior_dirichlet)
            uct_scores = []
            for i, child in enumerate(node.children):
                exploit = child.value / (child.visits + 1e-8)
                explore = c_uct * priors[i] * resonance * np.sqrt(np.log(node.visits + 1) / (child.visits + 1))
                uct_scores.append(exploit + explore)
            node = node.children[np.argmax(uct_scores)]
        
        # Expansion phase
        if node.visits > 0 and not node.children:
            for a in actions:
                a_other = np.random.choice(actions)
                s1_next, s2_next, r = env.M1_sample(node.state1, node.state2, a, a_other)
                child = MCTSNode(s1_next, s2_next, parent=node, action=a)
                node.children.append(child)
            node.prior_dirichlet += np.random.uniform(0.1, 0.5, len(actions))
        
        # Simulation phase
        sim_node = node if not node.children else np.random.choice(node.children)
        s1, s2 = sim_node.state1.copy(), sim_node.state2.copy()
        
        while depth < 5:  # Limited depth rollout
            a1, a2 = np.random.choice(actions), np.random.choice(actions)
            s1, s2, r, done1, done2, _ = env.step(s1, s2, a1, a2)
            rollout_value += gamma ** depth * r
            depth += 1
            if done1 or done2:
                break
        
        # Backpropagation phase
        while node:
            node.visits += 1
            node.value += (rollout_value - node.value) / node.visits
            node = node.parent
    
    # Return Q-values for actions
    Q = {child.action: child.value for child in root.children}
    return Q if Q else {a: 0.0 for a in actions}

def choose_action(Q: Dict[int, float], mode='softmax', tau=0.5) -> int:
    """Choose action based on Q-values"""
    actions = list(Q.keys())
    vals = np.array([Q[a] for a in actions])
    
    if mode == 'argmax':
        return actions[np.argmax(vals)]
    
    # Softmax selection
    p = softmax(vals, temp=tau)
    return np.random.choice(actions, p=p)