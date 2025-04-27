class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes television variables
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__past_volume = self.__volume


    def power(self) -> None:
        """
        Toggles On / Off Status
        """
        self.__status = not self.__status


    def mute(self) -> None:
        """
        Toggles Mute Status
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__past_volume
            else:
                self.__muted = True
                self.__past_volume = self.__volume
                self.__volume = 0


    def channel_up(self) -> None:
        """
        Method to increase the tv channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL


    def channel_down(self) -> None:
        """
        Method to decrease the tv channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL


    def volume_up(self) -> None:
        """
        Method to increase tv volume
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__past_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            self.__past_volume = self.__volume


    def volume_down(self) -> None:
        """
        Method to decrease tv volume
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__past_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            self.__past_volume = self.__volume


    def __str__(self) -> str:
        """
        Output function
        :return: Television status list
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


