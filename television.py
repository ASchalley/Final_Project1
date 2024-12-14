import csv
from PyQt6.QtWidgets import *
from remote import *


class Television(QMainWindow, Ui_MainWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 5
    MIN_CHANNEL = 0
    MAX_CHANNEL = 9

    def __init__(self) -> None:
        """
        Method to define variables and set up UI.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        super().__init__()
        self.setupUi(self)
        self.onoffButton.clicked.connect(lambda : self.power())

    def power(self) -> None:
        """
        Method to turn tv off and on.
        """
        if self.__status:
            self.__status = False
            self.onoffDisplay.setText("Power: OFF")
        else:
            self.__status = True
            self.onoffDisplay.setText("Power: ON")

    def mute(self) -> None:
        """
        Method to mute and unmute tv.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Method to increase tv channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease tv channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease tv volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to display tv status.
        :return: tv status.
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
