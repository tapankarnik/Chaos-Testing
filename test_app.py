from app_sliced import app

import pytest
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_app1(client):
    payload = dict(
        component_id = "worker"
        )
    payload = json.dumps(payload)
    result = client.post('/kill', data=payload, content_type='application/json')
    assert b"OK" in result.data

def test_app2(client):
    payload = dict(
        component_id = "worker"
        )
    payload = json.dumps(payload)
    result = client.post('/disconnect', data=payload, content_type='application/json')
    assert b"OK" in result.data
    
def test_app3(client):
    payload = dict(
        component_id = "worker"
        )
    payload = json.dumps(payload)
    result = client.post('/reconnect', data=payload, content_type='application/json')
    assert b"OK" in result.data

def test_app4(client):
    payload = dict(
        component_id = "abravesoldierinafghanistanonlycarriesouthisdutyandleadshisnationtovictory"
        )
    payload = json.dumps(payload)
    result = client.post('/kill', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app5(client):
    payload = dict(
        component_id = "abravesoldierinafghanistanonlycarriesouthisdutyandleadshisnationtovictory"
        )
    payload = json.dumps(payload)
    result = client.post('/disconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app6(client):
    payload = dict(
        component_id = "abravesoldierinafghanistanonlycarriesouthisdutyandleadshisnationtovictory"
        )
    payload = json.dumps(payload)
    result = client.post('/reconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app7(client):
    payload = dict(
        component_id = ""
        )
    payload = json.dumps(payload)
    result = client.post('/kill', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app8(client):
    payload = dict(
        component_id = ""
        )
    payload = json.dumps(payload)
    result = client.post('/disconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app9(client):
    payload = dict(
        component_id = ""
        )
    payload = json.dumps(payload)
    result = client.post('/reconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app10(client):
    payload = dict(
        component_id = None
        )
    payload = json.dumps(payload)
    result = client.post('/kill', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app11(client):
    payload = dict(
        component_id = None
        )
    payload = json.dumps(payload)
    result = client.post('/disconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app12(client):
    payload = dict(
        component_id = None
        )
    payload = json.dumps(payload)
    result = client.post('/reconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app13(client):
    payload = dict(
        component_id = "ABC8^#/~~~/"
        )
    payload = json.dumps(payload)
    result = client.post('/kill', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app14(client):
    payload = dict(
        component_id = "ABC8^#/~~~/"
        )
    payload = json.dumps(payload)
    result = client.post('/disconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_app15(client):
    payload = dict(
        component_id = "ABC8^#/~~~/"
        )
    payload = json.dumps(payload)
    result = client.post('/reconnect', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data
