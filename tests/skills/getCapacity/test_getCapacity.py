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
    assert skills.getCapacity() is None


def test_should_return_None_when_capacity_label_is_not_visible():
    skills = loadSkillsByImage('capacityLabelNotVisible.png')
    assert skills.getCapacity() is None


def test_should_return_327_when_gray_color():
    skills = loadSkillsByImage('capacityWith327AndGrayColor.png')
    assert skills.getCapacity() == 327


def test_should_return_327_when_green_color():
    skills = loadSkillsByImage('capacityWith327AndGreenColor.png')
    assert skills.getCapacity() == 327


def test_should_return_327_when_orange_color():
    skills = loadSkillsByImage('capacityWith327AndOrangeColor.png')
    assert skills.getCapacity() == 327


def test_should_return_318_218_when_gray_color():
    skills = loadSkillsByImage('capacityWith318218AndGrayColor.png')
    assert skills.getCapacity() == 318_218


def test_should_return_318_218_when_green_color():
    skills = loadSkillsByImage('capacityWith318218AndGreenColor.png')
    assert skills.getCapacity() == 318_218


def test_should_return_318_218_when_orange_color():
    skills = loadSkillsByImage('capacityWith318218AndOrangeColor.png')
    assert skills.getCapacity() == 318_218
