from tools.data import ReadData

### Parse input ###
lantern_start_pop = ReadData("2021/data/6_t.txt", lines=False, read_int=False)
lantern_start_pop.special_split(',', make_int=True)

class LantarnFish(object):
    def __init__(self, start_population):
        self.previous_day = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
        for i in start_population:
            self.previous_day[i] += 1

    def new_day(self):
        new_day = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
        for i in new_day:
            if i == 0:
                new_day[6] = self.previous_day[0]
                new_day[8] = self.previous_day[0]
            else:
                new_day[i - 1] += self.previous_day[i]
        self.previous_day = new_day

    def check_pop_size(self):
        total_fish = 0
        for i in self.previous_day:
            total_fish += self.previous_day[i]
        return total_fish

    def simulate_fish(self, days):
        for day in range(days):
            self.new_day()
        return self.check_pop_size()

# Part 1
lantarn_sim = LantarnFish(lantern_start_pop)
print(lantarn_sim.simulate_fish(80))

# Part 2
print(lantarn_sim.simulate_fish(256))