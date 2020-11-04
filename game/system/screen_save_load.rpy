screen save():
    use modal_background
    add "gui/screen_saveload_background.png" at pop
    modal True

    use file_slots(_("Save"))

screen load():
    use modal_background
    add "gui/screen_saveload_background.png" at pop
    modal True

    use file_slots(_("Load"))


screen file_slots(title):
    vbox:
        at pop
        xfill True

        null height 220
        hbox:
            spacing 40
            xalign 0.5
            for i in range(3):
                $ slot = i + 1
                $ slot_number = FileSlotName(slot, 3, auto="autosave")
                button:
                    xysize (375,200)
                    add 'gui/save_slot.png'
                    add FileScreenshot(slot) xoffset 4 yoffset 3

                    text FileTime(slot, format="{}. %b %d %Y, %I:%M%p".format(slot_number), empty="{}. Empty Save Slot".format(slot_number)) size 24 color "#a5c7df" yoffset 232 xsize 400 text_align 0.5

                    key "save_delete" action FileDelete(slot)
                    action FileAction(slot)
                null height 70

        use popup_controls(title.lower())

        hbox:
            spacing 1350
            xalign 0.5
            yoffset -200
            xoffset 3
            imagebutton idle 'gui/left_arrow_idle.png' hover 'gui/left_arrow_hover.png' action FilePagePrevious()
            imagebutton idle 'gui/right_arrow_idle.png' hover 'gui/right_arrow_hover.png' action FilePageNext()
