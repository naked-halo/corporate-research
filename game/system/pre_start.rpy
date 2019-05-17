# Rollback is enabled in developer mode since it's useful.
# In the release version, the mousewheel up opens the history screen instead of rolling back.

label pre_start:
    if config.developer:
        $ config.rollback_enabled = True
    show screen key_overlay
    return
