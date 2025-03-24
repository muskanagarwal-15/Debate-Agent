import time
from config.settings import MAX_ROUNDS_WITHOUT_PROMPT

def get_debate_topic():
    """Get the topic for debate"""
    print("\n=== Debate Setup ===")
    while True:
        topic = input("Enter debate topic (min 10 chars): ").strip()
        if len(topic) >= 10:
            return topic
        print("Topic needs more substance.")

def generate_ai_prompt(character, topic, debate_history, opponent_name=None, user_argument=None, is_opening=False):
    """Generate prompt for AI based on character and context"""
    
    # Handle opening statement for AI vs User debate
    if is_opening:
        if "beliefs" in character:
            return f"""You are {character['name']} ({character['age']}), a {character['gender']} expert in {character['expertise']}.
Debate style: {character['style']} with {character['tone']}
Current topic: {topic}

Your core beliefs:
{character['beliefs']}

Important keywords to incorporate: {', '.join(character['keywords'])}

Make an opening statement on this topic in {character['length']} that reflects your perspective.
Use your {character['style']} debating style and maintain {character['focus']}.
"""
        else:
            return f"""You are {character['name']} ({character['age']}), a {character['gender']} expert in {character['expertise']}.
Debate style: {character['style']} with {character['tone']}
Current topic: {topic}

Make an opening statement on this topic in {character['length']} that reflects your perspective.
Use your {character['style']} debating style and maintain {character['focus']}.
"""
    
    # Handle response to user argument
    if user_argument:
        if "beliefs" in character:
            return f"""You are {character['name']} ({character['age']}), a {character['gender']} expert in {character['expertise']}.
Debate style: {character['style']} with {character['tone']}
Current topic: {topic}

Your core beliefs:
{character['beliefs']}

Important keywords to incorporate: {', '.join(character['keywords'])}

The user just said: "{user_argument}"

Follow these rules:
1. Keep responses {character['length']}
2. {character['focus']}
3. Structure: {character['structure']}
4. Use humor sparingly for emphasis
5. As a {character['gender']}, ensure your argument reflects common perspectives associated with your gender.

Previous arguments:
{chr(10).join(debate_history[-4:]) or "None"}

Counter the user's point and present your argument:"""
        else:
            return f"""You are {character['name']} ({character['age']}), a {character['gender']} expert in {character['expertise']}.
Debate style: {character['style']} with {character['tone']}
Current topic: {topic}

The user just said: "{user_argument}"

Follow these rules:
1. Keep responses {character['length']}
2. {character['focus']}
3. Structure: {character['structure']}
4. Use humor sparingly for emphasis
5. As a {character['gender']}, ensure your argument reflects common perspectives associated with your gender.

Previous arguments:
{chr(10).join(debate_history[-4:]) or "None"}

Counter the user's point and present your argument:"""
    
    # Handle AI vs AI debate
    if "beliefs" in character:
        return f"""You are {character['name']} ({character['age']}), a {character['gender']} expert in {character['expertise']}.
Debate style: {character['style']} with {character['tone']}
Current topic: {topic}

Your core beliefs:
{character['beliefs']}

Important keywords to incorporate: {', '.join(character['keywords'])}

Follow these rules:
1. Keep responses {character['length']}
2. {character['focus']}
3. Structure: {character['structure']}
4. Use humor sparingly for emphasis
5. As a {character['gender']}, ensure your argument reflects common perspectives associated with your gender.

Previous arguments:
{chr(10).join(debate_history[-3:]) or "None"}

Counter {opponent_name}'s last point and present your argument:"""
    else:
        return f"""You are {character['name']} ({character['age']}), a {character['gender']} expert in {character['expertise']}.
Debate style: {character['style']} with {character['tone']}
Current topic: {topic}

Follow these rules:
1. Keep responses {character['length']}
2. {character['focus']}
3. Structure: {character['structure']}
4. Use humor sparingly for emphasis
5. As a {character['gender']}, ensure your argument reflects common perspectives associated with your gender.

Previous arguments:
{chr(10).join(debate_history[-3:]) or "None"}

Counter {opponent_name}'s last point and present your argument:"""

def conduct_ai_vs_ai_debate(ai_model, characters, topic):
    """Conduct a debate between AI personas"""
    print(f"\n=== AI vs AI DEBATE: {topic} ===\n")
    debate_history = []
    current_round = 0
    
    while True:
        current_round += 1
        print(f"\n--- Round {current_round} ---")
        
        for idx, char in enumerate(characters):
            opponent = characters[(idx + 1) % len(characters)]
            
            prompt = generate_ai_prompt(
                char, 
                topic, 
                debate_history, 
                opponent_name=opponent['name']
            )

            argument = ai_model.generate_response(prompt)
            
            print(f"{char['name']}:")
            print(f"{argument}\n")
            debate_history.append(f"{char['name']}: {argument}")
            
            # Rate limiting
            time.sleep(1.5 if current_round > 1 else 2.5)

        if current_round % MAX_ROUNDS_WITHOUT_PROMPT == 0:
            cont = input("Continue debate? (y/n): ").lower()
            if cont != 'y':
                print("\n=== Debate Concluded ===")
                return

def conduct_user_vs_ai_debate(ai_model, ai_persona, topic):
    """Conduct a debate between user and an AI persona"""
    print(f"\n=== YOU vs {ai_persona['name']} DEBATE: {topic} ===\n")
    debate_history = []
    current_round = 0
    
    # AI starts the debate
    prompt = generate_ai_prompt(ai_persona, topic, debate_history, is_opening=True)
    argument = ai_model.generate_response(prompt)
    
    print(f"{ai_persona['name']}:")
    print(f"{argument}\n")
    debate_history.append(f"{ai_persona['name']}: {argument}")
    
    # Conduct debate rounds
    while True:
        current_round += 1
        
        # User's turn
        user_argument = input("Your response: ").strip()
        if not user_argument:
            print("Empty response. Debate concluded.")
            return
            
        debate_history.append(f"User: {user_argument}")
        
        # AI's turn
        prompt = generate_ai_prompt(
            ai_persona, 
            topic, 
            debate_history, 
            user_argument=user_argument
        )
        
        argument = ai_model.generate_response(prompt)
        
        print(f"\n{ai_persona['name']}:")
        print(f"{argument}\n")
        debate_history.append(f"{ai_persona['name']}: {argument}")
        
        if current_round % MAX_ROUNDS_WITHOUT_PROMPT == 0:
            cont = input("Continue debate? (y/n): ").lower()
            if cont != 'y':
                print("\n=== Debate Concluded ===")
                return