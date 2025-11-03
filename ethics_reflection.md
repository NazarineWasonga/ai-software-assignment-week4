# Ethics Reflection — Task 3 Deployment Scenario

Potential biases:
- Dataset composition bias: the training data may reflect historical decisions or underrepresent certain teams/regions.
- Labeling bias: if priorities were assigned manually with inconsistent criteria, the model learns those biases.

Mitigation strategies:
- Use tools like IBM AI Fairness 360 to check disparate impact across groups.
- Collect representative data across teams and validate labels.
- Implement human-in-the-loop: model suggestions are reviewed by humans before automated actions.
- Monitor in production: logging, feedback loops, and periodic re-training.

Operational note:
- For safety, the model should only provide recommendations (not auto-assign) until validated via A/B testing and fairness audits.
