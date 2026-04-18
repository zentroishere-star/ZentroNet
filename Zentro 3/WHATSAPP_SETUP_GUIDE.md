# WhatsApp Chat Widget Configuration Guide

## Overview
A fully functional WhatsApp chat widget has been added to your Zentro project. Users can now directly communicate with your admin team through WhatsApp.

## Features
✅ **Floating Button** - Green WhatsApp button fixed at bottom-right of every page
✅ **Chat Modal** - Beautiful popup modal for collecting user information
✅ **Multi-Service Support** - Users can select what service they're inquiring about
✅ **Auto-Message Formatting** - Messages are automatically formatted with user details
✅ **Mobile Responsive** - Works perfectly on all devices
✅ **Smooth Animations** - Professional animations and transitions
✅ **Status Indicator** - Shows typical response time
✅ **Service Descriptions** - Lists all services your company offers

## Configuration

### Step 1: Update WhatsApp Number
Edit your `base.html` file and update the WhatsApp number in the `<html>` tag:

```html
<html lang="en" data-whatsapp-number="YOUR_WHATSAPP_NUMBER">
```

**Important**: Use international format without `+` or spaces
- Example: `919876543210` (India: 91 + number)
- Example: `14155552671` (USA: 1 + number)

### Step 2: Customize Services (Optional)
Edit `static/js/whatsapp-chat.js` and modify the services array in the constructor:

```javascript
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
```

### Step 3: Customize Business Name (Optional)
Update the `businessName` in the same file:

```javascript
businessName: 'Your Company Name'
```

## How It Works

1. **User clicks** the green WhatsApp button (bottom-right corner)
2. **Modal opens** with a form asking for:
   - Inquiry Type (Project, Service, Collaboration, Support, Other)
   - Name
   - Email
   - Message
3. **User fills** the form with their details
4. **User clicks** "Send on WhatsApp"
5. **WhatsApp opens** with pre-formatted message containing all details
6. **User completes** the conversation in WhatsApp

## File Locations

- **CSS**: `zentro_project/static/css/whatsapp-chat.css`
- **JavaScript**: `zentro_project/static/js/whatsapp-chat.js`
- **Template**: `zentro_project/templates/base.html`

## Styling Customization

### Change Primary Color
Edit `whatsapp-chat.css`:

```css
:root {
    --wa-primary: #25D366;        /* Main green color */
    --wa-secondary: #1f8857;      /* Darker green */
    --wa-dark: #0f3d2a;          /* Dark accent */
    --wa-light: #e8f5e9;         /* Light background */
}
```

### Change Button Position
In `whatsapp-chat.css`, modify:

```css
.whatsapp-float-button {
    bottom: 30px;    /* Distance from bottom */
    right: 30px;     /* Distance from right */
}
```

### Change Button Size
Modify these values in `.whatsapp-float-button`:

```css
width: 70px;
height: 70px;
```

## Mobile Responsiveness

The widget automatically adapts to different screen sizes:
- **Desktop**: Full-size button and large modal
- **Tablet**: Proportionally sized
- **Mobile**: Optimized for small screens with adjusted spacing

## Testing

1. **Open your website** in a browser
2. **Scroll to bottom-right** - you should see the green WhatsApp button
3. **Click the button** - the modal should open
4. **Fill in the form** with test data
5. **Click "Send on WhatsApp"** - should open WhatsApp with your message

### Testing Different Scenarios
- ✅ Test on mobile devices
- ✅ Test on tablets
- ✅ Test different inquiry types
- ✅ Test form validation (all fields required)
- ✅ Test modal close functionality

## Browser Compatibility

Works on:
- ✅ Chrome/Chromium
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## WhatsApp Number Format Guide

| Country | Format | Example |
|---------|--------|---------|
| India | 91XXXXXXXXXX | 919876543210 |
| USA | 1XXXXXXXXXX | 14155552671 |
| UK | 441XXXXXXXXX | 441632960000 |
| Australia | 61XXXXXXXXX | 61412345678 |
| Canada | 1XXXXXXXXXX | 14165552671 |
| Brazil | 55XXXXXXXXX | 5511987654321 |

**Find your country code**: https://www.countrycode.org/

## Features in Detail

### Auto-Message Formatting
When user sends message, it's automatically formatted as:

```
Hello Zentro Team!

I'm reaching out regarding: 💼 Project Inquiry

My Details:
Name: [Name]
Email: [Email]

Message:
[User Message]

Looking forward to hearing from you!
```

### Inquiry Types with Icons
- 💼 Project Inquiry
- 🛠️ Service Inquiry
- 🤝 Collaboration
- 🆘 Support
- ❓ Other

### Form Validation
- All fields are required
- Email format validation
- Custom error messages
- Form reset on cancel

## Troubleshooting

### Button Not Appearing
- Check if `whatsapp-chat.css` is linked in base.html
- Check if `whatsapp-chat.js` is linked in base.html
- Check browser console for JavaScript errors (F12 → Console)

### Modal Not Opening
- Ensure WhatsApp number is set correctly
- Check for JavaScript errors in console
- Verify Font Awesome icons are loading

### WhatsApp Not Opening
- Check if WhatsApp is installed on the device
- Verify phone number format is correct
- On desktop, ensure WhatsApp Web is signed in
- Try again with correct international format

### Form Not Submitting
- Ensure all fields are filled
- Check email format is valid
- Check console for any JavaScript errors

## Security Notes

- Phone numbers are NOT stored in the database
- All messages go directly to WhatsApp
- No personal data is collected (form data only used to open WhatsApp)
- HTTPS recommended for production

## Performance

- **Lightweight**: ~10KB combined CSS + JS
- **No external API calls**: Works offline after initial load
- **No jQuery dependency**: Pure vanilla JavaScript
- **Mobile optimized**: Minimal memory footprint

## Advanced Customization

### Modify Messages
Edit the `getInquiryLabel()` method in `whatsapp-chat.js`:

```javascript
getInquiryLabel(type) {
    const types = {
        'project_inquiry': '💼 Project Inquiry',
        'service_inquiry': '🛠️ Service Inquiry',
        'collaboration': '🤝 Collaboration',
        'support': '🆘 Support',
        'other': '❓ Other',
        'your_type': '🎯 Your Label'  // Add custom type
    };
    return types[type] || 'General Inquiry';
}
```

### Add More Form Fields
1. Add to HTML in `createModal()` method
2. Get values in `sendMessage()` method
3. Add to message formatting

## Support Services Shown

Currently configured services:
1. Web Development
2. Mobile Applications
3. UI/UX Design
4. Cloud Solutions
5. API Development
6. Consulting & Strategy

Modify in `whatsapp-chat.js` as shown in Step 2 above.

## Analytics

To track usage, you can add Google Analytics event:

```javascript
// Add inside sendMessage() method before window.open()
gtag('event', 'whatsapp_inquiry', {
    'inquiry_type': inquiryType,
    'user_name': name
});
```

## Next Steps

1. ✅ Update WhatsApp number (required)
2. ✅ Test the widget on your website
3. ✅ Customize colors if desired (optional)
4. ✅ Update services list to match your offerings (optional)
5. ✅ Deploy to production

## Go Live Checklist

- [ ] WhatsApp number updated
- [ ] Tested on desktop
- [ ] Tested on mobile
- [ ] Tested on tablet
- [ ] All services listed correctly
- [ ] Business name updated
- [ ] Colors match brand (if customized)
- [ ] Modal opens/closes smoothly
- [ ] WhatsApp opens with pre-filled message
- [ ] Response time is accurate

---

**For questions or issues, check the troubleshooting section above or review the JavaScript console for errors.**
