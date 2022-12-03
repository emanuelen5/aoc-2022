def get_score(p1, p2) -> int:
	p1 = ord(p1) - ord('A')
	p2 = ord(p2) - ord('X')

	# Draw
	diff = (p2 - p1) % 3

	if diff == 0:  # Draw
		round_score = 3
	if diff == 2: # Lost
		round_score = 0
	if diff == 1:  # Won
		round_score = 6
	# Lost
	return round_score + p2 + 1
