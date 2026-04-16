"""
Tests for the User model.

This module contains unit tests for the custom User model.
"""

import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
class TestUserModel:
    """Test suite for User model."""

    def test_create_user_with_email(self):
        """Test creating a user with email as username."""
        User = get_user_model()
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
        )
        
        assert user.email == 'test@example.com'
        assert user.username == ''
        assert user.check_password('testpass123')
        assert not user.is_staff
        assert user.is_active

    def test_create_user_without_email_raises_error(self):
        """Test that creating a user without email raises ValueError."""
        User = get_user_model()
        
        with pytest.raises(ValueError):
            User.objects.create_user(
                email='',
                password='testpass123',
            )

    def test_create_superuser(self):
        """Test creating a superuser."""
        User = get_user_model()
        superuser = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpass123',
        )
        
        assert superuser.email == 'admin@example.com'
        assert superuser.is_superuser
        assert superuser.is_staff
        assert superuser.is_active

    def test_user_str_returns_email(self):
        """Test that User string representation returns email."""
        User = get_user_model()
        user = User(email='string@example.com')
        
        assert str(user) == 'string@example.com'

    def test_user_email_is_unique(self):
        """Test that user email must be unique."""
        User = get_user_model()
        User.objects.create_user(
            email='unique@example.com',
            password='testpass123',
        )
        
        with pytest.raises(Exception):  # IntegrityError
            User.objects.create_user(
                email='unique@example.com',
                password='testpass123',
            )

    def test_user_verbose_names(self):
        """Test verbose names for User model."""
        User = get_user_model()
        user = User(email='verbose@example.com')
        
        assert user._meta.verbose_name == 'User'
        assert user._meta.verbose_name_plural == 'Users'

    def test_user_ordering(self):
        """Test that users are ordered by date_joined descending."""
        User = get_user_model()
        
        # Create users in different order
        user1 = User.objects.create_user(
            email='first@example.com',
            password='pass123',
        )
        user2 = User.objects.create_user(
            email='second@example.com',
            password='pass123',
        )
        
        users = list(User.objects.all())
        
        # Second user should be first (newest first)
        assert users[0] == user2
        assert users[1] == user1

    def test_user_required_fields(self):
        """Test that REQUIRED_FIELDS is empty (email is the only required field)."""
        User = get_user_model()
        
        assert User.REQUIRED_FIELDS == []

    def test_user_username_field(self):
        """Test that USERNAME_FIELD is set to email."""
        User = get_user_model()
        
        assert User.USERNAME_FIELD == 'email'
