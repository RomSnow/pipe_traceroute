import re
from dataclasses import dataclass

from get_RIPE.data_reader import read_data


@dataclass
class RipeData:
    as_: str
    country: str
    provider: str
    src: str

    def __str__(self):
        return f'as: {self.as_}, country: {self.country}, provider: {self.provider}'


def get_data_by_ip(ip: str) -> RipeData:
    return _parse_ripe_dara(read_data(ip))


def _parse_ripe_dara(msg: str) -> RipeData:
    as_ = ''
    country = ''
    provider = ''
    src = ''
    pattern = re.compile(r' {5}(.*)$')
    for line in msg.split('\n'):
        if line.startswith('origin'):
            as_ = pattern.findall(line)[0].strip()

        elif line.startswith('source'):
            src = pattern.findall(line)[0].strip()

        elif line.startswith('country'):
            country = pattern.findall(line)[0].strip()

        elif line.startswith('descr'):
            provider = pattern.findall(line)[0].strip()

    return RipeData(as_, country, provider, src)


if __name__ == '__main__':
    print(_parse_ripe_dara('origin:          AS15169\ncountry:       US\n'))
