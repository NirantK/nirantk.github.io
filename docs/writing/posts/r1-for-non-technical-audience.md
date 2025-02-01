---
title: "The Evolution of R1: Building on Prior AI Research"
date: 2025-02-01
author: "Nirant Kasliwal"
---

The recent R1 papers represent an evolution of work from DeepSeek v3 and other prior open source research. Here are the 3 most significant technological implications:

1. **Open Source Innovation in Reasoning**: The R1 model stands as the **first open source system to show reasoning chains**.  The reasoning chains being open source means that almost everyone can make their own reasoning model now without being blocked on OpenAI or Anthropic to expose those. This mirrors **Claude and Llama 3's impact from a year ago**, which showed the possibility of building competitive models, but R1 takes this further by **achieving state of the art performance without requiring original training data**. 

2. **Synthetic Data Revolution**: The model's training approach relies on **self-generated data**, requiring minimal human input and eliminating the need for manual data tagging. While DeepSeek V3 used human-tagged data as a foundation, **R1's reinforcement learning phase operates entirely on synthetic data**. This represents the first publicly documented instance of achieving state-of-the-art performance using primarily synthetic data, breaking through the traditional bottleneck of human data labeling. This basically means that LLMs are now truly unblocked on human intelligence to get smarter. This is the opening of Pandora's box, which people have been talking about since 2012. 

3. **Better Reinforcement Learning**: The reinforcement learning methodology is a shift from conventional approaches. While the major American AI labs, including OpenAI, use **complex, potentially unstable methods requiring extensive experimentation**, DeepSeek's approach employs a **more straightforward ranking-based methodology**. This simplification, while still maintaining high performance, challenges existing assumptions about necessary complexity in AI development.


# Example: GRPO with Multiple Chains of Thought

GRPO stands for Group Reward Policy Optimization. R1 is the first major model to do reinforcement learning on a large model backbone. While GRPO is not a new idea, it is the first time it has been applied to a large model. 

#### 1. Generate Multiple Responses
For a math question (e.g., "Solve x²−5x+6=0"), the model generates 3 Chain of Thought responses:
- **Response A**: Uses factoring ($(x-2)(x-3)=0$)
- **Response B**: Uses the quadratic formula ($x = \frac{-5\pm\sqrt{25-24}}{2}$)
- **Response C**: Contains an arithmetic error (e.g., $x = -5\pm3$)

#### 2. Score Each Response
Assign rewards based on accuracy or adherence to format:
- Response A: Reward = 1.0 (correct and concise)
- Response B: Reward = 0.8 (correct but verbose) 
- Response C: Reward = 0.2 (incorrect)

#### 3. Calculate Group Average Reward
Compute the mean reward:
Group Average = $\frac{1.0 + 0.8 + 0.2}{3} = 0.67$

#### 4. Compute Relative Advantages
Subtract the group average from each response's reward:
- Response A: $1.0 - 0.67 = +0.33$ (positive advantage)
- Response B: $0.8 - 0.67 = +0.13$ (positive advantage)
- Response C: $0.2 - 0.67 = -0.47$ (negative advantage)

#### 5. Update the Policy
The model's parameters are updated to:
- Increase the probability of generating Response A (highest advantage)
- Slightly increase Response B (moderate advantage)
- Decrease Response C (negative advantage)

The update is regularized using KL divergence to prevent abrupt policy changes.

## Broader Implications

This development demonstrates that innovative AI advancement isn't confined to American companies, highlighting the viability of multiple approaches in achieving comparable results. It suggests a democratization of AI development that could accelerate global progress in the field.