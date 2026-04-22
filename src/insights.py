class InsightGenerator:
    def __init__(self, campaigns):
        self.campaigns = campaigns

    def top_campaign(self):
        return max(self.campaigns, key=lambda x: x.roas())

    def worst_campaign(self):
        return min(self.campaigns, key=lambda x: x.roas())

    def summary(self):
        top = self.top_campaign()
        worst = self.worst_campaign()

        return {
            "top_campaign": top.name,
            "top_roas": round(top.roas(), 2),
            "worst_campaign": worst.name,
            "worst_roas": round(worst.roas(), 2)
        }