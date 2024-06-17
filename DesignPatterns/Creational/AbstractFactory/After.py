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


"""
--------- CREATED AN ABSTRACT MEDIA CLASS WHICH 
"""

class AbstractMedia(ABC):
    @abstractmethod
    def audio(self):
        pass

    @abstractmethod
    def video(self):
        pass


class Low(AbstractMedia):
    def audio(self):
        return LowQualityAudio()

    def video(self):
        return H234DecoderVideo()


class Medium(AbstractMedia):
    def audio(self):
        return MediumQualityAudio()

    def video(self):
        return HDDecoderVideo()


class High(AbstractMedia):
    def audio(self):
        return HighQualityAudio()

    def video(self):
        return FHDDecoderVideo()



def main():
    input_quality = input("enter the desired quality: ")

