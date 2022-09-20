
window.onload = function () {
    console.log(document.getElementsByTagName('pre')[0].innerHTML)
    let data = document.getElementsByTagName('pre')[0].innerHTML;
    chrome.storage.sync.set({'following':data});
  // var blob = new Blob([data], {type: "text/plain;charset=utf-8"});
  // saveAs(blob, "following.json");
    chrome.storage.sync.get('githubname',function(budget){
      var githuburl3="https://api.github.com/users/"+budget.githubname+"/followers";
       window.open(githuburl3)
       window.close();

    })

}