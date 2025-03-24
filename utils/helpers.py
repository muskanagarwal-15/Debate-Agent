def select_from_options(options, prompt, min_value=1, max_value=None):
    """Helper function to select from a list of options"""
    if max_value is None:
        max_value = len(options)
    
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input(f"{prompt} (number): "))
            if min_value <= choice <= max_value:
                return options[choice-1], choice
            print(f"Please enter a number between {min_value} and {max_value}")
        except ValueError:
            print("Invalid input. Please enter a number.")