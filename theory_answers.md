# Theory Answers — Week 4

Q1: How AI-driven code generation tools reduce development time and their limitations
- Benefits:
  - Suggest boilerplate, accelerate common patterns, reduce keystrokes.
  - Provide quick prototypes, help with API usage, and can surface best-practice idioms.
  - Assist with naming, docstrings, and unit-test sketches.
- Limitations:
  - Can generate incorrect or insecure code; suggestions need human review.
  - May propagate biases or anti-patterns learned from training data.
  - Not context-aware for high-level architecture; limited long-term project understanding.

Q2: Compare supervised vs unsupervised learning in automated bug detection
- Supervised:
  - Uses labeled historical bug reports to classify new issues (bug/not bug, severity).
  - Strong when labeled examples exist; provides interpretable metrics.
- Unsupervised:
  - Useful for anomaly detection (novel crashes, unusual log patterns) when labels are scarce.
  - Finds clusters of similar defects but requires analyst interpretation.

Q3: Why bias mitigation is critical for UX personalization
- Biased personalization can reinforce existing inequalities, exclude groups, or degrade accessibility.
- Ensures fairness, maintains trust, and avoids legal/ethical harms.

Case Study: AIOps in deployment pipelines — How it improves efficiency (two examples)
1. Automated anomaly detection in CI/CD: Detect flaky tests or unusual build failures and flag/prioritize them automatically.
2. Intelligent rollback/suggestion: Use historical deployments and outcomes to recommend safe rollback steps and predict risky deployments.

