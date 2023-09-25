
import urwid

# menus class
class GUI():
    def __init__(self, init):
        self.init = init


def main_Menu():
    
    choices = u'Show database New entry Update entry Delete entry Token search'.split()

    def menu(title, choices):
        body = [urwid.Text(title), urwid.Divider()]
        for c in choices:
            button = urwid.Button(c)
            urwid.connect_signal(button, 'click', item_chosen, c)
            body.append(urwid.AttrMap(button, None, focus_map='reversed'))
        return urwid.ListBox(urwid.SimpleFocusListWalker(body))

    def item_chosen(button, choice):
        response = urwid.Text([u'You chose ', choice, u'\n'])
        done = urwid.Button(u'Ok')
        urwid.connect_signal(done, 'click', exit_program)
        mainscreen.original_widget = urwid.Filler(urwid.Pile([response,
            urwid.AttrMap(done, None, focus_map='reversed')]))

    def exit_program(button):
        raise urwid.ExitMainLoop()

    mainscreen = urwid.Padding(menu(u'Choose option', choices), left=2, right=2)
    top = urwid.Overlay(mainscreen, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
        align='center', width=('relative', 60),
        valign='middle', height=('relative', 60),
        min_width=20, min_height=9)
    urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()

    return