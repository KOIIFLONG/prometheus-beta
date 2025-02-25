import logging
from enum import Enum, auto
from typing import Optional, Any

class UserPermissionLevel(Enum):
    """Enum representing different user permission levels."""
    GUEST = 0
    USER = 1
    ADMIN = 2
    SUPER_ADMIN = 3

class PermissionLogger:
    """
    A logger that restricts console message logging based on user permissions.
    
    Attributes:
        _current_user_level (UserPermissionLevel): Current user's permission level
    """
    
    def __init__(self, user_level: UserPermissionLevel = UserPermissionLevel.GUEST):
        """
        Initialize the PermissionLogger with a default user permission level.
        
        Args:
            user_level (UserPermissionLevel, optional): Initial user permission level. 
                                                        Defaults to GUEST.
        """
        self._current_user_level = user_level
        self._logger = logging.getLogger(__name__)
        
        # Configure basic logging to console
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def set_user_level(self, user_level: UserPermissionLevel) -> None:
        """
        Set the current user's permission level.
        
        Args:
            user_level (UserPermissionLevel): New user permission level
        """
        self._current_user_level = user_level
    
    def log(self, message: str, required_level: UserPermissionLevel = UserPermissionLevel.USER) -> None:
        """
        Log a message if the current user has sufficient permissions.
        
        Args:
            message (str): The message to log
            required_level (UserPermissionLevel, optional): Minimum permission level 
                                                            required to log the message. 
                                                            Defaults to USER.
        
        Raises:
            PermissionError: If the current user does not have sufficient permissions
        """
        if self._current_user_level.value >= required_level.value:
            self._logger.info(message)
        else:
            raise PermissionError(f"Insufficient permissions to log message. "
                                  f"Required: {required_level.name}, "
                                  f"Current: {self._current_user_level.name}")
    
    def debug(self, message: str) -> None:
        """
        Log a debug message for admin-level users.
        
        Args:
            message (str): The debug message to log
        
        Raises:
            PermissionError: If the current user is not an admin
        """
        self.log(message, UserPermissionLevel.ADMIN)
    
    def system(self, message: str) -> None:
        """
        Log a system-level message for super admin users.
        
        Args:
            message (str): The system message to log
        
        Raises:
            PermissionError: If the current user is not a super admin
        """
        self.log(message, UserPermissionLevel.SUPER_ADMIN)