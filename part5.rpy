#Part 3-2
label part5:
    scene black with fade
    "멍한 정신을 붙잡기 위해 그 자리에 오래도록 서 있어야 했다."
    centered "김옥균을 죽여라."
    "정훈은 질문해서는 안 되는 자리인 줄 알면서도 입을 열었다."
    
    jh "…왜, 저입니까?"
    
    "물어야 했다."
    "왜 나인지."
    "왜 하필 나인지."
    "이희는 정훈을 흘긋 바라보더니 입을 열지 않았다."
    "그는 엄 상궁을 향해 가볍게 눈짓할 뿐이었다."
    
    umm "{color=#FF8C00}홍종우{/color}는 글을 쓰는 문인, 사람을 죽일 그릇이 못 되네."
    $ get_achievement("hongjongwoo", trans=achievement_transform)
    umm "명분은 홍종우가, {color=#FF8C00}몸뚱아리{/color}는 자네가 빌려주게."
    jh "……."
    emp "…김옥균을 죽이면, 네가 원하는 모든 것을 들어주겠다."

    "……."
    "어지럽다."
    "비록 이 손에 묻힌 피가 수백이나, {color=#FF8C00}암살{/color}은 다른 차원의 문제였다."
    "누군가는 기만이라고 여기겠지."
    "하지만, 하지만…."

    '아이' "눈이다!"
    "어린아이의 외침에 흐릿했던 눈앞이 선명해진다."
    jh "아…."
    
    "눈이 내린다."
    "하얗고 작은 것들이 하늘에서 내려온다."
    "정훈은 어깨를 짓누르는 무게에 고개를 떨어뜨리고 말았다."
    "과연 품에 든 총체의 무게인지, 삶의 무게인지 모호했다."
    centered "무엇을 위해 조선에 돌아왔나."
    centered "감히 비상하리란 꿈을 가졌나."
    centered "인생이란, 얼어붙은 진창에 처박히는 것일 뿐인데."
    "어차피 {color=#FF8C00}던져진 운명{/color}이다."
    $ get_achievement("destiny", trans=achievement_transform)
    "정훈은 주먹을 세게 쥐고 한성을 빠져나갔다."

    #scene night sea
    #파도소리
    kog "바닷바람도 좋고."

    "종윤은 난간에 기대어 서 있는 옥균을 바라보고 섰다."

    jy "들떠 보이는군."
    kog "그러지 않을 이유가 없지."
    jy "얼굴도 좋아 보이고."
    kog "오랜만에 사람을 만나서 그래."
    jy "……."

    "옥균은 말이 없는 종윤을 돌아보았다."
    
    kog "자네 얼굴엔 수심이 가득하군."
    jy "하하… 내가 그랬나."
    kog "말해보게."
    jy "무얼."
    kog "자네가 걱정하는 것."

    "종윤은 짧게 한숨을 쉬더니 입을 열었다."

    jy "사실, 일본 정부의 속셈을 모르겠어."
    kog "속셈?"
    jy "자네를 본토로 부르면 당연히 {color=#FF8C00}개화파{/color}들이 집결할 텐데…."
    kog "…그렇겠지."
    jy "그걸 모르고 있진 않을 테고."
    kog "우리가 모인다 한들 그 힘이 이완만큼 크지 않다는 걸 일본 정부가 모르겠나. …분명 다른 뜻이 있겠지."

    "혹은, {color=#FF8C00}이완{/color}의 뜻일 수도 있고."
    "옥균은 뒷말까지 입 밖으로 꺼내진 않았다."
    "어차피 밀려오는 파도를 피할 방도는 없다."
    "국제정세뿐 아니라 조선도, 빠르게 변하고 있다."
    "이번 항해가 {color=#FF8C00}전쟁터{/color}로 나아가는 길임을 옥균이라고 모르지 않았다."

    kog "그래도 이렇게 탁 트인 바다를 보고 있으면 좋지 않나."
    jy "자네도 참."
    kog "걱정하지 말게. 다… {color=#FF8C00}하늘의 뜻{/color}일 테니."

    "저 멀리, 바다 건너 별빛이 점멸하였다."
    jump part6
    return
    
