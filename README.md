# side projects created
#keycode in schoology events key
#the keycode for any event
can i take munsons account?
        var event = document.createEvent("HTMLEvents");
        if (event) {
            event.keyCode = keyCode,
                event.initEvent(eventName, true, true),
                element.dispatchEvent(event);
        } else {
            event = document.createEventObject();
            event.keyCode = keyCode;
            event.eventType = eventName;
                    if (postedCreds[i].applicationGUID === app.applicationGUID)
                return postedCreds[i]
    isSameCred: function (existingCred, newCred) {

        if (existingCred["function"].toLowerCase() === ("password")) //Compare password with case!
        {
            if (existingCred.value !== newCred.value)
                return false;
        }
        else {
            if (existingCred.value.toLowerCase() !== newCred.value.toLowerCase())
                return false;
        }
        return true;
    },
    decodeBase64: function (s) {
        var e = {}, i, b = 0, c, x, l = 0, a, r = '', w = String.fromCharCode, L = s.length;
        var A = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
        for (i = 0; i < 64; i++) { e[A.charAt(i)] = i; }
        for (x = 0; x < L; x++) {
            c = e[s.charAt(x)]; b = (b << 6) + c; l += 6;
            while (l >= 8) { ((a = (b >>> (l -= 8)) & 0xff) || (x < (L - 2))) && (r += w(a)); }
        }
        return r;
    },              
