import pandas as pd
from pytrends.request import TrendReq


class GoogleTrends:
    def __init__(self):
        self._collection = list()

        # initiates Google connection
        self.pytrends = TrendReq(hl='en-US', tz=360)

    def get_response(self, keyword: str,
                     collect: bool=True,
                     **kwargs):
        """Default keyword arguments are used, unless chosen my user.
        Search must have at least one keyword and can have up to 5
        parameters: timeframe, geo, cat, tz, gprop"""
        #TODO: Handle multiple keywords, other parameters

        if not keyword:
            return None

        keywords = []
        keywords.append(keyword)
        self.pytrends.build_payload(kw_list=keywords,
                                    **kwargs)
        # timeframe syntax
        response = self.pytrends.interest_over_time()
        response = response.reset_index()

        if collect:
            self._collection.append(response)

        return response


      #TODO: create option csv report download 
#     def create_report(self, response):
#
# #         df = response.drop(columns=['isPartial'])
#         # creates a csv report of the data from the request
#         filename = 'InterestOverTime{}.csv'.format(1)
#
#         if self.cat:
#             cat_header = 'Category: ' + self.cat.name
#         else:
#             cat_header = 'Category: All categories'
#
#         with open(filename, "w") as f:
#             f.write(cat_header)
#             f.write('\n')
#
#         report = response.to_csv(filename,
#                                  columns=[response.columns[1], response.columns[2]],
#                                  sep=',',
#                                  encoding='utf-8',
#                                  index=False,
#                                  mode='a')
#         report = dfinal.to_csv(t, index=False, mode='a')
#         return report
