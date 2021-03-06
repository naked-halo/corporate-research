﻿# This script loads first. DON'T MOVE THIS.

# Declare main characters

define r = Character("Riley", color="#31bf11")
define l = Character("Lily", color="#bf1111")

# Define unseen NPCs
define guard = Character("Guard")
define clerk = Character("Clerk")
define woman = Character("Woman")
define video = Character("Video")

#Define sprites

# Sprites are given definitions as follows:
# Pose -> Body type -> Clothing -> Expression

image lily base_body l_neutral = im.FactorScale("images/sprites/lily/base_body/l_neutral.png", 0.30)
# image riley Archive RileyP5-B5-C0-H1-E14 = im.FactorScale("images/sprites/riley/Archive/RileyP5-B5-C0-H1-E14.png", 0.30)
# image riley Archive r_neutral = im.FactorScale("images/sprites/riley/Archive/r_neutral.png", 0.30)
image riley big_breast clothed arms_sides smile = im.FactorScale("images/sprites/riley/big_breast/clothed/arms_sides/smile.png", 0.30)
image riley big_breast nude arms_above neutral = im.FactorScale("images/sprites/riley/big_breast/nude/arms_above/neutral.png", 0.30)
image riley big_breast nude arms_above question = im.FactorScale("images/sprites/riley/big_breast/nude/arms_above/question.png", 0.30)
image riley big_breast nude arms_above sad = im.FactorScale("images/sprites/riley/big_breast/nude/arms_above/sad.png", 0.30)
image riley big_breast nude arms_above smile = im.FactorScale("images/sprites/riley/big_breast/nude/arms_above/smile.png", 0.30)
image riley big_breast nude arms_above smirk = im.FactorScale("images/sprites/riley/big_breast/nude/arms_above/smirk.png", 0.30)
image riley big_breast nude arms_sides _A = im.FactorScale("images/sprites/riley/big_breast/nude/arms_sides/_A.png", 0.30)
image riley big_breast nude arms_sides neutral = im.FactorScale("images/sprites/riley/big_breast/nude/arms_sides/neutral.png", 0.30)
image riley big_breast nude arms_sides question = im.FactorScale("images/sprites/riley/big_breast/nude/arms_sides/question.png", 0.30)
image riley big_breast nude arms_sides sad = im.FactorScale("images/sprites/riley/big_breast/nude/arms_sides/sad.png", 0.30)
image riley big_breast nude arms_sides smile = im.FactorScale("images/sprites/riley/big_breast/nude/arms_sides/smile.png", 0.30)
image riley big_breast nude arms_sides smirk = im.FactorScale("images/sprites/riley/big_breast/nude/arms_sides/smirk.png", 0.30)
image riley body_start clothed arms_sides smile = im.FactorScale("images/sprites/riley/body_start/clothed/arms_sides/smile.png", 0.30)
image riley body_start nude arms_above neutral = im.FactorScale("images/sprites/riley/body_start/nude/arms_above/neutral.png", 0.30)
image riley body_start nude arms_above question = im.FactorScale("images/sprites/riley/body_start/nude/arms_above/question.png", 0.30)
image riley body_start nude arms_above sad = im.FactorScale("images/sprites/riley/body_start/nude/arms_above/sad.png", 0.30)
image riley body_start nude arms_above smile = im.FactorScale("images/sprites/riley/body_start/nude/arms_above/smile.png", 0.30)
image riley body_start nude arms_above smirk = im.FactorScale("images/sprites/riley/body_start/nude/arms_above/smirk.png", 0.30)
image riley body_start nude arms_sides neutral = im.FactorScale("images/sprites/riley/body_start/nude/arms_sides/neutral.png", 0.30)
image riley body_start nude arms_sides question = im.FactorScale("images/sprites/riley/body_start/nude/arms_sides/question.png", 0.30)
image riley body_start nude arms_sides sad = im.FactorScale("images/sprites/riley/body_start/nude/arms_sides/sad.png", 0.30)
image riley body_start nude arms_sides smile = im.FactorScale("images/sprites/riley/body_start/nude/arms_sides/smile.png", 0.30)
image riley body_start nude arms_sides smirk = im.FactorScale("images/sprites/riley/body_start/nude/arms_sides/smirk.png", 0.30)
image riley extra_fat nude arms_above smirk = im.FactorScale("images/sprites/riley/extra_fat/nude/arms_above/smirk.png", 0.30)
image riley futa_hard nude arms_above smirk = im.FactorScale("images/sprites/riley/futa_hard/nude/arms_above/smirk.png", 0.30)
image riley futa_soft nude arms_above smile = im.FactorScale("images/sprites/riley/futa_soft/nude/arms_above/smile.png", 0.30)
image riley preg_lactate nude arms_above smirk = im.FactorScale("images/sprites/riley/preg_lactate/nude/arms_above/smirk.png", 0.30)
image riley preg_one nude arms_above neutral = im.FactorScale("images/sprites/riley/preg_one/nude/arms_above/neutral.png", 0.30)
image riley preg_one nude arms_above question = im.FactorScale("images/sprites/riley/preg_one/nude/arms_above/question.png", 0.30)
image riley preg_one nude arms_above sad = im.FactorScale("images/sprites/riley/preg_one/nude/arms_above/sad.png", 0.30)
image riley preg_one nude arms_above smile = im.FactorScale("images/sprites/riley/preg_one/nude/arms_above/smile.png", 0.30)
image riley preg_one nude arms_above smirk = im.FactorScale("images/sprites/riley/preg_one/nude/arms_above/smirk.png", 0.30)
image riley preg_three nude arms_above neutral = im.FactorScale("images/sprites/riley/preg_three/nude/arms_above/neutral.png", 0.30)
image riley preg_three nude arms_above question = im.FactorScale("images/sprites/riley/preg_three/nude/arms_above/question.png", 0.30)
image riley preg_three nude arms_above sad = im.FactorScale("images/sprites/riley/preg_three/nude/arms_above/sad.png", 0.30)
image riley preg_three nude arms_above smile = im.FactorScale("images/sprites/riley/preg_three/nude/arms_above/smile.png", 0.30)
image riley preg_three nude arms_above smirk = im.FactorScale("images/sprites/riley/preg_three/nude/arms_above/smirk.png", 0.30)
image riley preg_two nude arms_above neutral = im.FactorScale("images/sprites/riley/preg_two/nude/arms_above/neutral.png", 0.30)
image riley preg_two nude arms_above question = im.FactorScale("images/sprites/riley/preg_two/nude/arms_above/question.png", 0.30)
image riley preg_two nude arms_above sad = im.FactorScale("images/sprites/riley/preg_two/nude/arms_above/sad.png", 0.30)
image riley preg_two nude arms_above smile = im.FactorScale("images/sprites/riley/preg_two/nude/arms_above/smile.png", 0.30)
image riley preg_two nude arms_above smirk = im.FactorScale("images/sprites/riley/preg_two/nude/arms_above/smirk.png", 0.30)
## BGs:
## CGs:
# image cg_boobjob_1 = im.FactorScale("images/CG/cg_boobjob_1.png", 0.30)
# image cg_boobjob_2 = im.FactorScale("images/CG/cg_boobjob_2.png", 0.30)
# image cg_boobjob_3 = im.FactorScale("images/CG/cg_boobjob_3.png", 0.30)
# image cg_boobjob_4 = im.FactorScale("images/CG/cg_boobjob_4.png", 0.30)
# image cg_boobjob_5 = im.FactorScale("images/CG/cg_boobjob_5.png", 0.30)
# image cg_boobjob_6 = im.FactorScale("images/CG/cg_boobjob_6.png", 0.30)
# image cg_boobjob_7 = im.FactorScale("images/CG/cg_boobjob_7.png", 0.30)
# image cg_fap1 = im.FactorScale("images/CG/cg_fap1.png", 0.30)
# image cg_fap2 = im.FactorScale("images/CG/cg_fap2.png", 0.30)
# image cg_fap3 = im.FactorScale("images/CG/cg_fap3.png", 0.30)
# image cg_fap4 = im.FactorScale("images/CG/cg_fap4.png", 0.30)
# image cg_fap5 = im.FactorScale("images/CG/cg_fap5.png", 0.30)
# image cg_fap6 = im.FactorScale("images/CG/cg_fap6.png", 0.30)
# image cg_fap7 = im.FactorScale("images/CG/cg_fap7.png", 0.30)
# image cg_fap8 = im.FactorScale("images/CG/cg_fap8.png", 0.30)
# image cg_ride1 = im.FactorScale("images/CG/cg_ride1.png", 0.30)
# image cg_ride10 = im.FactorScale("images/CG/cg_ride10.png", 0.30)
# image cg_ride2 = im.FactorScale("images/CG/cg_ride2.png", 0.30)
# image cg_ride3 = im.FactorScale("images/CG/cg_ride3.png", 0.30)
# image cg_ride4 = im.FactorScale("images/CG/cg_ride4.png", 0.30)
# image cg_ride5 = im.FactorScale("images/CG/cg_ride5.png", 0.30)
# image cg_ride6 = im.FactorScale("images/CG/cg_ride6.png", 0.30)
# image cg_ride7 = im.FactorScale("images/CG/cg_ride7.png", 0.30)
# image cg_ride8 = im.FactorScale("images/CG/cg_ride8.png", 0.30)
# image cg_ride9 = im.FactorScale("images/CG/cg_ride9.png", 0.30)

