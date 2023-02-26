transform achievement_transform:
    on show:
        xalign .98 
        yalign -.3 
        linear 0.4 xalign .98 yalign .02
    on hide:
        linear 0.4 xalign 1.9 yalign .02

screen scr_achievement_get(title, a_text, icon, trans=achievement_transform):
    timer 2.4 action Hide("scr_achievement_get")
    window:
        at trans
        background "#333333cc"
        xalign .98
        yalign .02
        xysize (450, 100)
        hbox:
            vbox:
                spacing 10
                image icon
            vbox:
                xoffset 10
                xsize 330
                text title:
                    size 28
                    id title
                text a_text:
                    size 22
                    id a_text

screen scr_achievement_update(title, a_text, icon, cur_prog, max_prog, trans=achievement_transform):
    timer 2.4 action Hide("scr_achievement_update")
    window:
        at trans
        background "#333333cc"
        xalign .98
        yalign .02
        xysize (450, 100)

        #

        hbox:
            vbox:
                spacing 10
                image icon
                text "{0}/{1}".format(cur_prog, max_prog):
                    xcenter 0.5 
                    ycenter 0.2
            vbox:
                xoffset 10
                xsize 330
                text title:
                    size 28
                    id title
                text a_text:
                    size 22
                    id a_text


                



init python:
    def get_achievement(ach_id, trans=achievement_transform):
        ach = persistent.achievements_dict[ach_id]
        achievement.grant(ach_id)
        renpy.show_screen(_screen_name='scr_achievement_get', title=ach['title'],
                        a_text=ach['text'], icon=ach['icon'], trans=trans)

    def update_achievement(ach_id, to_add=1, trans=achievement_transform):
        persistent.achievements_dict[ach_id]["cur_prog"] += to_add
        ach = persistent.achievements_dict[ach_id]

        achievement.progress(ach_id, to_add)
        if ach['cur_prog'] > ach['max_prog']:
            persistent.achievements_dict[ach_id]["cur_prog"] = ach['max_prog']
            ach = persistent.achievements_dict[ach_id]

        renpy.show_screen(_screen_name='scr_achievement_update', title=ach['title'], a_text=ach['text'],
                        icon=ach['icon'], cur_prog=ach['cur_prog'], max_prog=ach['max_prog'], trans=trans)





    # Define your achievements here
    persistent.achievements_dict = {"test1": {"type": 0, # One time achievement
                                                            "title": "Yay!", # Also name for steam
                                                            "text": "Wow you've achieved!", # description
                                                            "icon": "images/icons/ach1.png" # 96x96 image
                                                            },
                                        "test2": {"type": 1, # Progress achievement
                                                            "title": "Progress!",
                                                            "text": "Making progress...",
                                                            "icon": "images/icons/ach1.png",
                                                            "cur_prog": 0, # current progress 
                                                            "max_prog": 3# maximal progress
                                                            },
                                        "ending_1": {"type": 0, # One time achievement
                                                            "title": "엔딩 1", # Also name for steam
                                                            "text": "너무나 많이 무엄한 죄", # description
                                                            "icon": "images/icons/ach1.png" # 96x96 image
                                                            },
                                        "ending_2": {"type": 0, # One time achievement
                                                            "title": "엔딩 2", # Also name for steam
                                                            "text": "거짓말이야", # description
                                                            "icon": "images/icons/ach1.png" # 96x96 image
                                                            },
                                        "ending_3": {"type": 0, # One time achievement
                                                            "title": "엔딩 3", # Also name for steam
                                                            "text": "캐붕", # description
                                                            "icon": "images/icons/ach1.png" # 96x96 image
                                                            },
                                        "ending_4": {"type": 0, # One time achievement
                                                            "title": "엔딩 4", # Also name for steam
                                                            "text": "패륜아", # description
                                                            "icon": "images/icons/ach1.png" # 96x96 image
                                                            },
                                        "ending_5": {"type": 0, # One time achievement
                                                            "title": "엔딩 5", # Also name for steam
                                                            "text": "효자 정훈", # description
                                                            "icon": "images/icons/ach1.png" # 96x96 image
                                                            },
                                        "ending_": {"type": 0, # One time achievement
                                                            "title": "엔딩 ", # Also name for steam
                                                            "text": "", # description
                                                            "icon": "images/icons/ach1.png" # 96x96 image
                                                            },
                                        "ending_": {"type": 0, # One time achievement
                                                            "title": "엔딩 ", # Also name for steam
                                                            "text": "", # description
                                                            "icon": "images/icons/ach1.png" # 96x96 image
                                                            },
                                        "ending_": {"type": 0, # One time achievement
                                                            "title": "엔딩 ", # Also name for steam
                                                            "text": "", # description
                                                            "icon": "images/icons/ach1.png" # 96x96 image
                                                            },
                                        "ending_": {"type": 0, # One time achievement
                                                            "title": "엔딩 ", # Also name for steam
                                                            "text": "", # description
                                                            "icon": "images/icons/ach1.png" # 96x96 image
                                                            },
                                        "ending_": {"type": 0, # One time achievement
                                                            "title": "엔딩 ", # Also name for steam
                                                            "text": "", # description
                                                            "icon": "images/icons/ach1.png" # 96x96 image
                                                            },
                                        "ending_": {"type": 0, # One time achievement
                                                            "title": "엔딩 ", # Also name for steam
                                                            "text": "", # description
                                                            "icon": "images/icons/ach1.png" # 96x96 image
                                                            }                   
                                        }
                                        

    for i, a in persistent.achievements_dict.items():
        if a['type'] == 0:
            achievement.register(i, steam=a['title'])
        if a['type'] == 1:
            achievement.register(i, steam=a['title'], stat_max=a['max_prog'])