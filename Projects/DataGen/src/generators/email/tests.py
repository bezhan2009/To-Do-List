import unittest
from datagen.src.generators.email.generator import generate_email, GeneratedEmail


class TestEmailGenerator(unittest.TestCase):
    def test_generate_email_real_domain(self):
        random_email = generate_email(real_domain=True)
        self.assertIsInstance(random_email, GeneratedEmail)
        self.assertIn(random_email.email.split('@')[1], ["gmail.com", "outlook.com", "yahoo.com"])
        local_part = random_email.email.split('@')[0]
        self.assertTrue(local_part[:-4].islower())
        self.assertTrue(local_part[:-4].isalpha())
        self.assertTrue(local_part[-4:].isdigit())

    def test_generate_email_random_domain(self):
        random_email = generate_email(real_domain=False)
        self.assertIsInstance(random_email, GeneratedEmail)
        domain = random_email.email.split('@')[1]
        self.assertIn('.', domain)
        self.assertTrue(domain.split('.')[0].islower())
        self.assertTrue(domain.split('.')[1].islower())
        local_part = random_email.email.split('@')[0]
        self.assertTrue(local_part[:-4].islower())
        self.assertTrue(local_part[:-4].isalpha())
        self.assertTrue(local_part[-4:].isdigit())

    def test_generated_email_str(self):
        email = "testuser1234@gmail.com"
        generated_email = GeneratedEmail(email)
        self.assertEqual(str(generated_email), email)

    def test_generated_email_repr(self):
        email = "testuser1234@gmail.com"
        generated_email = GeneratedEmail(email)
        self.assertEqual(repr(generated_email), 'GeneratedEmail(email=testuser1234@gmail.com)')


if __name__ == '__main__':
    unittest.main()
