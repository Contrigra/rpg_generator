import pytest

from django.urls import reverse


class TestKnave:

    @pytest.mark.django_db
    def test_character_generation_return(self, client):
        response = client.get(
            reverse('character_page'))
        assert response.status_code == 200, f'Status is not 200' \
                                            f' {response.status_code}'

    @pytest.mark.django_db
    def test_character_generation_content(self, client):
        response = client.get(
            f'http://localhost:8000/create_character/generate/')

        assert isinstance(response.content, bytes)
