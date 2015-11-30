import xml.etree.ElementTree as ElementTree

from base import BaseTestCase
from flask import url_for


class ViewsTests(BaseTestCase):
    # Ensures rout '/' renders the correct view
    def test_index_should_render_default_view(self):
        # act
        self.client.get('/')

        # assert
        self.assert_template_used('index.html')

    def test_post_to_welcome_should_serve_twiml(self):
        # act
        response = self.client.post('/ivr/welcome')
        twiml = ElementTree.fromstring(response.data)

        # assert
        assert not twiml.findall("./Gather/Play") is None
        assert twiml.findall("./Gather")[0].attrib["action"] == url_for('menu')

    def test_post_to_menu_with_digit_1_should_serve_twiml_with_say_twice_and_hangup(self):
        # act
        response = self.client.post('/ivr/menu', data=dict(Digits="1"), follow_redirects=True)
        twiml = ElementTree.fromstring(response.data)

        # assert
        assert len(twiml.findall("./Say")) == 2
        assert not twiml.findall("./Hangup") is None

    def test_post_to_menu_with_digit_2_should_serve_twiml_with_gather_and_say(self):
        # act
        response = self.client.post('/ivr/menu', data=dict(Digits="2"), follow_redirects=True)
        twiml = ElementTree.fromstring(response.data)

        # assert
        assert not twiml.findall("./Say") is None
        assert twiml.findall("./Gather")[0].attrib["action"] == url_for('planets')

    def test_post_to_menu_with_digit_other_than_1_or_2_should_redirect_to_welcome(self):
        # act
        response = self.client.post('/ivr/menu', data=dict(Digits="4"), follow_redirects=True)
        twiml = ElementTree.fromstring(response.data)

        # assert
        assert not twiml.findall("./Redirect") is None
        assert twiml.findall("./Redirect")[0].text == url_for('welcome')

    def test_post_to_planets_with_digit_2_3_or_4_should_serve_twiml_with_dial(self):
        # act
        response = self.client.post('/ivr/planets', data=dict(Digits="4"), follow_redirects=True)
        twiml = ElementTree.fromstring(response.data)

        # assert
        assert not twiml.findall("./Dial")[0].text is None

    def test_post_to_planets_with_digit_other_than_2_3_or_4_should_redirect_to_welcome(self):
        # act
        response = self.client.post('/ivr/planets', data=dict(Digits="*"), follow_redirects=True)
        twiml = ElementTree.fromstring(response.data)

        # assert
        assert not twiml.findall("./Redirect") is None
        assert twiml.findall("./Redirect")[0].text == url_for('welcome')
