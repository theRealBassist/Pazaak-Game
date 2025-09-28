import curses
from curses import wrapper

CARD_SIZE = (7, 8)
CARD_SHAPE = (" _____ \n" \
             "|     |\n" \
             "|     |\n" \
             "|     |\n" \
             "|     |\n" \
             "|_____|\n")


def main(stdscr):
    # stdscr.clear()
    # stdscr.addstr(0,0,"parent")
    # stdscr.refresh()                # draw parent first

    # card = curses.newwin(3, 10, 2, 2)
    # card.addstr(0,0,"child")
    # card.refresh()                  # draw child last so it's visible
    # stdscr.getch()

    stdscr.clear()
    stdscr.refresh()

    cards = []
    x = 0
    while x < 3:
        y=0
        while y < 3:
            card = curses.newwin(CARD_SIZE[0], CARD_SIZE[1], y*CARD_SIZE[0], x*CARD_SIZE[1])
            card.addstr(0,0, CARD_SHAPE)
            cards.append(card)
            y += 1
        x += 1
    
    for card in cards:
        card.refresh()
    
    stdscr.getch()

wrapper(main)