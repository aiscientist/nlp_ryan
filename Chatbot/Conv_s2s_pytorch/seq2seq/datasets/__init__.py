from .text import LinedTextDataset
from .open_subtitles import OpenSubtitles2016
from .wmt import WMT16_de_en
from .multi_language import MultiLanguageDataset
from .coco_caption import CocoCaptions

__all__ = ('LinedTextDataset',
           'OpenSubtitles2016',
           'MultiLanguageDataset',
           'WMT16_de_en',
           'CocoCaptions')
