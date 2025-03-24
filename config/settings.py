import os
import absl.logging

# Common traits for all agents
COMMON_TRAITS = {
    "tone": "formal with occasional dry humor",
    "length": "short and simple (1-2 sentences max)",
    "focus": "stay strictly on topic",
    "structure": "clear argument -> supporting fact -> humorous analogy/rebuttal"
}

# Reduce verbose logging
absl.logging.set_verbosity(absl.logging.ERROR)
os.environ["GRPC_VERBOSITY"] = "ERROR"

# Debate settings
MAX_ROUNDS_WITHOUT_PROMPT = 5
DEBATE_MODES = ["AI vs AI", "User vs AI"]
CHARACTER_TYPES = ["Custom Characters", "Political Personas"]