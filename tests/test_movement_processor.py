import pytest
import esper
from gnome_wars.main import Velocity, Renderable, MovementProcessor
from unittest.mock import Mock


@pytest.fixture
def movement_processor():
    return MovementProcessor(0, 800, 0, 600)


def test_entity_movement(movement_processor):
    entity = esper.create_entity()
    velocity = Velocity(x=5, y=5)
    mock_image = Mock()
    mock_image.get_width.return_value = 10
    mock_image.get_height.return_value = 10
    renderable = Renderable(mock_image, 100, 100)
    esper.add_component(entity, velocity)
    esper.add_component(entity, renderable)
    esper.add_processor(movement_processor)

    # Process the world to update entity positions
    esper.process()

    # Assert that entity moved as expected
    assert renderable.x == 105
    assert renderable.y == 105
