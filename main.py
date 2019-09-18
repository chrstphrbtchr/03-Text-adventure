import sys, logging, json, os

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def render(game,current):
    '''Print out a description of the current location'''
    with open('THE_UNREAL_ESTATE.json') as json_file:        
        game = json.load(json_file)
        # I could not figure out a way to make this code run without
        # typing the above lines a lot, so sorry about that.
    r = game["rooms"]
    c = r[current]
    print("\n")
    print(c["name"])
    print(c["desc"])
    return True
    
def check_input(game, current, verbs):
    '''Request input from the player, validate the input'''
    user_input = input("Would you like to go NORTH, SOUTH, EAST, or WEST? ").strip().upper()
    with open('THE_UNREAL_ESTATE.json') as json_file:
            game = json.load(json_file)
    if (len(user_input)):
        user_input = normalizedVerb(user_input,game["verbs"])
    return user_input

def update(user_input, game, current, verb):
    with open('THE_UNREAL_ESTATE.json') as json_file:
        game = json.load(json_file)
    game["rooms"][current]["exits"]
    for e in game["rooms"][current]["exits"]:
        if user_input == e["verb"] and e['target'] !='NoExit':
            return e['target']
    else:
        print("\nYou shake your head and try again...")
        return current
    
def normalizedVerb(user_input, verbs):
    with open('THE_UNREAL_ESTATE.json') as json_file:
            game = json.load(json_file)
    for v in game["verbs"]:
        if user_input == v['v']:
            return v['map']
    return ""

    

def main():
    game = {}
    with open('THE_UNREAL_ESTATE.json') as json_file:
        game = json.load(json_file)

    current = "START"

    quit=False
    while not quit:

        #Render the world first
        with open('THE_UNREAL_ESTATE.json') as json_file:
            game = json.load(json_file)
        render(game['rooms'],current)
        #Check for player input
        with open('THE_UNREAL_ESTATE.json') as json_file:
            game = json.load(json_file)
        user_input = check_input(game["rooms"], current,game["verbs"])
        #Update the state of the world
        with open('THE_UNREAL_ESTATE.json') as json_file:
            game = json.load(json_file)
        current = update(user_input, game["rooms"], current, game["verbs"])

    return render


if __name__ == '__main__':
    main()