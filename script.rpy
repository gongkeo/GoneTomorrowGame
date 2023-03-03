# 게임 스크립트
default preferences.text_cps = 30

# 이미지 정의
image black = "bg_black.png"
image sea = "bg_sea.jpg"
image river = "bg_river.jpg"
image hallway = "bg_hallway.jpg"
image harbor = "bg_harbor.jpg"
image street = "bg_street.jpg"
image palaceos = "bg_palaceos.jpg"

#메인 캐릭터
define jh = Character('정훈', color="#a0a0a0", who_outlines=[(0.3, "#000000")])
define hjh = Character('한정훈', color="#ffffff", who_outlines=[(0.3, "#000000")])
define kog = Character('김옥균', color="#ffffff", who_outlines=[(0.3, "#000000")])
define jy = Character('종윤', color="#5587ED", who_outlines=[(0.3, "#000000")])
define emp = Character('이희', color="#F6F6F6", who_outlines=[(0.3, "#000000")])
define umm = Character('엄 상궁', color="#23A41A", who_outlines=[(0.3, "#000000")])
define iw = Character('이완', color="#740000", who_outlines=[(0.3, "#292929")])
define iy = Character('이연', color="#38610B", who_outlines=[(0.3, "#292929")])
define soph = Character('Sophie', color="#143d8e", who_outlines=[(0.3, "#292929")])
define wada = Character('와다', color="#9cf89f", who_outlines=[(0.3, "#000000")])
define hsg1 = Character('홍승규', color="#FF7171", who_outlines=[(0.3, "#000000")])

#엑스트라
define pw = Character('상궁', color="#FFD9FA", who_outlines=[(0.3, "#000000")])
define stu = Character('승무원', color="#FFD9FA", who_outlines=[(0.3, "#000000")])
define ct = Character('뱃사공', color="#FFD9FA", who_outlines=[(0.3, "#000000")])
define top = Character('상선', color="#FFD9FA", who_outlines=[(0.3, "#000000")])
define eus = Character('응식', color="#FFD9FA", who_outlines=[(0.3, "#000000")])
define jumo = Character('주모', color="#FFD9FA", who_outlines=[(0.3, "#000000")])
define cus = Character('손님들', color="#FFD9FA", who_outlines=[(0.3, "#000000")])
define actr = Character('???', color="#FFD9FA", who_outlines=[(0.3, "#000000")])
define hsg2 = Character('???', color="#FF7171", who_outlines=[(0.3, "#000000")])
define hjm = Character('하지메', color="#FFD9FA", who_outlines=[(0.3, "#000000")])

#색 설정
define highlight = "#FF8C00"

#자간 설정
init -2:
    style nvl_dialogue:
        line_spacing 10
    style say_dialogue:
        line_spacing 10 

#변수
default _choice = -1
default kog_like = 0

#파이썬 구문
init python:
    pass

#지속데이터 정의
default persistent.part1 = True
default persistent.part2 = False
default persistent.part3 = False
default persistent.part4 = False

default persistent.ep1 = True
default persistent.ep2 = False
default persistent.ep3 = False
default persistent.ep4 = False

label start:
    jump part1
    return

