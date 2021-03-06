# Zad. 2.3 (1.5 pkt) 
# Narysuj w konsoli, z wykorzystaniem rekurencji, pionowa linijke o zadanych
# parametrach: (dlugosc w danych jednostkach, liczba poziomow zagniezdzen).
# Podzialka ma byc „dwukierunkowa”, co widac na obrazku ponizej.

class Ruler:
    def __init__(self, num_inches, major_length):
        self.__num_inches = num_inches
        self.__major_length = major_length

    def draw_line(self, tick_length, tick_label=''):
        line = (' ' * (self.__major_length - tick_length)) + ('-' * tick_length * 2)
        if tick_label:
            line += ' ' + tick_label
        print(line)

    def draw_interval(self, center_length):
        if center_length > 0:
            self.draw_interval(center_length - 1)
            self.draw_line(center_length)
            self.draw_interval(center_length - 1)

    def draw_ruler(self):
        self.draw_line(self.__major_length, '0')
        for j in range(1, 1 + self.__num_inches):
            self.draw_interval(self.__major_length - 1)
            self.draw_line(self.__major_length, str(j))


if __name__ == '__main__':
    ruler = Ruler(2, 5)
    ruler.draw_ruler()
