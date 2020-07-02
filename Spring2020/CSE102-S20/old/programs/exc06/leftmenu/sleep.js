function sleep(ms)
{ var now = new Date();
  var later;
  do { later = new Date(); } while(later-now < ms);
}
