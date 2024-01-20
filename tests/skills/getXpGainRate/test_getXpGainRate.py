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
    assert skills.getXpGainRate() is None


def test_should_return_None_when_skills_xp_gain_rate_label_is_not_visible():
    skills = loadSkillsByImage('xpGainRateLabelMinimized.png')
    assert skills.getXpGainRate() is None


def test_should_return_50_when_pixels_are_orange():
    skills = loadSkillsByImage('xpGainRateWith50Percentage.png')
    assert skills.getXpGainRate() == 50


def test_should_return_100_when_pixels_are_gray():
    skills = loadSkillsByImage('xpGainRateWith100Percentage.png')
    assert skills.getXpGainRate() == 100


def test_should_return_150_when_pixels_are_green():
    skills = loadSkillsByImage('xpGainRateWith150Percentage.png')
    assert skills.getXpGainRate() == 150
