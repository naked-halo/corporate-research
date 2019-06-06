# This script loads first. DON'T MOVE THIS.

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
# Pose -> Body type -> Clothing -> Head -> Expression

#Riley Normal (B1)
image riley arms normal nude neutral = im.FactorScale("/images/sprites/riley/B1/RileyP0-B1-C0-H1-E1.png", 0.30)
image riley arms normal nude smile = im.FactorScale("/images/sprites/riley/B1/RileyP0-B1-C0-H1-E2.png", 0.30)
image riley arms normal nude sad = im.FactorScale("/images/sprites/riley/B1/RileyP0-B1-C0-H1-E3.png", 0.30)
image riley arms normal nude mad = im.FactorScale("/images/sprites/riley/B1/RileyP0-B1-C0-H1-E1.png", 0.30)
image riley arms normal nude surprise = im.FactorScale("/images/sprites/riley/B1/RileyP0-B1-C0-H1-E5.png", 0.30)
image riley arms normal nude embarassed = im.FactorScale("/images/sprites/riley/B1/RileyP0-B1-C0-H1-E1.png", 0.30)
image riley arms normal nude nervous = im.FactorScale("/images/sprites/riley/B1/RileyP0-B1-C0-H1-E1.png", 0.30)
image riley arms normal nude question = im.FactorScale("/images/sprites/riley/B1/RileyP0-B1-C0-H1-E1.png", 0.30)
image riley arms normal nude shrug = im.FactorScale("/images/sprites/riley/B1/RileyP0-B1-C0-H1-E1.png", 0.30)
image riley arms normal nude pout = im.FactorScale("/images/sprites/riley/B1/RileyP0-B1-C0-H1-E1.png", 0.30)
image riley arms normal nude laugh = im.FactorScale("/images/sprites/riley/B1/RileyP0-B1-C0-H1-E1.png", 0.30)
image riley arms normal nude nervous = im.FactorScale("/images/sprites/riley/B1/RileyP0-B1-C0-H1-E1.png", 0.30)
image riley arms normal nude smirk = im.FactorScale("/images/sprites/riley/B1/RileyP0-B1-C0-H1-E14.png", 0.30)
image riley raised normal nude neutral = im.FactorScale("/images/sprites/riley/B1/RileyP5-B1-C0-H1-E1.png", 0.30)
image riley raised normal nude smile = im.FactorScale("/images/sprites/riley/B1/RileyP5-B1-C0-H1-E2.png", 0.30)
image riley raised normal nude sad = im.FactorScale("/images/sprites/riley/B1/RileyP5-B1-C0-H1-E3.png", 0.30)
image riley raised normal nude mad = im.FactorScale("/images/sprites/riley/B1/RileyP5-B1-C0-H1-E1.png", 0.30)
image riley raised normal nude surprise = im.FactorScale("/images/sprites/riley/B1/RileyP5-B1-C0-H1-E5.png", 0.30)
image riley raised normal nude question = im.FactorScale("/images/sprites/riley/B1/RileyP5-B1-C0-H1-E1.png", 0.30)
image riley raised normal nude smirk = im.FactorScale("/images/sprites/riley/B1/RileyP5-B1-C0-H1-E14.png", 0.30)

#Riley w/ Bigger breasts (B2)
image riley arms bigboobs nude neutral = im.FactorScale("/images/sprites/riley/B2/RileyP0-B2-C0-H1-E1.png", 0.30)
image riley arms bigboobs nude smile = im.FactorScale("/images/sprites/riley/B2/RileyP0-B2-C0-H1-E2.png", 0.30)
image riley arms bigboobs nude sad = im.FactorScale("/images/sprites/riley/B2/RileyP0-B2-C0-H1-E3.png", 0.30)
image riley arms bigboobs nude mad = im.FactorScale("/images/sprites/riley/B2/RileyP0-B2-C0-H1-E1.png", 0.30)
image riley arms bigboobs nude surprise = im.FactorScale("/images/sprites/riley/B2/RileyP0-B2-C0-H1-E4.png", 0.30)
image riley arms bigboobs nude embarassed = im.FactorScale("/images/sprites/riley/B2/RileyP0-B2-C0-H1-E1.png", 0.30)
image riley arms bigboobs nude smirk = im.FactorScale("/images/sprites/riley/B2/RileyP0-B2-C0-H1-E14.png", 0.30)
image riley raised bigboobs nude neutral = im.FactorScale("/images/sprites/riley/B2/RileyP5-B2-C0-H1-E1.png", 0.30)
image riley raised bigboobs nude smile = im.FactorScale("/images/sprites/riley/B2/RileyP5-B2-C0-H1-E2.png", 0.30)
image riley raised bigboobs nude sad = im.FactorScale("/images/sprites/riley/B2/RileyP5-B2-C0-H1-E3.png", 0.30)
image riley raised bigboobs nude mad = im.FactorScale("/images/sprites/riley/B2/RileyP5-B2-C0-H1-E1.png", 0.30)
image riley raised bigboobs nude surprise = im.FactorScale("/images/sprites/riley/B2/RileyP5-B2-C0-H1-E4.png", 0.30)
image riley raised bigboobs nude embarassed = im.FactorScale("/images/sprites/riley/B2/RileyP5-B2-C0-H1-E1.png", 0.30)
image riley raised bigboobs nude smirk = im.FactorScale("/images/sprites/riley/B2/RileyP5-B2-C0-H1-E14.png", 0.30)

