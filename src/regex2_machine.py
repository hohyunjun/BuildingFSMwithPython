from regex2_states import s0

class Regex2Device(object):
    def __init__(self):
        self.state = s0()

    def on_event(self, event):
        self.state = self.state.on_event(event)

regex = Regex2Device()
x = input("Regex의 인스턴스를 입력하세요 : ")


for i in x:
    regex.on_event(i)

answerstate = "s4"
regexstate = str(regex.state)

if str(regex.state) == answerstate :
    print('1')
else :
    print('0')
