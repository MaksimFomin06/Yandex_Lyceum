N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, nota="до", is_long=False):
        self.nota = LONG_PITCHES[PITCHES.index(nota)] if is_long else nota

    def __str__(self):
        return self.nota

    def __eq__(self, other):
        return PITCHES.index(self.short_nota()) == PITCHES.index(other.short_nota())

    def __lt__(self, other):
        return PITCHES.index(self.short_nota()) < PITCHES.index(other.short_nota())

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return PITCHES.index(self.short_nota()) > PITCHES.index(other.short_nota())

    def __ge__(self, other):
        return self > other or self == other

    def short_nota(self):
        return PITCHES[LONG_PITCHES.index(self.nota)] if self.nota in LONG_PITCHES else self.nota

    def __rshift__(self, shift):
        index = (PITCHES.index(self.short_nota()) + shift) % N
        return Note(PITCHES[index], is_long=self.nota in LONG_PITCHES)

    def __lshift__(self, shift):
        index = (PITCHES.index(self.short_nota()) - shift) % N
        return Note(PITCHES[index], is_long=self.nota in LONG_PITCHES)

    def get_interval(self, other):
        if self == other:
            return INTERVALS[0]
        
        first_index = PITCHES.index(self.short_nota())
        second_index = PITCHES.index(other.short_nota())
        
        distance = min(abs(second_index - first_index), N - abs(second_index - first_index))
        
        return INTERVALS[distance]


class LoudNote(Note):
    def __str__(self):
        return self.nota.upper()


class DefaultNote(Note):
    pass


class NoteWithOctave(Note):
    def __init__(self, nota, octave, is_long=False):
        super().__init__(nota, is_long)
        self.octave = octave

    def __str__(self):
        return f"{self.nota} ({self.octave})"


LONG_SUFFIXES = {
    "до": "до-о",
    "ре": "ре-э",
    "ми": "ми-и",
    "фа": "фа-а",
    "соль": "со-оль",
    "ля": "ля-а",
    "си": "си-и"
}
