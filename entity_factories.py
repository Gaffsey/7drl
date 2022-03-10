from components.ai import HostileEnemy, BossAI, CandleAI
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Actor, Item

player = Actor(
    char="@", 
    color=(255, 255, 255), 
    name="You", 
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=100, base_defense=100, base_power=100),
    inventory=Inventory(capacity=26),

    )

orc = Actor(
    char="*", 
    color=(63, 127, 63), 
    name="Salt Spider", 
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=1, base_defense=0, base_power=0),
    inventory=Inventory(capacity=0),
    )



boss1 = Actor(
    char="B", 
    color=(255, 255, 255), 
    name="Boss",     
    ai_cls=BossAI,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=50, base_power=200),
    inventory=Inventory(capacity=0),
)


golden_candle = Item(
    char="i",
    color=(255, 255, 0),
    name="Golden Candle",
    consumable=consumable.GoldenCandle(number_of_turns=7, radius=5),
)



burning_candle = Actor(
    char="i", 
    color=(255, 255, 0), 
    name="Boss",     
    ai_cls=CandleAI,
    equipment=Equipment(),
    fighter=Fighter(hp=00, base_defense=50, base_power=200),
    inventory=Inventory(capacity=0),
)

dagger = Item(
    char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger()
)

sword = Item(char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Sword())

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail())