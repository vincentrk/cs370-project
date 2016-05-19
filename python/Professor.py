from State import State

class Professor:
    def __init__(self, , terrain_map):
        self.state = terrain_map.get_prof_state()
        self.terrain_map = terrain_map

    def move(self, direction):
        # self.state.move(direction)
        raise NotImplemented

    def get_surroundings(self):
        # neighbors = self.terrain_map.get_neighbors(self.state.point)
        #
        raise NotImplemented

    def __str__(self):
        res = "----Professor----\n"
        res += "State: " + str(self.state)
        return res

