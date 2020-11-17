#Chars
define e = Character(("Sol"), what_color="#BD1518")
define i = Character ("", what_color="#BD1518")


# The game starts here.
label start:
    scene bg sunset

    show sol

    # dialogue

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # End of game.

    return
