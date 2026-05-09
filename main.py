class TreeType:
    """Umumiy ma'lumot — bir marta saqlanadi."""
    def __init__(self, name, color, texture):
        self.name    = name
        self.color   = color
        self.texture = texture

    def draw(self, x, y):
        print(f"  {self.name}({self.color}) → ({x},{y})")

class TreeFactory:
    _types = {}

    @classmethod
    def get(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls._types:
            cls._types[key] = TreeType(name, color, texture)
            print(f"  [Yangi tip] {name}")
        return cls._types[key]

    @classmethod
    def count(cls): return len(cls._types)

class Tree:
    """Noyob ma'lumot — har bir daraxt uchun."""
    def __init__(self, x, y, tree_type):
        self.x, self.y = x, y
        self.type      = tree_type

    def draw(self): self.type.draw(self.x, self.y)

class Forest:
    def __init__(self): self._trees = []

    def plant(self, x, y, name, color, texture):
        t = TreeFactory.get(name, color, texture)
        self._trees.append(Tree(x, y, t))

    def draw_all(self):
        for t in self._trees: t.draw()

if __name__ == "__main__":
    forest = Forest()
    forest.plant(1, 2, "Qarag'ay", "yashil", "ignabargli")
    forest.plant(3, 4, "Qarag'ay", "yashil", "ignabargli")
    forest.plant(5, 1, "Terak",    "och yashil", "tekis")
    forest.plant(2, 8, "Qarag'ay", "yashil", "ignabargli")

    forest.draw_all()
    print(f"\n1000 daraxt, faqat {TreeFactory.count()} tip xotirada")
