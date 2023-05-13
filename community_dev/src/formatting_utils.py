import datetime


def human_date(d: datetime.date):
    """
    Convert a datetime.date object to a human readable date.

    Args:
        d (datetime.date): _description_
    """

    def ordinal(n: int):
        return "%d%s" % (
            n,
            "tsnrhtdd"[((n // 10 % 10 != 1) * (n % 10 < 4) * n % 10) :: 4],
        )

    formatted_date = d.strftime(f"{ordinal(d.day)} %B %Y")
    return formatted_date
