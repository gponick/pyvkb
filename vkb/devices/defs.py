from .base import VENDOR_ID
from .gladiatork import GladiatorK, GladiatorKLH
from .gladiatornxt import GladiatorNXT

VKB_DEVICES = {0x0132: GladiatorK, 0x0133: GladiatorKLH, 0x0200: GladiatorNXT}
