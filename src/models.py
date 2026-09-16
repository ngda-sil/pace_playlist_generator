from dataclasses import dataclass, field


def s_to_ms(seconds):
    """Convert seconds to ms"""

    return seconds * 1000


@dataclass
class IntervalSession:
    """Interval Session requested by the user"""

    dist_m: int
    m_pace: int
    s_pace: int
    rest_s: int
    rep: int
    rest_ms: int = field(init=False)
    effort_duration_ms: int = field(init=False)

    def __post_init__(self):
        if self.dist_m <= 0:
            raise ValueError("distance must be greater than 0")
        if self.m_pace < 0:
            raise ValueError("pace minutes must be greater than 0")
        if (self.s_pace < 0) or (self.s_pace >= 60):
            raise ValueError("pace seconds must be between 0 and 59")
        if self.m_pace + self.s_pace == 0:
            raise ValueError("pace cannot be 0:00")
        if self.rest_s < 0:
            raise ValueError("rest seconds must be 0 or greater")
        if self.rep <= 0:
            raise ValueError("repetitions must be greater than 0")

        self.rest_ms = s_to_ms(self.rest_s)
        self.effort_duration_ms = self._calculate_effort_duration_in_ms(
            self.m_pace, self.s_pace, self.dist_m
        )

    def _calculate_effort_duration_in_ms(self, m, s, dist_m):
        """Convert min/s to ms on given distance in meter."""

        return (m * 60 + s) * dist_m
