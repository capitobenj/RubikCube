from Classes.rubikcube import rbcube
from Classes.tabcompletion import MyCompleter
import readline
cube = rbcube() 

def main(cube):
    actions = ["print", "rotate-left", "rotate-right", "change to face", "exit"]
    completer = MyCompleter(actions)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    while True:
        value = input("Action (Tab for options): ")
        if value in actions:
            if value == actions[0]:
                cube.print_all()
            elif value == actions[1]:
                row = input("row to rotate: ")
                cube.rotate_left(int(row))
                cube.print_all()
            elif value == actions[2]:
                row = input("row to rotate: ")
                cube.rotate_right(int(row))
                cube.print_all()
            elif value == actions[3]:
                face = input("Face: ")
                cube.change_face(int(face))
                cube.print_all()
            elif value == 'exit':
                break
main(cube)
