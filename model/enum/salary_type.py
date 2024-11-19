import enum


class SalaryType(enum.Enum):
    ANNUAL = "ANNUAL"
    MONTHLY = "MONTHLY"
    DAILY = "DAILY"
    HOURLY = "HOURLY"
    PER_CASE = "PER_CASE"
    COMPANY_POLICY = "COMPANY_POLICY"
