screen choice(items):
    use modal_background
    modal True

    vbox:
        style_group "choice"
        xalign 0.5
        yalign 0.5

        for i in items:
            frame:
                add 'gui/choice_button.png' xalign 0.5 yalign 0.5
                textbutton i.caption action i.action
            null height 36

style choice_frame:
    background None
    padding (0,0)
    margin (0,0)
    xalign 0.5
    ymaximum 105

style choice_button_text is outlined
style choice_button_text:
    color color.button
    hover_color color.hover
    font font.bold
    yoffset -6

style choice_button:
    xalign 0.5
    yalign 0.5
