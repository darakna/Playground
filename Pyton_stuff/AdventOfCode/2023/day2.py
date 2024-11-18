def check_validity(hands):
    for hand in hands:
        cubes = hand.split(", ")
        #print(cubes)
        for cube in cubes:
            cube_values = cube.split()
            if conditions[cube_values[1]]<int(cube_values[0]):
                return 0
    return 1


def get_power(hands):
    minimal_conditions = {"red":0,
                          "green":0,
                          "blue":0}
    for hand in hands:
        cubes = hand.split(", ")
        for cube in cubes:
            cube_values = cube.split()
            if minimal_conditions[cube_values[1]]<int(cube_values[0]):
                 minimal_conditions[cube_values[1]] = int(cube_values[0])
    return minimal_conditions["red"] * minimal_conditions["green"] * minimal_conditions["blue"]
    


def game_validation(game):
    game_id = 0
    hands = game.strip("\n").split(": ")[1].split("; ")
    game_id = int(game.split(":")[0].split()[1])
    is_valid = check_validity(hands)
    #print("Game id: {}, Games: {}, Line: {}".format(game_id, hands, game))
    power = get_power(hands)
    #print(power, hands)
    return game_id * is_valid, power



def check_games(values):
    sum = 0
    sum2= 0
    for line in values:
        value, power = game_validation(line)
        sum += value
        sum2 += power
    return sum, sum2



conditions = {"red":12,
              "green":13,
               "blue":14}
value_file = r"E:\Programare\Playground\Pyton_stuff\AdventOfCode\2023\input_day2.txt"
filereader = open(value_file)
values = filereader.readlines()
print(check_games(values))