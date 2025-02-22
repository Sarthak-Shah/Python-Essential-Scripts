from stack_with_list_linkedList import Stack


class StringReversalWithStack(Stack):
    def __init__(self):
        Stack.__init__(self)

    def pushString(self, data: str):
        for char in data:
            self.push(char)

    def reverseString(self):
        reversed_value = ""
        while self.is_empty() is False:
            reversed_value = reversed_value + self.pop()
        return reversed_value


if __name__ == "__main__":
    trial = StringReversalWithStack()
    # trial.push("W")
    trial.pushString("abcdef_SharkTankIndiaSeason2")
    print(trial.reverseString())
