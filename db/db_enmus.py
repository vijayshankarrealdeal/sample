from enum import Enum

class Game(Enum):
    CARDS = "cards"
    TRUTH_DARE = "truth_dare"
    BORRD_GAME = "board_game"
    SCRATH = "scratch"


class GameLevel(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    INTENSE = "intense"
    SUPER = "super"

class UserType(Enum):
    ADMIN = "admin"
    USER = "user"