# pybandit

A Python library for all popular multiarmed bandit algorithms.


##Roadmap

The following algorithms are currently being explored before we set a roadmap for the first release.

1. Epsilon Bandit:
    1. Epsilon-greedy strategy (done)
    2. Epsilon-first strategy (in progress)
    3. Epsilon-decreasing strategy
    4. Epsilon-adaptive strategy
2. Bayesian Bandit
    1. Thompson Sampling
3. Contextual Bandit
    1. Linear Classifier
        1. LinUCB (Upper Confidence Bound) algorithm:
        2. LinRel (Linear Associative Reinforcement Learning) algorithm:
    2. Non-linear Classifier
        1. UCBogram algorithm
        2. NeuralBandit algorithm
        3. KernelUCB algorithm
        4. Bandit Forest algorithm
    3. Constrained
        1. UCB-ALP algorithm
    4. Greedy
        1. Contextual-Epsilon-greedy strategy
4. Adverserial Bandit
5. Dueling Bandit
6. Collaborative Bandit
    1. COFIBA
    