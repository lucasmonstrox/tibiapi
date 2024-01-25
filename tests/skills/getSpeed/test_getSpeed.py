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
    assert skills.getSpeed() is None


def test_should_return_None_when_soul_points_label_is_not_visible():
    skills = loadSkillsByImage('speedLabelNotVisible.png')
    assert skills.getSpeed() is None


def test_should_return_729():
    skills = loadSkillsByImage('speedWith729.png')
    assert skills.getSpeed() == 729


def test_should_return_65535():
    skills = loadSkillsByImage('speedWith65535.png')
    assert skills.getSpeed() == 65_535
