screen main_menu():
    add '#FAFAFA'
    add 'gui/window_icon.png' xalign 0.5 yalign 0.5

    vbox:
        style_group "main_menu"
        xalign 1.0
        yalign 1.0
        textbutton _("Start") action Start() xalign 1.0
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Extras") action None #ShowMenu("extras")
        # textbutton _("About") action ShowMenu("about")
        # textbutton _("Help") action ShowMenu("help")
        textbutton _("Quit") action Quit(confirm=not main_menu)
        null height 20
        text "version [config.version]" size 24

style main_menu_button:
    xalign 1.0
    padding (0,0)
    margin (0,0)

style main_menu_button_text:
    size 52
    color color.button
    hover_color color.hover
    insensitive_color color.disabled
