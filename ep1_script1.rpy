label ep1_script1:
    jump part2
    return

#Part 2
label part2:
    $ persistent.part2 = True
    emp "아직이라더냐."

    scene palaceos with fade
    umm "곧 당도할 것입니다."

    "이희는 붙박이듯 앉아 눈을 내리깔고 있었다."
    
    if not achievement.has("coffee"):
        $ get_achievement("coffee", trans=achievement_transform)
    umm "{color=#FF8C00}가비{/color}라도 들일까요."
    emp "되었다."
    emp "…입이 쓰구나."

    "이희가 가볍게 손짓하였다."
    "엄 상궁은 머리를 조아리곤 자리에서 물러났다."
    "혼자 남겨진 이희는 창밖으로 시선을 돌렸다."
    
    show black with fade
    centered "전하와 함께 다음날 청천백일을 바라보기 위함입니다!"
    "벌써 아홉 해 전 일이다."
    "잊힐 만도 하건만, 여전히 또렷하다."
    "그날의 비명, 광기, 죽음…."
    "이희는 눈을 질끈 감았다."

    emp "…고얀 놈."

    "지키지 못할 약조거든 입에 올리질 말았어야지."

    hide black with dissolve
    "…햇볕이 쓰라리다."
    "비단 아래 거죽까지 타들어가는 것 같다."
    "입 안이 바싹 마른다."
    "이 빛이 그곳에도 가 닿길."
    show black
    centered "그대도 반드시 아프길." with fade
    if not achievement.has("lovehate"):
        $ get_achievement("lovehate", trans=achievement_transform)
    hide black

    #scene palaceis
    scene black
    pw "여기서부턴 {color=#FF8C00}상선 영감{/color}을 따라가시면 됩니다."
    jh "…고맙습니다."

    "상궁은 별다른 대꾸 없이 고개만 주억이고 사라졌다."
    "늙수그레한 환관 한 명이 문턱을 넘어 앞으로 다가왔다."
    
    if not achievement.has("sangseon"):
        $ get_achievement("sangseon", trans=achievement_transform)
    top "{color=#FF8C00}정훈{/color}?"
    jh "그렇습니다."
    top "금일 입궐은 다른 이들에게 함구해야 할 것이다."
    jh "…예."
    top "또한 전하의 용안을 바로 보아서는 아니되고 {color=#FF8C00}하문하시는 것{/color}에만 답해야 한다."
    jh "그리하겠습니다."
    top "그리고…."
    umm "상선 영감."

    "저를 부르는 소리에 상선이 뒤를 돌았다."
    "엄숙한 분위기의 여인이 서 있었다."
    "아마 대전을 뫼시는 상궁인 듯싶었다."

    umm "그만하면 되셨습니다. {color=#FF8C00}법도{/color}를 아주 모르는 자는 아닌 것 같으니."
    top "과연 이만하면 되는 것인가."
    umm "염려마십시오."

    "여인은 천천히 정훈을 돌아보더니 웃는 듯 마는 듯한 표정을 지었다."

    umm "따라오시게."

    if not achievement.has("pyeonjeon"):
        $ get_achievement("pyeonjeon", trans=achievement_transform)

    "정훈은 천천히 {color=#FF8C00}편전{/color} 안으로 걸음을 옮겼다."

    #scene palaceis
    umm "전하, 불란서에서 정훈이란 자가 들었습니다."
    emp "들라 하라."

    "문이 열렸다."
    "정훈은 반투명한 장막 뒤에서 {color=#FF8C00}빛나는 두 눈{/color}을 마주하였다."
    "정훈은…"
    menu:
        "그를 뚫어져라 바라보았다.":
            umm "……."
            emp "……."
            jh "……."
            top "네 이놈! 어서 엎드리지 못할까!"
            top "전하, 안 되겠습니다. 이런 {color=#FF8C00}무도한 자{/color}에게 믿고 맡길 일은 없습니다."
            top "당장 이놈을 {color=#FF8C00}매질{/color}하겠습니다!"
            jh "자, 자, 잠깐↗!!!"
            "당황한 정훈은 삑사리를 내고 말았다!"
            jh "안돼!!!"
            centered "{color=#FF8C00}엔딩 1{/color}. 너무나 많이 무엄한 죄"
            centered "새로운 선택지를 골라보자."
            $ achievement.grant("ending1")
            show black with fade
            call polite
        "급하게 고개를 숙였다.":
            "정훈은 다급히 몸을 숙이고 고개를 바닥에 처박았다."

    emp "…정훈."

    "정훈은 눈을 굴리다가 더듬거리며 겨우 대답했다."

    jh "예, …전하."
    emp "불란서에서 {color=#FF8C00}군인{/color}으로 지냈다지."

    "정훈은 고개를 슬며시 들어 엄 상궁을 돌아보았다."
    "엄 상궁은 작게 눈짓하였다."

    jh "…그렇습니다."
    emp "허면 {color=#FF8C00}홍종우{/color}란 자를 아느냐."
    centered "홍종우라면…."
    "정훈은 조선으로 떠나오기 직전, 벗과 나눈 대화를 떠올렸다."
    soph "홍종우라는 {color=#FF8C00}조선인 유학생{/color}이 있는데," with fade
    jh "홍종우?"
    soph "이 책을 프랑스말로 번역해서 출간했대. 대단하지?"
    jh "……."

    jh "그것이…."
    umm "전하께서 하문하시네."
    "정훈은 임금의 질문에…."
    menu:
        "잘 아는 사이라고 둘러댔다.":
            jh "그럼요, 잘 알고 있습니다."
            emp "그래? 그럼 홍종우가 불란서 외무장관과 독대했다는 사실도 알고 있겠군."
            jh "어… 그게…."
            emp "방금 네 입으로 잘 안다고 하지 않았느냐?"
            jh "전하, 그것이……."
            top "이놈이 어느 안전이라고 감히 거짓을 고하느냐!"
            "대체 저 어르신은 또 어디서 튀어나온 거야!"
            top "전하! 당장 이놈을 {color=#FF8C00}매질{/color}하겠습니다!"
            jh "저, 전하!"
            emp "그리하라!"
            jh "전하!"
            jh "전하아!!!"
            centered "{color=#FF8C00}엔딩 2{/color}. 거짓말이야"
            centered "새로운 선택지를 골라보자."
            $ achievement.grant("ending2")
            show black with fade
            call honor
        "솔직하게 모른다고 대답했다.":
            jh "실은… 이름만, 들어보았습니다."
            emp "그래."

    "정훈은 죄라도 지은 사람처럼 고개를 푹 숙이고 일어나지 못했다."
    
    jh "송구…합니다."
    emp "상관없다."

    "이희는 자리에서 천천히 자리에서 일어났다."
    "정훈은 움찔하였으나, 엄 상궁의 {color=#FF8C00}서슬퍼런 눈빛{/color}에 차마 함부로 움직이지 못했다."
    "이희는 얇은 손가락으로 장막을 걷어내고 정훈을 향해 한발짝 다가섰다."
    "그제야 보다못한 엄 상궁이 임금 앞에 고개를 숙였다."

    umm "전하."

    "이희는 손짓하며 그를 물리고 정훈의 머리맡에 서 마른 어깨를 내려다보았다."

    emp "엄아."
    umm "…예, 전하."
    emp "오늘이 며칠이냐."
    umm "{color=#FF8C00}12월 6일{/color}입니다."
    emp "정훈."

    "정훈은 한참 숨죽이고 엎드려 있다 겨우 시선만 올렸다."

    emp "오늘이 무슨 날인지 아느냐."
    "오늘은……."
    menu:
        "임금의 생일이다.":
            emp "…아니다."
            jh "아, 아닙니까?"
            emp "겠냐?"
            jh "예?"
            emp "겠냐고."
            top "전하, 이놈 말하는 본새가 간신과 다르지 않습니다. 당장 {color=#FF8C00}매질{/color}을 하겠습니다!"
            centered "{color=#FF8C00}엔딩 3{/color}. 아첨은 그만"
            centered "김옥균을 어여삐 한 사람의 말을 잘 들어보자."
            $ achievement.grant("ending3")
            show black with fade
            call jjan

        "김옥균이 일본으로 도망간 날이다.":
            $ kog_like += 1
            emp "그래. 잘 알고 있구나. 온 나라가 떠들썩했으니."

        "제가 그걸 어찌….":
            emp "그래. 모를 수도 있지. 벌써 구 년 전 일이니 말이다."
            jh "……."
            if not achievement.has("okgyoon"):
                $ get_achievement("okgyoon", trans=achievement_transform)
            emp "김옥균을 아느냐."
            jh "…알고 있습니다."
            jh "그러면 되었다."

    emp "……."
    
    "이희는 온몸이 쓰라린 듯한 표정으로 고개를 떨어뜨렸다."
    "이내 입술을 달싹이다가 도로 다물어버렸다."
    "그는 엄 상궁을 바라보며 고개를 끄덕였다."
    "그러자 엄 상궁은 {color=#FF8C00}비단 봉투에 싸인 서찰{/color}을 머리맡에 내려놓았다."
    
    emp "…네가 할 일은 간단하지만, 목숨을 걸어야 한다."
    emp "일을 꾸며 속이고 유인하여 결행해야 한다."
    emp "네가 본 것, 들은 것 모두 과인에게만 알리고, 잊어야 한다."
    jh "…제가 할 일이란 게 무엇입니까?"
    emp "……."
    
    "이희는 차갑게 식은 눈으로 허공 어딘가를 응시하였다."
    "마치 그곳에 {color=#FF8C00}김옥균{/color}이 있는 것처럼."
    
    emp "홍종우의 이름으로 {color=#FF8C00}역적 김옥균{/color}에게 접근해라."
    emp "그놈도 홍종우에 대해 이미 알고 있을 테니…."
    emp "암살이 두려워 새 사람을 만나지 않아도 호기심이 생길 것이야."
    emp "그렇게 김옥균에게 접근해서,"
    jh "……."
    emp "김옥균을… 죽여라."

    jump part3
    return

