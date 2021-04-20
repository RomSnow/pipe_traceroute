class Formatter:
    def __init__(self, str_len: int, *elements):
        self.str_len = str_len
        self.elements = elements

    def get_string(self) -> str:
        out_str = ''
        coll_len = self.str_len // len(self.elements)

        for el in self.elements:
            s = str(el)
            out_str += s + ' ' * (coll_len - len(s))

        return out_str
