import pytest
import run

class TestApi:

    post_keys ={"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}



    @pytest.fixture
    def app_instance(self):
        app = run.app
        #app.config.from_pyfile("testing.py")  #если хотим заменить какие-то данные при тестах удобно
        test_client = app.test_client()
        return test_client


    def test_all_posts_has_correct_stratus(self,app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        assert result.status_code == 200

        #single_post
    def test_single_post_has_correct_stratus(self,app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        assert result.status_code == 200

    def test_single_post_non_existent404(self,app_instance):
        result = app_instance.get("/api/posts/777", follow_redirects=True)
        assert result.status_code == 404

    def test_single_post_has_correct_keys(self,app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        post = result.get_json()
        post_keys = set(post.keys())
        assert post_keys == self.post_keys


