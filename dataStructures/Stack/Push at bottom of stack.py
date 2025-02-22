from stack_with_list_linkedList import StackWithLinedList

"""
Recursion and stack are best friends.
Since implicit stack calls also uses recursion.
"""


class StackWithBottomPush(StackWithLinedList):
    def __init__(self):
        StackWithLinedList.__init__(self)

    def bottomPush(self, data):
        if self.is_empty():
            self.push(data)
            return
        top = self.pop()
        self.bottomPush(data)
        self.push(top)


if __name__ == "__main__":
    trial = StackWithBottomPush()
    trial.push(1)
    trial.push(2)
    trial.push(3)
    trial.bottomPush("recession")
    while trial.is_empty() is False:
        print(trial.pop())