label part6:
    scene black with fade
    centered "…훈!"
    jh "……."
    centered "한정훈!"
    "누군가가 나를 부르고 있다."
    "소피?"
    "아니, 소피의 목소리는 아니다."
    "무엇보다 그이는 내 진짜 이름을 모른다."
    "그렇다면 누구…."
    centered "네가 날 죽였어."
    "소름 끼치는 목소리가 속삭였다."
    "총성과 함께 눈앞이 빨갛게 물든다."
    centered "네가 날 죽였어!"
    "형체를 알 수 없이 {color=#FF8C00}짓이겨진 손{/color}이 목을 조른다."
    jh "윽, 그만…."
    actr "그렇게 많은 사람을 죽여 죄악을 쌓고도 살길 바라나?"
    jh "나는…."
    centered "이젠 너도 죽어야 해!"

    jh "허억, 윽…."

    scene harbor with fade
    "정훈은 헐떡이며 겨우 몸을 일으켰다."
    "…또 {color=#FF8C00}그 꿈{/color}이다."
    "파견을 갔다 오면 으레 꾸던 꿈."
    $ get_achievement("nightmare", trans=achievement_transform)
    "한동안 멀어졌다고 생각했는데, 조선을 떠나면서부터 하루도 거르지 않고 찾아왔다."
    "정훈은 손바닥으로 얼굴을 감싸고 숨을 몰아쉬었다."
    jh "……."
    "괴로운 이유는 숨을 쉴 수 없어서가 아니었다."
    "여전히 숨을 쉬고 있기에 괴롭다."
    "정훈은 떨리는 손을 뻗어 가방을 뒤적였다."
    "{color=#FF8C00}궐련{/color} 한 개비를 입에 물고 라이터를 열었다."
    $ get_achievement("cigarette", trans=achievement_transform)
    "딸깍이는 소리와 함께 불이 붙는다."
    "생각이 연기처럼 어지럽게 뒤엉켰다."
    "상념이 사라지길 바라진 않았다."
    "어차피 떠안고 가야 할 것들이라고 생각했다."
    "정훈은 연기를 몇 번 더 빨아들이고 재떨이에 끝을 비벼 껐다."
    "가슴이 갑갑해도 풀어헤칠 타이가 없다."
    "정훈은 결국…."
    menu ship:
        "갑판으로 나갔다.":
            $ kog_like += 1
            "정훈은 갑판에 나가 바람이라도 쐬어보기로 했다."
        "다시 누워 잠을 청했다.":
            "정훈은 몸을 웅크리고 다시 잠을 청하기로 했다."
            "앞으로의 날에 비하면 이 정도 악몽은 아무것도 아니리라."
            jump part7
    
    #scene night sea
    #파도소리
    jh "……."
    "공기가 견딜 수 없이 시리다."
    "바닷바람이 뼛속 깊은 곳까지 파고들어 얼어붙는다."
    "사지가 제 것이 아닌 기분이 들었다."
    "…아니, 그게 사실일지도."
    "내 이름은 잊어야 한다."
    "정훈은 제 처지가 참 우습다고 생각했다."
    "이름을 잊고 산 지 오래인데, 막상 다른 사람이 되라 하니 그럴 수 없음을 뼈저리게 깨닫는다."
    "내가 버린 이름까지 {color=#FF8C00}낙인{/color}이 되어 나를 따라다닌다."
    $ get_achievement("name", trans=achievement_transform)
    "내가 버린 나라까지 무게가 되어 나를 짓누른다."

    jh "홍종우…."
    "낯선 이름을 입에 올려보았다."
    "실수는 곧 죽음이 될 것이다."
    "그의 이름 대신 내 이름을 말하면 그 자리가 무덤이 되겠지."
    "…마지막 순간에는 {color=#FF8C00}나{/color}로 죽고 싶다."
    "그렇게 비겁한 바람을 품었다."
    jump part7
    return

