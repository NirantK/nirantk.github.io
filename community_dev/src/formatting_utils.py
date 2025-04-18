import datetime
from typing import Union


def human_date(d: Union[datetime.date, datetime.datetime]) -> str:
    """Convert a datetime.date or datetime.datetime object to a human readable date.

    Args:
        d: Date or datetime object to format

    Returns:
        Formatted date string (e.g., "1st January 2023")
    """
    def ordinal(n: int) -> str:
        """Convert a number to an ordinal string (1st, 2nd, 3rd, etc.).

        Args:
            n: Number to convert

        Returns:
            Ordinal string representation
        """
        return "%d%s" % (
            n,
            "tsnrhtdd"[((n // 10 % 10 != 1) * (n % 10 < 4) * n % 10) :: 4],
        )

    # If datetime, extract just the date part
    if isinstance(d, datetime.datetime):
        d = d.date()
        
    formatted_date = d.strftime(f"{ordinal(d.day)} %B %Y")
    return formatted_date
