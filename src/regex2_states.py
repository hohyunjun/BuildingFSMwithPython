from state import State

class s0(State):
    def on_event(self, event):
        if event == 'x':
            return s1()

        return s5()

class s1(State):
    def on_event(self, event):
        if event == 'y':
            return s2()
        elif event == 'x':
            return self
        elif event == 'a' or event == 'b':
            return s5()

class s2(State):
    def on_event(self, event):
        if event == 'a':
            return s3()

        return s5()

class s3(State):
    def on_event(self, event):
        if event == 'a':
            return self
        elif event== 'x' or event=='y':
            return s5()
        elif event=='b':
            return s4()

class s4(State):
    def on_event(self, event):
        if event=='x' or event=='y':
            return s5()
        elif event=='a' or event=='b':
            return s5()

class s5(State):
    def on_event(self, event):
        return self
