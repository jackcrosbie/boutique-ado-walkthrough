/* use jquery to get public key, slice off 1st and last chars as they will be "" */
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
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