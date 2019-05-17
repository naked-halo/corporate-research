init python:
    if config.developer:
        # Pressing F5 quits the game, no questions asked. Only used for developer purposes.
        config.underlay.append(renpy.Keymap(K_F5=Quit(confirm=False)))
