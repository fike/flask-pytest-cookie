import re


# def test_index(app, client):
#     del app
#     res = client.get('/')
#     assert res.status_code == 200
    # expected = {'hello': 'world'}
    # assert expected == json.loads(res.get_data(as_text=True))

def test_cookie(app, client):
    del app
    response = client.get("/")
    assert response.status_code == 200
    cookie_header = response.headers['Set-Cookie']
    cookie_color = re.match('^color=(ligthgray|orange|purple)', cookie_header)
    cookie_match = str(cookie_color.group(1))
    print(cookie_match)
    assert cookie_match in str(['ligthgray', 'orange', 'purple'])
     
