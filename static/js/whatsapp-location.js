/**
 * WhatsApp Location-Based Floating Chat Widget
 * With Indian States and Districts
 * Professional ES6 Class Implementation
 */

class WhatsAppLocationWidget {
    // Comprehensive Indian State-District Mapping
    static STATE_DISTRICT_MAP = {

        'Karnataka': [
            'Select a District',
                'Bagalkot',
                'Ballari',
                'Belagavi',
                'Bengaluru Rural',
                'Bengaluru Urban',
                'Bidar',
                'Chamarajanagar',
                'Chikballapur',
                'Chikkamagaluru',
                'Chitradurga',
                'Dakshina Kannada',
                'Davanagere',
                'Dharwad',
                'Gadag',
                'Kalaburagi',
                'Hassan',
                'Haveri',
                'Kodagu',
                'Kolar',
                'Koppal',
                'Mandya',
                'Mysuru',
                'Raichur',
                'Ramanagara',
                'Shivamogga',
                'Tumakuru',
                'Udupi',
                'Uttara Kannada',
                'Vijayapura',
                'Yadgir',
                'Vijayanagara'
        ],
        'Kerala': [
            'Select a District',
                'Alappuzha',
                'Ernakulam',
                'Idukki',
                'Kannur',
                'Kasaragod',
                'Kollam',
                'Kottayam',
                'Kozhikode',
                'Malappuram',
                'Palakkad',
                'Pathanamthitta',
                'Thiruvananthapuram',
                'Thrissur',
                'Wayanad'
        ],
 
    
        'Tamil Nadu': [
            'Select a District',
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
            'Virudhunagar'
        ],
     
    };

    constructor(config = {}) {
        // Configuration
        this.phoneNumber = config.phoneNumber || this.getPhoneFromHtml();
        
        // State management
        this.isOpen = false;
        this.selectedState = '';
        this.selectedDistrict = '';
        this.selectedUserType = '';
        this.isLoading = false;
        
        // DOM elements cache
        this.elements = {};
        
        // Initialize on DOM ready
        this.init();
    }

    /**
     * Get phone number from HTML data attribute
     */
    getPhoneFromHtml() {
        const html = document.querySelector('html');
        return html?.getAttribute('data-whatsapp-number') || '918015649044';
    }

    /**
     * Initialize the widget
     */
    init() {
        // Remove any old widgets first
        this.cleanupOldWidgets();
        
        // Create new widget
        this.createHTML();
        this.cacheElements();
        this.attachEventListeners();
        this.logClick('Widget initialized - Old widgets removed');
    }

    /**
     * Clean up old widget instances and DOM
     */
    cleanupOldWidgets() {
        try {
            // Remove old widget classes from DOM
            const oldElements = [
                '.whatsapp-float-button:not(.whatsapp-location-button)',
                '.whatsapp-modal-overlay',
                '.whatsapp-modal',
                '.whatsapp-chat-panel:not(.whatsapp-location-panel)',
                '.whatsapp-float-chat',
                '[class*="whatsapp-modal-overlay"]'
            ];
            
            oldElements.forEach(selector => {
                const elements = document.querySelectorAll(selector);
                elements.forEach(el => {
                    try {
                        el.remove();
                    } catch(e) {
                        // Ignore errors
                    }
                });
            });
            
            // Kill old instance variables
            if (window.whatsappChat) {
                try {
                    window.whatsappChat = null;
                } catch(e) {}
            }
            
            if (window.whatsappModernChat) {
                try {
                    window.whatsappModernChat = null;
                } catch(e) {}
            }
            
            console.log('[WhatsApp Widget] Cleaned up old widget instances');
        } catch(e) {
            console.log('[WhatsApp Widget] Cleanup process complete');
        }
    }

