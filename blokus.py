import numpy as np
import numpy.typing as npt
import pygame
import pygame.gfxdraw


coord = tuple[int, int]

empty_board = np.zeros((20, 20), dtype=np.int8)
player_corners = {
    "red": set([(0, 0)]),
    "blu": set([(0, -1)]),
    "grn": set([(-1, 0)]),
    "ylw": set([(-1, -1)]),
}


class Polyomino:
    def __init__(self, squares: set[coord]) -> None:
        self.squares = squares

    def footprint(self) -> tuple[int, int]:
        mx = max(self.squares, key=lambda x: x[0])[0]
        my = max(self.squares, key=lambda x: x[1])[1]

        return (min(mx, my), max(mx, my))

    def flip_x(self):
        mx = max(self.squares, key=lambda x: x[0])[0]
        self.squares = set(map(lambda x: (-x[0], x[1]), self.squares))
        self.translate((mx, 0))

        return self

    def translate(self, rel: coord):
        self.squares = set(map(lambda x: (x[0] + rel[0], x[1] + rel[1]), self.squares))
        return self


# https://i.ebayimg.com/images/g/cj8AAOSwdXhekQcT/s-l1200.jpg
polyominos: list[Polyomino] = [
    Polyomino(set([(0, 0)])),  # 1
    Polyomino(set([(0, 0), (0, 1)])),  # 2
    Polyomino(set([(0, 0), (0, 1), (0, 2)])),  # 3
    Polyomino(set([(0, 0), (0, 1), (1, 0)])),  # 4
    Polyomino(set([(0, 0), (0, 1), (0, 2), (0, 3)])),  # 5
    Polyomino(set([(0, 0), (1, 0), (1, 1), (1, 2)])),  # 6
    Polyomino(set([(0, 0), (0, 1), (1, 1), (0, 2)])),  # 7
    Polyomino(set([(0, 0), (0, 1), (1, 0), (1, 1)])),  # 8
    Polyomino(set([(0, 1), (1, 1), (1, 0), (2, 0)])),  # 9
    Polyomino(set([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])),  # 10
    Polyomino(set([(0, 0), (1, 0), (1, 1), (1, 2), (1, 3)])),  # 11
    Polyomino(set([(0, 0), (0, 1), (1, 1), (1, 2), (1, 3)])),  # 12
    Polyomino(set([(0, 0), (0, 1), (1, 0), (1, 1), (1, 2)])),  # 13
    Polyomino(set([(0, 0), (1, 0), (1, 1), (1, 2), (0, 2)])),  # 14
    Polyomino(set([(0, 0), (0, 1), (0, 2), (1, 2), (0, 3)])),  # 15
    Polyomino(set([(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)])),  # 16
    Polyomino(set([(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)])),  # 17
    Polyomino(set([(0, 2), (1, 2), (1, 1), (2, 1), (2, 0)])),  # 18
    Polyomino(set([(0, 1), (0, 2), (1, 1), (2, 1), (2, 0)])),  # 19
    Polyomino(set([(0, 1), (0, 2), (1, 1), (1, 0), (2, 1)])),  # 20
    Polyomino(set([(0, 1), (1, 1), (1, 0), (1, 2), (2, 1)])),  # 21
]


def valid_move(
    b: npt.NDArray[np.int8], b_coord: coord, p: Polyomino, p_coord: coord
) -> bool:
    print(p.squares)
    p.translate(b_coord)
    print(p.squares)

    return True


pygame.init()
screen = pygame.display.set_mode((1000, 1000))


def draw_grid(s: pygame.Surface):
    s.fill("grey")
    for i in range(50, 1000, 50):
        pygame.gfxdraw.hline(s, 0, 1000, i, (255, 0, 0))
        pygame.gfxdraw.vline(s, i, 0, 1000, (255, 0, 0))


while True:
    draw_grid(screen)

    pygame.display.flip()
