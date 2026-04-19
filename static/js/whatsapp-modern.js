/**
 * WhatsApp Modern Floating Chat Widget
 * Professional chat panel with form UI
 * Similar to Stanza Living, Airbnb, etc.
 */

class WhatsAppModernChat {
    constructor(config = {}) {
        // Configuration
        this.phoneNumber = config.phoneNumber || '918015649044';
        this.stateData = config.stateData || this.getDefaultStates();
        this.districtData = config.districtData || this.getDefaultDistricts();
        this.localityData = config.localityData || this.getDefaultLocalities();
        this.userTypes = config.userTypes || ['Student', 'Working Professional', 'Other'];
        
        // State management
        this.isOpen = false;
        this.selectedState = '';
        this.selectedDistrict = '';
        this.selectedLocality = '';
        this.selectedUserType = '';
        
        // DOM elements
        this.elements = {};
        
        // Initialize
        this.init();
    }

    /**
     * Get default states (can be overridden)
     */
    getDefaultStates() {
        return [
            { value: '', label: 'Select a State' },
            { value: 'tamil_nadu', label: 'Tamil Nadu' },
            { value: 'karnataka', label: 'Karnataka' },
            { value: 'maharashtra', label: 'Maharashtra' },
            { value: 'delhi', label: 'Delhi' }
        ];
    }