    /**
     * Dynamically create HTML structure
     */
    createHTML() {
        // Main container
        const container = document.createElement('div');
        container.innerHTML = '<button class="whatsapp-location-button" aria-label="Open WhatsApp chat"><i class="fab fa-whatsapp"></i></button>' +
                             '<div class="whatsapp-location-overlay"></div>' +
                             '<div class="whatsapp-location-panel">' +
                             '<div class="whatsapp-location-header">' +
                             '<div class="whatsapp-location-header-title">' +
                             '<h3><i class="fab fa-whatsapp"></i> Chat with us</h3>' +
                             '<p>Help you find accommodation</p>' +
                             '</div>' +
                             '<button class="whatsapp-location-close" aria-label="Close chat"><i class="fas fa-times"></i></button>' +
                             '</div>' +
                             '<div class="whatsapp-location-body">' +
                             '<div class="whatsapp-location-info">' +
                             '<strong>To help us serve you better:</strong>' +
                             '<p>Please share your location.</p>' +
                             '</div>'+
                             '<form class="whatsapp-location-form" id="whatsappLocationForm">'+
                             '<div class="whatsapp-location-form-group">'+
                             '<label for="stateSelect">Select Your State <span class="required">*</span></label>'+
                             '<select id="stateSelect" class="whatsapp-location-select" aria-label="Select state" required>'+
                             '<option value="">Select a State</option>'+
                             '</select></div>'+
                             '<div class="whatsapp-location-form-group">'+
                             '<label for="districtSelect">Select District <span class="required">*</span></label>'+
                             '<select id="districtSelect" class="whatsapp-location-select" aria-label="Select district" disabled required>'+
                             '<option value="">Select a District</option>'+
                             '</select></div>'+
                             '<div class="whatsapp-location-form-group">'+
                             '<label for="userTypeSelect">I am a <span class="required">*</span></label>'+
                             '<select id="userTypeSelect" class="whatsapp-location-select" aria-label="Select user type" required>'+
                             '<option value="">Select Type</option>'+
                             '<option value="Student">Student</option>'+
                             '<option value="Working Professional">Working Professional</option>'+
                             '</select></div>'+
                             '</form></div>'+
                             '<div class="whatsapp-location-button-section">'+
                             '<button class="whatsapp-location-start-btn" id="startChatBtn" disabled aria-label="Start chat on WhatsApp">'+
                             '<i class="fab fa-whatsapp"></i> Start Chat'+
                             '</button></div>'+
                             '<div class="whatsapp-location-status">'+
                             '<div class="status-dot"></div>'+
                             '<span>Reply time: 2 hours</span>'+
                             '</div></div>'+
                             '</div>';

        document.body.appendChild(container);
    }

    /**
     * Cache DOM elements for performance
     */
    cacheElements() {
        this.elements = {
            button: document.querySelector('.whatsapp-location-button'),
            overlay: document.querySelector('.whatsapp-location-overlay'),
            panel: document.querySelector('.whatsapp-location-panel'),
            closeBtn: document.querySelector('.whatsapp-location-close'),
            stateSelect: document.getElementById('stateSelect'),
            districtSelect: document.getElementById('districtSelect'),
            userTypeSelect: document.getElementById('userTypeSelect'),
            startBtn: document.getElementById('startChatBtn'),
            form: document.getElementById('whatsappLocationForm')
        };

        // Populate states
        this.populateStates();
    }

    /**
     * Populate state dropdown
     */
    populateStates() {
        const states = Object.keys(WhatsAppLocationWidget.STATE_DISTRICT_MAP);
        
        states.forEach(state => {
            const option = document.createElement('option');
            option.value = state;
            option.textContent = state;
            this.elements.stateSelect.appendChild(option);
        });
    }

    /**
     * Populate district dropdown based on selected state
     */
    populateDistricts(state) {
        // Clear previous districts
        this.elements.districtSelect.innerHTML = '<option value="">Select a District</option>';
        this.selectedDistrict = '';

        if (!state) {
            this.elements.districtSelect.disabled = true;
            return;
        }

        const districts = WhatsAppLocationWidget.STATE_DISTRICT_MAP[state] || [];
        
        districts.forEach(district => {
            const option = document.createElement('option');
            option.value = district;
            option.textContent = district;
            this.elements.districtSelect.appendChild(option);
        });

        this.elements.districtSelect.disabled = false;
        this.checkFormValidity();
    }

    /**
     * Check form validity and enable/disable button
     */
    checkFormValidity() {
        const isValid = this.selectedState && this.selectedDistrict && this.selectedUserType;
        
        if (isValid) {
            this.elements.startBtn.disabled = false;
        } else {
            this.elements.startBtn.disabled = true;
        }
    }

