transform popup_transform:
    on show:
        xalign .98 
        yalign -.3 
        linear 0.4 xalign .98 yalign .02
    on hide:
        linear 0.4 xalign 1.9 yalign .02

screen scr_episode_get(title, trans=popup_transform):
    timer 2.4 action Hide("scr_episode_get")
    window:
        at trans
        background "#333333cc"
        xysize (400, 100)
        text title:
            xalign 0.5
            yalign 0.5
            size 30
            id title

init python:
    def get_epsiode(title, trans=popup_transform):
        persistent.ep2 = True
        renpy.show_screen(_screen_name='scr_episode_get', title=title, trans=trans)
