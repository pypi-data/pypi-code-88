from coh2_stats.performance.performance_page import PerformancePage

class PerformancePageCollection:
    def __init__(self, pages: list) -> None:
        self.pages = pages

    def get_performance_page_list(self):
        performance_list = []
        for page in self.pages:
            pp = PerformancePage(page)
            performance_list.append(pp)
        return performance_list
