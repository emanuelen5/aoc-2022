from enum import Enum


diff_draw = 0
diff_win = 1
diff_lose = 2


def get_score(p1, p2) -> int:
	p1 = ord(p1) - ord('A')
	p2 = ord(p2) - ord('X')

	diff = (p2 - p1) % 3

	if diff == diff_draw:
		round_score = 3
	elif diff == diff_lose:
		round_score = 0
	elif diff == diff_win:
		round_score = 6

	return round_score + p2 + 1


class Outcome(Enum):
	lose = 'X'
	draw = 'Y'
	win = 'Z'


def get_shape_for_outcome(p1, outcome_char) -> str:
	outcome = Outcome(outcome_char)
	
	if outcome is Outcome.lose:
		diff = diff_lose
	elif outcome is Outcome.draw:
		diff = diff_draw
	elif outcome is Outcome.win:
		diff = diff_win

	p2_index = ord(p1) - ord('A') + diff
	return chr((p2_index % 3) + ord('X'))
	