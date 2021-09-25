using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Titanium.Extensions
{
    internal static class EnumManagement
    {
        public static string GetDescription(this Enum instance)
        {
            var genericEnumType = instance.GetType();
            var memberInfo = genericEnumType.GetMember(instance.ToString());

            if (memberInfo is not null && memberInfo.Length > 0)
            {
                var attr = memberInfo[0].GetCustomAttributes(typeof(DescriptionAttribute), false);
                if (attr is not null && attr.Length > 0)
                    return ((DescriptionAttribute)attr.ElementAt(0)).Description;
            }

            return "";
        }


    }
}
