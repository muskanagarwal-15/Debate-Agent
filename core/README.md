# AI Debate Agent

## Project Description

This AI Debate Agent is a terminal-based application that allows multiple users to create personas and engage in AI-driven debates on various topics. The application supports two primary modes of interaction:

### 1. Multi-User Persona Debate
Users can create custom personas with unique characteristics, and the AI will facilitate debates between these personas on selected topics.

### 2. User-AI and AI-AI Debate
Users can select topics and AI characters (such as political parties or historical figures) to engage in debates.

## Features
- Create custom user personas
- Generate AI personas with distinct characteristics
- Support for multiple debate modes
- Topic-based debate generation
- Terminal-based interaction

## Project Structure
```
ai-debate-agent/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── persona.py
│   ├── debate_engine.py
│   ├── topic_generator.py
│   └── ai_agent.py
│
├── data/
│   ├── personas.json
│   └── topics.json
│
├── utils/
│   ├── __init__.py
│   ├── text_processor.py
│   └── conversation_manager.py
│
├── config/
│   └── settings.py
│
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main application:
```bash
python src/main.py
```

### Debate Modes
1. Multi-User Persona Debate
2. User-AI and AI-AI Debate

## Dependencies
- Python 3.8+
- OpenAI's GPT or similar language model
- JSON for data storage
- Rich (for enhanced terminal formatting)

## Contribution
Contributions are welcome! Please read the contribution guidelines before submitting a pull request.

## License
[Specify your license here]

## Future Enhancements
- Web interface
- More advanced persona generation
- Machine learning-based persona evolution
- Advanced debate scoring and analysis
```