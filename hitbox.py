class Hitbox:
    def __init__(self, dimensions, knockback, launch_angle):
        self.dimensions = dimensions
        self.knockback = knockback
        self.launch_angle = launch_angle

    def attack_hitbox(self):
        direction = Character.character_direction
        if direction == 'L':
            self.rect = (['hitbox'], ['hitbox'], character_location - ['x_distance'], character_location + ['y_distance'])
        elif direction == 'R':
            self.rect = (['hitbox'], ['hitbox'], character_location + ['x_distance'], character_location + ['y_distance'])




