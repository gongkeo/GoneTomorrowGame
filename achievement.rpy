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
        xalign .90
        yalign .02
        xysize (750, 160)
        hbox:
            vbox:
                xoffset 20
                yoffset 20
                image icon
            vbox:
                xoffset 45
                yoffset 5
                spacing 5
                xsize 570
                text title:
                    size 28
                    id title
                text a_text:
                    size 21
                    id a_text

screen scr_achievement_update(title, a_text, icon, cur_prog, max_prog, trans=achievement_transform):
    timer 2.4 action Hide("scr_achievement_update")
    window:
        at trans
        background "#333333cc"
        xalign .90
        yalign .02
        xysize (550, 120)
        hbox:
            vbox:
                spacing 10
                image icon
                text "{0}/{1}".format(cur_prog, max_prog):
                    xcenter 0.5 
                    ycenter 0.2
            vbox:
                xoffset 10
                xsize 550
                text title:
                    size 28
                    id title
                text a_text:
                    size 21
                    id a_text


                



init python:

    def get_achievement(ach_id, trans=achievement_transform):
        ach = persistent.achievements_dict[ach_id]
        achievement.grant(ach_id)
        renpy.show_screen(_screen_name='scr_achievement_get', title=ach['title'],
                        a_text=ach['text'], icon=im.Scale("images/icons/trophy.png", 120, 120), trans=trans)

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
    persistent.achievements_dict = {    "leewan": {"type": 0,
                                                            "category": 0,
                                                            "title": "인물정보 '총리대신'",
                                                            "title_": "총리대신",
                                                            "text": "총리대신 이완은 고종을 손바닥 위에 올려놓고 좌지우지하는 인물이다. 갑신정변 당시 김옥균에 의해 제거될 뻔했으나, 청군을 끌어들여 김옥균을 몰아내고 살아남았다."
                                                            },                  
                                        "coffee": {"type": 0,
                                                            "category": 1,
                                                            "title": "잡학정보 '가비'",
                                                            "title_": "가비",
                                                            "text": "커피. 고종은 외국에서 들여온 커피를 즐겨 마셨다. 심지어는 와플까지 즐겼을 정도로 서양문물, 특히 먹을거리에 진심이었다."
                                                            },
                                        "lovehate": {"type": 0,
                                                            "category": 0,
                                                            "title": "인물정보 '애증'",
                                                            "title_": "애증",
                                                            "text": "고종은 갑신정변 당시 자신을 두고 일본으로 도망친 김옥균에게 애증을 품고 있다."
                                                            },
                                        "sangseon": {"type": 0,
                                                            "category": 1,
                                                            "title": "잡학정보 '상선'",
                                                            "title_": "상선",
                                                            "text": "내시부 수장. 환관 중에 가장 높은 종2품 관직이다."
                                                            },
                                        "pyeonjeon": {"type": 0,
                                                            "category": 1,
                                                            "title": "잡학정보 '편전'",
                                                            "title_": "편전",
                                                            "text": "임금이 평상시에 거처하면서 정사를 보는 전각이다. 경복궁은 '사정전', 창덕궁은 '선정전'이 그 궁궐의 편전이다."
                                                            },
                                        "okgyoon": {"type": 0,
                                                            "category": 0,
                                                            "title": "인물정보 '김옥균'",
                                                            "title_": "김옥균",
                                                            "text": "갑신정변의 주역. 갑신정변이 실패하자 일본으로 망명하였다. 현재는 암살 위협에 시달리고 있다."
                                                            },
                                        "gapshin": {"type": 0,
                                                            "category": 1,
                                                            "title": "잡학정보 '갑신년'",
                                                            "title_": "갑신년",
                                                            "text": "60간지의 21번째 해이다. 여기서 갑신년은 1884년, 즉 갑신정변이 있었던 해를 말한다."
                                                            },
                                        "sick": {"type": 0,
                                                            "category": 0,
                                                            "title": "인물정보 '병'",
                                                            "title_": "병",
                                                            "text": "정훈의 아버지는 병을 앓고 있다. 때문에 정훈이 책임지고 돈을 벌러 온갖일을 하는 중이다."
                                                            },
                                        "pimatgil": {"type": 0,
                                                            "category": 1,
                                                            "title": "잡학정보 '피맛길'",
                                                            "title_": "피맛길",
                                                            "text": "말을 피한다는 뜻을 가지고 있다. 고관대작들이 지나는 대로를 벗어나 평민들이 편하게 오갈 수 있도록 형성된 보도다."
                                                            },
                                        "yookjo": {"type": 0,
                                                            "category": 1,
                                                            "title": "잡학정보 '육조거리'",
                                                            "title_": "육조거리",
                                                            "text": "경복궁 남향의 대문인 광화문 앞 대로. 조선시대 여섯 개의 중앙관청인 이·호·예·병·형·공조가 있었던 데서 유래하였다."
                                                            },
                                        "hongjongwoo": {"type": 0,
                                                            "category": 0,
                                                            "title": "인물정보 '홍종우'",
                                                            "title_": "홍종우",
                                                            "text": "조선 최초의 프랑스 유학생. 조선의 소설들을 프랑스말로 번역해서 출판하기도 했으며, 실제 역사에서는 김옥균을 암살한 장본인이다."
                                                            },
                                        "destiny": {"type": 0,
                                                            "category": 0,
                                                            "title": "인물정보 '던져진 운명'",
                                                            "title_": "던져진 운명",
                                                            "text": "정훈은 기대를 가지고 조선에 돌아왔으나, 임금으로부터 김옥균을 암살하라는 명령을 받았다."
                                                            },
                                        "nightmare": {"type": 0,
                                                            "category": 0,
                                                            "title": "인물정보 '악몽'",
                                                            "title_": "악몽",
                                                            "text": "정훈은 전투를 치르고 올 때마다 목이 졸리는 꿈을 꾸었다. 김옥균을 암살하라는 명령을 받은 후 다시 시작되었다."
                                                            },
                                        "cigarette": {"type": 0,
                                                            "category": 1,
                                                            "title": "잡학정보 '궐련'",
                                                            "title_": "궐련",
                                                            "text": "얇은 종이로 말아놓은 담배."
                                                            },
                                        "name": {"type": 0,
                                                            "category": 0,
                                                            "title": "인물정보 '버린 이름'",
                                                            "title_": "버린 이름",
                                                            "text": "조선을 떠나며 팔았던 족보는 그를 죄책감으로 옭아매어 끝끝내 따라다니고 있다."
                                                            },
                                        "donghak": {"type": 0,
                                                            "category": 1,
                                                            "title": "잡학정보 '동학농민혁명'",
                                                            "title_": "동학농민혁명",
                                                            "text": "동학교도 전봉준이 중심이 되어 일으킨 반봉건·반외세 운동이다. 김옥균이 사망한 해인 1894년에 일어난 일이다."
                                                            },
                                        "leehongjang": {"type": 0,
                                                            "category": 1,
                                                            "title": "잡학정보 '이홍장'",
                                                            "title_": "이홍장",
                                                            "text": "청나라의 관리이자 정치가. 양무운동을 주도하였으며, 외교에 깊이 관여했다."
                                                            },
                                        "hongseunggyoo": {"type": 0,
                                                            "category": 0,
                                                            "title": "인물정보 '홍승규'",
                                                            "title_": "홍승규",
                                                            "text": "김옥균 암살 작전을 위해 만났다. 서로 진짜 이름도, 나이도 모르지만 임금의 명을 받은, 동일한 처지다."
                                                            },
                                        "leeyiljik": {"type": 0,
                                                            "category": 1,
                                                            "title": "잡학정보 '이일직'",
                                                            "title_": "이일직",
                                                            "text": "실제 역사 속 이일직은 상인으로 홍종우와 공모하여 김옥균을 암살하는 데에 도움을 주었다."
                                                            },
                                        "silly": {"type": 0,
                                                            "category": 0,
                                                            "title": "인물정보 '헛소리'",
                                                            "title_": "헛소리",
                                                            "text": "김옥균은 과거 유락정에서 돈을 수없이 날려 친구인 종윤의 속을 썩인 바 있다. 이제는 처음 본 사람에게도 20엔을 요구하기까지 한다. 하지만 그의 큰 그림은…."
                                                            },
                                        "genius": {"type": 0,
                                                            "category": 0,
                                                            "title": "인물정보 '수재'",
                                                            "title_": "수재",
                                                            "text": "월수소조천하. 김옥균이 6세에 지은 시다."
                                                            },
                                        "": {"type": 0,
                                                            "category": 0,
                                                            "title": "",
                                                            "title_": "",
                                                            "text": ""
                                                            },
                                        "": {"type": 0,
                                                            "category": 0,
                                                            "title": "",
                                                            "title_": "",
                                                            "text": ""
                                                            },
                                        "": {"type": 0,
                                                            "category": 0,
                                                            "title": "",
                                                            "title_": "",
                                                            "text": ""
                                                            }            
                                        }

    persistent.profile_items = { "ending1" : "엔딩 1: 너무나 많이 무엄한 죄",
    "ending2" : "엔딩 2: 거짓말이야",
    "ending3" : "엔딩 3: 아첨은 그만",
    "ending4" : "엔딩 4: 효자 정훈"
    }                                    

    for i, a in persistent.achievements_dict.items():
        if a['type'] == 0:
            achievement.register(i, steam=a['title'])
        if a['type'] == 1:
            achievement.register(i, steam=a['title'], stat_max=a['max_prog'])
