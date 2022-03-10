from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import random
import entity_factories
import actions
import color
import components.ai
import components.inventory
from components.base_component import BaseComponent
from exceptions import Impossible
from input_handlers import ActionOrHandler, AreaRangedAttackHandler, SingleRangedAttackHandler
import components.fighter
import entity

if TYPE_CHECKING:
    from entity import Actor, Item
    
class Consumable(BaseComponent):
    parent: Item
    
    def get_action(self, consumer: Actor) -> Optional[ActionOrHandler]:
        return actions.ItemAction(consumer, self.parent)
        
    def activate(self, action: actions.ItemAction) -> None:
        raise NotImplementedError()
    
    def consume(self) -> None:
        entity = self.parent
        inventory = entity.parent
        if isinstance(inventory, components.inventory.Inventory):
            inventory.items.remove(entity)
            
class GoldenCandle(Consumable):
    def __init__(self, radius: int):
        self.radius = radius
        
            
    def activate(self, action: actions.ItemAction) -> None:
        consumer = action.entity
        target = action.target_actor

        entity.Entity.place(entity_factories.burning_candle)
        
        self.consume()
