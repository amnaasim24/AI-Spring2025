total_cards = 52
red_cards = 26
hearts = 13
face_cards = 12
diamond_face_cards = 3
queen_cards = 4
spade_face_cards = 3
queen_of_spades = 1

p_red = red_cards / total_cards

p_heart_given_red = hearts / red_cards

p_diamond_given_face = diamond_face_cards / face_cards

unique_favorable = spade_face_cards + queen_cards - queen_of_spades
p_spade_or_queen_given_face = unique_favorable / face_cards

print("P(Red card) =", p_red)
print("P(Heart | Red card) =", p_heart_given_red)
print("P(Diamond | Face card) =", p_diamond_given_face)
print("P(Spade or Queen | Face card) =", p_spade_or_queen_given_face)