"""Initialize test users with Report Creator and Report Reviewer roles."""
from flask_appbuilder.security.sqla.models import User

def create_user(security_manager, username, first_name, last_name, email, role_names, password="admin"):
    """Create a user with specified roles."""
    user = security_manager.find_user(username)
    if not user:
        user = security_manager.add_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            role=security_manager.find_role("Gamma"),  # Base role
            password=password,
        )
        
        # Add additional roles
        for role_name in role_names:
            role = security_manager.find_role(role_name)
            if role:
                user.roles.append(role)
            else:
                print(f"Role {role_name} not found")
                
        security_manager.get_session.commit()
        print(f"Created user {username} with roles: {', '.join(role_names)}")
    else:
        print(f"User {username} already exists")


def load_test_users(security_manager):
    """Create test users with Report Creator and Report Reviewer roles."""
    print("Creating test users...")
    
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
