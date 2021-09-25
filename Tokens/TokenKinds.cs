using System;
using System.ComponentModel;
using System.Linq;


namespace Titanium.Tokens {
    public enum Tokens
    {
        // Literals
        [Description("(")]
        OpenPar = '(',
        [Description(")")]
        ClosePar = ')',
        [Description(":")]
        Colon = ':',
        [Description("{")]
        OpenBrace = '{',
        [Description("}")]
        CloseBrace = '}',
        [Description("[")]
        OpenBracket = '[',
        [Description("]")]
        CloseBracket = ']'

    }
    

}