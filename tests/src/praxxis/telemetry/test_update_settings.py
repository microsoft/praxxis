import pytest

def test_quit_update_settings(setup, monkeypatch, telemetry_db):
    from src.praxxis.telemetry import update_settings

    with monkeypatch.context() as m:
        m.setattr("builtins.input", lambda *args: 'q')
        assert update_settings.update_settings(telemetry_db) == 0


def test_value_error(setup, telemetry_db):
    from src.praxxis.telemetry import update_settings

    assert update_settings.get_ordinal("not_ord", update_settings.get_values(telemetry_db), telemetry_db) == "not_ordinal"

def test_edit_settings(setup, monkeypatch, telemetry_db):
    from src.praxxis.telemetry import update_settings
    import os 

    with monkeypatch.context() as m:
        m.setattr("builtins.input", lambda *args: 'nn')
        update_settings.edit_settings(1, update_settings.get_values(telemetry_db), telemetry_db)
