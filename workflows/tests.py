from django.test import TestCase
from workflows.models import Step

class StepTestCase(TestCase):
    def setUp(self):
        Step.objects.create(name="request")

    def test_step_has_name(self):
        # Steps have a name
        req = Step.objects.get(name="request")
        self.assertEqual(req.name, "request")