/* use jquery to get public key, slice off 1st and last chars as they will be "" */
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

/* stripe template with color changed */
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    /* color matches bootstrap text danger class */
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

/* card element */
var card = elements.create('card', {
    style: style
});
/* mount card to div that was previously created */
card.mount('#card-element');

// handle realtime validation errors on the card element. Icon and text added
card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `
        $(errorDiv).html(html);
    } else {
        errorDiv.textcontent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    // disable card element and submit buttons to prevent multiple submissions
    ev.preventDefault();
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true);
    // method to send card info securely to Stripe
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            // if error re-enable card and submit btn so user can fix
            $(errorDiv).html(html);
            card.update({
                'disabled': false
            });
            $('#submit-button').attr('disabled', false);
        } else {
            // if everything succeeds we submit form
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});