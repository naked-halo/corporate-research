screen confirm(message, yes_action, no_action):
    use modal_background
    add "gui/screen_confirm_background.png" at pop
    modal True

    frame:
        background None
        at pop
        xysize (800,500)

        text _(message) xalign 0.5 yalign 0.5 xsize 780 yoffset -20

        hbox:
            style_group "options_control"
            xalign 0.5
            spacing 20
            yalign 0.70

            textbutton _("YES") action yes_action
            textbutton _("NO") action no_action
            key "mouseup_3" action no_action
            key "game_menu" action no_action
