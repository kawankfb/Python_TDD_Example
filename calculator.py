class Calculator:

    def __init__(self):
        self.__memory = []

    def store_in_memory(self, value):
        self.__memory.append(value)

    def read_from_memory(self):
        return self.__memory.pop()

    def peek_at_memory(self):
        return self.__memory[len(self.__memory)-1]

    def add(self, first_value, second_value):
        pass

    def sub(self, first_value, second_value):
        pass

    def mul(self, first_value, second_value):
        pass

    def div(self, first_value, second_value):
        pass
