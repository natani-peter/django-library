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


# usage

if __name__ == "__main__":
    editor = Editor()
    history = History()
    editor.setContent("Hello World Kampala")
    history.pushState(editor.createState())
    editor.setContent("Hello World From Uganda")
    history.pushState(editor.createState())
    editor.setContent("Hello World From East Africa")
    history.pushState(editor.createState())
    editor.setContent("Hello World From Africa")
    print(editor.content)
    print(editor.restoreState(history.popState()))
    print(editor.restoreState(history.popState()))
    print(editor.restoreState(history.popState()))
    print(editor.restoreState(history.popState()))
