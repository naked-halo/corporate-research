# TODO Text Speed and Auto Text Speed are ambigious, consider adding tooltips
screen preferences():
    use modal_background
    add "gui/screen_options_background.png" at pop
    modal True

    frame:
        at pop
        background None
        xysize (640, 500)

        vbox:
            style_group "options"
            yoffset 30
            spacing 75

            bar value Preference("music volume")
            bar value Preference("text speed")
            bar value Preference("auto-forward time")

            $ fullscreen_toggle = 'gui/toggle_on.png' if store._preferences.fullscreen else 'gui/toggle_off.png'
            imagebutton idle fullscreen_toggle action[Preference("display", "toggle")]

            use popup_controls('preferences')

style options_image_button:
    xoffset 170

style options_slider:
    thumb None
    left_bar "gui/bar_full.png"
    right_bar "gui/bar_empty.png"
    xoffset 170
