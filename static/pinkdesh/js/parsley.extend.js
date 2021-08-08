window.Parsley.addValidator('uppercase', {
    validateString: function(value, requirement) {
        var uppercase = value.match(/[A-Z]/g) || [];
        return uppercase.length >= requirement;
    },
    messages: {
        en: 'Your password must contain at least (%s) uppercase letter.'
    }
});
//has lowercase
window.Parsley.addValidator('lowercase', {
    validateString: function(value, requirement) {
        var lowecases = value.match(/[a-z]/g) || [];
        return lowecases.length >= requirement;
    },
    messages: {
        en: 'Your password must contain at least (%s) lowercase letter.'
    }
});

//has number
window.Parsley.addValidator('number', {
    validateString: function(value, requirement) {
        var numbers = value.match(/[0-9]/g) || [];
        return numbers.length >= requirement;
    },
    messages: {
        en: 'Your password must contain at least (%s) number.'
    }
});

//national number
window.Parsley.addValidator('national-number', {
    validateString: function(value, requirement) {
        console.log(value);
        /*var numbers = value.match(/[0-9]/g) || [];
        return numbers.length >= requirement;*/
    },
    messages: {
        en: 'Your password must contain at least (%s) number.'
    }
});

//has special char
window.Parsley.addValidator('special', {
    validateString: function(value, requirement) {
        var specials = value.match(/[^a-zA-Z0-9]/g) || [];
        return specials.length >= requirement;
    },
    messages: {
        en: 'Your password must contain at least (%s) special characters.'
    }
});