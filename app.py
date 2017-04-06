input_data = []
other_players_cards = []
full_deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
             10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
acceptable_inputs = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A", "t", "j", "q", "k", "a"}
set_of_ten_value_cards = {"T", "J", "Q", "K"}
global number_of_possible_cards_you_could_draw_if_ace_is_eleven
global number_of_possible_cards_you_could_draw
global number_of_aces
global sum_of_input_data


# This is mostly here for the future when I make this much more usable
def reset_deck():
    full_deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9,
                 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


# This method allows you to input the cards in your hand, returning the total value of your hand and the number of aces
# in it, updating the full_deck list with this info
def create_new_hand():
    number_of_aces = 0
    while True:
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
            number_of_aces = number_of_aces + 1
            full_deck.remove(1)
        else:
            input_data[x] = int(input_data[x])
            full_deck.remove(input_data[x])

    sum_of_input_data = sum(input_data)
    return sum_of_input_data, number_of_aces


# Simply prints out value of your hand, pretty useless, to be honest, but here for posterity
def current_value_of_hand(sum_of_input_data):
    print("Current value of your hand is, at least, " + str(sum_of_input_data))

# The cool bit - this is where it calculates the probably that you draw a card that won't bring you over 21. This is
# actually a very basic and bad way to count cards, and next step is bringing in the high/low card counting system.
def calculate_probabilities(sum_of_input_data, number_of_aces):
    number_of_possible_cards_you_could_draw = 0
    number_of_possible_cards_you_could_draw_if_ace_is_eleven = 0
    distance_to_being_bust = 22 - sum_of_input_data
    for x in range(len(full_deck)):
        if full_deck[x] < distance_to_being_bust:
            number_of_possible_cards_you_could_draw += 1
        else:
            break

    probability_of_going_over_21 = (number_of_possible_cards_you_could_draw / len(full_deck)) * 100
    print("The probability of drawing a card that does not bring you over 21 is: " + str(
        round(probability_of_going_over_21, 2)) + "%")

    if number_of_aces > 0 and sum_of_input_data + 10 < 22:
        sum_if_making_ace_eleven = sum_of_input_data + 10
        print("If you count an ace in your hand as eleven, the value of you hand is: " + str(
            sum_if_making_ace_eleven))
        if sum_if_making_ace_eleven == 21:
            print("However, counting an ace as eleven would bring your total to 21")
        distance_to_being_bust_if_ace_is_eleven = 22 - sum_if_making_ace_eleven
        for x in range(len(full_deck)):
            if full_deck[x] < distance_to_being_bust_if_ace_is_eleven:
                number_of_possible_cards_you_could_draw_if_ace_is_eleven += 1
            else:
                break
        probability_of_going_over_21_if_ace_is_eleven = (
                                                        number_of_possible_cards_you_could_draw_if_ace_is_eleven / len(
                                                            full_deck)) * 100
        print(
            "The probability of drawing a card that does not bring you over 21 if you count an ace in your hand as eleven is: " + str(
                round(probability_of_going_over_21_if_ace_is_eleven, 2)) + "%")


def remove_other_players_cards_from_deck():
    while True:
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


# The main method, calls upon the methods above. Do I need to explain that?
def main():
    value_of_hand, no_aces_in_hand = create_new_hand()
    current_value_of_hand(value_of_hand)
    while True:
        other_cards_availableyn = input("Do you have any cards from your opponents' hands to put in? Y/N\n")
        if other_cards_availableyn == "Y" or other_cards_availableyn == "y":
            remove_other_players_cards_from_deck()
            break
        elif other_cards_availableyn == "N" or other_cards_availableyn == "n":
            break
        else:
            print("Uh. Sorry, we didn't recognise what you just said. Try again?")
            continue
    calculate_probabilities(value_of_hand, no_aces_in_hand)


main()
