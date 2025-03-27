from hangul_utils import convert_key

# 텍스트 보정
ko_texts = [
    convert_key("메밀꽃 필 무렵", "en"),
    convert_key("여름장이란 애시당초에 글러서 해는 아직 중천에 있건만 장판은 벌써 쓸쓸하 ", "en"),
    convert_key("고 더운 햇발이 벌려 놓은 전시장 밑으로 등줄기를 훅훅 볶는다. ", "en"),
    convert_key("마을 사람들은 거의 돌아간 뒤요, 팔리지 못한 나무꾼 패가 길거리에 궁싯거 ", "en"),
    convert_key("리고 들 있었으나, 석유 병이나 받고 고깃마리나 사면 족할 것이 ", "en"),

    convert_key("축들을 바라고 언제까지든지 버티고 있을 법은 없다. 칩침스럽게 날아드는 파 ", "en"),
    convert_key("리 떼도 장난꾼 각다귀들도 귀찮다. 얼금뱅이요 왼손잡이인 드팀전의 ", "en"),
    convert_key("허생원은 기어이 등업의 조선달을 낚구어 보았다.  \"그만 거둘까.\" ", "en"),
    convert_key(" \"갈 생각했네. 봉평장에서 한번이나 흐뭇하게 사본 일이 있었을까. ", "en"),
    convert_key("내일 대화 장에서나 한 몫 벌어야겠네.\" ", "en"),

    convert_key(" \"오늘밤은 밤을 새서 걸어야 될 걸.\" ", "en"),
    convert_key(" \"달이 뜨렷다.\" ", "en"),
    convert_key("절렁절렁 소리를 내며 조선달이 그 날 산 돈을 따지는 것을 보고 허생원은 ", "en"),
    convert_key("말뚝에서 넓은 휘장을 걷고 벌려 놓았던 물건을 거두기 ", "en"),
    convert_key("시작했다. 무명필과 주단 바리가 두 고리짝에 꼭 찼다. 멍석 위에는 천조각이 ", "en"),

    convert_key("어수선하게 남았다. ", "en"),
    convert_key(" 다른 축들도 벌써 거의 짐을 걷고 있었다. 약바르게 떠나는 패도 ", "en"),
    convert_key("있었다. 어물 장수도 땜장이도 엿장수도, 생강 장사도 꼴들이 보이지 ", "en"),
    convert_key("않았다. 내일은 진부와 대화에 장이 선다. 측들은 그 어느 쪽으로든지 ", "en"),
    convert_key("밤을 새며, 육, 칠십리 밤길을 타박거리지 않으면 안된다. 장판은 잔치 ", "en"),

    convert_key("뒤 마당같이 어수선하게 벌어지고 술집에서는 싸움이 터져 있었다. ", "en"),
    convert_key("주정꾼 욕지거리에 섞여 계집의 앙칼진 목소리가 찢어졌다. 장날 저녁은 ", "en"),
    convert_key("정해 놓고 계집의 고함소리로 시작되는 것이다. ", "en"),
    convert_key(" \"생원, 시침을 떼도 다 아니. 충줏집 말야.\" ", "en"),
    convert_key(" 계집 목소리로 문득 생각난 듯이 조선달은 비죽이 웃는다. ", "en"),

    convert_key(" \"화중지병이지. 연소패들을 적수로 하구야 대거리가 돼야 말이지.\" ", "en"),
    convert_key(" \"그렇지도 않을걸. 측들이 사족을 못쓰는 것도 사실은 사실이나, 아무리 ", "en"),
    convert_key("그렇다 군 해도 왜 그 동이 말일세. 감쪽같이 충줏집을 후린 눈치거든.\" ", "en"),
    convert_key(" \"무어 그 애숭이가? 물건 가질 낚았나부지. 확실한 녀석인 줄 알았더니.\" ", "en"),
    convert_key(" \"그 길만은 알 수 있나... 궁리 말구 가보세나 그려. 한 내턱 씀세.\" ", "en"),

]

en_texts = [
    "The Selfish Giant ",
    " Every afternoon, as they were coming from school, the children used ",
    "to go and play in the giant's garden. ",
    " It was a large lovely garden, with soft green grass.  Here and there ",
    "over the grass stook beautiful flowers like stars, and there were ",

    "twelve peachtrees that in the springtime broke out into delicate blos- ",
    "soms of pink and pearl, and in the autumn bore rich fruit.  The birds ",
    "sat in the trees and sang so sweetly that the children used to stop ",
    "their games in order to listen to them.  \"How happy we are here!\" they ",
    "cried to each other. ",

    " One day the Giant came back.  He had been to visit his friend the ",
    "Cornish ogre, and had stayed with him for seven years.  After the seven ",
    "years were over he had said all that he had to say, for his conversa- ",
    "tion was limited, and he determined to return to his own castle.  When",
    "he arrived he saw the children playing in the garden. ",

    " \"What are you doing here?\" he cried in a very gruff voice, and the "
    "children ran away. ",
    " \"My own garden is my own garden,\" said the Giant; \"anyone can under- ",
    "stand that, and I will allow nobody to play in it but myself.\"  So he ",
    "built a high wall all round it, and put up a notice-board. ",

    " TRESPASSERS WILL BE PROSECUTED ",
    " He was a very selfish Giant. ",
    " The poor children had now nowhere to play.  They tried to play in the ",
    "road was very dusty and full of hard stones, and they did not like it. ",
    "They used to wander round the high wall when their lessons were over, ",

    "and talk about the beautiful garden inside.  \"How happy we were there!\" ",
    "they said to each other. ",
    " Then the Spring came, and all over the country there were little blos- ",
    "soms and little birds.  Only in the garden of the Selfish Giant it was ",
    "still winter.  The birds did not care to sing in it as there were no"

]