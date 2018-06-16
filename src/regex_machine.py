from regex_states import s0

class RegexDevice(object):
    def __init__(self):
        self.state = s0()

    def on_event(self, event):
        self.state = self.state.on_event(event)

regex = RegexDevice()
x = input("Regex의 인스턴스를 입력하세요 : ")


for i in x:
    regex.on_event(i)

print(regex.state)

answer = "s3"
regexstate = str(regex.state)
print(type(regexstate))
print(type(answer))
print(regexstate)

if str(regex.state) == answer :
    print('true')
else :
    print('false')
