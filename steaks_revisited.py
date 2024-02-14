# by Kami Bigdely
# Extract class
class Steak:
    WELL_DONE = 3000
    MEDIUM = 2500
    COOKED_CONSTANT = 0.05

    def __init__(self, time, temperature, pressure):
        self.time = time
        self.temperature = temperature
        self.pressure = pressure

    def is_cooked_to_criteria(self, desired_state):
        return self.is_well_done(desired_state) or self.is_medium(desired_state)

    def is_well_done(self, desired_state):
        return desired_state == 'well-done' and self.get_cooking_progress() >= self.WELL_DONE

    def is_medium(self, desired_state):
        return desired_state == 'medium' and self.get_cooking_progress() >= self.MEDIUM

    def get_cooking_progress(self):
        return self.time * self.temperature * self.pressure * self.COOKED_CONSTANT


time = 30  # [min]
temp = 103  # [celcius]
pressure = 20  # [psi]
desired_state = 'well-done'

steak = Steak(time, temp, pressure)

if steak.is_cooked_to_criteria(desired_state):
    print('Cooking is done.')
else:
    print('Ongoing cooking.')
