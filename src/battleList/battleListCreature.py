from functools import cached_property


class BattleListCreature:
    @cached_property
    def name(self) -> str:
        return 'unknown'

    @cached_property
    def healthPercentage(self) -> int:
        return 100
