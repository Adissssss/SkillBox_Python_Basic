class Air:
    def __init__(self):
        self.name = 'Air'

    def __str__(self):
        return 'Air'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()


class Earth:
    def __init__(self):
        self.name = 'Earth'

    def __str__(self):
        return 'Earth'

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()


class Fire:
    def __init__(self):
        self.name = 'Fire'

    def __str__(self):
        return 'Fire'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Vapor()


class Water:
    def __init__(self):
        self.name = 'Water'

    def __str__(self):
        return 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()


class Lightning:
    def __init__(self):
        self.name = 'Lightning'

    def __str__(self):
        return 'Lightning'


class Dust:
    def __init__(self):
        self.name = 'Dust'

    def __str__(self):
        return 'Dust'


class Dirt:
    def __init__(self):
        self.name = 'Dirt'

    def __str__(self):
        return 'Dirt'


class Storm:
    def __init__(self):
        self.name = 'Storm'

    def __add__(self, other):
        if isinstance(other, Lava):
            return Vsem_GG()

    def __str__(self):
        return 'Storm'


class Vapor:
    def __init__(self):
        self.name = 'Vapor'

    def __str__(self):
        return 'Vapor'


class Lava:
    def __init__(self):
        self.name = 'Lava'

    def __add__(self, other):
        if isinstance(other, Storm):
            return Vsem_GG()

    def __str__(self):
        return 'Lava'


class Vsem_GG:
    def __init__(self):
        self.name = 'Vsem_GG'

    def __str__(self):
        return 'Vsem_GG'
