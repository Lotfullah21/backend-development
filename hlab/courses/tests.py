from django.test import TestCase


class CourseRoutesTests(TestCase):
    def test_feedbackform_route_is_not_captured_by_course_slug(self):
        response = self.client.get("/courses/feedbackform/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "name")
        self.assertContains(response, "comment")
        self.assertContains(response, "Submit")

    def test_unknown_course_returns_404(self):
        response = self.client.get("/courses/unknown-course/")

        self.assertEqual(response.status_code, 404)

    def test_feedbackform_accepts_post(self):
        response = self.client.post(
            "/courses/feedbackform/",
            {"name": "Lotfullah", "comment": "Useful course", "rating": 5},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Thank you for your feedback Lotfullah")
