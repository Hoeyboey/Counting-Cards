input_data = []
other_players_cards = []
full_deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
inputting_data = True
inputting_other_players_data = True
acceptable_inputs = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A", "t", "j", "q", "k", "a"}
sum_if_making_ace_eleven = 0
distance_to_being_bust_if_ace_is_eleven = 0
number_of_possible_cards_you_could_draw_if_ace_is_eleven = 0
set_of_ten_value_cards = {"T", "J", "Q", "K"}
number_of_aces = 0
number_of_possible_cards_you_could_draw = 0
number_of_possible_cards_you_could_draw_counting_other_players_cards = 0
probability_of_going_over_21_if_ace_is_eleven_counting_other_players_cards = 0
number_of_possible_cards_you_could_draw_if_ace_is_eleven_counting_other_players_cards = 0

while inputting_data:
    card_input = input("Please input your next card, input 0 if you have nothing else to input:\n")
    if card_input != "0":
        if card_input in acceptable_inputs:
            input_data.append(card_input)
        else:
            print("That's not an acceptable input!")
    else:
        break

for x in range(len(input_data)):
    if input_data[x].upper() in set_of_ten_value_cards:
        input_data[x] = 10
    elif input_data[x].upper() == "A":
        input_data[x] = 1
        number_of_aces = number_of_aces+1
        full_deck.remove(1)
    else:
        input_data[x] = int(input_data[x])
        full_deck.remove(input_data[x])

sum_of_input_data = sum(input_data)

print("Current value of your hand is, at least, " + str(sum_of_input_data))
distance_to_being_bust = 22 - sum_of_input_data

for x in range(len(full_deck)):
    if full_deck[x]<distance_to_being_bust:
        number_of_possible_cards_you_could_draw += 1
    else:
        break

probability_of_going_over_21 = (number_of_possible_cards_you_could_draw / len(full_deck)) * 100
print("The probability of drawing a card that does not bring you over 21 is: " + str(round(probability_of_going_over_21, 2)) + "%")

if 1 in input_data:
    if sum_of_input_data + 10 < 22:
        sum_if_making_ace_eleven = sum_of_input_data + 10
        print("If you count an ace in your hand as eleven, the value of you hand is: " + str(sum_if_making_ace_eleven))
        if sum_if_making_ace_eleven == 21:
            print("However, counting an ace as eleven would bring your total to 21")
        distance_to_being_bust_if_ace_is_eleven = 22 - sum_if_making_ace_eleven
        for x in range(len(full_deck)):
            if full_deck[x] < distance_to_being_bust_if_ace_is_eleven:
                number_of_possible_cards_you_could_draw_if_ace_is_eleven += 1
            else:
                break
        probability_of_going_over_21_if_ace_is_eleven = (number_of_possible_cards_you_could_draw_if_ace_is_eleven / len(full_deck)) * 100
        print("The probability of drawing a card that does not bring you over 21 if you count an ace in your hand as eleven is: " + str(
            round(probability_of_going_over_21_if_ace_is_eleven, 2)) + "%")

while inputting_other_players_data:
    other_players_card_input = input("Please input the cards you know other players hold:\n")
    if other_players_card_input != "0":
        if other_players_card_input in acceptable_inputs:
            other_players_cards.append(other_players_card_input)
        else:
            print("That's not an acceptable input!")
    else:
        break

for x in range(len(other_players_cards)):
    if other_players_cards[x].upper() in set_of_ten_value_cards:
        other_players_cards[x] = 10
        full_deck.remove(10)
    elif other_players_cards[x].upper() == "A":
        other_players_cards[x] = 1
        full_deck.remove(1)
    else:
        other_players_cards[x] = int(other_players_cards[x])
        full_deck.remove(other_players_cards[x])

for x in range(len(full_deck)):
    if full_deck[x] < distance_to_being_bust:
        number_of_possible_cards_you_could_draw_counting_other_players_cards += 1
    else:
        break

probability_of_going_over_21_counting_other_players_cards = (number_of_possible_cards_you_could_draw_counting_other_players_cards / len(full_deck)) * 100
print("The probability of not going over 21 when including other players' cards is: " + str(probability_of_going_over_21_counting_other_players_cards) + "%")

if 1 in input_data:
    if sum_of_input_data + 10 < 22:
        sum_if_making_ace_eleven = sum_of_input_data + 10
        distance_to_being_bust_if_ace_is_eleven = 22 - sum_if_making_ace_eleven
        for x in range(len(full_deck)):
            if full_deck[x] < distance_to_being_bust_if_ace_is_eleven:
                number_of_possible_cards_you_could_draw_if_ace_is_eleven_counting_other_players_cards += 1
            else:
                break
        probability_of_going_over_21_if_ace_is_eleven_counting_other_players_cards = (number_of_possible_cards_you_could_draw_if_ace_is_eleven_counting_other_players_cards / len(full_deck)) * 100
        print("The probability of not going over 21 when including other players' cards and taking an ace in your hand to mean 11 is: " + str(probability_of_going_over_21_if_ace_is_eleven_counting_other_players_cards) + "%")

