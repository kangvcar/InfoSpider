window.onload = function () {
    chrome.storage.sync.get('cnblogname',function(budget){
        var cnblog1="https://home.cnblogs.com/u/"+budget.cnblogname+"/";
         window.open(cnblog1)
      })
}