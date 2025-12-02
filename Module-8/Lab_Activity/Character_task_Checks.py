# Vrajkumar Patel
# November 16, 2025
# Problem 5: Checks a game character's items and debuffs against task requirements.

class Character:
    # Class structure provided in the problem description is maintained
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses
        
    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

def check_task_readiness(character):
    """
    Checks if the character has the necessary items and lacks required debuffs 
    for three different tasks. Prints the confirmation check.
    """
    items = character.weapons
    debuffs = character.weaknesses
    
    print(f"--- Character Profile for {character.nickname} ---")
    print(f"Current Items: {items}")
    print(f"Current Debuffs: {debuffs}\n")

    # --- Task 1: Climb a mountain --- [cite: 36]
    # Needs: rope, coat, first aid kit. Cannot have: slow.
    needs_rope = 'rope' in items
    needs_coat = 'coat' in items
    needs_first_aid_kit = 'first aid kit' in items
    has_slow_debuff = 'slow' in debuffs
    
    can_climb = (needs_rope and needs_coat and needs_first_aid_kit) and (not has_slow_debuff)
    
    print("Task 1: Climb a mountain (needs: rope, coat, first aid kit, NOT slow)")
    print(f"  Check Result: {can_climb}")
    if can_climb:
        print("Ready to climb the mountain!")
    else:
        print("Not ready. Missing items or has 'slow' debuff.")
    print("-" * 20)
    
    # --- Task 2: Cook a meal --- [cite: 37]
    # Needs: pan, groceries. Cannot have: small.
    needs_pan = 'pan' in items
    needs_groceries = 'groceries' in items
    has_small_debuff = 'small' in debuffs
    
    can_cook = (needs_pan and needs_groceries) and (not has_small_debuff)
    
    print("Task 2: Cook a meal (needs: pan, groceries, NOT small)")
    print(f"  Check Result: {can_cook}")
    if can_cook:
        print("Ready to cook a meal!")
    else:
        print("Not ready. Missing items or has 'small' debuff.")
    print("-" * 20)

    # --- Task 3: Write a book --- [cite: 38]
    # Needs: pen, paper, idea. Cannot have: confusion.
    needs_pen = 'pen' in items
    needs_paper = 'paper' in items
    needs_idea = 'idea' in items
    has_confusion_debuff = 'confusion' in debuffs
    
    can_write = (needs_pen and needs_paper and needs_idea) and (not has_confusion_debuff)
    
    print("Task 3: Write a book (needs: pen, paper, idea, NOT confusion)")
    print(f"  Check Result: {can_write}")
    if can_write:
        print("Ready to write a book!")
    else:
        print("Not ready. Missing items or has 'confusion' debuff.")
    print("-" * 20)

# Create the character object as described in the problem
player1 = Character('Dragon Slayer', 
                    ['pan', 'paper', 'idea', 'rope', 'groceries'], 
                    ['slow'])

# Test the function
check_task_readiness(player1)