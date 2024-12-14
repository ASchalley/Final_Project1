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
        self.muteButton.clicked.connect(lambda: self.mute())
        self.volumeUp.clicked.connect(lambda: self.volume_up())
        self.volumeDown.clicked.connect(lambda: self.volume_down())
        self.channelUp.clicked.connect(lambda: self.channel_up())
        self.channelDown.clicked.connect(lambda: self.channel_down())
        self.channelButton1.clicked.connect(lambda: self.set_channel(1))
        self.channelButton2.clicked.connect(lambda: self.set_channel(2))
        self.channelButton3.clicked.connect(lambda: self.set_channel(3))
        self.channelButton4.clicked.connect(lambda: self.set_channel(4))
        self.channelButton5.clicked.connect(lambda: self.set_channel(5))
        self.channelButton6.clicked.connect(lambda: self.set_channel(6))
        self.channelButton7.clicked.connect(lambda: self.set_channel(7))
        self.channelButton8.clicked.connect(lambda: self.set_channel(8))
        self.channelButton9.clicked.connect(lambda: self.set_channel(9))
        self.channelButton0.clicked.connect(lambda: self.set_channel(0))

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
                self.muteDisplay.setText("Mute: OFF")
            else:
                self.__muted = True
                self.muteDisplay.setText("Mute: ON")

    def channel_up(self) -> None:
        """
        Method to increase tv channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
                self.channelDisplay.setText(f"Channel: {self.__channel}")
            else:
                self.__channel = Television.MIN_CHANNEL
                self.channelDisplay.setText(f"Channel: {self.__channel}")

    def channel_down(self) -> None:
        """
        Method to decrease tv channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
                self.channelDisplay.setText(f"Channel: {self.__channel}")
            else:
                self.__channel = Television.MAX_CHANNEL
                self.channelDisplay.setText(f"Channel: {self.__channel}")

    def set_channel(self, desiredchannel) -> None:
        """
        Method to return to the previous channel entered.
        """
        if self.__status:
            self.__channel = desiredchannel
            self.channelDisplay.setText(f"Channel: {self.__channel}")


    def volume_up(self) -> None:
        """
        Method to increase tv volume.
        """
        if self.__status:
            self.__muted = False
            self.muteDisplay.setText("Mute: OFF")
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.volumeDisplay.setText(f"Volume: {self.__volume}")

    def volume_down(self) -> None:
        """
        Method to decrease tv volume.
        """
        if self.__status:
            self.__muted = False
            self.muteDisplay.setText("Mute: OFF")
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.volumeDisplay.setText(f"Volume: {self.__volume}")