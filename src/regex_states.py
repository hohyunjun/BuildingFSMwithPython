from state import State

class s0(State):
    def on_event(self, event):
        if event == 'a':
            return s1()

        return self

class s1(State):
    def on_event(self, event):
        if event == 'b':
            return s2()
        elif event == 'a' or event == 'c':
            return s0()

class s2(State):
    def on_event(self, event):
        if event == 'b':
            return self
        elif event == 'a':
            return s0()
        elif event == 'c':
            return s3()

class s3(State):
    def on_event(self, event):
        if event == 'a' or event=='b':
            return s4()
        elif event== 'c':
            return s4()

class s4(State):
    def on_event(self, event):
        pass
