class Hitbox:
    def __init__(self, hitbox_dimensions):
        self.character_direction = character_direction
        self.hitbox_dimensions = hitbox_dimensions

    def attack_hitbox(self):
        direction = Character.character_direction
        if direction == 'L':
            self.rect = marshal_moveset['hitbox', 'hitbox', character_location - 'x_distance', character_location - 'y_distance']
        elif direction == 'R':
            self.rect = marshal_moveset['hitbox', 'hitbox', character_location + 'x_distance', character_location + 'y_distance']




