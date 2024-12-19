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