    /**
     * Get default districts based on state (can be overridden)
     */
    getDefaultDistricts() {
        return {
            'tamil_nadu': [
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
            'karnataka': [
                'Select a District',
                'Bengaluru',
                'Bengaluru Rural',
                'Belagavi',
                'Ballari',
                'Bijapur',
                'Bidar',
                'Chikballapur',
                'Chikkamagalur',
                'Chitradurga',
                'Dakshina Kannada',
                'Davangere',
                'Dharwad',
                'Gadag',
                'Hassan',
                'Haveri',
                'Kalaburagi',
                'Kannur',
                'Kodagu',
                'Kolar',
                'Koppal',
                'Mandya',
                'Mysuru',
                'Raichur',
                'Shivamogga',
                'Tumkur',
                'Udupi',
                'Uttara Kannada',
                'Yadgir'
            ],
            'maharashtra': [
                'Select a District',
                'Mumbai',
                'Pune',
                'Nagpur',
                'Thane',
                'Ahmednagar',
                'Akola',
                'Amravati',
                'Aurangabad',
                'Bhandara',
                'Buldhana',
                'Dhule',
                'Gondia',
                'Hingoli',
                'Jalgaon',
                'Jalna',
                'Kolhapur',
                'Latur',
                'Nashik',
                'Nanded',
                'Nandurbar',
                'Raigad',
                'Ratnagiri',
                'Sangli',
                'Satara',
                'Sindhudurg',
                'Solapur',
                'Wardha',
                'Washim',
                'Yavatmal'
            ],
            'delhi': [
                'Select a District',
                'North',
                'North East',
                'East',
                'South East',
                'South',
                'South West',
                'West',
                'North West',
                'Central'
            ]
        };
    }

    /**
     * Get default localities (can be overridden)
     */
    getDefaultLocalities() {
        return {
            'Chennai': [
                'Select a Locality',
                'Adyar',
                'Alwarpet',
                'Anna Nagar',
                'Appasamudram',
                'Ayanavaram',
                'Besant Nagar',
                'Broadway',
                'Chintadripet',
                'Chetpet',
                'Chepauk',
                'Chinatown',
                'Choolaimedu',
                'Egmore',
                'George Town',
                'Gopalapuram',
                'Guindy',
                'Besant',
                'Kodambakkam',
                'Kolathur',
                'Koyambedu',
                'Luz',
                'Mylapore',
                'Nandanam',
                'Nanganallur',
                'Nesapakkam',
                'Nungambakkam',
                'Okkiyam Thoraipakkam',
                'Palavakkam',
                'Pallavaram',
                'Purasawalkam',
                'Saidapet',
                'Samuelson Road',
                'Santhome',
                'Selaiyur',
                'Semmencheri',
                'Shenoy Nagar',
                'Shoolagiri',
                'Sowcarpet',
                'Taramani',
                'Teynampet',
                'Thirumullaivoyal',
                'Thirumulla',
                'Thiruvanmiyur',
                'Thoraipakkam',
                'Tondiarpet',
                'TP Nagar',
                'Triplicane',
                'Vadapalani',
                'Villivakkam',
                'Virugambakkam',
                'Vomur',
                'Vyasarpadi',
                'Walajah Road',
                'Yercaud'
            ],
            'Bengaluru': [
                'Select a Locality',
                'Koramangala',
                'Indiranagar',
                'Marathahalli',
                'Whitefield',
                'Electronic City',
                'JP Nagar',
                'HSR Layout',
                'Bellandur',
                'BTM Layout'
            ],
            'Mumbai': [
                'Select a Locality',
                'Fort',
                'Bandra',
                'Andheri',
                'Lower Parel',
                'Juhu',
                'Powai',
                'Malad',
                'Thane',
                'Navi Mumbai'
            ]
        };
    }

    /**
     * Initialize the widget
     */
    init() {
        this.createHTML();
        this.cacheElements();
        this.attachEventListeners();
        this.disableStartButton();
    }

    /**
     * Create HTML structure
     */
    createHTML() {
        // Floating button
        const floatingButton = document.createElement('div');
        floatingButton.className = 'whatsapp-float-button';
        floatingButton.id = 'whatsapp-float-btn';
        floatingButton.innerHTML = `
            <i class="fab fa-whatsapp"></i>
            <div class="whatsapp-tooltip">Chat with us 👋</div>
        `;
        floatingButton.setAttribute('role', 'button');
        floatingButton.setAttribute('aria-label', 'Open WhatsApp chat');
        floatingButton.setAttribute('tabindex', '0');
        document.body.appendChild(floatingButton);

        // Chat overlay
        const overlay = document.createElement('div');
        overlay.className = 'whatsapp-chat-overlay';
        overlay.id = 'whatsapp-overlay';
        overlay.setAttribute('role', 'presentation');
        document.body.appendChild(overlay);

        // Chat panel
        const panel = document.createElement('div');
        panel.className = 'whatsapp-chat-panel';
        panel.id = 'whatsapp-chat-panel';
        panel.setAttribute('role', 'dialog');
        panel.setAttribute('aria-labelledby', 'whatsapp-chat-title');
        panel.innerHTML = `
            <!-- Header -->
            <div class="whatsapp-chat-header">
                <div class="whatsapp-chat-header-content">
                    <h3 id="whatsapp-chat-title">
                        <i class="fab fa-whatsapp"></i>
                        Chat with us
                    </h3>
                    <p>To help us serve you better, please let us know the area in which you're looking for accommodation.</p>
                </div>
                <button class="whatsapp-close-btn" id="whatsapp-close-btn" aria-label="Close chat panel">
                    <i class="fas fa-times"></i>
                </button>
            </div>

            <!-- Body -->
            <div class="whatsapp-chat-body">
                <!-- Info Box -->
                <div class="whatsapp-info-box">
                    <p>📍 Tell us your location and preferences so we can help you find the perfect accommodation.</p>
                </div>

                <!-- Form -->
                <form class="whatsapp-form" id="whatsapp-form" name="whatsapp-chat-form">
                    <!-- State Dropdown -->
                    <div class="whatsapp-form-group">
                        <label for="whatsapp-state">Select a State</label>
                        <select 
                            id="whatsapp-state" 
                            name="state" 
                            required
                            aria-label="Select your state"
                        >
                            <option value="">Choose a state...</option>
                        </select>
                    </div>

                    <!-- District Dropdown -->
                    <div class="whatsapp-form-group">
                        <label for="whatsapp-district">Select a District</label>
                        <select 
                            id="whatsapp-district" 
                            name="district" 
                            required
                            disabled
                            aria-label="Select your district"
                        >
                            <option value="">Choose a district...</option>
                        </select>
                    </div>

                    <!-- Locality Dropdown -->
                    <div class="whatsapp-form-group">
                        <label for="whatsapp-locality">Select a Locality</label>
                        <select 
                            id="whatsapp-locality" 
                            name="locality" 
                            required
                            disabled
                            aria-label="Select your locality"
                        >
                            <option value="">Choose a locality...</option>
                        </select>
                    </div>

                    <!-- User Type Dropdown -->
                    <div class="whatsapp-form-group">
                        <label for="whatsapp-type">I'm a</label>
                        <select 
                            id="whatsapp-type" 
                            name="type" 
                            required
                            aria-label="Select your profile type"
                        >
                            <option value="">Select an option...</option>
                        </select>
                    </div>

                    <!-- Start Chat Button -->
                    <button 
                        type="submit" 
                        class="whatsapp-btn whatsapp-btn-start" 
                        id="whatsapp-start-btn"
                        disabled
                        aria-label="Start WhatsApp chat"
                    >
                        <i class="fab fa-whatsapp"></i>
                        <span>Start Chat</span>
                    </button>
                </form>

                <!-- Status -->
                <div class="whatsapp-status">
                    <span class="whatsapp-status-dot"></span>
                    <span>We typically reply within 2 hours</span>
                </div>
            </div>

        `;
        document.body.appendChild(panel);
    }

    /**
     * Cache DOM elements
     */
    cacheElements() {
        this.elements = {
            floatingButton: document.getElementById('whatsapp-float-btn'),
            overlay: document.getElementById('whatsapp-overlay'),
            panel: document.getElementById('whatsapp-chat-panel'),
            closeButton: document.getElementById('whatsapp-close-btn'),
            form: document.getElementById('whatsapp-form'),
            stateSelect: document.getElementById('whatsapp-state'),
            districtSelect: document.getElementById('whatsapp-district'),
            localitySelect: document.getElementById('whatsapp-locality'),
            typeSelect: document.getElementById('whatsapp-type'),
            startButton: document.getElementById('whatsapp-start-btn')
        };

        // Populate state dropdown
        this.populateStates();
        
        // Populate user type dropdown
        this.populateUserTypes();
    }

    /**
     * Populate state dropdown
     */
    populateStates() {
        this.stateData.forEach((state) => {
            const option = document.createElement('option');
            option.value = state.value;
            option.textContent = state.label;
            this.elements.stateSelect.appendChild(option);
        });
    }

    /**
     * Populate user type dropdown
     */
    populateUserTypes() {
        this.userTypes.forEach((type, index) => {
            const option = document.createElement('option');
            option.value = index === 0 ? '' : type;
            option.textContent = type;
            if (index > 0) this.elements.typeSelect.appendChild(option);
        });
    }

    /**
     * Populate district dropdown based on selected state
     */
    populateDistricts(state) {
        // Clear existing options
        this.elements.districtSelect.innerHTML = '';

        // Get districts for selected state
        const districts = this.districtData[state] || [];

        districts.forEach(district => {
            const option = document.createElement('option');
            option.value = district === 'Select a District' ? '' : district;
            option.textContent = district;
            this.elements.districtSelect.appendChild(option);
        });

        // Disable if no data
        this.elements.districtSelect.disabled = districts.length === 0;
    }

    /**
     * Populate locality dropdown based on selected district
     */
    populateLocalities(district) {
        // Clear existing options
        this.elements.localitySelect.innerHTML = '';

        // Get localities for selected district
        const localities = this.localityData[district] || [];

        localities.forEach(locality => {
            const option = document.createElement('option');
            option.value = locality === 'Select a Locality' ? '' : locality;
            option.textContent = locality;
            this.elements.localitySelect.appendChild(option);
        });

        // Disable if no data
        this.elements.localitySelect.disabled = localities.length === 0;
    }

    /**
     * Attach event listeners
     */
    attachEventListeners() {
        // Float button click
        this.elements.floatingButton.addEventListener('click', () => this.togglePanel());
        this.elements.floatingButton.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.togglePanel();
            }
        });

        // Close button
        this.elements.closeButton.addEventListener('click', () => this.closePanel());

        // Overlay click
        this.elements.overlay.addEventListener('click', () => this.closePanel());

        // State change
        this.elements.stateSelect.addEventListener('change', (e) => {
            this.selectedState = e.target.value;
            this.populateDistricts(this.selectedState);
            this.selectedDistrict = ''; // Reset district
            this.elements.districtSelect.value = '';
            this.selectedLocality = ''; // Reset locality
            this.elements.localitySelect.value = '';
            this.elements.localitySelect.innerHTML = '<option value="">Choose a locality...</option>';
            this.checkFormValidity();
        });

        // District change
        this.elements.districtSelect.addEventListener('change', (e) => {
            this.selectedDistrict = e.target.value;
            this.populateLocalities(this.selectedDistrict);
            this.selectedLocality = ''; // Reset locality
            this.elements.localitySelect.value = '';
            this.checkFormValidity();
        });

        // Locality change
        this.elements.localitySelect.addEventListener('change', (e) => {
            this.selectedLocality = e.target.value;
            this.checkFormValidity();
        });

        // User type change
        this.elements.typeSelect.addEventListener('change', (e) => {
            this.selectedUserType = e.target.value;
            this.checkFormValidity();
        });

        // Form submit
        this.elements.form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleStartChat();
        });

        // Keyboard navigation (Escape key)
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.isOpen) {
                this.closePanel();
            }
        });
    }

    /**
     * Check if form is valid and enable/disable button
     */
    checkFormValidity() {
        const isValid = this.selectedState && this.selectedDistrict && this.selectedLocality && this.selectedUserType;
        
        if (isValid) {
            this.enableStartButton();
        } else {
            this.disableStartButton();
        }
    }

    /**
     * Enable start button
     */
    enableStartButton() {
        this.elements.startButton.disabled = false;
        this.elements.startButton.setAttribute('aria-disabled', 'false');
    }

    /**
     * Disable start button
     */
    disableStartButton() {
        this.elements.startButton.disabled = true;
        this.elements.startButton.setAttribute('aria-disabled', 'true');
    }

    /**
     * Toggle chat panel
     */
    togglePanel() {
        if (this.isOpen) {
            this.closePanel();
        } else {
            this.openPanel();
        }
    }

    /**
     * Open chat panel
     */
    openPanel() {
        this.isOpen = true;
        
        // Add active class
        this.elements.panel.classList.add('active');
        this.elements.overlay.classList.add('active');
        
        // Focus on first field
        setTimeout(() => {
            this.elements.stateSelect.focus();
        }, 100);

        // Prevent body scroll
        document.body.style.overflow = 'hidden';
        
        // Announce to screen readers
        this.announce('Chat panel opened');
    }

    /**
     * Close chat panel
     */
    closePanel() {
        this.isOpen = false;
        
        // Remove active class
        this.elements.panel.classList.remove('active');
        this.elements.overlay.classList.remove('active');
        
        // Allow body scroll
        document.body.style.overflow = '';
        
        // Announce to screen readers
        this.announce('Chat panel closed');
    }

    /**
     * Handle start chat button click
     */
    handleStartChat() {
        if (!this.validateForm()) {
            return;
        }

        // Set loading state
        this.setLoadingState(true);

        // Create message
        const message = this.createMessage();
        
        // Encode message
        const encodedMessage = encodeURIComponent(message);

        // Create WhatsApp URL
        const whatsappUrl = `https://wa.me/${this.phoneNumber}?text=${encodedMessage}`;

        // Simulate delay for UX
        setTimeout(() => {
            // Open WhatsApp
            window.open(whatsappUrl, '_blank');
            
            // Reset form
            this.resetForm();
            
            // Close panel
            this.closePanel();
            
            // Reset loading state
            this.setLoadingState(false);
            
            // Show success message
            this.showNotification('Opening WhatsApp...');
        }, 500);
    }

    /**
     * Validate form
     */
    validateForm() {
        if (!this.selectedState || !this.selectedDistrict || !this.selectedLocality || !this.selectedUserType) {
            this.showNotification('Please fill all fields', 'error');
            return false;
        }
        return true;
    }

    /**
     * Create formatted message
     */
    createMessage() {
        const timestamp = new Date().toLocaleTimeString();
        const message = `Hi, I am looking for accommodation in ${this.selectedState}, ` +
                       `District: ${this.selectedDistrict}, ` +
                       `Locality: ${this.selectedLocality}, ` +
                       `I am a ${this.selectedUserType}.`;
        return message;
    }

    /**
     * Reset form
     */
    resetForm() {
        this.elements.form.reset();
        this.selectedState = '';
        this.selectedDistrict = '';
        this.selectedLocality = '';
        this.selectedUserType = '';
        this.elements.districtSelect.disabled = true;
        this.elements.localitySelect.disabled = true;
        this.disableStartButton();
    }

    /**
     * Set loading state
     */
    setLoadingState(isLoading) {
        if (isLoading) {
            this.elements.startButton.disabled = true;
            this.elements.startButton.classList.add('loading');
            this.elements.startButton.innerHTML = `
                <span class="whatsapp-spinner"></span>
                <span>Opening...</span>
            `;
        } else {
            this.elements.startButton.disabled = false;
            this.elements.startButton.classList.remove('loading');
            this.elements.startButton.innerHTML = `
                <i class="fab fa-whatsapp"></i>
                <span>Start Chat</span>
            `;
        }
    }

    /**
     * Show notification
     */
    showNotification(message, type = 'success') {
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: ${type === 'error' ? '#ef4444' : '#25D366'};
            color: white;
            padding: 16px 24px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            z-index: 10000;
            animation: slideInRight 0.3s ease;
            font-size: 14px;
            font-weight: 500;
        `;
        notification.textContent = message;
        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }

    /**
     * Announce message to screen readers
     */
    announce(message) {
        const ariaLive = document.createElement('div');
        ariaLive.setAttribute('role', 'status');
        ariaLive.setAttribute('aria-live', 'polite');
        ariaLive.setAttribute('aria-atomic', 'true');
        ariaLive.style.position = 'absolute';
        ariaLive.style.left = '-10000px';
        ariaLive.textContent = message;
        document.body.appendChild(ariaLive);

        setTimeout(() => ariaLive.remove(), 1000);
    }

    /**
     * Public method to update configuration
     */
    updateConfig(config) {
        if (config.phoneNumber) this.phoneNumber = config.phoneNumber;
        if (config.stateData) this.stateData = config.stateData;
        if (config.districtData) this.districtData = config.districtData;
        if (config.localityData) this.localityData = config.localityData;
        if (config.userTypes) this.userTypes = config.userTypes;
    }

    /**
     * Public method to open panel programmatically
     */
    open() {
        this.openPanel();
    }

    /**
     * Public method to close panel programmatically
     */
    close() {
        this.closePanel();
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    // Get configuration from data attributes or use defaults
    const htmlElement = document.documentElement;
    const phoneNumber = htmlElement.getAttribute('data-whatsapp-number') || '918015649044';
    
    // Create chat widget instance
    window.whatsappChat = new WhatsAppModernChat({
        phoneNumber: phoneNumber,
        userTypes: ['Student', 'Working Professional', 'Other']
    });
});

// Add slide animations if not already in CSS
if (!document.querySelector('style[data-whatsapp-animations]')) {
    const style = document.createElement('style');
    style.setAttribute('data-whatsapp-animations', '');
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
}