#Part 3
label part3:
    $ persistent.part3 = True
    #회상인 걸 알 수 있는 효과음 넣기
    scene black with fade
    if not achievement.has("gapshin"):
        $ get_achievement("gapshin", trans=achievement_transform)
    "갑신년, 이제 막 {color=#FF8C00}입추{/color}가 지났다."
    "아직 모기 입은 비뚤어지지 않았지만, 아침저녁으로 바람이 선선하게 분다."
    "정훈은 {color=#FF8C00}물동이 세 개{/color}를 지고 종로를 걷고 있었다."

    #scene street with fade

    hjh "물 사려- 물 사려-"
    eus "정훈아, 여기 물 한 동이 주거라."

    "아버지와 자주 왕래하는 {color=#FF8C00}행상 주인 응식{/color}이다."
    "아버지가 병상에 누운 후로는 심부름을 시키고 값을 준 고마운 사람이다."
    "정훈은 종종걸음으로 달려가 물동이를 내려놓았다."

    hjh "예에, {color=#FF8C00}이 전{/color}입니다."
    eus "그래, {color=#FF8C00}춘부장{/color}은 안녕하시고?"
    hjh "근래 들어 차도가 좀 있으십니다."

    "응식은 다행이라면서 물값을 치렀다."
    "정훈은 이 전을 호주머니에 넣었다."
    "꾸벅 인사하고 물동이를 들려던 찰나, 응식이 그를 불러세웠다."

    eus "잠깐만 기다려라."
    "응식은 유지에 싼 {color=#FF8C00}약과{/color}를 건넸다."
    "이때 정훈은…."
    menu:
        "감사하게 약과를 받았다.":
            "응식은 정훈의 손에 약과를 쥐여주었다."
            "그는 맛있게 먹으라며 머리를 쓰다듬었다."
            "정훈은 약과를 호주머니에 넣었다."
            eus "지금 바로 먹지 않고?"
            hjh "아버지께서 약과를 좋아하셔서요."
            eus "{color=#FF8C00}한 씨{/color}는 복도 많지. 이런 아들을 두었으니."
            "정훈은 어색하게 웃으며 아무 말도 하지 않았다."
            "응식은 곧 큰길 쪽을 가리켰다."
            eus "피맛길 따라가면 물 필요한 집 몇군데 더 있을 거다. 어서 털고 집에 들어가거라."
            hjh "예, 감사합니다."
            if not achievement.has("pimatgil"):
                $ get_achievement("pimatgil", trans=achievement_transform)
            "정훈은 피맛길을 따라가기로 했다."
            jump pmg

        "받을 수 없다며 거절했다.":
            "응식은 한 번 더 권했지만, 정훈은 끝내 받지 않았다."
            eus "그럼 물 두 동이 마저 다오."
            "정훈은 우물쭈물하며 물 두 동이를 통에 부어주었다."
            "응식은 물값을 치르고 {color=#FF8C00}약값{/color}이라며 일 전을 더 얹어주었다."
            hjh "저는... 받을 수 없습니다."
            eus "아버지와의 의리라고 생각해다오."
            "정훈은 더 거절하기 민망해 감사히 받았다."
            "정훈은 일 전을 호주머니에 마저 넣었다."
            eus "곧 해가 지겠구나. 오늘치 약은 지었니."
            if not achievement.has("sick"):
                $ get_achievement("sick", trans=achievement_transform)
            hjh "지어서 들어가야죠. 오늘도 감사했습니다."
            "응식은 웃으며 정훈의 머리를 쓰다듬어주었다."
            "정훈은 육조거리로 향하는 피맛길과 종각으로 향하는 시전 사이에서 고민했다."
            menu:
                "육조거리에 나가보기로 했다.":
                    jump part4
                "아버지 약을 지어 일찍 집에 가기로 했다.":
                    jump dutiful

        "우물쭈물하며 대답하지 않았다.":
            "응식은 정훈의 손에 약과를 쥐여주었다."
            "그는 맛있게 먹으라며 머리를 쓰다듬었다."
            "정훈은 약과를 호주머니에 넣었다."
            eus "지금 바로 먹지 않고?"
            hjh "아버지께서 약과를 좋아하셔서요."
            eus "{color=#FF8C00}한 씨{/color}는 복도 많지. 이런 아들을 두었으니."
            "정훈은 어색하게 웃으며 아무 말도 하지 않았다."
            "응식은 곧 큰길 쪽을 가리켰다."
            eus "피맛길 따라가면 물 필요한 집 몇군데 더 있을 거다. 어서 털고 집에 들어가거라."
            hjh "예, 감사합니다."
            "정훈은 피맛길을 따라가기로 했다."
            jump pmg
    return

