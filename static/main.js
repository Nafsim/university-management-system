// Load SweetAlert2 from CDN if not already loaded
if (typeof Swal === 'undefined') {
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/sweetalert2@11';
    document.head.appendChild(script);
}

// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', function() {
    setupAllButtonHandlers();
});

// ==================== MAIN HANDLER SETUP ====================
function setupAllButtonHandlers() {
    const allButtons = document.querySelectorAll('button:not(.navbar-brand), a.btn, a[class*="btn"]');
    
    allButtons.forEach(button => {
        if (button.hasListener) return;
        
        const text = button.textContent.trim().toLowerCase();
        const classList = button.className.toLowerCase();
        
        // Determine action type
        let actionType = getActionType(text, classList, button);
        
        if (actionType) {
            button.addEventListener('click', function(e) {
                handleButtonClick(e, this, actionType);
            });
            button.hasListener = true;
        }
    });
    
    // Handle delete forms separately
    setupDeleteForms();
}

// ==================== GET ACTION TYPE ====================
function getActionType(text, classList, element) {
    // Delete/Remove
    if (text.includes('delete') || text.includes('dlt') || text.includes('remove') ||
        classList.includes('delete') || classList.includes('danger')) {
        return 'delete';
    }
    
    // Pay Now
    if (text.includes('pay') || text.includes('payment')) {
        return 'pay';
    }
    
    // Upload Marks / Mark Upload
    if (text.includes('upload mark') || text.includes('mark upload') || 
        text.includes('upload') && (text.includes('mark') || text.includes('score'))) {
        return 'upload_marks';
    }
    
    // Results
    if (text.includes('result') || text.includes('grade')) {
        return 'result';
    }
    
    // Details / View
    if (text.includes('detail') || text.includes('view') || text.includes('info')) {
        return 'details';
    }
    
    // Edit
    if (text.includes('edit') || text.includes('modify')) {
        // Allow normal navigation for links
        if (element.tagName === 'A' && element.getAttribute('href')) {
            return null;
        }
        return 'edit';
    }
    
    // Upload (general)
    if (text.includes('upload')) {
        return 'upload';
    }
    
    return null;
}

// ==================== MAIN CLICK HANDLER ====================
function handleButtonClick(e, element, actionType) {
    e.preventDefault();
    
    switch(actionType) {
        case 'delete':
            handleDelete(element);
            break;
        case 'pay':
            handlePayment(element);
            break;
        case 'upload_marks':
            handleMarkUpload(element);
            break;
        case 'result':
            handleResult(element);
            break;
        case 'details':
            handleDetails(element);
            break;
        case 'edit':
            handleEdit(element);
            break;
        case 'upload':
            handleUpload(element);
            break;
    }
}

// ==================== DELETE HANDLER ====================
function handleDelete(element) {
    const itemName = getItemName(element);
    
    Swal.fire({
        title: 'Are you sure?',
        text: `You want to delete ${itemName}?`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Yes, delete it!',
        cancelButtonText: 'Cancel'
    }).then((result) => {
        if (result.isConfirmed) {
            submitOrNavigate(element);
        }
    });
}

// ==================== PAYMENT HANDLER ====================
function handlePayment(element) {
    const amount = getAmount(element);
    
    Swal.fire({
        title: 'Process Payment',
        text: `You are about to pay ${amount}. Continue?`,
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#28a745',
        cancelButtonColor: '#6c757d',
        confirmButtonText: 'Yes, pay now!',
        cancelButtonText: 'Cancel'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: 'Processing',
                text: 'Processing your payment...',
                icon: 'info',
                allowOutsideClick: false,
                didOpen: () => {
                    Swal.showLoading();
                }
            });
            submitOrNavigate(element);
        }
    });
}

