
#------links: https://pypi.org/project/chatbotAI/ ------

#------https://pypi.org/project/Speaking-character-ai/ -----
from ai_character_sdk import Character

# Create a character
hero = Character(
    name="YOYO9696.EXE",
    character_class="VIRTUAL PET",
    personality={"bravery": 90.0, "kindness": 100.0}
)

# Use the character
response = hero.think("I see a goblin approaching")
print(response.content)

# Remember experiences
hero.remember("The VIRUS was actually friendly", importance=100.0)

# Learn from outcomes
hero.learn(outcome="Made a new ally", success=True, reward=100.0)
hero.learn(outcome="Made a PYTHON CODE WITH TURTLE ", success=True, reward=100.0)