#Part 3-1
label part4:
    $ persistent.part4 = True

    "아직 해가 완전히 지지 않았다."
    "정훈은 푸르게 빛나는 하늘 아래에 섰다."
    if not achievement.has("yookjo"):
        $ get_achievement("yookjo", trans=achievement_transform)
    "탁 트인 {color=#FF8C00}육조거리{/color}에는 마차와 가마가 오간다."
    "정훈은 처마 아래에 숨어서 지나다니는 사람을 지켜보았다."
    "거리는 생각보다 평화롭다."
    "세상이 뒤집힐 기미 같은 건 보이지 않았다."
    "그때…"

    centered "저 멀리, 오십 보쯤 떨어진 곳에 옥도포를 입은 사내가 보였다."
    centered "짧게 자른 머리와 위풍당당한 걸음에 시선을 빼앗겼다."

    "정훈은 한참이나 그를 바라보았다."
    "문득 사내가 걸음을 멈추었다."
    "정훈은 급하게 기둥 뒤에 숨었다."
    "사내는 분명히 이쪽을 보았다."
    "정훈은 빠르게 뛰는 심장을 어쩌지 못했다."
    "이때 정훈은…"
    menu:
        "눈싸움이라도 하듯 마찬가지로 눈을 떼지 않는다.":
            $ _choice = 1
            $ kog_like += 1
            "눈이 마주쳤다."
            "사내 역시 한참이나 정훈을 바라보았다."
            "정훈은 끝까지 눈을 피하지 않았다."
            "부끄러워할 필요도, 이유도 없다고 생각했다."
            "사내는 곧 희미한 미소를 보이고는 {color=#FF8C00}광화문{/color}으로 들어갔다."
            "정훈은 다리에 힘이 풀려 그 자리에 주저앉고 말았다."
            centered "빛나는 두 눈의 저 사내는 누구지?"
            "정훈은 해가 완전히 지고 나서야 자리를 뜰 수 있었다."
            "도저히 잊기 힘든 순간이라 확신할 수 있었다."

        "도망치듯 집으로 달려간다.":
            $ _choice = 0
            "정훈은 집까지 빠르게 달렸다."
            "분명 그 사내는 나를 보지 못했을 것이다."
            "보지 못했어야 한다."
            "남루한 옷을 부끄러워한 적 없지만, 그런 문제가 아니었다."
            "그 사내는 너무 빛나고 있었다."
            "잠깐 마주친 것이지만 알 수 있었다."
            "정훈은 오늘 일을 그 누구에게도 말하지 않기로 결심했다."

    jump ep1_script2
    
    return