# 게임 시작
label part1:
    scene black
    pause 2
    show text "끝은 새로운 시작이니, 누군가는 그 길을 가야 한다." with dissolve
    pause 2
    hide text with dissolve

    #Intro
    #장전음
    play sound "audio/Handling.mp3" 
    "장전되는 소리가 나직이 울렸다."
    stop sound

    "단 한 발이면 모든 게 끝난다."
    "…모든 게 끝난다."
    "정훈은 {color=#FF8C00}방아쇠{/color}에 검지를 올렸다."
    "옥균은 그제야 활자에서 눈을 떼어 고개를 들었다."
    "죽음 같은 정적이 흐른다."
    
    #사진?
    jh "……."
    kog "…곰곰이 생각해보았네."
    jh "……."
    kog "자네와 내가 {color=#FF8C00}이룩할 수 있는 세상{/color}은 어떤 모습일까."
    
    "정훈은 눈앞이 아득해지는 걸 느꼈다."
    centered "이룩할 수 있는 세상." with fade
    centered "당신과 함께 이룩할 수 있는 세상."
    centered "그런 건 없다고 믿었고, 없을 것이다."
    "하지만 차마 부정할 수가 없다."
    "왜, 왜 나는 어떠한 말도 하지 못 하나."
    "정훈은 심장이 저릿해지는 감각을 느꼈다."

    kog "해서, 내 물음에 답해주었으면 하는데."
    
    "더 들을 필요가 있나."
    "그래서는 안 되는 줄 알면서도 망설이고 있다."
    "정훈은 한 발 앞으로 나서며 총구를 들이밀었다."

    kog "불란서 말로 {color=#FF8C00}희망{/color}이 무엇인가."

    "정훈은 망설이다가 입을 열었다."

    jh "…Desir."
    kog "{color=#FF8C00}혁명{/color}은, 무엇인가."
    jh "Revolution."
    kog "그럼… {color=#FF8C00}동지{/color}는 무엇인가."

    "이건 {color=#FF8C00}시험{/color}이다."
    centered "잔인하고, 명료한 시험." with fade

    jh "……."

    #총성+검은바탕
    play sound "audio/Handling.mp3"
    play sound "audio/Gunfire.mp3"
    pause(3.0)
    stop sound

    #인트로 화면? 있으면 좋겠지만... 생략 가능
    
    #part 1
    scene sea with fade
    "{color=#FF8C00}갑판{/color}에 섰다."
    "차디찬 바닷바람이 숨통을 조이듯 밀려든다."
    "감회가 새로울 거란 예상과는 달리," 
    "눈앞에 펼쳐진 광경에 모든 기대가 무너졌다."

    jh "그대로네…."

    "십 년 전이나 지금이나, {color=#FF8C00}조선{/color}은 다를 게 없었다."
    "어째서 달라진 게 아무것도 없나."
    "저 바다 건너 세상은 하루가 멀다하고 새로워지는데."
    "물론, 그대로라서, 그대로이기에 난……."
    "아니. 아니다. 답보는 시대와 맞지 않는다."

    jh "……."
    
    "현기증이 일어 생각을 멈추었다."
    "짙은 한숨이 싸늘한 공기 위로 흩어졌다."
    "뒤로 다가오는 인기척에 습관적으로 뒤를 돌았다."

    stu "배가 곧 정박합니다. 이만 선실로 들어가시지요."

    "갑판에 있던 다른 손님들이 하나둘 사라졌다."
    "청의 언어를 할 수 있는 건 아니지만, 대충 눈치로 알아들을 수 있었다."
    "정훈은 가볍게 목례하고 선실로 들어갔다."

    scene hallway with fade
    "좁은 복도를 따라 걸었다."
    "걸을 때마다 마룻바닥이 소리를 낸다."
    "모서리를 돌아 대화 소리가 들린다."

    iy "곧 눈이 올 모양입니다."
    iw "한바탕 장설이면 좋겠군."
    iy "이제 더는 {color=#FF8C00}청{/color}에 갈 일이 없으시겠지요?"
    iw "그래. …{color=#FF8C00}그 자{/color}와는 더 이상 할 말이 없어."

    "사람은 둘."
    "중년 남자와 젊은 남자다."
    "걸음이 가까워진다."
    "정훈은 바닥에 꽂아두었던 시선을 올렸다."

    "{color=#FF8C00}나이 든 남자{/color}가 이쪽을 바라보고 있다."
    "찰나 마주친 눈이 날카롭다."

    iw "……."
    jh "……."

    "정훈은 그 눈을…."
    menu:
        "계속 바라본다.":
            "이완은 정훈을 바라보며 혀를 쯔, 찼다."
            iw "무도한 자군."
            "실로 오랜만에 들은 조선말인데, 본새가 말이 아니다."
            "정훈은 대충 상황을 모면하기 위해 고개를 숙이고 걸음을 옮겼다."
            "곁을 지나치려던 찰나, 팔이 붙들렸다."
            "젊은 남자 쪽이었다."
            iy "이분이 누구신지 알고."
            "정훈은 이렇게 대답했다."
            menu:
                "…제가 알아야 합니까?":
                    iy "뭐야?"
                    iw "됐다."
                    "젊은 남자가 손찌검이라도 할 기세로 다가섰지만,"
                    "나이 든 남자가 그를 말렸다."
                    iw "패기가 마음에 드는군."
                    jh "……."
                    iw "나는 조선의 총리대신, 이완일세."
                    $ get_achievement("leewan", trans=achievement_transform)
                    "정훈은 마지못해 고개를 숙였다."
                    "이완은 비릿한 웃음을 띠고 말했다."
                    iw "또 보지."
                    "씩씩대는 젊은 남자를 뒤로한 채, 중년의 남자는 앞서 지나가 버렸다."

                "모릅니다.":
                    iy "뭐야?"
                    iw "그럴 줄 알았다. 내 앞에서 굽히지 않는 걸 보면."
                    "정훈은 서늘한 눈으로 그를 바라보았다."
                    "뭐, 왕이라도 된단 말인가?"
                    iw "허나 기억해 두게."
                    jh "……."
                    iw "조선에서 나를 모르는 자는 수상쩍단 소릴 듣는다네."
                    iw "그만 가지."
                    "그들은 좁은 복도를 지나 선실로 들어가 버렸다."

        "그만 피한다.":
            "배가 정박하는 소리에 시선을 거두고 걸음을 옮겼다."
            "…신경 쓸 겨를은 없다."

    "정훈은 선실로 돌아갔다."
    "그리고 품에 있는 전보를 생각했다."

    scene black with dissolve
    centered "국왕이 속히 알현할 것을 명하다."
    centered "이건 분명 나에게 보낸 전보라고 했다." 
    centered "나를 찾는다." 
    centered "…조선이 나를 찾는다." with fade

    "정훈은 제 심정처럼 일렁이는 파도를 바라보았다."

    scene harbor with fade
    "배가 정박하는 소리에 걸음을 옮겼다."
    
    stu "{color=#FF8C00}일등칸 손님{/color}부터 한 분씩 내리십쇼!"

    "삼등칸에 있던 이들은 무어라 중얼거리며 문을 닫고 들어갔다."
    "그들을 돌아보던 정훈은 작은 일수 가방만 손에 쥔 채 출구로 향했다."
    "오랜만에 육지를 밟으니 발바닥이 허공에 뜬 느낌이다."
    "익숙하지 않은 걸음을 옮겼다."
    "선착장에 멍하니 서 있는 정훈에게 나이 든 여자가 다가왔다."
    "차림을 보니 {color=#FF8C00}궁인{/color}인 것 같았다."

    pw "{color=#FF8C00}불란서의 전보{/color}를 받고 온 분인지요."
    jh "…그렇습니다."
    pw "{color=#FF8C00}나루{/color}까지는 말을 타고 가셔야 합니다."
    pw "저를 따라오시지요."

    menu:
        "…말을 탈 줄 모르는데.":
            jh "실은 제가… 말을 탈 줄 모릅니다."
        "말을… 탈 줄 알아야 하는 거였군.":
            jh "실은 제가… 말을 탈 줄 모릅니다."

    "상궁은 눈을 크게 뜨고 한참 말이 없었다."
    "어색한 침묵이 흐르고 마침내 입을 열었다."

    pw "…거기까진 생각지 못했군요."
    pw "기마를 하란 게 아니니 안심하고 오르기만 하십시오."

    "더 할 말이 없어졌다."
    "정훈은 말 두 필 중 뒤에 있는 놈을 골라 탔다."
    "상궁이 말에 올라 박차를 가했다."
    "말이 천천히 움직이기 시작했다."

    scene street with fade
    "발 아래로 공기가 스친다."
    "지나다니는 사람들은 죄다 {color=#FF8C00}남루한 하얀 옷{/color}을 입고 있다."
    "장옷을 걸친 상궁은 고개도 돌리지 않은 채 말했다."

    pw "주변에 시선을 주지 마십시오."
    jh "…왜 그래야 합니까?"

    "상궁은 그제야 뒤돌아 냉랭한 눈을 떴다."

    pw "긍휼한 눈을 보였다간 거지 아이들이 달려들 겁니다."
    jh "……."
    pw "그대는 전하의 명을 받고 왔을 뿐, 소란을 일으켜선 안 됩니다."
    jh "명심… 하겠습니다."

    "두 사람은 나루에 닿을 때까지 아무 말도 하지 않았다."

    scene river with fade
    "강가에 배 한 척이 묶여있다."
    "사공은 뱃전에서 꾸벅꾸벅 졸고 있다."
    "상궁은 곧장 다가가 사공에게 일렀다."

    pw "이보게!"
    ct "…예, 예!"

    "나직이 불렀을 뿐인데, 천지개벽하는 소리라도 들은 것처럼 놀라 자빠졌다."
    "상궁은 어처구니가 없다는 듯 혀를 찼다."

    pw "내 분명 언질 주었건만, 어찌 잠이나 자고 있단 말인가."
    ct "그, 그게… 유시가 다 되도록 오질 않으시니…."
    pw "됐네. 어서 이분을 뫼시게."
    ct "예, 예… 이쪽으로 타시죠, {color=#FF8C00}나리{/color}."

    "‘나리’ 소리에 정훈은 놀란 듯 사공을 보았지만,"
    "그 자리에 있는 누구도 그런 걸 신경 쓰진 않는 것 같았다."

    jh "…나리."

    "정훈은 들릴 듯 말 듯 독백했다."

    scene black with fade
    jump ep1_script1
    return
