class Campaign:
    def __init__(self, name, spend, revenue, clicks):
        self.name = name
        self.spend = float(spend)
        self.revenue = float(revenue)
        self.clicks = float(clicks)

    @classmethod
    def from_row(cls, row):
        return cls(
            name=row["campaign"],
            spend=row["spend"],
            revenue=row["revenue"],
            clicks=row["clicks"]
        )

    def roas(self):
        return self.revenue / self.spend if self.spend else 0

    def cpc(self):
        return self.spend / self.clicks if self.clicks else 0

    def efficiency_label(self):
        if self.roas() > 2 and self.cpc() < 10:
            return "High Efficiency"
        elif self.roas() < 1:
            return "Loss Making"
        return "Average"