#엔딩 1: 예의바르게 굴자
label polite:
    "문이 열렸다."
    "정훈은 반투명한 장막 뒤에서 {color=#FF8C00}빛나는 두 눈{/color}을 마주하였다."
    "정훈은…"

    menu:
        "뚫어져라 바라보았다.":
            umm "……."
            emp "……."
            jh "……."
            top "네 이놈! 어서 엎드리지 못할까!"
            top "전하, 안 되겠습니다. 이런 {color=#FF8C00}무도한 자{/color}에게 믿고 맡길 일은 없습니다."
            top "당장 이놈을 {color=#FF8C00}매질{/color}하겠습니다!"
            jh "자, 자, 잠깐↗!!!"
            "당황한 정훈은 삑사리를 내고 말았다!"
            jh "안돼!!!"
            centered "{color=#FF8C00}엔딩 1{/color}. 너무나 많이 무엄한 죄"
            centered "새로운 선택지를 골라보자."
            $ achievement.grant("ending1")
            show black with fade
            jump polite
        "급하게 고개를 숙였다.":
            "정훈은 다급히 몸을 숙이고 고개를 바닥에 처박았다."
    return

#엔딩 2: 솔직하게 대답하자
label honor:
    jh "……."
    umm "전하께서 하문하시네."
    "정훈은 임금의 질문에…."

    menu:
        "잘 아는 사이라고 둘러댔다.":
            jh "그럼요, 잘 알고 있습니다."
            emp "그래? 그럼 홍종우가 불란서 외무장관과 독대했다는 사실도 알고 있겠군."
            jh "어… 그게…."
            emp "방금 네 입으로 잘 안다고 하지 않았느냐?"
            jh "전하, 그것이……."
            top "이놈이 어느 안전이라고 감히 거짓을 고하느냐!"
            "대체 저 어르신은 또 어디서 튀어나온 거야!"
            top "전하! 당장 이놈을 {color=#FF8C00}매질{/color}하겠습니다!"
            jh "저, 전하!"
            emp "그리하라!"
            jh "전하!"
            jh "전하아!!!"
            centered "{color=#FF8C00}엔딩 2{/color}. 거짓말이야"
            centered "새로운 선택지를 골라보자."
            $ achievement.grant("ending2")
            show black with fade
            jump honor

        "솔직하게 모른다고 대답했다.":
            jh "실은… 이름만, 들어보았습니다."
            emp "그래."
    return

