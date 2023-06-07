import datetime
from typing import List


def split_date(start_date: str, end_date: str) -> List[List[str]]:
    """
    按天切割时间
    :param start_date: 起始时间
    :param end_date: 结束时间
    :return: 按天分割后的时间列表
    """
    start_date = datetime.datetime.strptime(start_date[0:10], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date[0:10], "%Y-%m-%d")
    if start_date > end_date:
        raise Exception("传入的起始时间大于结束时间")
    time_durations = []
    while (end_date - start_date).days > 1:
        tmp_end_date = start_date + datetime.timedelta(1)
        time_durations.append([str(start_date), str(tmp_end_date)])
        start_date = tmp_end_date
    if start_date != end_date:
        time_durations.append([str(start_date), str(end_date)])
    time_durations.append([str(end_date), str(end_date).replace("00:00:00", "23:59:59")])
    return time_durations


def gap_days(higher_date: str, lower_date: str) -> int:
    higher_date = datetime.datetime.strptime(higher_date[0:10], "%Y-%m-%d")
    lower_date = datetime.datetime.strptime(lower_date[0:10], "%Y-%m-%d")
    num = (higher_date - lower_date).days
    return num


def ago_date(days: int = 0, hours: int = 0, minutes: int = 0) -> datetime.datetime:
    return datetime.datetime.now() - datetime.timedelta(days=days, hours=hours, minutes=minutes)


if __name__ == "__main__":
    durations = split_date('2022-03-05', '2022-03-07')
    print(durations)
