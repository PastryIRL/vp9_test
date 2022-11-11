# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

image vp9test_vid = Movie(play="vp9test_1.webm")
image vp8test_vid = Movie(play="vp8test_1.webm")

label start:


    scene bg black

    "This is a demo to showcase the problem with laggy VP9 playback in RenPy 8.0.3. Same video plays smoothly in 7.4.11."
    
    scene vp9test_vid
    with dissolve 

    pause

    "As you can see, the playback suffers from some serious frame drop."
    "Let's try the same video in VP8 format."

    scene vp8test_vid
    with dissolve

    pause

    "This is what it should look like. No frame drop."
    "The same VP9 video plays smoothly in RenPy 7.4.11, but not in 8.0.3."
    "Feel free to rollback to the previous video and compare the two."
    "Additionally, this project is compatible with both RenPy versions, so you can run it on both and compare the results."


    # This ends the game.

    return
