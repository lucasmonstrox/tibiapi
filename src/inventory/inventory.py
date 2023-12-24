class Inventory:
    mainBackpack: str
    amulet: str | None
    ring: str | None
    helmet: str | None
    weapon: str | None
    armor: str | None
    shield: str | None
    legs: str | None
    boots: str | None

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
