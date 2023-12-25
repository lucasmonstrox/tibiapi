from typing import Optional


class Inventory:
    mainBackpack: str
    amulet: Optional[str]
    ring: Optional[str]
    helmet: Optional[str]
    weapon: Optional[str]
    armor: Optional[str]
    shield: Optional[str]
    legs: Optional[str]
    boots: Optional[str]

    def isMainBackpackEquipped(self) -> bool:
        return True

    def isAmuletEquipped(self) -> bool:
        return True

    def isRingEquipped(self) -> bool:
        return True

    def isHelmetEquipped(self) -> bool:
        return True

    def isWeaponEquipped(self) -> bool:
        return True

    def isArmorEquipped(self) -> bool:
        return True

    def isShieldEquipped(self) -> bool:
        return True

    def isLegsEquipped(self) -> bool:
        return True

    def isBootsEquipped(self) -> bool:
        return True
