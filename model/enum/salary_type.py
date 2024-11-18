import enum


class SalaryType(enum.Enum):
    ANNUAL = "연봉"
    MONTHLY = "월급"
    DAILY = "일급"
    HOURLY = "시급"
    PER_CASE = "건별"
    COMPANY_POLICY = "회사내규"