// ==================== MARK UPLOAD HANDLER ====================
function handleMarkUpload(element) {
    Swal.fire({
        title: 'Upload Marks',
        text: 'Are you sure you want to upload marks? This action cannot be undone.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#6c757d',
        confirmButtonText: 'Yes, upload!',
        cancelButtonText: 'Cancel'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: 'Uploading',
                text: 'Please wait...',
                icon: 'info',
                allowOutsideClick: false,
                didOpen: () => {
                    Swal.showLoading();
                }
            });
            submitOrNavigate(element);
        }
    });
}

// ==================== RESULT HANDLER ====================
function handleResult(element) {
    Swal.fire({
        title: 'View Results',
        text: 'Loading your results...',
        icon: 'info',
        confirmButtonText: 'OK'
    }).then(() => {
        submitOrNavigate(element);
    });
}

// ==================== DETAILS HANDLER ====================
function handleDetails(element) {
    Swal.fire({
        title: 'Details',
        text: 'Loading details...',
        icon: 'info',
        confirmButtonText: 'OK'
    }).then(() => {
        submitOrNavigate(element);
    });
}

// ==================== EDIT HANDLER ====================
function handleEdit(element) {
    Swal.fire({
        title: 'Edit Item',
        text: 'Opening edit form...',
        icon: 'info',
        confirmButtonText: 'OK'
    }).then(() => {
        submitOrNavigate(element);
    });
}

// ==================== UPLOAD HANDLER ====================
function handleUpload(element) {
    Swal.fire({
        title: 'Upload File',
        text: 'Are you sure you want to upload this file?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#6c757d',
        confirmButtonText: 'Yes, upload!',
        cancelButtonText: 'Cancel'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: 'Uploading',
                text: 'Please wait...',
                icon: 'info',
                allowOutsideClick: false,
                didOpen: () => {
                    Swal.showLoading();
                }
            });
            submitOrNavigate(element);
        }
    });
}

// ==================== HELPER FUNCTIONS ====================

function getItemName(element) {
    // Try to get from table row
    const row = element.closest('tr');
    if (row) {
        const cells = row.querySelectorAll('td');
        if (cells.length > 0) {
            return cells[1]?.textContent.trim() || 'this item';
        }
    }
    
    // Try to get from data attribute
    const itemName = element.getAttribute('data-item-name');
    if (itemName) return itemName;
    
    return 'this item';
}

function getAmount(element) {
    // Try to find amount in the page
    const amountElements = document.querySelectorAll('p, span, td, strong');
    for (let el of amountElements) {
        const text = el.textContent.trim();
        if (text.includes('৳') || text.includes('$')) {
            return text;
        }
    }
    return '৳12,500';
}

function submitOrNavigate(element) {
    // Check if it's inside a form
    const form = element.closest('form');
    if (form) {
        form.submit();
        return;
    }
    
    // Check for href
    const href = element.getAttribute('href') || element.getAttribute('data-url');
    if (href) {
        window.location.href = href;
        return;
    }
    
    // If button has data-action, trigger that
    const action = element.getAttribute('data-action');
    if (action) {
        // Trigger custom action
        console.log('Action triggered:', action);
    }
}

// ==================== DELETE FORM HANDLER ====================
function setupDeleteForms() {
    document.querySelectorAll('form').forEach(form => {
        if (form.hasDeleteListener) return;
        
        const submitButtons = form.querySelectorAll('button[type="submit"]');
        submitButtons.forEach(btn => {
            const text = btn.textContent.trim().toLowerCase();
            if (text.includes('delete') || text.includes('dlt')) {
                btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    const itemName = getItemName(form);
                    
                    Swal.fire({
                        title: 'Are you sure?',
                        text: `You want to delete ${itemName}?`,
                        icon: 'warning',
                        showCancelButton: true,
                        confirmButtonColor: '#d33',
                        cancelButtonColor: '#3085d6',
                        confirmButtonText: 'Yes, delete it!',
                        cancelButtonText: 'Cancel'
                    }).then((result) => {
                        if (result.isConfirmed) {
                            form.submit();
                        }
                    });
                });
            }
        });
        
        form.hasDeleteListener = true;
    });
}

