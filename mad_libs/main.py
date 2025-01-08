# def get_input function
def get_input(words_type: str):
    user_input: str = input(f"Enter a {words_type}: ")
    return user_input

noun1 = get_input("noun")
noun2 = get_input("noun")
noun3 = get_input("noun")
noun4 = get_input("noun")
verb1 = get_input("verb")
verb2 = get_input("verb")
verb3 = get_input("verb")
adjective1 = get_input("adjective")
adjective2 = get_input("adjective")

story = f"""
Once upon a time, in a {adjective1} land, there lived a {adjective2} {noun1} who loved to {verb1}. Every morning, the {noun1} would visit a {noun2} near their home to {verb2}. This {noun2} was not just any ordinary {noun2}—it was said to be the heart of the {adjective1} land.

One day, while {verb2}ing at the {noun2}, the {adjective2} {noun1} noticed a strange {noun3} glowing faintly nearby. Intrigued, they decided to {verb3} it. As they approached the {noun3}, they felt a {adjective1} warmth radiating from it.

When they touched the {noun3}, a hidden passage opened beneath the {noun2}. Filled with curiosity, the {adjective2} {noun1} ventured inside. The passage led to a vast, hidden chamber filled with ancient {noun4}. Among the treasures, a single object stood out—a golden {noun3}.

Suddenly, the chamber began to tremble! A booming voice echoed, “Who dares to disturb the sacred {noun3}?” It was the guardian of the {adjective1} land, a mythical {noun2} that had long protected the realm. The {adjective2} {noun1} quickly explained their intentions and promised to return the {noun3} to its rightful place.

The guardian, impressed by the {noun1}'s courage, agreed to let them go—but only if they could complete a challenge. The {adjective2} {noun1} had to {verb3} through a maze filled with {noun4} traps and find the true resting place of the {noun3}.

With determination and the help of their {adjective2} instincts, the {noun1} navigated the maze, avoiding traps by {verb2}ing and solving puzzles. At last, they placed the {noun3} on its pedestal, restoring balance to the {adjective1} land.

As a reward, the guardian gifted the {noun1} a piece of the {noun3}'s magic, allowing them to {verb1} with greater power and purpose than ever before. The {adjective2} {noun1} returned home, forever changed by their {adjective1} adventure.

From that day on, the {noun1} cherished their time at the {noun2}, always remembering the importance of bravery, kindness, and respect for the mysteries of their {adjective1} land.
"""

print(story)