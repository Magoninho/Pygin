from game_engine.scene import Scene
from elements.game_objects.main_scene_controller import MainSceneController


class MainScene(Scene):

    def __init__(self):
        """
        Create the list of game_objects and call the superclass constructor passing the list
        """
        self.init_game_objects_controllers_reference_list = [MainSceneController]
        super(MainScene, self).__init__(self.init_game_objects_controllers_reference_list)