from config.settings import DEBATE_MODES, CHARACTER_TYPES
from core.model import AIModel
from core.persona import get_custom_characters, select_political_personas, select_ai_opponent
from core.debate import get_debate_topic, conduct_ai_vs_ai_debate, conduct_user_vs_ai_debate
from utils.helpers import select_from_options

def main():
    print("=== AI Debate Simulator 2.0 ===")
    
    # Initialize AI model
    ai_model = AIModel()
    
    # Select debate mode
    print("\n=== Select Debate Mode ===")
    mode, _ = select_from_options(DEBATE_MODES, "Select a mode")
    
    # Get debate topic
    topic = get_debate_topic()
    
    if mode == "AI vs AI":
        # Determine character selection method
        print("\n=== Select Character Type ===")
        char_type, _ = select_from_options(CHARACTER_TYPES, "Select character type")
        
        if char_type == "Custom Characters":
            characters = get_custom_characters()
        else:  # Political Personas
            characters = select_political_personas()
        
        input("\nPress Enter to begin the debate...")
        conduct_ai_vs_ai_debate(ai_model, characters, topic)
    else:  # User vs AI
        ai_opponent = select_ai_opponent()
        input("\nPress Enter to begin the debate...")
        conduct_user_vs_ai_debate(ai_model, ai_opponent, topic)

if __name__ == "__main__":
    main()