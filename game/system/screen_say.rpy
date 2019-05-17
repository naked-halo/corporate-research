screen say(who, what):
    frame:
        background "gui/screen_say_background.png"
        xalign 0.5
        yalign 1.0
        ysize 305

        if who is not None:
            text who.upper() id "who"

        # say text yoffset changes if there's a name or not
        $ say_text_yoffset = 170 if who != None else 140
        text what id "what" yoffset say_text_yoffset

        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0

        hbox:
            style_group "say_quick_menu"
            xalign 1.0
            yalign 1.0
            spacing 10
            yoffset -170

            textbutton _("history") action Show('history')
            textbutton _("skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("auto") action Preference("auto-forward", "toggle")
            textbutton _("save") action [FileTakeScreenshot(), Show('save')]
            textbutton _("load") action Show('load')
            textbutton _("options") action Show('preferences')

style say_label is default_bold
style say_label is outlined
style say_label:
    color color.button
    size 44
    xoffset 300
    yoffset 100

style say_dialogue is default_text
style say_dialogue is outlined
style say_dialogue:
    xsize 1250
    xoffset 340

style say_quick_menu_button_text is default_text
style say_quick_menu_button_text is outlined
style say_quick_menu_button_text is hoverable
style say_quick_menu_button_text:
    size 28
