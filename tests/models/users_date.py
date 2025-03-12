from tests.models.user import User

guest = User(
    full_name='Ignatov Andrey',
    email='test-mail2025@gmail.com',
    current_address='Test address 2025',
    permanent_address='Test permanent address 2025'

)

admin = User(
    full_name='Super Admin',
    email='test-admin2025@gmail.com',
    current_address='Test address 2025 admin',
    permanent_address='Test permanent address 2025 admin'

)