#엔딩 3: 아는 대로 대답하자
label jjan:
    emp "오늘이 무슨 날인지 아느냐."
    "오늘은……."

    menu:
        "임금의 생일이다.":
            emp "…아니다."
            jh "아, 아닙니까?"
            emp "겠냐?"
            jh "예?"
            emp "겠냐고."
            top "전하, 이놈 말하는 본새가 간신과 다르지 않습니다. 당장 {color=#FF8C00}매질{/color}을 하겠습니다!"
            centered "{color=#FF8C00}엔딩 3{/color}. 아첨은 그만"
            $ achievement.grant("ending3")
            show black with fade
            jump jjan

        "김옥균이 일본으로 도망간 날이다.":
            $ kog_like += 1
            emp "그래. 잘 알고 있구나. 온 나라가 떠들썩했으니."

        "제가 그걸 어찌….":
            emp "그래. 모를 수도 있지. 벌써 구 년 전 일이니 말이다."
            jh "……."
            emp "김옥균을 아느냐."
            jh "…알고 있습니다."
            jh "그러면 되었다."
    return

#엔딩 4: 효도도 좋지만...
label dutiful:
    "정훈은 약을 지어서 바로 집에 돌아왔다."
    "아버지는 일찍 잠에 드신 듯했다."
    "오늘도 평소와 다를 것 없는 하루였다고 정훈은 생각했다."
    $ achievement.grant("ending4")
    centered "{color=#FF8C00}엔딩 4{/color}. 효자 정훈"
    centered "일탈해보자."
    jump part3

#최종엔딩
label result:
    if __choice == 1:
        "트루엔딩"
        #트루엔딩 진행: 김옥균을 살릴 수 있다
    else:
        "노멀엔딩"
        #노멀엔딩 진행: 김옥균을 살리는 선택지는 없다

#중간 에피소드 - 피맛골
label pmg:
    scene black with fade
    hjh "물 사려- 물 사려-"
    jumo "여기 물 두 동이 주어라!"
    "정훈은 빠릿빠릿한 움직임으로 물 두 동이를 통에 모두 부었다."
    "주모가 값을 치렀다."
    hjh "감사합니다."
    "평상에서 국밥을 먹던 손님들이 숙덕거린다."
    cus "{color=#FF8C00}김옥균 선생{/color}이 일본에서 들어왔다지?"
    cus "이번엔 아주 이를 간 모양이야."
    cus "세상이 또 뒤집히겠구만…."
    cus "우리 사는 데 지장만 없으면 좋겠는데 말이야…."
    "정훈은 자기도 모르게 손님들의 대화에 귀를 기울였다."
    "그러자 주모는 뭘 그렇게 훑어보냐는 눈으로 보았다."
    "정훈은 그제야 쫓기듯 빈 동이를 지고 자리를 떴다."
    "피맛길을 따라 걷던 정훈은…."
    menu:
        "육조거리에 나가보기로 했다.":
            call part4
        "아버지 약을 지어 일찍 집에 가기로 했다.":
            jump dutiful
    return
