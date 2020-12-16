from app_sliced import app

import pytest
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_app1_valid_input_kill(client):
    payload = dict(
        component_id = "worker"
        )
    payload = json.dumps(payload)
    result = client.post('/kill', data=payload, content_type='application/json')
    assert b"OK" in result.data

def test_app2_valid_input_disconnect(client):
    payload = dict(
        component_id = "worker"
        )
    payload = json.dumps(payload)
    result = client.post('/disconnect', data=payload, content_type='application/json')
    assert b"OK" in result.data
    
def test_app3_valid_input_reconnect(client):
    payload = dict(
        component_id = "worker"
        )
    payload = json.dumps(payload)
    result = client.post('/reconnect', data=payload, content_type='application/json')
    assert b"OK" in result.data

def test_app4_invalid_string_1_kill(client):
    payload = dict(
        component_id = "abravesoldierinafghanistanonlycarriesouthisdutyandleadshisnationtovictory"
        )
    payload = json.dumps(payload)
    result = client.post('/kill', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app5_invalid_string_1_disconnect(client):
    payload = dict(
        component_id = "abravesoldierinafghanistanonlycarriesouthisdutyandleadshisnationtovictory"
        )
    payload = json.dumps(payload)
    result = client.post('/disconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app6_invalid_string_1_reconnect(client):
    payload = dict(
        component_id = "abravesoldierinafghanistanonlycarriesouthisdutyandleadshisnationtovictory"
        )
    payload = json.dumps(payload)
    result = client.post('/reconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app7_invalid_string_2_kill(client):
    payload = dict(
        component_id = ""
        )
    payload = json.dumps(payload)
    result = client.post('/kill', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app8_invalid_string_2_disconnect(client):
    payload = dict(
        component_id = ""
        )
    payload = json.dumps(payload)
    result = client.post('/disconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app9_invalid_string_2_reconnect(client):
    payload = dict(
        component_id = ""
        )
    payload = json.dumps(payload)
    result = client.post('/reconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app10_invalid_string_3_kill(client):
    payload = dict(
        component_id = None
        )
    payload = json.dumps(payload)
    result = client.post('/kill', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app11_invalid_string_3_disconnect(client):
    payload = dict(
        component_id = None
        )
    payload = json.dumps(payload)
    result = client.post('/disconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app12_invalid_string_3_reconnect(client):
    payload = dict(
        component_id = None
        )
    payload = json.dumps(payload)
    result = client.post('/reconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app13_invalid_string_4_kill(client):
    payload = dict(
        component_id = "ABC8^#/~~~/"
        )
    payload = json.dumps(payload)
    result = client.post('/kill', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app14_invalid_string_4_disconnect(client):
    payload = dict(
        component_id = "ABC8^#/~~~/"
        )
    payload = json.dumps(payload)
    result = client.post('/disconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app15_invalid_string_4_reconnect(client):
    payload = dict(
        component_id = "ABC8^#/~~~/"
        )
    payload = json.dumps(payload)
    result = client.post('/reconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data