#Riley w/ Bigger breasts + Pregnancy (B3)
image riley arms smallpreg nude neutral = im.FactorScale("/images/sprites/riley/B3/RileyP0-B3-C0-H1-E1.png", 0.30)
image riley arms smallpreg nude smile = im.FactorScale("/images/sprites/riley/B3/RileyP0-B3-C0-H1-E2.png", 0.30)
image riley arms smallpreg nude sad = im.FactorScale("/images/sprites/riley/B3/RileyP0-B3-C0-H1-E3.png", 0.30)
image riley arms smallpreg nude mad = im.FactorScale("/images/sprites/riley/B3/RileyP0-B3-C0-H1-E1.png", 0.30)
image riley arms smallpreg nude surprise = im.FactorScale("/images/sprites/riley/B3/RileyP0-B3-C0-H1-E5.png", 0.30)
image riley arms smallpreg nude embarassed = im.FactorScale("/images/sprites/riley/B3/RileyP0-B3-C0-H1-E1.png", 0.30)
image riley arms smallpreg nude smirk = im.FactorScale("/images/sprites/riley/B3/RileyP0-B3-C0-H1-E14.png", 0.30)

#Riley w/ Bigger breasts + Pregnancy (B4)
image riley arms medpreg nude neutral = im.FactorScale("/images/sprites/riley/B4/RileyP0-B4-C0-H1-E1.png", 0.30)
image riley arms medpreg nude smile = im.FactorScale("/images/sprites/riley/B4/RileyP0-B4-C0-H1-E2.png", 0.30)
image riley arms medpreg nude sad = im.FactorScale("/images/sprites/riley/B4/RileyP0-B4-C0-H1-E3.png", 0.30)
image riley arms medpreg nude mad = im.FactorScale("/images/sprites/riley/B4/RileyP0-B4-C0-H1-E1.png", 0.30)
image riley arms medpreg nude surprise = im.FactorScale("/images/sprites/riley/B4/RileyP0-B4-C0-H1-E5.png", 0.30)
image riley arms medpreg nude embarassed = im.FactorScale("/images/sprites/riley/B4/RileyP0-B4-C0-H1-E1.png", 0.30)
image riley arms medpreg nude smirk = im.FactorScale("/images/sprites/riley/B4/RileyP0-B2-C0-H1-E14.png", 0.30)

#Riley w/ Bigger breasts + Pregnancy (B5) + lactation
image riley arms bigpreg nude neutral = im.FactorScale("/images/sprites/riley/B5/RileyP0-B5-C0-H1-E1.png", 0.30)
image riley arms bigpreg nude smile = im.FactorScale("/images/sprites/riley/B5/RileyP0-B5-C0-H1-E2.png", 0.30)
image riley arms bigpreg nude sad = im.FactorScale("/images/sprites/riley/B5/RileyP0-B5-C0-H1-E3.png", 0.30)
image riley arms bigpreg nude mad = im.FactorScale("/images/sprites/riley/B5/RileyP0-B5-C0-H1-E1.png", 0.30)
image riley arms bigpreg nude surprise = im.FactorScale("/images/sprites/riley/B5/RileyP0-B5-C0-H1-E4.png", 0.30)
image riley arms bigpreg nude embarassed = im.FactorScale("/images/sprites/riley/B5/RileyP0-B5-C0-H1-E1.png", 0.30)
image riley arms bigpreg nude smirk = im.FactorScale("/images/sprites/riley/B5/RileyP0-B5-C0-H1-E14.png", 0.30)

