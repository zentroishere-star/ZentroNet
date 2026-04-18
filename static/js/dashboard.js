/**
 * Zentro Admin Dashboard JavaScript
 * Handles interactivity for navigation, forms, modals, and animations
 */

// ===========================
// 1. NAVBAR & NAVIGATION
// ===========================

document.addEventListener('DOMContentLoaded', function() {
    initializeNavbar();
    initializeFormValidation();
    initializeDeleteConfirmation();
    initializeAnimations();
    initializeSearch();
});

function initializeNavbar() {
    const userMenuBtn = document.getElementById('userMenuBtn');
    const userMenu = document.getElementById('userMenu');
    
    if (userMenuBtn && userMenu) {
        // Toggle dropdown
        userMenuBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            userMenu.classList.toggle('show');
            userMenuBtn.classList.toggle('active');
        });
        
        // Close on outside click
        document.addEventListener('click', function(e) {
            if (!userMenuBtn.parentElement.contains(e.target)) {
                userMenu.classList.remove('show');
                userMenuBtn.classList.remove('active');
            }
        });
    }
    
    // Active link highlighting
    highlightActiveSidebarItem();
}

function highlightActiveSidebarItem() {
    const currentPath = window.location.pathname;
    const sidebarItems = document.querySelectorAll('.sidebar-item');
    
    sidebarItems.forEach(item => {
        item.classList.remove('active');
        const link = item.querySelector('a');
        if (link && link.getAttribute('href') === currentPath) {
            item.classList.add('active');
        }
    });
}

// ===========================
// 2. FORM VALIDATION
// ===========================

function initializeFormValidation() {
    const forms = document.querySelectorAll('form[data-validate]');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    addFieldError(field, 'This field is required');
                } else {
                    removeFieldError(field);
                }
            });
            
            if (!isValid) {
                e.preventDefault();
            }
        });
        
        // Remove errors on input
        const fields = form.querySelectorAll('input, textarea, select');
        fields.forEach(field => {
            field.addEventListener('input', function() {
                removeFieldError(this);
            });
        });
    });
}

function addFieldError(field, message) {
    field.classList.add('error');
    const errorDiv = field.parentElement.querySelector('.field-error');
    if (errorDiv) {
        errorDiv.textContent = message;
        errorDiv.style.display = 'block';
    }
}

function removeFieldError(field) {
    field.classList.remove('error');
    const errorDiv = field.parentElement.querySelector('.field-error');
    if (errorDiv) {
        errorDiv.style.display = 'none';
    }
}

// ===========================
// 3. DELETE CONFIRMATION
// ===========================

function initializeDeleteConfirmation() {
    const deleteButtons = document.querySelectorAll('[data-confirm="delete"]');
    
    deleteButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item? This action cannot be undone.')) {
                e.preventDefault();
            }
        });
    });
}

// ===========================
// 4. ANIMATIONS
// ===========================

function initializeAnimations() {
    // Fade in cards on load
    const cards = document.querySelectorAll('.dashboard-card, .stat-card');
    cards.forEach((card, index) => {
        card.style.animation = `fadeInUp 0.5s ease-out ${index * 0.1}s both`;
    });
    
    // Animate stat counters
    const statValues = document.querySelectorAll('[data-stat-value]');
    statValues.forEach(element => {
        const finalValue = parseInt(element.textContent);
        animateCounter(element, finalValue);
    });
}

function animateCounter(element, finalValue) {
    let currentValue = 0;
    const increment = Math.ceil(finalValue / 30);
    const interval = setInterval(() => {
        currentValue += increment;
        if (currentValue >= finalValue) {
            element.textContent = finalValue;
            clearInterval(interval);
        } else {
            element.textContent = currentValue;
        }
    }, 30);
}

// ===========================
// 5. SEARCH FUNCTIONALITY
// ===========================

function initializeSearch() {
    const searchInput = document.getElementById('quickSearch');
    if (searchInput) {
        let searchTimeout;
        searchInput.addEventListener('input', function(e) {
            clearTimeout(searchTimeout);
            const searchTerm = this.value.toLowerCase();
            
            // Implement search on page (client-side for lists)
            const items = document.querySelectorAll('[data-searchable]');
            let matchCount = 0;
            
            items.forEach(item => {
                const text = item.textContent.toLowerCase();
                if (text.includes(searchTerm) || searchTerm === '') {
                    item.style.display = '';
                    item.style.animation = 'fadeIn 0.3s ease-out';
                    matchCount++;
                } else {
                    item.style.display = 'none';
                }
            });
            
            // Show "no results" message
            const noResultsMsg = document.querySelector('[data-no-results]');
            if (noResultsMsg) {
                if (matchCount === 0 && searchTerm) {
                    noResultsMsg.style.display = 'block';
                } else {
                    noResultsMsg.style.display = 'none';
                }
            }
        });
    }
}

// ===========================
// 6. TABLE ACTIONS
// ===========================

function deleteItem(itemId, itemType) {
    if (confirm(`Are you sure you want to delete this ${itemType}?`)) {
        // Add loading state to button
        const deleteBtn = event.target;
        deleteBtn.disabled = true;
        deleteBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Deleting...';
    }
}

function editItem(itemId) {
    console.log('Edit item:', itemId);
}

// ===========================
// 7. MODAL HANDLING
// ===========================

function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('show');
        document.body.style.overflow = 'hidden';
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('show');
        document.body.style.overflow = 'auto';
    }
}

// Close modal on outside click
document.addEventListener('click', function(e) {
    if (e.target.classList.contains('modal-overlay')) {
        e.target.parentElement.classList.remove('show');
        document.body.style.overflow = 'auto';
    }
});

// ===========================
// 8. UTILITY FUNCTIONS
// ===========================

function showNotification(message, type = 'success', duration = 3000) {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <i class="fas fa-check-circle"></i>
        <span>${message}</span>
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.classList.add('show');
    }, 10);
    
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, duration);
}

function formatDate(date) {
    return new Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    }).format(new Date(date));
}

// ===========================
// 9. CSS ANIMATIONS (Add to CSS file)
// ===========================
// @keyframes fadeInUp {
//     from {
//         opacity: 0;
//         transform: translateY(20px);
//     }
//     to {
//         opacity: 1;
//         transform: translateY(0);
//     }
// }
// 
// @keyframes fadeIn {
//     from { opacity: 0; }
//     to { opacity: 1; }
// }
