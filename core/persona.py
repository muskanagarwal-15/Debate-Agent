from config.settings import COMMON_TRAITS
from config.personas import POLITICAL_PERSONAS

def create_persona(name, age, gender, expertise, style):
    """Create a persona with the given attributes"""
    return {
        'name': name,
        'age': age,
        'gender': gender,
        'expertise': expertise,
        'style': style,
        'previous_arguments': [],
        **COMMON_TRAITS
    }

def get_political_persona(party_key):
    """Get a specific political persona by party key"""
    if party_key not in POLITICAL_PERSONAS:
        raise ValueError(f"Party {party_key} not found in predefined personas")
    
    persona_data = POLITICAL_PERSONAS[party_key]
    persona = create_persona(
        persona_data["name"], 
        persona_data["age"],
        persona_data["gender"],
        persona_data["expertise"],
        persona_data["style"]
    )
    # Add political-specific attributes
    persona["beliefs"] = persona_data["beliefs"]
    persona["keywords"] = persona_data["keywords"]
    return persona

def get_custom_characters():
    """Get custom characters defined by users"""
    characters = []
    while True:
        try:
            num_characters = int(input("Enter number of debate participants (2-6): "))
            if 2 <= num_characters <= 6:
                break
            print("Please enter between 2-6")
        except ValueError:
            print("Invalid input. Enter a number.")

    print("\n=== Character Setup ===")
    for i in range(num_characters):
        print(f"\nCharacter #{i+1}")

        name = input("Name: ").strip()
        age = input("Age: ").strip()
        gender = input("Gender (male/female/other): ").strip().lower()
        while gender not in ["male", "female", "other"]:
            print("Invalid gender. Please enter 'male', 'female', or 'other'.")
            gender = input("Gender (male/female/other): ").strip().lower()

        expertise = input("Area of expertise: ").strip()
        style = input("Debating style (e.g., aggressive, logical, emotional): ").strip()

        character = create_persona(name, age, gender, expertise, style)
        characters.append(character)
    return characters

def create_custom_opponent():
    """Create a custom opponent for user vs AI debate"""
    print("\n=== Create Your Opponent ===")
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    gender = input("Gender (male/female/other): ").strip().lower()
    while gender not in ["male", "female", "other"]:
        print("Invalid gender. Please enter 'male', 'female', or 'other'.")
        gender = input("Gender (male/female/other): ").strip().lower()
    expertise = input("Area of expertise: ").strip()
    style = input("Debating style: ").strip()
    
    return create_persona(name, age, gender, expertise, style)

def select_political_personas():
    """Select from predefined political personas"""
    available_parties = list(POLITICAL_PERSONAS.keys())
    
    print("\n=== Available Political Parties ===")
    for i, party in enumerate(available_parties, 1):
        print(f"{i}. {party.upper()} - {POLITICAL_PERSONAS[party]['name']}")
    
    selected_personas = []
    while True:
        try:
            selections = input("\nSelect parties (comma-separated numbers, e.g., 1,3): ").strip()
            indices = [int(idx.strip()) - 1 for idx in selections.split(',')]
            
            if all(0 <= idx < len(available_parties) for idx in indices) and 2 <= len(indices) <= 6:
                for idx in indices:
                    party = available_parties[idx]
                    selected_personas.append(get_political_persona(party))
                break
            else:
                print("Invalid selection. Please select 2-6 valid options.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid numbers separated by commas.")
    
    return selected_personas

def select_ai_opponent():
    """Select an AI opponent for User vs AI debate"""
    print("\n=== Select Debate Category ===")
    categories = ["Political", "Custom"]
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            choice = int(input("Select a category (number): "))
            if 1 <= choice <= len(categories):
                category = categories[choice-1]
                break
            print(f"Please enter a number between 1 and {len(categories)}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if category == "Political":
        # Select from predefined political personas
        available_parties = list(POLITICAL_PERSONAS.keys())
        
        print("\n=== Available Political Parties ===")
        for i, party in enumerate(available_parties, 1):
            print(f"{i}. {party.upper()} - {POLITICAL_PERSONAS[party]['name']}")
        
        while True:
            try:
                choice = int(input("Select your opponent (number): "))
                if 1 <= choice <= len(available_parties):
                    party = available_parties[choice-1]
                    return get_political_persona(party)
                print(f"Please enter a number between 1 and {len(available_parties)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:  # Custom
        return create_custom_opponent()