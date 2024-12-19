"""Initialization module for Superset."""

def init_app_users(security_manager):
    """Initialize application users."""
    print("Creating test users...")
    
    from .init_users import create_user
    
    # Create a Report Creator
    create_user(
        security_manager=security_manager,
        username="report_creator",
        first_name="Report",
        last_name="Creator",
        email="report_creator@example.com",
        role_names=["Report Creator", "Gamma"],
    )
    
    # Create a Report Reviewer
    create_user(
        security_manager=security_manager,
        username="report_reviewer", 
        first_name="Report",
        last_name="Reviewer",
        email="report_reviewer@example.com",
        role_names=["Report Reviewer", "Gamma"],
    )
    
    # Create a user with both roles
    create_user(
        security_manager=security_manager,
        username="report_admin",
        first_name="Report",
        last_name="Admin",
        email="report_admin@example.com", 
        role_names=["Report Creator", "Report Reviewer", "Gamma"],
    )

    # Create an admin user
    create_user(
        security_manager=security_manager,
        username="admin",
        first_name="Super",
        last_name="Admin",
        email="admin@example.com",
        role_names=["Admin"],
    )

    print("Finished creating test users")
