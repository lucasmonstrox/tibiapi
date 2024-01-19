import os
from tibiapi._common.rectImage import RectImage
from tibiapi.skills import Skills
from tibiapi.utils.image import load


def loadSkillsByImage(imagePath: str) -> Skills:
    currentPath = os.path.dirname(os.path.abspath(__file__))
    skillsImage = load(f'{currentPath}/images/{imagePath}')
    skillsRectImage = RectImage(0, 0, skillsImage)
    return Skills(skillsRectImage)


def test_should_return_None_when_skills_container_is_minimized():
    skills = loadSkillsByImage('skillsMinimized.png')
    assert skills.getLevelPercentage() is None


def test_should_return_0_when_level_bar_is_empty():
    skills = loadSkillsByImage('skillsWith0Percentage.png')
    assert skills.getLevelPercentage() == 0


def test_should_return_1_when_level_bar_is_1_of_percentage():
    skills = loadSkillsByImage('skillsWith1Percentage.png')
    assert skills.getLevelPercentage() == 1


def test_should_return_5_when_level_bar_is_5_of_percentage():
    skills = loadSkillsByImage('skillsWith5Percentage.png')
    assert skills.getLevelPercentage() == 5


def test_should_return_10_when_level_bar_is_10_of_percentage():
    skills = loadSkillsByImage('skillsWith10Percentage.png')
    assert skills.getLevelPercentage() == 10


def test_should_return_15_when_level_bar_is_15_of_percentage():
    skills = loadSkillsByImage('skillsWith15Percentage.png')
    assert skills.getLevelPercentage() == 15


def test_should_return_20_when_level_bar_is_20_of_percentage():
    skills = loadSkillsByImage('skillsWith20Percentage.png')
    assert skills.getLevelPercentage() == 20


def test_should_return_25_when_level_bar_is_25_of_percentage():
    skills = loadSkillsByImage('skillsWith25Percentage.png')
    assert skills.getLevelPercentage() == 25


def test_should_return_30_when_level_bar_is_30_of_percentage():
    skills = loadSkillsByImage('skillsWith30Percentage.png')
    assert skills.getLevelPercentage() == 30


def test_should_return_35_when_level_bar_is_35_of_percentage():
    skills = loadSkillsByImage('skillsWith35Percentage.png')
    assert skills.getLevelPercentage() == 35


def test_should_return_40_when_level_bar_is_40_of_percentage():
    skills = loadSkillsByImage('skillsWith40Percentage.png')
    assert skills.getLevelPercentage() == 40


def test_should_return_45_when_level_bar_is_45_of_percentage():
    skills = loadSkillsByImage('skillsWith45Percentage.png')
    assert skills.getLevelPercentage() == 45


def test_should_return_50_when_level_bar_is_50_of_percentage():
    skills = loadSkillsByImage('skillsWith50Percentage.png')
    assert skills.getLevelPercentage() == 50


def test_should_return_55_when_level_bar_is_55_of_percentage():
    skills = loadSkillsByImage('skillsWith55Percentage.png')
    assert skills.getLevelPercentage() == 55


def test_should_return_60_when_level_bar_is_60_of_percentage():
    skills = loadSkillsByImage('skillsWith60Percentage.png')
    assert skills.getLevelPercentage() == 60


def test_should_return_65_when_level_bar_is_65_of_percentage():
    skills = loadSkillsByImage('skillsWith65Percentage.png')
    assert skills.getLevelPercentage() == 65


def test_should_return_70_when_level_bar_is_70_of_percentage():
    skills = loadSkillsByImage('skillsWith70Percentage.png')
    assert skills.getLevelPercentage() == 70


def test_should_return_75_when_level_bar_is_75_of_percentage():
    skills = loadSkillsByImage('skillsWith75Percentage.png')
    assert skills.getLevelPercentage() == 75


def test_should_return_80_when_level_bar_is_80_of_percentage():
    skills = loadSkillsByImage('skillsWith80Percentage.png')
    assert skills.getLevelPercentage() == 80


def test_should_return_85_when_level_bar_is_85_of_percentage():
    skills = loadSkillsByImage('skillsWith85Percentage.png')
    assert skills.getLevelPercentage() == 85


def test_should_return_90_when_level_bar_is_90_of_percentage():
    skills = loadSkillsByImage('skillsWith90Percentage.png')
    assert skills.getLevelPercentage() == 90


def test_should_return_95_when_level_bar_is_95_of_percentage():
    skills = loadSkillsByImage('skillsWith95Percentage.png')
    assert skills.getLevelPercentage() == 95


def test_should_return_99_when_level_bar_is_99_of_percentage():
    skills = loadSkillsByImage('skillsWith99Percentage.png')
    assert skills.getLevelPercentage() == 99
