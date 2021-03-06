import requests
import random


def generate_random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    res = requests.get(url)
    pokemon = res.json()
    return {
        'name': pokemon['name'],
        'exp': pokemon['base_experience'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }


def find_pokemon():
    print('Your Pokemon choices are:')
    pokemon_data = []
    for x in range(3):
        random_pokemon = generate_random_pokemon()
        pokemon_data.append(random_pokemon)
        print((x+1), random_pokemon['name'])
    pokemon_choice = str(input('Which one would you like to choose? Select a number... \n'))
    if pokemon_choice == '1':
        return pokemon_data[0]
    if pokemon_choice == '2':
        return pokemon_data[1]
    if pokemon_choice == '3':
        return pokemon_data[2]
    else:
        print('You have entered an incorrect value, let\'s try again \n')
        run()


def coin_toss():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'heads'
    if flip == 1:
        return 'tails'


def opponent_stat_choice():
    choice = random.randint(0, 2)
    if choice == 0:
        return 'exp'
    if choice == 1:
        return 'height'
    if choice == 2:
        return 'weight'


def finish_game():
    end_choice = input('Would you like to play again? \n yes (y) or no (n) \n')
    if end_choice == 'y' or end_choice == 'yes':
        print('\n')
        run()
    else:
        return


def run():
    print('Welcome to Pokemon Top Trumps! Best of three wins, good luck and may the odds be in your favour!')
    my_pokemon = find_pokemon()
    print('You have chosen {}'.format(my_pokemon['name']))
    opponent_pokemon = generate_random_pokemon()
    print('Your opponent\'s Pokemon is {}'.format(opponent_pokemon['name']))
    my_coin_pick = str(input('This coin toss will determine if you can choose a stat or your opponent chooses, '
                             'please choose: \n heads or \n tails \n'))

    if my_coin_pick != 'heads' and my_coin_pick != 'tails':
        print('Oops there seems to be an error, let\'s try that again \n')
        run()

    if my_coin_pick == coin_toss():
        stat_choice = input('You win the coin toss, which stat do you want to use? '
                            'You can choose between: '
                            '\n exp (The base experience gained for defeating this Pokémon) '
                            '\n height (The height of this Pokémon in decimetres) '
                            '\n weight (The weight of this Pokémon in hectograms.) \n')

        my_stat = my_pokemon[stat_choice]
        opponent_stat = opponent_pokemon[stat_choice]
        result_message = 'Your Pokemon\'s {} is {} and your opponent\'s {} is {}' \
            .format(stat_choice, my_stat, stat_choice, opponent_stat)
        print(result_message)

        if my_stat > opponent_stat:
            print('You win!')
            finish_game()
        if my_stat < opponent_stat:
            print('Sadly, you lose')
            finish_game()
        if my_stat == opponent_stat:
            print('It\'s a tie, let\'s try again')
            run()
    else:
        opponent_choice = opponent_stat_choice()
        print('You lose the coin toss, your opponent chooses the {} stat'.format(opponent_choice))
        my_stat = my_pokemon[opponent_choice]
        opponent_stat = opponent_pokemon[opponent_choice]
        result_message = 'Your Pokemon\'s {} is {} and your opponent\'s {} is {}' \
            .format(opponent_choice, my_stat, opponent_choice, opponent_stat)
        print(result_message)

        if my_stat > opponent_stat:
            print('You win!')
            finish_game()
        if my_stat < opponent_stat:
            print('Sadly, you lose')
            finish_game()
        if my_stat == opponent_stat:
            print('It\'s a tie, let\'s try again \n')
            run()


run()
