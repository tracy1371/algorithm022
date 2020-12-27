class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], filters: List[int]) -> List[int]:
        FlavorFlag = filters[0]
        PriceFlag = filters[1]
        DistanceFlag = filters[2]
        temp = []
        if FlavorFlag == 0:
            for ind, res in enumerate(restaurants):
                dict = {}
                if res[3] <= PriceFlag and res[4] <= DistanceFlag:
                    dict['rate'] = res[1]
                    dict['id'] = res[0]
                    dict['res'] = res
                    dict['loc'] = ind
                    temp.append(dict)
            sortedtemp = sorted(temp, key=lambda x: (-x['rate'], -x['id']))
            return [y['loc'] for y in sortedtemp]
        else:
            for ind, res in enumerate(restaurants):
                dict = {}
                if res[3] <= PriceFlag and res[4] <= DistanceFlag and res[2] == 1:
                    dict['rate'] = res[1]
                    dict['id'] = res[0]
                    dict['res'] = res
                    dict['loc'] = ind
                    temp.append(dict)
            sortedtemp = sorted(temp, key=lambda x: (-x['rate'], -x['id']))
            return [y['loc'] for y in sortedtemp]





