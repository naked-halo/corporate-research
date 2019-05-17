# common/reused screens

screen key_overlay():
    key "mouseup_3" action Show("preferences")
    if not config.developer:
        key "mouseup_4" action Show("history")

screen modal_background():
    add "#0008" at modal_fade

screen popup_controls(screen_name):
    hbox:
        xalign 0.5
        style_group "options_control"
        spacing 30
        if not renpy.context()._menu:
            textbutton "TITLE" action MainMenu()
        textbutton "CLOSE" action Hide(screen_name)
    key "mouseup_3" action Hide(screen_name)

# common transforms, unique behaviours should be set up in their respective files

transform pop(z=0.85):
    xalign 0.5
    yalign 0.5
    on show:
        alpha 0.0
        zoom z

        parallel:
            easein 0.35 zoom 1.0

        parallel:
            easein 0.35 alpha 1.0

    on hide:
        alpha 1.0
        zoom 1.0

        parallel:
            easeout 0.35 zoom z
        parallel:
            easeout 0.35 alpha 0.0

transform modal_fade:
    on show:
        easein 0.5 alpha 1.0

    on hide:
        easein 0.5 alpha 0.0

transform center_center():
    xalign 0.5
    yalign 0.5
