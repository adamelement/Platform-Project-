class Hitbox:
    def __init__(self, knock_back, launch_angle):
        self.character_direction = character_direction
        self.hitbox_dimensions = hitbox_dimensions

    def attack_hitbox(self):
        direction = Character.character_direction
        if direction == 'L':
            self.rect = (['hitbox'], ['hitbox'], character_location - ['x_distance'], character_location + ['y_distance'])
        elif direction == 'R':
            self.rect = (['hitbox'], ['hitbox'], character_location + ['x_distance'], character_location + ['y_distance'])




