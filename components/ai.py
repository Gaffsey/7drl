from __future__ import annotations

import random
from typing import List, Optional, Tuple, TYPE_CHECKING

import numpy as np
import tcod

from actions import Action, BumpAction, MeleeAction, MovementAction, WaitAction

if TYPE_CHECKING:
    from entity import Actor

class BaseAI(Action):
    entity: Actor
    def perform(self) -> None:
        raise NotImplementedError()
        
    def get_path_to(self, dest_x: int, dest_y: int) -> List[Tuple[int, int]]:
    
        cost = np.array(self.entity.gamemap.tiles["walkable"], dtype=np.int8)
        
        for entity in self.entity.gamemap.entities:
            if entity.blocks_movement and cost[entity.x, entity.y]:
                cost[entity.x, entity.y] += 10
                
        graph = tcod.path.SimpleGraph(cost=cost, cardinal=2, diagonal=3)
        pathfinder = tcod.path.Pathfinder(graph)
        
        pathfinder.add_root((self.entity.x, self.entity.y))
        
        path: List[List[int]] = pathfinder.path_to((dest_x, dest_y))[1:].tolist()
        
        return [(index[0], index[1]) for index in path]


class HostileEnemy(BaseAI):
    def __init__(self, entity: Actor):
        super().__init__(entity)
        self.path: List[Tuple[int, int]] = []
        
    def perform(self) -> None:
        target = self.engine.player
        dx = target.x - self.entity.x
        dy = target.y - self.entity.y
        distance = max(abs(dx), abs(dy))
        
        if self.engine.game_map.visible[self.entity.x, self.entity.y]:
            if distance <= 1:
                return MeleeAction(self.entity, dx, dy).perform()
                
            self.path = self.get_path_to(target.x, target.y)
            
        if self.path:
            dest_x, dest_y = self.path.pop(0)
            return MovementAction(
                self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
            ).perform()
            
        return WaitAction(self.entity).perform()
class CandleAI(BaseAI):
    def __init__(
        self, entity: Actor
):
        super().__init__(entity)
        
    def perform(self) -> None:
        for tile in self.engine.game_map.render:
        
            if tile.distance(*target_xy) <= self.radius:   
                append(self.game_map.lit)
        self.engine.message_log.add_message(
        f"The {self.entity.name} flickers in the dark, illuminating the dungeon."
        )
        

            
    
class BossAI(BaseAI):
    def __init__(self, entity: Actor):
        super().__init__(entity)
        self.path: List[Tuple[int, int]] = []

    def perform(self) -> None:
        
        target = self.engine.player
        dx = target.x - self.entity.x
        dy = target.y - self.entity.y
        distance = max(abs(dx), abs(dy))
        if self.engine.turn  % 2 == 0:
                
            if self.engine.game_map.visible[self.entity.x, self.entity.y]:
                if distance <=1:
                    return MeleeAction(self.entity, dx, dy).perform()
                elif 2 <= distance <= 3:
                    self.engine.message_log.add_message("You hear a shallow, rattling breath drawing closer.")                

                elif 4 <= distance <= 5:
                    self.engine.message_log.add_message("You hear the hear the slick sound of meat over bone and smell the scent of rotting flesh.")
                if 6 <= distance <= 7:
                    self.engine.message_log.add_message("You hear the creak of floorboards drawing nearer.")
                            
                self.path = self.get_path_to(target.x, target.y)


            if self.path:
                dest_x, dest_y = self.path.pop(0)
                return MovementAction(
                self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
                ).perform()

                        
        else:
            return WaitAction(self.entity).perform()                 