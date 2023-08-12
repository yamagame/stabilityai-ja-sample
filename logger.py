import os
import logging

from copy import copy

MAPPING = {
    'DEBUG': 37,  # white
    'INFO': 36,  # cyan
    'WARNING': 33,  # yellow
    'ERROR': 31,  # red
    'CRITICAL': 41,  # white on red bg
}

PREFIX = '\033['
SUFFIX = '\033[0m'


class ColoredFormatter(logging.Formatter):
    def __init__(self, patern):
        logging.Formatter.__init__(self, patern)

    def format(self, record):
        colored_record = copy(record)
        levelname = colored_record.levelname
        seq = MAPPING.get(levelname, 37)  # default white
        colored_levelname = ('{0}{1}m{2}{3}') \
            .format(PREFIX, seq, levelname, SUFFIX)
        colored_record.levelname = colored_levelname
        return logging.Formatter.format(self, colored_record)


def getLogger(name):
    loglevel = os.environ.get("PYTHON_LOG_LEVEL", "WARNING")
    log = logging.getLogger(name)
    log.setLevel(logging.getLevelName(loglevel.upper()))
    stream_handler = logging.StreamHandler()
    formatter = ColoredFormatter(
        '%(asctime)s - %(levelname)s:%(name)s - %(message)s')
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)
    return log


out = """こんにちは。日本海新聞営業企画部の森です。このコーナーでは、日頃わたしが感じていることや、福井のニュースを中心にいろいろ書きつづっていきたいと思います。よろしくお願いします。 さて、今回のテーマは、「ふるさと納税」。最近、テレビ・新聞などで取りあげられることが多いので、ご存じの方も多いと思います。 ふるさと納税とは、自分の出身地である「ふるさと」を応援するという気持ちを寄附すること。生まれた故郷や、お世話になったふるさとなど、応援したい自治体を選べます。個人が円を超えた金額について、自己負担円を除いた全額"""

if __name__ == '__main__':
    log = getLogger(__name__)
    log.critical("critical")
    log.error("error")
    log.warning("warning")
    log.info("info")
    log.debug("debug")

    str = out.split('。')
    for s in str:
        print(s.strip())
