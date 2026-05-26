from unittest import case

from code.level import Level


class EntityFactory:

    def get_entity(entity_name: str, position=(0,0):
        match entity_name:
            case "Level1Bg":
                list_bg = []