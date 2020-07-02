function checkForm(form)
{  if (checkExpire(form.expiration_date))
      form.submit();
   return false;
}

function checkExpire(field)
{  var arr = field.value.split("/");
   var mm=arr[0], yy=arr[1];
   if ( ! (1 <= mm && 12 >= mm  &&
           11 <=yy && 22 >= yy))
   return formErr(field, field.value);
   return true;
} 

function formErr(entry, msg)
{  alert(entry.name + ": " + msg + " is invalid.");
   entry.focus();
   entry.select();
   return false;
}
