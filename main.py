import pyautogui as pg
import time
from hangul_utils import convert_key


time.sleep(2)

# 텍스트 보정
texts = [
    convert_key("메밀꽃 필 무렵", "en")
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


for index in range(len(en_texts)):
    pg.write(en_texts[index], interval=0.15)
