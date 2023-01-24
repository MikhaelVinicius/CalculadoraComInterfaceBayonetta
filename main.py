from calculadora import make_root, make_display, Mlabel, make_buttons
from classe_Calculadora import Calcu
def main():

    root = make_root()
    display = make_display(root)
    label = Mlabel(root)
    buttons = make_buttons(root)
    calcu = Calcu(root,label,display,buttons)
    calcu.start()



main()