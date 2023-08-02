from enum import Enum


class ToolChoices(Enum):
    PAN = 1
    SELECT = 2


class Tool:
    def __init__(self, root):
        self.tool = ToolChoices.SELECT
        self.root = root

    def set_pan(self):
        self.tool = ToolChoices.PAN
        self.root.config(cursor='hand2')

    def set_select(self):
        self.tool = ToolChoices.SELECT
        self.root.config(cursor='arrow')

    def move_entity(self, entity):
        pass