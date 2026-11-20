"""Uch qatlamli muhitda suv filtratsiyasi: har bir ajratuvchida elastik suv zaxirasi,
qatlamlarda K(x,y), bosimsiz yuqori qatlam, quduqlar, infiltratsiya va bug'lanish."""
from .tor import Tor
from .model import Model, Quduq
from .yechuvchi import Yechuvchi
from . import etalon

__all__ = ["Tor", "Model", "Quduq", "Yechuvchi", "etalon"]
__version__ = "0.1.0"