label part7:
    #scene night street
    "웃고 떠드는 사람이 거리를 메우고 있었다."
    "옥균은 만면 가득 여유로운 웃음을 띠고 완보로 걸었다."

    kog "오랜만에 이렇게 사람 많은 곳에 나오니 사람 사는 것 같고 좋구만. 그런데 어쩌지. 이 많은 사람 중에 누가 내 목에 칼을 들이대면."

    "농담이 분명한 말에도 종윤은 차마 웃지 못하고 미간을 좁혔다."

    jy "옥균이."
    kog "알겠네. 농도 모르고."

    "종윤은 고개를 저으며 허탈하게 웃었다."
    wada "선생님."
    "반 발짝 뒤에 서 있던 와다가 그를 불러세웠다."
    "옥균은 걸음을 멈추고 와다를 돌아보았다."
    kog "어찌 그러는가."
    wada "이만 들어가시는 게 어떻습니까?"
    kog "왜. 누가 습격하기라도 할까 봐?"
    wada "……."
    jy "그래. 사람이 너무 많으니 불안하네."

    "난감해하는 와다 대신 종윤이 말을 이었다."
    "옥균은 어깨를 으쓱이며 화제를 돌렸다."
    "옥균이 선택한 화제는…."
    menu speek:
        "만나기로 한 홍종우에 관하여":
            kog "그 친구는 언제 온다고?"
            jy "내일일세."
            kog "홍종우라고 했지."
            jy "그래. 불란서에서 외무장관과 독대까지 했던 인사라고 하네."
            kog "…{color=#FF8C00}이홍장{/color}에게 들렀다 오는 길이면 여독이 이만저만 아니겠군."
            $ get_achievement("leehongjang", trans=achievement_transform)
            "나직이 흐르는 옥균의 음성이 의미심장했다."
        "조선에 있을 그분에 관하여":
            kog "혹시 조선에서 들어온 소식은 없나."
            jy "…전하의 안위가 궁금한가."
            kog "그리 들렸다면 하는 수 없지."
            jy "근래 전주에서 일이 터진 모양이더군. 농민들이 {color=#FF8C00}봉기{/color}를 일으켰다고."
            $ get_achievement("donghak", trans=achievement_transform)
            kog "……."
            jy "무슨 생각을 하나."
            kog "글쎄. …내가 조선에 있었다면 어떤 쪽에 힘이 되었을까 생각해 보았네."
            jy "옥균이."
            kog "…확신이 서지 않는 걸 보니, 나도 영 그른 모양이야."

    "한참 생각에 잠겨있던 옥균은 여전히 걱정스러운 얼굴의 두 사람을 번갈아 보다가 마지못해 끄덕였다."
    kog "그래. 그만 들어가지, 들어가."
    "세 사람은 천천히 인파 사이로 사라졌다."

    #scene day street
    "하늘이 맑다."
    "정훈은 기차역에서 나와 거리로 나섰다."
    "그의 손에는 작은 쪽지가 들려있다."
    "'Hotel 新星 321號'"
    "빠른 걸음으로 거리를 가로질러 호텔로 향했다."

    #scene hotel
    "붉은 카펫이 길게 늘어진 로비에 들어섰다."
    "계단 끝에 중절모를 눌러쓴 두 명의 사내가 서 있다."
    "그들은 분명 이쪽을 바라보고 있었다."
    "정훈은 주변을 살피며 그들에게 다가갔다."
    "그러자 {color=#FF8C00}키가 큰 쪽{/color}이 한 발짝 나오며 입을 열었다."

    actr "홍종우."

    "정훈은 작게 고개를 끄덕이며 {color=#FF8C00}전보{/color}를 꺼내 보여주었다."
    "그러자 {color=#FF8C00}큰 눈의 사내{/color}가 손짓하며 앞장서 계단을 올랐다."
    "그들은 3층 복도 끝까지 걸었다."
    "앞서 걷던 사내는 321호의 문을 열고 말했다."

    hsg2 "다섯 시, 호텔 앞. 검고 긴 코트를 입고 나오시오."
    hsg2 "혹여 이전에 연통할 일이 생기거든 한 층 더 올라와 같은 호수로 찾아오면 됩니다."

    "정훈은 대답하기 위해 입술을 달싹였으나 사내들은 이미 나선형의 계단 아래로 사라진 후였다."
    "방으로 들어와 시계를 확인했다."
    "두 시 반. 약속한 시각까지는 아직 넉넉히 남았다."
    "정훈은…."
    menu:
        "방에 머무르기로 했다.":
            "아직 기울지 않은 해가 창으로 물밀듯 쏟아진다."
            "정훈은 쏟아지는 피로를 이기지 못하고 침대 끝에서 엎어지듯 누웠다."
            "노곤하다."
            "고요한 초침 소리만 들린다."
            "정훈은 그만 잠에 들었다."
            jump part8
        "밖에 나가보기로 했다.":
            "호텔 밖으로 나서자 좀 전에 만났던 이 중 {color=#FF8C00}큰 눈을 가진 자{/color}가 서 있었다."
            hsg2 "할 말이 있는 거요?"
            "정훈은 대뜸 묻는 말에 둘러댔다."
            jh "…주변을 살펴놓아야 할 듯하여."
            "그러자 남자는 조금 허무하다는 듯 그를 바라보았다."
            "그는 담벼락에 기대어 {color=#FF8C00}담배를{/color} 권했다."
            "정훈은 굳이 물리지 않고 목례하며 받았다."

            hsg2 "그리 딱딱하게 굴 거 없소. 어차피 같은 처지 아니오?"
            jh "……."
            hsg2 "뭐, 상황이 상황이라 통성명은 못 하지만, 홍승규라 부르시오."
            $ get_achievement("hongseunggyoo", trans=achievement_transform)
            jh "홍승규…."
            hsg1 "누가 물으면 그대 홍종우와는 친척 사이인 거요."

            "짐작건대, 그게 그의 진짜 이름은 아닌 것 같았다."
            "뭐, 이쪽도 신분을 숨기고 있긴 마찬가지지만."
            "정훈은 하늘로 흩어지는 연기를 바라보았다."
            "그를 곁눈질 하던 홍승규는 담배를 입에 문 채로 말했다."

            hsg1 "불란서에서 군인으로 있었다 들었소."
            jh "…그렇습니다."
            hsg1 "진짜 홍종우가 불란서 유학생이라더니, 그런 연 때문에 여기까지 흘러들어온 모양이오."

            "틀린 말은 아니었으나, 어쩐지 마음 한구석을 쿡쿡 찔리는 기분이 들어 대꾸하지 않았다."
            "오직 그 때문에 {color=#FF8C00}몸뚱아리{/color}를 빌려주는 처지가 되었다."
            "그게 사실이다."
            "어떠한 큰 뜻 같은 건 없다."

            hsg1 "작전에 관한 건 미리 들어 알 것이오."
            jh "예."

            "먼저, 정훈을 제외한 두 사람이 근처 건물에서 잠복한다."
            "공포탄을 먼저 쏜 후, 대열이 흐트러지면 김옥균의 앞을 막아서 대신 총을 맞는다."
            "그것이 내일 있을 작전의 전부였다."
            hsg1 "가장 안전한 탄알을 고르긴 했는데, 엇나가면 목숨을 장담할 수 없소."
            jh "알고 있습니다."
            hsg1 "…죽을 수도 있다는데 퍽 태연하시오."

            "정훈은 고개를 돌려 홍승규를 바라보았다."
            "그는 잠시 단어를 고르다 입을 열었다."

            jh "…{color=#FF8C00}전쟁터{/color}와 다를 것이 없으니까요."
            hsg1 "…생각해 보니, 맞는 말이오. 내 어리석었소."
            "홍승규는 허탈한 미소를 지으며 담배를 벽돌 사이에 비벼 껐다."
            "그는 호텔 앞 계단을 오르며 손을 흔들었다."
            hsg1 "잘 쉬고, 이따 봅시다."
            "정훈은 덧없이 맑은 하늘을 우러러보았다."
            jump part8

    return