#Define CGs and backgrounds
image cg_boobjob_1 = im.FactorScale("/images/cg/cg_boobjob_1.png", 0.5)
image cg_boobjob_2 = im.FactorScale("/images/cg/cg_boobjob_2.png", 0.5)
image cg_boobjob_3 = im.FactorScale("/images/cg/cg_boobjob_3.png", 0.5)
image cg_boobjob_4 = im.FactorScale("/images/cg/cg_boobjob_4.png", 0.5)
image cg_boobjob_5 = im.FactorScale("/images/cg/cg_boobjob_5.png", 0.5)
image cg_boobjob_6 = im.FactorScale("/images/cg/cg_boobjob_6.png", 0.5)
image cg_boobjob_7 = im.FactorScale("/images/cg/cg_boobjob_7.png", 0.5)

#Define transforms
transform common(x = 0):
    subpixel True
    transform_anchor True
    xcenter 0.5
    yanchor 1.0
    ypos 1080
    on show:
        # This block is called when the image is first shown.
        alpha 0
        xoffset x
        linear 0.25 alpha 1
    on replaced:
        alpha 1
        linear 0.25 alpha 0
        ease 0.75 xoffset x
# This is so that characters don't blip out of existence.
transform transform_hide:
    on hide:
        linear 0.25 alpha 0

#This places characters in the center.
transform centered:
    common()

#This places characters on the center-right.
transform center_right:
    common(300)

#This places characters on the center-left.
transform center_left:
    common(-300)

#Define transitions
define titjobDissolve = MultipleTransition([
False, Dissolve (0.4),
im.FactorScale("/images/cg/cg_boobjob_2.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_boobjob_4.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_boobjob_5.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_boobjob_4.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_boobjob_2.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_boobjob_4.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_boobjob_5.png", 0.5), Dissolve (0.7),
True])

define rileyRideMountDissolve = MultipleTransition([
False, Dissolve (0.4),
im.FactorScale("/images/cg/cg_ride_2.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_ride_3.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_ride_4.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_ride_5.png", 0.5), Dissolve (0.7),
True])

# The game starts here.

label start:
    #sets up anything else in pre_start, then starts the game.
    call pre_start from _call_pre_start
    call real_start from _call_real_start
return