#Riley w/ Addl. Fat (B6)
image riley fatboobneutral = "/images/sprites/riley/r_neutral.png"
image riley fatboobsmile = "/images/sprites/riley/r_neutral.png"
image riley fatbooblaugh = "/images/sprites/riley/r_neutral.png"
image riley fatboobneutralcrossed = "/images/sprites/riley/r_neutral.png"
image riley fatboobsmilecrossed = "/images/sprites/riley/r_neutral.png"
image riley fatbooblaughcrossed = "/images/sprites/riley/r_neutral.png"
image riley fatboobshrug = "/images/sprites/riley/r_neutral.png"
image riley fatboobquestion = "/images/sprites/riley/r_neutral.png"
image riley fatboobsurprised = "/images/sprites/riley/r_neutral.png"
image riley fatboobsmirk = "/images/sprites/riley/r_neutral.png"

#Riley w/ Addl. Fat + Penis (B7)
image riley fatfutaneutral = "/images/sprites/riley/r_neutral.png"
image riley fatfutasmile = "/images/sprites/riley/r_neutral.png"
image riley fatfutasad = "/images/sprites/riley/r_neutral.png"
image riley fatfutaembarassed = "/images/sprites/riley/r_neutral.png"
image riley fatfutalaugh = "/images/sprites/riley/r_neutral.png"
image riley fatfutaneutralcrossed = "/images/sprites/riley/r_neutral.png"
image riley fatfutasmilecrossed = "/images/sprites/riley/r_neutral.png"
image riley fatfutasadcrossed = "/images/sprites/riley/r_neutral.png"
image riley fatfutalaughcrossed = "/images/sprites/riley/r_neutral.png"
image riley fatfutashrug = "/images/sprites/riley/r_neutral.png"
image riley fatfutaquestion = "/images/sprites/riley/r_neutral.png"
image riley fatfutanervous = "/images/sprites/riley/r_neutral.png"
image riley fatfutaarousedpants = "/images/sprites/riley/r_neutral.png"
image riley fatfutaarousednipple = "/images/sprites/riley/r_neutral.png"
image riley fatfutasmilepenis = "/images/sprites/riley/r_neutral.png"
image riley fatfutalipspenis = "/images/sprites/riley/r_neutral.png"

#Lily Normal (B1)
image lily neutral = "/images/sprites/lily/l_neutral.png"
image lily frown = "/images/sprites/lily/l_neutral.png"
image lily surprised = "/images/sprites/lily/l_neutral.png"
image lily smallsmile = "/images/sprites/lily/l_neutral.png"
image lily neutralhips = "/images/sprites/lily/l_neutral.png"
image lily frownhips = "/images/sprites/lily/l_neutral.png"
image lily surprisedhips = "/images/sprites/lily/l_neutral.png"
image lily smallsmilehips = "/images/sprites/lily/l_neutral.png"
image lily inhaleecig = "/images/sprites/lily/l_neutral.png"
image lily exhaleecig = "/images/sprites/lily/l_neutral.png"

#Lily + Penis (B2)
image lily futaneutral = "/images/sprites/lily/l_neutral.png"
image lily futafrown = "/images/sprites/lily/l_neutral.png"
image lily futasurprised = "/images/sprites/lily/l_neutral.png"
image lily futasmallsmile = "/images/sprites/lily/l_neutral.png"
image lily futaneutralhips = "/images/sprites/lily/l_neutral.png"
image lily futafrownhips = "/images/sprites/lily/l_neutral.png"
image lily futasurprisedhips = "/images/sprites/lily/l_neutral.png"
image lily futasmallsmilehips = "/images/sprites/lily/l_neutral.png"
image lily futainhaleecig = "/images/sprites/lily/l_neutral.png"
image lily futaexhaleecig = "/images/sprites/lily/l_neutral.png"
image lily futaembarassed = "/images/sprites/lily/l_neutral.png"
image lily futaaroused = "/images/sprites/lily/l_neutral.png"

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
define titjobdissolve = MultipleTransition([
False, Dissolve (0.4),
im.FactorScale("/images/cg/cg_boobjob_2.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_boobjob_4.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_boobjob_5.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_boobjob_4.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_boobjob_2.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_boobjob_4.png", 0.5), Dissolve (0.7),
im.FactorScale("/images/cg/cg_boobjob_5.png", 0.5), Dissolve (0.7),
True])

# The game starts here.

label start:
    #sets up anything else in pre_start, then starts the game.
    call pre_start
    call real_start
return
