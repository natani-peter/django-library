from typing import List


class EditorState:
    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return self.content


class Editor:
    def __init__(self):
        self.content: str = ""

    def createState(self):
        return EditorState(self.content)

    def setContent(self, content: str):
        self.content = content

    def restoreState(self, state: EditorState):
        if state:
            self.content = state.content
            return self.content
        else:
            return self.content


class History:
    def __init__(self):
        self.states: List[EditorState] = []

    def pushState(self, state: EditorState):
        self.states.append(state)

    def popState(self):
        if len(self.states) > 0:
            return self.states.pop()
        else:
            pass


class Tool:
    def __init__(self, name: str):
        self.name = name

    def draw(self, action):
        pass


class SelectTool(Tool):
    def __init__(self):
        super().__init__("Select Tool")

    def draw(self, action):
        if action == 'down':
            print('A + sign')

        if action == 'up':
            print('the highlighted text is selected')


class BrushTool(Tool):
    def __init__(self):
        super().__init__("Brush Tool")

    def draw(self, action):
        if action == 'down':
            print('a little circle sign')
        if action == 'up':
            print('the brush shades a little color')


class User:
    @staticmethod
    def use(a_tool: Tool):
        return a_tool


# usage

if __name__ == "__main__":
    myUser = User()
    select_tool = myUser.use(SelectTool())
    select_tool.draw('down')
