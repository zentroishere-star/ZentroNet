// WhatsApp Chat Widget JavaScript

class WhatsAppChat {
    constructor(options = {}) {
        this.phoneNumber = options.phoneNumber || '1234567890'; // Default, should be configured
        this.businessName = options.businessName || 'Zentro Team';
        this.services = options.services || [
            'Web Development',
            'Mobile Applications',
            'UI/UX Design',
            'Consulting',
            'Custom Solutions'
        ];
        this.responseTime = options.responseTime || '2-4 hours';
        
        this.init();
    }

    init() {
        this.createFloatButton();
        this.createModal();
        this.attachEventListeners();
    }

    createFloatButton() {
        const floatButton = document.createElement('div');
        floatButton.className = 'whatsapp-float-button';
        floatButton.id = 'whatsapp-float-btn';
        floatButton.innerHTML = '<i class="fab fa-whatsapp"></i>';
        floatButton.title = 'Chat with us on WhatsApp';
        document.body.appendChild(floatButton);
    }

    createModal() {
        const modal = document.createElement('div');
        modal.className = 'whatsapp-modal-overlay';
        modal.id = 'whatsapp-modal-overlay';

        modal.innerHTML = `
            <div class="whatsapp-modal">
                <div class="whatsapp-modal-header">
                    <h3>
                        <i class="fab fa-whatsapp"></i>
                        <span style="color: white;">Chat with Us</span>
                    </h3>
                    <button class="whatsapp-modal-close" id="whatsapp-modal-close">
                        <i class="fas fa-times"></i>
                    </button>
                </div>

                <div class="whatsapp-modal-body">
                    <div class="whatsapp-info-section">
                        <p>👋 Welcome to ${this.businessName}! We're here to help you with any questions about our projects and services.</p>
                    </div>

                    <div style="margin-bottom: 20px;">
                        <h4 style="margin: 0 0 12px 0; color: #333; font-size: 14px; font-weight: 600;">Our Services:</h4>
                        <ul class="whatsapp-services-list">
                            ${this.services.map(service => `<li>${service}</li>`).join('')}
                        </ul>
                    </div>

                    <form class="whatsapp-form" id="whatsapp-form">
                        <div class="whatsapp-form-group">
                            <label for="wa-inquiry-type">Inquiry Type</label>
                            <select id="wa-inquiry-type" name="inquiry_type" required>
                                <option value="">Select an option</option>
                                <option value="project_inquiry">Project Inquiry</option>
                                <option value="service_inquiry">Service Inquiry</option>
                                <option value="collaboration">Collaboration</option>
                                <option value="support">Support</option>
                                <option value="other">Other</option>
                            </select>
                        </div>

                        <div class="whatsapp-form-group">
                            <label for="wa-name">Your Name</label>
                            <input type="text" id="wa-name" name="name" placeholder="Enter your name" required>
                        </div>

                        <div class="whatsapp-form-group">
                            <label for="wa-email">Your Email</label>
                            <input type="email" id="wa-email" name="email" placeholder="Enter your email" required>
                        </div>

                        <div class="whatsapp-form-group">
                            <label for="wa-message">Your Message</label>
                            <textarea id="wa-message" name="message" placeholder="Tell us about your project or inquiry..." required></textarea>
                        </div>

                        <div class="whatsapp-btn-group">
                            <button type="submit" class="whatsapp-btn whatsapp-btn-primary" id="whatsapp-send-btn">
                                <i class="fab fa-whatsapp"></i>
                                Send on WhatsApp
                            </button>
                            <button type="reset" class="whatsapp-btn whatsapp-btn-secondary" id="whatsapp-cancel-btn">
                                <i class="fas fa-times"></i>
                                Cancel
                            </button>
                        </div>

                        <div class="whatsapp-status">
                            <span class="whatsapp-status-dot"></span>
                            <strong>Typical response time: ${this.responseTime}</strong>
                        </div>
                    </form>
                </div>
            </div>
        `;

        document.body.appendChild(modal);
    }

    attachEventListeners() {
        const floatBtn = document.getElementById('whatsapp-float-btn');
        const modal = document.getElementById('whatsapp-modal-overlay');
        const closeBtn = document.getElementById('whatsapp-modal-close');
        const form = document.getElementById('whatsapp-form');
        const cancelBtn = document.getElementById('whatsapp-cancel-btn');

        // Open modal
        floatBtn.addEventListener('click', () => {
            modal.classList.add('active');
        });

        // Close modal
        closeBtn.addEventListener('click', () => {
            modal.classList.remove('active');
        });

        cancelBtn.addEventListener('click', () => {
            modal.classList.remove('active');
            form.reset();
        });

        // Close modal when clicking outside
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
            }
        });

        // Handle form submission
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.sendMessage();
        });
    }

    sendMessage() {
        const inquiryType = document.getElementById('wa-inquiry-type').value;
        const name = document.getElementById('wa-name').value;
        const email = document.getElementById('wa-email').value;
        const message = document.getElementById('wa-message').value;

        // Validate inputs
        if (!inquiryType || !name || !email || !message) {
            alert('Please fill in all fields');
            return;
        }

        // Format message for WhatsApp
        const inquiryLabel = this.getInquiryLabel(inquiryType);
        const whatsappMessage = `Hello ${this.businessName} Team!\n\n` +
            `I'm reaching out regarding: ${inquiryLabel}\n\n` +
            `My Details:\n` +
            `Name: ${name}\n` +
            `Email: ${email}\n\n` +
            `Message:\n${message}\n\n` +
            `Looking forward to hearing from you!`;

        // Create WhatsApp URL
        const encodedMessage = encodeURIComponent(whatsappMessage);
        const whatsappUrl = `https://wa.me/${this.phoneNumber}?text=${encodedMessage}`;

        // Open WhatsApp (will open app on mobile, web on desktop)
        window.open(whatsappUrl, '_blank');

        // Reset form and close modal
        document.getElementById('whatsapp-form').reset();
        document.getElementById('whatsapp-modal-overlay').classList.remove('active');

        // Show success message
        this.showNotification('Your message has been sent! WhatsApp will open shortly.');
    }

    getInquiryLabel(type) {
        const types = {
            'project_inquiry': '💼 Project Inquiry',
            'service_inquiry': '🛠️ Service Inquiry',
            'collaboration': '🤝 Collaboration',
            'support': '🆘 Support',
            'other': '❓ Other'
        };
        return types[type] || 'General Inquiry';
    }

    showNotification(message) {
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: #25D366;
            color: white;
            padding: 15px 20px;
            border-radius: 6px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            z-index: 1000;
            animation: slideInRight 0.3s ease;
        `;
        notification.textContent = message;
        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }
}

// Initialize WhatsApp Chat Widget when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    // Get WhatsApp number from data attribute or default
    const phoneNumber = document.documentElement.getAttribute('data-whatsapp-number') || '919876543210'; // Replace with your number
    
    const whatsappChat = new WhatsAppChat({
        phoneNumber: phoneNumber,
        businessName: 'Zentro Team',
        services: [
            'Web Development',
            'Mobile Applications',
            'UI/UX Design',
            'Cloud Solutions',
            'API Development',
            'Consulting & Strategy'
        ],
        responseTime: '2-4 hours'
    });
});

// Add animation styles dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
