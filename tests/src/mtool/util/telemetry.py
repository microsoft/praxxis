from src.mtool.util import telemetry

def test_send(root, filename, current_scene_db):
    telemetry.send(root, filename, current_scene_db)

