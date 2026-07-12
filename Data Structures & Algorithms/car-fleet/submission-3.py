class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carsWithSpeed = []
        for i in range(len(position)):
            carsWithSpeed.append([position[i], speed[i]])
        carsWithSpeed.sort(reverse = True)
        t1 = (target-carsWithSpeed[0][0])/carsWithSpeed[0][1]
        fleet = 1
        for i in range(len(position)):
            t2 = (target-carsWithSpeed[i][0])/carsWithSpeed[i][1]
            if t2 <= t1:
                continue
            fleet+=1
            t1=t2
        return fleet