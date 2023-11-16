class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__muteLifeRaft = 0

    def power(self) -> None:
        """
        Method turns power True and False
        Other methods here check to see if this is True and False
        :return:
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Method decresases volume to MIN_VOLUME
        does not work if self.__status == False
        :return: None
        """
        if self.__status:
            self.__muted = True
            self.__muteLifeRaft = self.__volume
            self.__volume = Television.MIN_VOLUME

    def channel_up(self) -> None:
        """
        Method to increases channel number
        does not work if self.__status == False
        loops back to MIN_CHANNEL if over 3
        :return: None
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease channel number
        does not work if self.__status == False
        Loops to MAX_CHANNEL if under 0
        :return: None
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to raise volume
        turns self.__mute to false when called
        does not work if self.__status == False
        :return: None
        """
        if self.__status and not self.__muted:
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
        elif self.__muted:
            self.__volume = self.__muteLifeRaft
            self.__volume += 1
            self.__muted = False

    def volume_down(self) -> None:
        """
        Method to lower volume
        turns self.__mute to false when called
        does not work if self.__status == False
        :return: None
        """
        if self.__status and not self.__muted:
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
        elif self.__muted:
            self.__volume = self.__muteLifeRaft
            self.__volume -= 1
            self.__muted = False

    def __str__(self) -> str:
        """
        method to show tv status
        :return: tv status
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
