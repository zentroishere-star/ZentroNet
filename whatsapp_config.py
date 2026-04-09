# WhatsApp Chat Widget Configuration
# This file contains all the configuration for the WhatsApp chat widget

# IMPORTANT: Set your WhatsApp business number here
# Format: Country Code + Number (no + or spaces)
# Examples:
#   India: 919876543210
#   USA: 14155552671
#   UK: 441632960000
WHATSAPP_NUMBER = "918015649044"  # ← UPDATE THIS WITH YOUR BUSINESS NUMBER

# Business/Company name
BUSINESS_NAME = "Zentro Team"

# Services offered (shown in the widget)
SERVICES = [
    "Web Development",
    "Mobile Applications",
    "UI/UX Design",
    "Cloud Solutions",
    "API Development",
    "Consulting & Strategy",
]

# Typical response time
RESPONSE_TIME = "2-4 hours"

# Location Configuration
# Supported States and Districts
STATES = [
    {'value': 'tamil_nadu', 'label': 'Tamil Nadu'},
    {'value': 'karnataka', 'label': 'Karnataka'},
    {'value': 'maharashtra', 'label': 'Maharashtra'},
    {'value': 'delhi', 'label': 'Delhi'},
]

# Tamil Nadu Districts (38 total)
TAMIL_NADU_DISTRICTS = [
    'Ariyalur',
    'Chengalpattu',
    'Chennai',
    'Coimbatore',
    'Cuddalore',
    'Dharmapuri',
    'Dindigul',
    'Erode',
    'Kallakurichi',
    'Kanchipuram',
    'Kanniyakumari',
    'Karur',
    'Krishnagiri',
    'Madurai',
    'Mayiladuthurai',
    'Nagapattinam',
    'Namakkal',
    'Nilgiris',
    'Perambalur',
    'Pudukkottai',
    'Ramanathapuram',
    'Ranipet',
    'Salem',
    'Sivaganga',
    'Tenkasi',
    'Thanjavur',
    'Theni',
    'Thoothukudi',
    'Tiruchirappalli',
    'Tirunelveli',
    'Tirupattur',
    'Tiruppur',
    'Tiruvallur',
    'Tiruvannamalai',
    'Tiruvarur',
    'Vellore',
    'Viluppuram',
    'Virudhunagar',
]

# Widget appearance settings
WIDGET_CONFIG = {
    # Colors (CSS color values)
    "primary_color": "#25D366",      # Main green
    "secondary_color": "#1f8857",    # Darker green
    "dark_color": "#0f3d2a",         # Dark accent
    "light_color": "#e8f5e9",        # Light background
    
    # Position
    "bottom_position": "30px",       # Distance from bottom
    "right_position": "30px",        # Distance from right
    
    # Size
    "button_width": "70px",
    "button_height": "70px",
    "button_icon_size": "40px",
    
    # Animations
    "enable_pulse_animation": True,
    "enable_hover_effect": True,
    
    # Modal
    "modal_width": "450px",
    "modal_max_width_percent": "90%",
}

# Inquiry type options (in the dropdown)
INQUIRY_TYPES = [
    {"value": "project_inquiry", "label": "💼 Project Inquiry"},
    {"value": "service_inquiry", "label": "🛠️ Service Inquiry"},
    {"value": "collaboration", "label": "🤝 Collaboration"},
    {"value": "support", "label": "🆘 Support"},
    {"value": "other", "label": "❓ Other"},
]

# Form placeholders and labels
FORM_LABELS = {
    "inquiry_type": "Inquiry Type",
    "name": "Your Name",
    "email": "Your Email",
    "message": "Your Message",
}

FORM_PLACEHOLDERS = {
    "name": "Enter your name",
    "email": "Enter your email",
    "message": "Tell us about your project or inquiry...",
}

# Modal messages
MODAL_MESSAGES = {
    "header": "Chat with Us",
    "welcome": "Welcome to {business_name}! We're here to help you with any questions about our projects and services.",
    "services_label": "Our Services:",
    "status_online": "Typical response time: {response_time}",
    "submit_button": "Send on WhatsApp",
    "cancel_button": "Cancel",
    "success_message": "Your message has been sent! WhatsApp will open shortly.",
}

# Enable/Disable widget
ENABLE_WHATSAPP_WIDGET = True

# Widget logging (for debugging)
DEBUG_MODE = False

