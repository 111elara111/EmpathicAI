EmpathicAI

EmpathicAI is an artificial emotional intelligence framework for building empathetic conversational agents and affect-aware systems. It provides components for emotion detection, empathetic response generation, and evaluation tooling so researchers and engineers can prototype emotionally-intelligent assistants quickly.

Badges: [build] [license] [python-version] [coverage]

## Why EmpathicAI?

- Make conversational systems more human-centered by modeling emotional context.
- Modular: drop-in emotion detectors, response planners, and policy layers.
- Research + Production friendly: simple examples, tests, and CI.

## Features

- Emotion classification from text (prebuilt models + easy plugins)
- Response templates and generation strategies with empathy-first defaults
- Evaluation scripts for measuring empathy, appropriateness, and user satisfaction
- Example notebooks and lightweight demo server

## Quickstart

1. Clone
   ```bash
   git clone https://github.com/111elara111/EmpathicAI.git
   cd EmpathicAI
   ```
2. Create and activate virtualenv
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install
   ```bash
   pip install -e .
   ```
4. Run tests
   ```bash
   pytest
   ```

## Examples

Minimal usage example:

```python
from empathicai import EmotionDetector, EmpathyPlanner

# load a detector and planner
# (replace with real model names in docs)
detector = EmotionDetector.from_pretrained("base-text-emotion")
emotions = detector.predict("I just lost my job and I'm terrified about the future.")
planner = EmpathyPlanner()
reply = planner.plan_response(emotions, user_message="I just lost my job...")
print(reply)
```

See docs/ and examples/ for more complete guides.

## Demos

This repository includes 13 demos in the `demos/` directory. Each demo demonstrates a core feature or integration — see `demos/README.md` for details and how to run them locally.

## Contributing

We welcome contributions — see CONTRIBUTING.md for how to get started and CODE_OF_CONDUCT.md for expectations.

## Roadmap & How to help

- Add more pre-trained emotion models
- Improve evaluation suite
- Create demo web UI / GitHub Pages demo

## License

This project is licensed under the MIT License — see LICENSE for details.

## Contact

Owner: 111elara111 — https://github.com/111elara111