    /**
     * Attach event listeners
     */
    attachEventListeners() {
        // Button click - toggle panel
        this.elements.button.addEventListener('click', () => this.togglePanel());

        // Close button click
        this.elements.closeBtn.addEventListener('click', () => this.closePanel());

        // Overlay click
        this.elements.overlay.addEventListener('click', () => this.closePanel());

        // State select change
        this.elements.stateSelect.addEventListener('change', (e) => {
            this.selectedState = e.target.value;
            this.populateDistricts(this.selectedState);
            this.logClick(`State selected: ${this.selectedState}`);
        });

        // District select change
        this.elements.districtSelect.addEventListener('change', (e) => {
            this.selectedDistrict = e.target.value;
            this.checkFormValidity();
            this.logClick(`District selected: ${this.selectedDistrict}`);
        });

        // User type select change
        this.elements.userTypeSelect.addEventListener('change', (e) => {
            this.selectedUserType = e.target.value;
            this.checkFormValidity();
            this.logClick(`User type selected: ${this.selectedUserType}`);
        });

        // Start chat button
        this.elements.startBtn.addEventListener('click', () => this.handleStartChat());

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.isOpen) {
                this.closePanel();
            }
        });

        // Disable "Select a District" option
        this.elements.districtSelect.addEventListener('click', () => {
            const option = this.elements.districtSelect.querySelector('option[value=""]');
            if (option) {
                option.disabled = true;
            }
        });
    }

    /**
     * Toggle panel open/close
     */
    togglePanel() {
        if (this.isOpen) {
            this.closePanel();
        } else {
            this.openPanel();
        }
    }

    /**
     * Open panel
     */
    openPanel() {
        this.isOpen = true;
        this.elements.panel.classList.add('active');
        this.elements.overlay.classList.add('active');
        this.logClick('Panel opened');
    }

    /**
     * Close panel
     */
    closePanel() {
        this.isOpen = false;
        this.elements.panel.classList.remove('active');
        this.elements.overlay.classList.remove('active');
        this.logClick('Panel closed');
    }

    /**
     * Handle start chat button click
     */
    handleStartChat() {
        if (!this.validateForm()) {
            this.showNotification('Please fill all fields', 'error');
            return;
        }

        this.setLoadingState(true);

        // Create message
        const message = this.createMessage();
        
        // Simulate slight delay
        setTimeout(() => {
            this.setLoadingState(false);
            
            // Encode message
            const encodedMessage = encodeURIComponent(message);
            
            // Create WhatsApp URL
            const whatsappUrl = `https://wa.me/${this.phoneNumber}?text=${encodedMessage}`;
            
            // Log the action
            this.logClick(`Chat started - Message: ${message}`);
            
            // Show notification
            this.showNotification('Opening WhatsApp...', 'success');
            
            // Open WhatsApp
            window.open(whatsappUrl, '_blank');
            
            // Close panel after a moment
            setTimeout(() => {
                this.closePanel();
                this.resetForm();
            }, 500);
        }, 600);
    }

    /**
     * Create the message to be sent
     */
    createMessage() {
        return `Hi, I am looking for accommodation in ${this.selectedDistrict}, ${this.selectedState}. I am a ${this.selectedUserType}.`;
    }

    /**
     * Validate form
     */
    validateForm() {
        return this.selectedState && this.selectedDistrict && this.selectedUserType;
    }

    /**
     * Reset form
     */
    resetForm() {
        this.elements.form.reset();
        this.elements.districtSelect.innerHTML = '<option value="">Select a District</option>';
        this.elements.districtSelect.disabled = true;
        this.selectedState = '';
        this.selectedDistrict = '';
        this.selectedUserType = '';
        this.checkFormValidity();
    }

    /**
     * Set loading state
     */
    setLoadingState(isLoading) {
        this.isLoading = isLoading;
        if (isLoading) {
            this.elements.startBtn.classList.add('whatsapp-location-loading');
            this.elements.startBtn.disabled = true;
        } else {
            this.elements.startBtn.classList.remove('whatsapp-location-loading');
            this.checkFormValidity();
        }
    }

    /**
     * Show notification toast
     */
    showNotification(message, type = 'success') {
        const notification = document.createElement('div');
        notification.className = `whatsapp-location-notification ${type}`;
        notification.textContent = message;
        notification.setAttribute('role', 'status');
        notification.setAttribute('aria-live', 'polite');
        
        document.body.appendChild(notification);
        
        // Auto remove after 3 seconds
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }

    /**
     * Log clicks for analytics (development)
     */
    logClick(message) {
        console.log(`[WhatsApp Widget] ${message}`);
    }
}

// Initialize widget when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.whatsappLocationWidget = new WhatsAppLocationWidget();
});
