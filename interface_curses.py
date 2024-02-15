import curses

def main(stdscr):
    # Efface l'écran et affiche une chaîne de bienvenue
    stdscr.clear()
    stdscr.addstr(0, 0, "Bienvenue dans mon application !")
    stdscr.refresh()

    # Boucle principale pour traiter les entrées utilisateur
    while True:
        # Attend une entrée utilisateur
        key = stdscr.getch()

        # Si l'utilisateur appuie sur 'q', quitte l'application
        if key == ord('q'):
            break
        else:
            # Affiche la touche pressée par l'utilisateur
            stdscr.addstr(2, 0, f"Touche pressée : {chr(key)}")
            stdscr.refresh()

# Exécute la fonction principale avec l'interface curses
curses.wrapper(main)
