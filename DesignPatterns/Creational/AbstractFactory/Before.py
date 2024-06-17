from abc import ABC, abstractmethod
import pylint
"""
Scenario : 3 types of Audio, 3 types of Video; based on their quality.
"""


class BaseAudioClass(ABC):
    """
    This is the parent Abstract Base Class for Audio
    """
    @abstractmethod
    def message(self, message):
        """ converts the message """
        raise NotImplementedError

    @abstractmethod
    def save(self, filepath):
        """
        saves the audio to a filepath
        :return:
        """
        raise NotImplementedError


class LowQualityAudio(BaseAudioClass):
    """
    The base class for audio
    """
    def message(self, message):
        """ converts the message
        :return:
        """
        raise NotImplementedError

    def save(self, filepath):
        """
        saves the audio to a filepath
        :return:
        """
        raise NotImplementedError


class MediumQualityAudio(BaseAudioClass):
    """
    The base class for audio
    """
    def message(self, message):
        """ converts the message
        :return:
        """
        raise NotImplementedError

    def save(self, filepath):
        """
        saves the audio to a filepath
        :return:
        """
        raise NotImplementedError


class HighQualityAudio(BaseAudioClass):
    """
    The base class for audio
    """
    def message(self, message):
        """ converts the message
        :return:
        """
        raise NotImplementedError

    def save(self, filepath):
        """
        saves the audio to a filepath
        :return:
        """
        raise NotImplementedError


class BaseVideoClass(ABC):
    """
    This is the parent Abstract Base Class for Audio
    """
    @abstractmethod
    def video(self, message):
        """ converts the message """
        raise NotImplementedError

    @abstractmethod
    def save(self, filepath):
        """
        saves the audio to a filepath
        :return:
        """
        raise NotImplementedError


class H234DecoderVideo(BaseVideoClass):
    def video(self, message):
        """ converts the message """
        raise NotImplementedError

    def save(self, filepath):
        """
        saves the audio to a filepath
        :return:
        """
        raise NotImplementedError


class HDDecoderVideo(BaseVideoClass):
    def video(self, message):
        """ converts the message """
        raise NotImplementedError

    def save(self, filepath):
        """
        saves the audio to a filepath
        :return:
        """
        raise NotImplementedError


class FHDDecoderVideo(BaseVideoClass):
    def video(self, message):
        """ converts the message """
        raise NotImplementedError

    def save(self, filepath):
        """
        saves the audio to a filepath
        :return:
        """
        raise NotImplementedError


def main():
    input_quality = input("enter the quality of Audio desired")

    if input_quality == 'low':
        audio = LowQualityAudio()
        video = H234DecoderVideo()
    elif input_quality == 'medium':
        audio = MediumQualityAudio()
        video = HDDecoderVideo()
    else:
        audio = HighQualityAudio()
        video = FHDDecoderVideo()

    # calling the functions
    audio.save()
    audio.message()

    video.save()
    video.message()


help(pylint.run_pyreverse())
# pylint.run_pyreverse(['D:\git\pythonProjects\DesignPatterns\Creational\AbstractFactory\Before.py'])

