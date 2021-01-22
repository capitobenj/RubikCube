from Classes.rubikcube import rbcube
from Classes.tabcompletion import MyCompleter
cube = rbcube()


def main(cube):
    actions = ['print', 'rotate left', 'rotate right', 'change to face']
    completer = MyCompleter(actions)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    while True:
        input = raw_input("Input: ")
        if input is actions[0]:
            cube.print_all()
        elif input is actions[1]:
            break
        elif input is actions[2]:
            row = raw_input("Wich row you wanna rotate? ")
            cube.rotate_right(row)
            cube.print_all()
        elif input is actions[3]:
            face = raw_input("Wich face you wanna face??")
            cube.change_face(face)
            cube.print_all()
        
        
