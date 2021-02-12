class Excuse:
    def __init__(self, numb1, numb2):
        self.numb1 = numb1
        self.numb2 = numb2

    @staticmethod
    def use_error(numb1, numb2):
        try:
            return (numb1 / numb2)

        except:
            return f"Законы математики так не считают."

print(Excuse.use_error(50, 0))
use = Excuse(80, 4)
print(use.use_error(20, 0))