import pathlib
from tibiapi._common.rectImage import RectImage
from tibiapi.skills import Skills
from tibiapi.utils.image import load


def loadSkillsByImage(imagePath: str) -> Skills:
    currentPath = pathlib.Path(__file__).parent.resolve()
    skillsImage = load(f'{currentPath}/images/{imagePath}')
    skillsRectImage = RectImage(0, 0, skillsImage)
    return Skills(skillsRectImage)


def test_should_return_None_when_skills_container_is_minimized():
    skills = loadSkillsByImage('skillsMinimized.png')
    assert skills.getMana() is None


def test_should_return_None_when_mana_label_is_not_visible():
    skills = loadSkillsByImage('manaLabelNotVisible.png')
    assert skills.getMana() is None


def test_should_return_150():
    skills = loadSkillsByImage('manaWith150.png')
    assert skills.getMana() == 150


def test_should_return_110_850():
    skills = loadSkillsByImage('manaWith110850.png')
    assert skills.getMana() == 110_850
