class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Store speeds of the cars
        speeds = {}
        for i in range(0, len(position)):
            speeds[position[i]] = speed[i]

        # Sort positions in descending order
        position.sort(reverse=True)

        fleets = []

        for i in range(0, len(position)):
            dist = target - position[i]
            time = dist / speeds[position[i]]

            # First car fleet
            if i == 0:
                fleets.append(time)
            # If prev car's time is less, add to fleets
            elif fleets[len(fleets)-1] < time:
                fleets.append(time)

        return len(fleets)
        
        



        