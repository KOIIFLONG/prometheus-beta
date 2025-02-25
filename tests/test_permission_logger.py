import pytest
import logging
from src.permission_logger import PermissionLogger, UserPermissionLevel

class TestPermissionLogger:
    def setup_method(self):
        """Setup a fresh logger before each test"""
        self.logger = PermissionLogger()
    
    def test_default_guest_log_fails(self, caplog):
        """Test that a guest cannot log a user-level message"""
        with pytest.raises(PermissionError):
            self.logger.log("User message")
    
    def test_user_can_log_user_message(self, caplog):
        """Test that a user can log a user-level message"""
        self.logger.set_user_level(UserPermissionLevel.USER)
        caplog.set_level(logging.INFO)
        
        self.logger.log("User message")
        assert "User message" in caplog.text
    
    def test_admin_can_log_user_and_debug_messages(self, caplog):
        """Test that an admin can log user and debug messages"""
        self.logger.set_user_level(UserPermissionLevel.ADMIN)
        caplog.set_level(logging.INFO)
        
        # User-level log
        self.logger.log("User message")
        assert "User message" in caplog.text
        
        # Debug log
        self.logger.debug("Debug message")
        assert "Debug message" in caplog.text
    
    def test_super_admin_can_log_all_messages(self, caplog):
        """Test that a super admin can log all messages"""
        self.logger.set_user_level(UserPermissionLevel.SUPER_ADMIN)
        caplog.set_level(logging.INFO)
        
        # User-level log
        self.logger.log("User message")
        assert "User message" in caplog.text
        
        # Debug log
        self.logger.debug("Debug message")
        assert "Debug message" in caplog.text
        
        # System log
        self.logger.system("System message")
        assert "System message" in caplog.text
    
    def test_debug_log_requires_admin(self, caplog):
        """Test that debug log requires admin permissions"""
        with pytest.raises(PermissionError):
            self.logger.debug("Debug message")
    
    def test_system_log_requires_super_admin(self, caplog):
        """Test that system log requires super admin permissions"""
        with pytest.raises(PermissionError):
            self.logger.system("System message")
    
    def test_message_contains_permission_error_details(self):
        """Test that permission error includes details about required and current levels"""
        try:
            self.logger.debug("Unauthorized message")
        except PermissionError as e:
            assert "Required: ADMIN" in str(e)
            assert "Current: GUEST" in str(e)