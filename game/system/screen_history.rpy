# TODO polish scrollbar and relocate related all code to this file
# define gui.history_scrollbar = Borders(14, 18, 14, 18)

screen history():
    use modal_background
    add "gui/screen_history_background.png" at pop
    modal True
    predict False

    frame:
        at pop
        background None
        padding (20,20)
        xysize (1060,630)

        vbox:
            yoffset -20
            spacing 40
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                side_yfill True
                yinitial 1.0

                vbox:
                    spacing 60
                    for h in _history_list:
                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)

                        if h.who:
                            hbox:
                                spacing 30
                                text h.who color color.button font font.bold size 32 xsize 300
                                text '"' + what + '"' color color.text font font.regular size 28
                        else:
                            text what color color.text font font.regular size 28

                    if not _history_list:
                        label _("The dialogue history is empty.")

            use popup_controls('history')
