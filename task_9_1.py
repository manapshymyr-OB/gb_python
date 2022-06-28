import time


class TrafficLight:

    __light_states = {'RED': 7, 'YELLOW': 3, 'GREEN': 7}
    __colors = ''

    def running(self):
        for color, time_sleep in self.__light_states.items():
            self.__colors = color
            print(f"TrafficLight switched to state '{self.__colors}' "
                  f"on {time_sleep} seconds")

            time.sleep(time_sleep)


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()