label part8:
    #scene night street with fade
    "축제가 한창이었다."
    "{color=#FF8C00}무도자들{/color}이 일렬로 서 춤을 선보였다."
    "옥균은 주머니에 손을 꽂은 채 어딘가를 망연히 바라보고 있었다."

    jy "옥균이, 무슨 생각을 그리 하나."
    "종윤의 물음에도 그는 오직 정면을 바라볼 뿐이었다."
    kog "나를 찾아올 객에게 무슨 말을 처음으로 건넬까, 고민하고 있네."
    jy "말?"
    kog "{color=#FF8C00}첫인상{/color}이 중요하지 않겠나. 더구나 중요한 만남이라면."
    jy "그저 자네답게 하면 되지."

    "옥균은 웃으며 고개를 끄덕였다."

    kog "나답게라. 그러면 되겠군."
    jy "그런 걸 다 고민하고."
    kog "오랜만에 만나는 새 사람 아닌가. 성의는 보여야지."

    "그때, 옥균을 찾은 하지메가 언덕 위에서 환하게 웃어 보였다."
    "그는 빠르게 달려와 뒤에 선 사내를 소개했다."
    hjm "선생님, {color=#FF8C00}이일신 선생{/color}께서 소개하라고 하신 분을 모시고 왔습니다."
    $ get_achievement("leeyiljik", trans=achievement_transform)
    "와다는 사내의 앞을 가로막고 양손을 들어 올릴 것을 청했다."
    "그러자 사내는 말 없이 수긍하며 순순히 몸수색에 응했다."
    jh "…홍종우라고 합니다. 이렇게 만나 뵙게 되어, 영광입니다."
    "옥균은 자신을 ‘홍종우’라 소개한 {color=#FF8C00}홍안의 사내{/color}를 꿰뚫을 듯 바라보았다."
    "저를 향해 뻗은 다부진 손을 흘끔거렸다."
    "그는 곧 여유가 흐르는 웃음을 지었다."
    kog "자네 {color=#FF8C00}20엔{/color} 있나?"
    $ get_achievement("silly", trans=achievement_transform)
    "당혹스러움을 감추지 못한 {color=#FF8C00}눈빛{/color}이 흔들린다."
    "옥균은 저 눈을 잘 알았다."
    "긴장한 태가 나는 것으로 보아 둘 중 하나겠지."
    "이 사람을 진정으로 존경하거나, 혹은…."
    centered "그때, 총성이 하늘을 울렸다."
    centered "거리를 메운 웃음소리가 비명으로 변질하였다."
    "종윤은 다급히 옥균을 감싸며 뒷걸음질 쳤다."
    "하지메는 총구가 선명한 건물 위를 가리키며 외쳤다."
    hjm "저기!"
    "정훈이 몸을 날려 옥균의 앞을 가로막았다."
    "총성이 한 번 더 들렸다."
    "정훈의 팔을 스쳐 지나간 {color=#FF8C00}탄환{/color}이 흙바닥에 파묻혔다."
    "살이 터지며 피가 튀었다."
    "종윤이 정훈 곁으로 황급히 다가갔다."
    "종윤은 제 겉옷을 벗어 그의 어깨를 감싸주었다."
    "옥균은 {color=#FF8C00}핏자국{/color}이 선명한 흙바닥을 응시하고 있었다."
    "종윤이 하얗게 질린 얼굴로 그를 불렀다."

    jy "옥균이!"
    kog "……."
    centered "둘 중 하나겠지."
    centered "이 사람을 진정으로 존경하거나, 혹은…."
    
    kog "…이 목숨을 거두러 왔거나."
    #To Be Continued.
    #에피소드 2가 열렸습니다 팝업
    $ get_epsiode("에피소드 2가 열렸습니다.")
    return

